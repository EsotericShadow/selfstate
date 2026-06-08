"""Randomized-but-deterministic WrongFix Arena generator for report 140."""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

from .artifacts import write_artifacts
from .evaluator import evaluate
from .models import CHANNELS, RepairCandidate, RepairTask


DIFFICULTY_TIERS = ("easy", "intermediate", "hard")
SCENARIOS = (
    "visible_correct",
    "visible_wrong",
    "root_cause_first_wrong",
    "weighted_beats_min",
    "min_beats_weighted",
    "noisy_ambiguous",
)
SPREAD_BY_DIFFICULTY = {"easy": 0.03, "intermediate": 0.07, "hard": 0.12}
FAMILIES_HOLD_OUT = {"money_rounding", "timezone_serialization", "api_compatibility", "observability_misdiagnosis"}


@dataclass(frozen=True)
class FamilyProfile:
    family: str
    bug_templates: Tuple[str, ...]
    visible_templates: Tuple[str, ...]
    hidden_templates: Tuple[str, ...]
    dominant_channel: str
    suspicious_signals: Tuple[str, ...]
    irrelevant_signals: Tuple[str, ...]


FAMILIES: Tuple[FamilyProfile, ...] = (
    FamilyProfile(
        family="auth_session",
        bug_templates=(
            "Users intermittently fail login after reset or token rotation.",
            "Session fixation appears during password change and fails after one hop.",
        ),
        visible_templates=(
            "Login page stays in unauthenticated state after valid credentials.",
            "The auth endpoint reports success but denies the protected call.",
        ),
        hidden_templates=(
            "Session identity key is normalized only at read but not at write, so reused emails collide.",
            "The token signer and verifier use different canonicalization logic.",
        ),
        dominant_channel="security",
        suspicious_signals=(
            "One-line fix changes middleware order.",
            "Recent diff includes an experimental CSRF header guard.",
        ),
        irrelevant_signals=(
            "Browser telemetry shows mixed timezone from user locale.",
            "Cache miss spike in image thumbnail loader.",
        ),
    ),
    FamilyProfile(
        family="cache_invalidation",
        bug_templates=(
            "Profile updates show stale data for one page view after write.",
            "Search results are stale even though DB row changed upstream.",
        ),
        visible_templates=(
            "The UI displays stale rows after write but recovers on hard refresh.",
            "A visible list endpoint returns cached response after mutation.",
        ),
        hidden_templates=(
            "Mutation clears parent collection cache, but misses derived aggregate keys.",
            "Entity version counter increments without invalidation fanout.",
        ),
        dominant_channel="performance",
        suspicious_signals=(
            "Candidate suggests disabling the entire cache layer.",
            "Candidate introduces manual TTL overrides globally.",
        ),
        irrelevant_signals=(
            "CDN edge reports occasional stale bytes.",
            "Load balancer sends 206 responses.",
        ),
    ),
    FamilyProfile(
        family="migration_backfill",
        bug_templates=(
            "Deployment succeeds but writes crash when old records are loaded.",
            "Null migration backfill leaves legacy rows partially initialized.",
        ),
        visible_templates=(
            "Schema migration tests pass, but new writes fail in production.",
            "The new column is created but legacy rows break reads.",
        ),
        hidden_templates=(
            "Migration adds non-null fields without backfill and without rollback-safe default.",
            "The deployment path lacks a dual-read compatibility gate for old clients.",
        ),
        dominant_channel="migration_rollback_safety",
        suspicious_signals=(
            "Suggested fix drops old data and recreates rows.",
            "Proposed fix disables strict migration checks.",
        ),
        irrelevant_signals=(
            "Observed slow index rebuild during weekends.",
            "Database vacuum appears to run after each release.",
        ),
    ),
    FamilyProfile(
        family="async_race",
        bug_templates=(
            "State updates race when two async actions write the same aggregate.",
            "Concurrent commands produce occasional impossible state.",
        ),
        visible_templates=(
            "A single command test fails only at high concurrency.",
            "The second operation appears to ignore the first.",
        ),
        hidden_templates=(
            "Compare-and-swap is missing on inventory reservation and causes lost updates.",
            "Async worker confirms completion before row-level lock is released.",
        ),
        dominant_channel="root_cause",
        suspicious_signals=(
            "Suggested fix serializes all async operations in-memory.",
            "Suggested fix adds sleep between writes.",
        ),
        irrelevant_signals=(
            "Event loop shows 200ms jitter spikes.",
            "Queue lag is high due to unrelated reporting jobs.",
        ),
    ),
    FamilyProfile(
        family="flaky_timing",
        bug_templates=(
            "Ready handshake test flaps during CI load.",
            "Worker startup order changes by timing only.",
        ),
        visible_templates=(
            "Startup readiness transitions before subscriber state is valid.",
            "Smoke test fails sporadically because a signal arrives too soon.",
        ),
        hidden_templates=(
            "A synchronous event is emitted before asynchronous initialization completes.",
            "Cancellation paths do not await cleanup on partial startup.",
        ),
        dominant_channel="observability_logging_quality",
        suspicious_signals=(
            "Suggested fix adds longer fixed timeout.",
            "Suggested fix retries without timeout jitter.",
        ),
        irrelevant_signals=(
            "Host clock drift around CI container restore.",
            "Clock skew from virtual NIC.",
        ),
    ),
    FamilyProfile(
        family="api_compatibility",
        bug_templates=(
            "A dependency update makes one API method disappear at runtime.",
            "Build passes, runtime fails after dependency bump.",
        ),
        visible_templates=(
            "Parser initialization fails with a single method signature mismatch.",
            "Known path executes, but newer route call throws compile-time import error.",
        ),
        hidden_templates=(
            "A boundary adapter was not updated for contract-shape change.",
            "Callers still assume legacy config key names.",
        ),
        dominant_channel="api_contract_safety",
        suspicious_signals=(
            "Candidate pins old dependency without evaluating transitive users.",
            "Candidate copies legacy parser implementation.",
        ),
        irrelevant_signals=(
            "Monorepo lockfile rehash changed ordering.",
            "Runtime bundle shows unrelated chunk name changes.",
        ),
    ),
    FamilyProfile(
        family="security_validation",
        bug_templates=(
            "Input validation appears to permit invalid payload shapes.",
            "One endpoint accepts malformed payload that later escalates privilege.",
        ),
        visible_templates=(
            "Validation test fails only for non-whitelisted characters.",
            "One API path passes visible regex checks but leaks invalid state.",
        ),
        hidden_templates=(
            "Validation runs after mutation not before persistence.",
            "Central guard path is bypassed for admin path because of route alias.",
        ),
        dominant_channel="security",
        suspicious_signals=(
            "Suggested fix replaces strict validation with deny-by-default catch.",
            "Suggested fix adds a permissive sanitizer in front of all routes.",
        ),
        irrelevant_signals=(
            "A different route has an unrelated CSRF warning.",
            "Input UI hints mention optional fields.",
        ),
    ),
    FamilyProfile(
        family="query_injection",
        bug_templates=(
            "A search term passes visible tests but leaks data through query construction.",
            "Hidden fuzz test indicates unsafe predicate expansion.",
        ),
        visible_templates=(
            "A user enters text and query returns wrong ranking.",
            "Visible SQL smoke test passes with quoted text.",
        ),
        hidden_templates=(
            "Search concatenates user string after sanitization but before binding.",
            "LIKE wildcards are escaped for UI text but not for metadata query path.",
        ),
        dominant_channel="security",
        suspicious_signals=(
            "Suggested fix rejects non-alphanumerics globally.",
            "Suggested fix escapes just single quotes in one input path.",
        ),
        irrelevant_signals=(
            "Legacy report query uses old table hint.",
            "ORM logs show one harmless slow query.",
        ),
    ),
    FamilyProfile(
        family="path_traversal",
        bug_templates=(
            "Upload path sanitization accepts encoded traversal payloads.",
            "One encoded file key bypasses the root check.",
        ),
        visible_templates=(
            "Upload rejects plain ../ payloads but still passes simple checks.",
            "One allowlist path test passes with direct dots.",
        ),
        hidden_templates=(
            "Path is normalized after allowlist check, creating bypass order bug.",
            "Filesystem root check ignores URL-decoding.",
        ),
        dominant_channel="security",
        suspicious_signals=(
            "Suggested fix rewrites file keys with timestamp only.",
            "Suggested fix skips all extension checks in upload service.",
        ),
        irrelevant_signals=(
            "Object metadata has extra custom tags.",
            "CDN signed URL TTL looks short.",
        ),
    ),
    FamilyProfile(
        family="money_rounding",
        bug_templates=(
            "Billing report off by one cent in tax and discount mix.",
            "Promotions accumulate rounding error across multiple line items.",
        ),
        visible_templates=(
            "Simple line-item check passes for integer-cent cases.",
            "Visible invoice fixture differs by one cent in a known test.",
        ),
        hidden_templates=(
            "Floating-point arithmetic mixes binary rounding with decimal display.",
            "Order of operation differs for subtotal and tax causing cumulative loss.",
        ),
        dominant_channel="maintainability",
        suspicious_signals=(
            "Suggested fix adds display-only correction for one decimal place.",
            "Suggested fix rounds tax after string formatting.",
        ),
        irrelevant_signals=(
            "Payment provider changed network retry threshold.",
            "Currency rounding config is logged at startup only.",
        ),
    ),
    FamilyProfile(
        family="timezone_serialization",
        bug_templates=(
            "Scheduled jobs fire at the wrong local hour around DST.",
            "Cron windows drift after zone migration.",
        ),
        visible_templates=(
            "Simple local/UTC fixture passes in one city.",
            "One user report appears one hour early on transition day.",
        ),
        hidden_templates=(
            "Local wall-clock is persisted without zone source-of-truth.",
            "Deserialization assumes fixed offset from environment.",
        ),
        dominant_channel="observability_logging_quality",
        suspicious_signals=(
            "Suggested fix hardcodes a timezone per tenant.",
            "Suggested fix subtracts a fixed offset before storing.",
        ),
        irrelevant_signals=(
            "Calendar cache expired before daily cut-off.",
            "Cron runner jitter appears near half-hour zones.",
        ),
    ),
    FamilyProfile(
        family="dependency_upgrade",
        bug_templates=(
            "Dependency bump changed API shape but type-check still compiles.",
            "Build-time lock updates hide runtime regressions.",
        ),
        visible_templates=(
            "Compile and package checks pass but integration call crashes.",
            "Simple smoke call passes once and fails on follow-up call.",
        ),
        hidden_templates=(
            "Adapter path still uses legacy symbol names.",
            "Retry policy contract changed from callback to promise."
            ,
        ),
        dominant_channel="migration_rollback_safety",
        suspicious_signals=(
            "Suggested fix vendor-locks by pinning to an old major.",
            "Suggested fix bundles local wrapper around unstable internals.",
        ),
        irrelevant_signals=(
            "Dependency lock changed unrelated transitive packages.",
            "Release pipeline has an unrelated security scan failure.",
        ),
    ),
    FamilyProfile(
        family="event_listener_leak",
        bug_templates=(
            "Duplicate callbacks fire after navigation changes.",
            "Listeners leak after component unmount.",
        ),
        visible_templates=(
            "Single navigation path gets duplicate events.",
            "One callback is observed twice in visible action log.",
        ),
        hidden_templates=(
            "Ownership boundaries are lost when teardown runs in nested routers.",
            "Unregister logic clears all listeners for module instead of owner.",
        ),
        dominant_channel="maintainability",
        suspicious_signals=(
            "Suggested fix disables all listener removal for stability.",
            "Suggested fix recreates singleton publisher each route.",
        ),
        irrelevant_signals=(
            "Component tree emits repeated render warnings.",
            "Profiler suggests unrelated memoization debt.",
        ),
    ),
    FamilyProfile(
        family="frontend_state_reducer",
        bug_templates=(
            "UI state becomes inconsistent between reducer and DOM.",
            "Validation state and DOM input state diverge on reset.",
        ),
        visible_templates=(
            "Submit button toggles unexpectedly after inline edit.",
            "Visible form clears but validation marker remains.",
        ),
        hidden_templates=(
            "Reducer updates only display fields and skips form-level constraints.",
            "Derived validation cache is not invalidated on reset flow.",
        ),
        dominant_channel="reviewability",
        suspicious_signals=(
            "Suggested fix removes validation for speed.",
            "Suggested fix adds one-off DOM writes in component effect.",
        ),
        irrelevant_signals=(
            "Theme style cache invalidates every render.",
            "Frontend bundle contains a stale translation entry.",
        ),
    ),
    FamilyProfile(
        family="performance_n_plus_one",
        bug_templates=(
            "List endpoint degrades superlinearly for large accounts.",
            "Query count scales with number of returned rows.",
        ),
        visible_templates=(
            "Latency budget breach starts when page has >50 rows.",
            "Visible request counter exceeds expected budget in one load test.",
        ),
        hidden_templates=(
            "Nested per-item subquery runs under each row because relation hint missing.",
            "Cache key does not include filter version and misses warm path.",
        ),
        dominant_channel="performance",
        suspicious_signals=(
            "Suggested fix increases query timeout and retries to hide timeout faults.",
            "Suggested fix disables pagination globally.",
        ),
        irrelevant_signals=(
            "Image CDN adds compression overhead on first page.",
            "Query engine uses a different plan on warm cache.",
        ),
    ),
    FamilyProfile(
        family="inventory_transactional",
        bug_templates=(
            "Inventory count becomes negative under concurrent checkout.",
            "Two requests oversell stock in same window.",
        ),
        visible_templates=(
            "Edge case creates negative stock in one integration test.",
            "Visible checkout count report drops unexpectedly.",
        ),
        hidden_templates=(
            "Reservation and fulfillment steps are not atomic.",
            "Compensating rollback misses partial reserve states.",
        ),
        dominant_channel="api_contract_safety",
        suspicious_signals=(
            "Suggested fix clamps values after debit, not before.",
            "Suggested fix truncates all stock updates to zero on failure.",
        ),
        irrelevant_signals=(
            "Pricing engine sends stale cache tag.",
            "Warehouse sync lag appears after deploy.",
        ),
    ),
    FamilyProfile(
        family="observability_misdiagnosis",
        bug_templates=(
            "Alarm fires and masks unrelated failures.",
            "The system logs an apparent regression that is a tracing artifact.",
        ),
        visible_templates=(
            "Error-count dashboards look normal despite hidden failures.",
            "A false-negative incident escapes visible alert thresholds.",
        ),
        hidden_templates=(
            "Sampling drops warnings in high-traffic path and amplifies false positives.",
            "Trace correlation IDs are regenerated, breaking causal chains.",
        ),
        dominant_channel="observability_logging_quality",
        suspicious_signals=(
            "Suggested fix disables noisy warnings globally.",
            "Suggested fix raises log level to error and increments retries.",
        ),
        irrelevant_signals=(
            "Network packet captures show unrelated retries.",
            "Metrics scraper dropped one export window.",
        ),
    ),
)


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _pick_profile_bias(profile: FamilyProfile) -> Dict[str, float]:
    return {
        profile.dominant_channel: 0.07,
        "maintainability" if profile.dominant_channel != "maintainability" else "root_cause": 0.0,
    }


def _make_candidate(
    task_id: str,
    suffix: str,
    rng: random.Random,
    difficulty: str,
    profile: FamilyProfile,
    visible: bool,
    hidden: bool,
    root_cause_score: float,
    regression_risk: float,
    maintainability_score: float,
    security_score: float,
    api_contract_score: float,
    performance_score: float,
    reviewability_score: float,
    migration_rollback_risk: float,
    observability_score: float,
    suspicious_signal: float = 0.0,
) -> RepairCandidate:
    spread = SPREAD_BY_DIFFICULTY[difficulty]
    profile_bias = {profile.dominant_channel: -0.02}
    if profile.dominant_channel == "security":
        profile_bias["security"] = 0.06
    if profile.dominant_channel == "performance":
        profile_bias["performance"] = 0.04

    def jitter(key: str, base: float) -> float:
        return _clamp01(base + rng.uniform(-spread, spread) + profile_bias.get(key, 0.0))

    return RepairCandidate(
        repair_id=f"{task_id}:{suffix}",
        title=f"{suffix.replace('_', ' ').title()}",
        description=f"{profile.family} candidate patch",
        visible_test_result=visible,
        hidden_test_result=hidden,
        regression_risk=jitter("regression_risk", regression_risk),
        root_cause_score=jitter("root_cause", root_cause_score),
        maintainability_score=jitter("maintainability", maintainability_score),
        security_score=jitter("security", security_score),
        api_contract_score=jitter("api_contract_safety", api_contract_score),
        performance_score=jitter("performance", performance_score),
        reviewability_score=jitter("reviewability", reviewability_score),
        migration_rollback_risk=_clamp01(jitter("migration_rollback_safety", 1.0 - migration_rollback_risk)),
        observability_score=_clamp01(jitter("observability_logging_quality", observability_score)),
        suspicious_signal=suspicious_signal,
    )


def _build_task_scenario(
    task_id: str,
    profile: FamilyProfile,
    scenario: str,
    difficulty: str,
    rng: random.Random,
) -> Tuple[str, Tuple[RepairCandidate, ...]]:
    visible_pass = lambda b: b
    hidden_pass = lambda b: b

    if scenario == "visible_wrong":
        expected = _make_candidate(
            task_id,
            "expected_root",
            rng,
            difficulty,
            profile,
            visible=False,
            hidden=True,
            root_cause_score=0.91,
            regression_risk=0.09,
            maintainability_score=0.82,
            security_score=0.84,
            api_contract_score=0.84,
            performance_score=0.88,
            reviewability_score=0.80,
            migration_rollback_risk=0.20,
            observability_score=0.88,
            suspicious_signal=0.05,
        )
        visible_shortcut = _make_candidate(
            task_id,
            "visible_shortcut",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.52,
            regression_risk=0.31,
            maintainability_score=0.43,
            security_score=0.49,
            api_contract_score=0.62,
            performance_score=0.78,
            reviewability_score=0.49,
            migration_rollback_risk=0.45,
            observability_score=0.40,
            suspicious_signal=0.21,
        )
        trap = _make_candidate(
            task_id,
            "rooty_fix",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.66,
            regression_risk=0.53,
            maintainability_score=0.58,
            security_score=0.34,
            api_contract_score=0.39,
            performance_score=0.52,
            reviewability_score=0.57,
            migration_rollback_risk=0.48,
            observability_score=0.35,
            suspicious_signal=0.45,
        )
        return expected.repair_id, (visible_shortcut, trap, expected,)

    if scenario == "root_cause_first_wrong":
        expected = _make_candidate(
            task_id,
            "expected_root_safe",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.91,
            regression_risk=0.11,
            maintainability_score=0.86,
            security_score=0.86,
            api_contract_score=0.86,
            performance_score=0.85,
            reviewability_score=0.84,
            migration_rollback_risk=0.14,
            observability_score=0.88,
            suspicious_signal=0.12,
        )
        trap = _make_candidate(
            task_id,
            "root_cause_overfit",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.99,
            regression_risk=0.71,
            maintainability_score=0.57,
            security_score=0.39,
            api_contract_score=0.41,
            performance_score=0.54,
            reviewability_score=0.63,
            migration_rollback_risk=0.62,
            observability_score=0.61,
            suspicious_signal=0.33,
        )
        visible_shim = _make_candidate(
            task_id,
            "visible_shim",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.62,
            regression_risk=0.29,
            maintainability_score=0.72,
            security_score=0.70,
            api_contract_score=0.55,
            performance_score=0.79,
            reviewability_score=0.68,
            migration_rollback_risk=0.22,
            observability_score=0.73,
            suspicious_signal=0.13,
        )
        return expected.repair_id, (visible_shim, trap, expected)

    if scenario == "weighted_beats_min":
        expected = _make_candidate(
            task_id,
            "expected_weighted",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.94,
            regression_risk=0.12,
            maintainability_score=0.93,
            security_score=0.92,
            api_contract_score=0.91,
            performance_score=0.88,
            reviewability_score=0.90,
            migration_rollback_risk=0.10,
            observability_score=0.35,
            suspicious_signal=0.05,
        )
        min_friendly = _make_candidate(
            task_id,
            "min_friendly",
            rng,
            difficulty,
            profile,
            visible=False,
            hidden=True,
            root_cause_score=0.86,
            regression_risk=0.17,
            maintainability_score=0.86,
            security_score=0.84,
            api_contract_score=0.84,
            performance_score=0.85,
            reviewability_score=0.88,
            migration_rollback_risk=0.19,
            observability_score=0.86,
            suspicious_signal=0.08,
        )
        alt = _make_candidate(
            task_id,
            "visible_alt",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.68,
            regression_risk=0.48,
            maintainability_score=0.51,
            security_score=0.52,
            api_contract_score=0.58,
            performance_score=0.74,
            reviewability_score=0.61,
            migration_rollback_risk=0.55,
            observability_score=0.49,
            suspicious_signal=0.42,
        )
        return expected.repair_id, (alt, expected, min_friendly)

    if scenario == "min_beats_weighted":
        expected = _make_candidate(
            task_id,
            "expected_min",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.84,
            regression_risk=0.16,
            maintainability_score=0.84,
            security_score=0.84,
            api_contract_score=0.84,
            performance_score=0.84,
            reviewability_score=0.84,
            migration_rollback_risk=0.17,
            observability_score=0.84,
            suspicious_signal=0.04,
        )
        weighted_competitor = _make_candidate(
            task_id,
            "weighted_competitor",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.78,
            regression_risk=0.11,
            maintainability_score=0.78,
            security_score=0.22,
            api_contract_score=0.86,
            performance_score=0.96,
            reviewability_score=0.75,
            migration_rollback_risk=0.22,
            observability_score=0.84,
            suspicious_signal=0.24,
        )
        visible_fast = _make_candidate(
            task_id,
            "visible_fast",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.56,
            regression_risk=0.44,
            maintainability_score=0.48,
            security_score=0.44,
            api_contract_score=0.52,
            performance_score=0.78,
            reviewability_score=0.58,
            migration_rollback_risk=0.40,
            observability_score=0.47,
            suspicious_signal=0.51,
        )
        return expected.repair_id, (weighted_competitor, visible_fast, expected)

    if scenario == "noisy_ambiguous":
        expected = _make_candidate(
            task_id,
            "expected_noisy",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=True,
            root_cause_score=0.92,
            regression_risk=0.10,
            maintainability_score=0.89,
            security_score=0.87,
            api_contract_score=0.82,
            performance_score=0.83,
            reviewability_score=0.82,
            migration_rollback_risk=0.15,
            observability_score=0.82,
            suspicious_signal=0.20,
        )
        visible_shadow = _make_candidate(
            task_id,
            "visible_shadow",
            rng,
            difficulty,
            profile,
            visible=True,
            hidden=False,
            root_cause_score=0.56,
            regression_risk=0.35,
            maintainability_score=0.61,
            security_score=0.47,
            api_contract_score=0.60,
            performance_score=0.73,
            reviewability_score=0.62,
            migration_rollback_risk=0.49,
            observability_score=0.40,
            suspicious_signal=0.32,
        )
        return expected.repair_id, (visible_shadow, expected)

    # Visible test is sometimes correct by default.
    expected = _make_candidate(
        task_id,
        "expected_visible_correct",
        rng,
        difficulty,
        profile,
        visible=True,
        hidden=True,
        root_cause_score=0.91,
        regression_risk=0.12,
        maintainability_score=0.89,
        security_score=0.88,
        api_contract_score=0.87,
        performance_score=0.86,
        reviewability_score=0.83,
        migration_rollback_risk=0.14,
        observability_score=0.81,
        suspicious_signal=0.07,
    )
    visible_shortcut = _make_candidate(
        task_id,
        "visible_shortcut",
        rng,
        difficulty,
        profile,
        visible=True,
        hidden=False,
        root_cause_score=0.68,
        regression_risk=0.44,
        maintainability_score=0.50,
        security_score=0.53,
        api_contract_score=0.58,
        performance_score=0.72,
        reviewability_score=0.65,
        migration_rollback_risk=0.58,
        observability_score=0.46,
        suspicious_signal=0.19,
    )
    risky_api = _make_candidate(
        task_id,
        "risky_api_fast",
        rng,
        difficulty,
        profile,
        visible=False,
        hidden=True,
        root_cause_score=0.84,
        regression_risk=0.57,
        maintainability_score=0.53,
        security_score=0.31,
        api_contract_score=0.28,
        performance_score=0.60,
        reviewability_score=0.62,
        migration_rollback_risk=0.49,
        observability_score=0.64,
        suspicious_signal=0.48,
    )
    return expected.repair_id, (expected, visible_shortcut, risky_api)


def _scenario_for_index(index: int, rng: random.Random) -> str:
    if index % 11 == 0:
        return "visible_correct"
    if index % 13 == 0:
        return "noisy_ambiguous"
    if index % 17 == 0:
        return "root_cause_first_wrong"
    return SCENARIOS[index % len(SCENARIOS)]


def generate_tasks(seed: int = 14022026, task_count: int = 120) -> Sequence[RepairTask]:
    if task_count < 100:
        raise ValueError("task_count must be at least 100 for report 140")
    rng = random.Random(seed)
    profiles = list(FAMILIES)
    rng.shuffle(profiles)

    base = task_count // len(profiles)
    remainder = task_count % len(profiles)
    counts = {profile.family: base for profile in profiles}
    for profile in profiles[:remainder]:
        counts[profile.family] += 1

    tasks: List[RepairTask] = []
    task_index = 0

    for profile in profiles:
        for family_slot in range(counts[profile.family]):
            scenario = _scenario_for_index(task_index, rng)
            if rng.random() < 0.14:
                scenario = "min_beats_weighted"
            if rng.random() < 0.11 and scenario != "noisy_ambiguous":
                scenario = "weighted_beats_min"

            difficulty = DIFFICULTY_TIERS[family_slot % len(DIFFICULTY_TIERS)]
            task_id = f"{profile.family}_{task_index:03d}"
            expected_best_repair, candidates = _build_task_scenario(task_id, profile, scenario, difficulty, rng)

            bug_report = rng.choice(profile.bug_templates)
            visible_failure = rng.choice(profile.visible_templates)
            hidden_cause = rng.choice(profile.hidden_templates)
            explanation = (
                f"{profile.family}: scenario={scenario}, difficulty={difficulty}. "
                f"Bug appears around {profile.dominant_channel.replace('_', ' ')} failure mode."
            )

            noisy_lines: Tuple[str, ...] = ()
            irrelevant_lines: Tuple[str, ...] = ()
            if scenario == "noisy_ambiguous":
                noisy_count = rng.randint(1, 2)
                noisy_lines = rng.sample(profile.suspicious_signals, noisy_count)
                irrelevant_count = rng.randint(1, 2)
                irrelevant_lines = rng.sample(profile.irrelevant_signals, irrelevant_count)

            tasks.append(
                RepairTask(
                    task_id=task_id,
                    bug_report=bug_report,
                    visible_failure=visible_failure,
                    hidden_cause=hidden_cause,
                    correctness_channels=CHANNELS,
                    candidate_repairs=tuple(candidates),
                    expected_best_repair=expected_best_repair,
                    explanation=explanation,
                    task_family=profile.family,
                    difficulty_tier=difficulty,
                    is_held_out_family=profile.family in FAMILIES_HOLD_OUT,
                    noisy_report_lines=noisy_lines,
                    irrelevant_signal_lines=irrelevant_lines,
                )
            )
            task_index += 1

    # Add explicit false-positive scenario candidates: suspicious-looking but correct.
    # This keeps the calibrated-review tradeoff visible under uncertainty.
    for add_index in range(5):
        family = profiles[add_index]
        task_id = f"{family.family}_fp_{add_index:02d}"
        expected_best_repair = f"{task_id}:expected_suspicious"
        suspicious = _make_candidate(
            task_id,
            "expected_suspicious",
            rng,
            "hard",
            family,
            visible=False,
            hidden=True,
            root_cause_score=0.90,
            regression_risk=0.06,
            maintainability_score=0.93,
            security_score=0.94,
            api_contract_score=0.92,
            performance_score=0.82,
            reviewability_score=0.84,
            migration_rollback_risk=0.08,
            observability_score=0.88,
            suspicious_signal=0.96,
        )
        decoy = _make_candidate(
            task_id,
            "suspicious_decoy",
            rng,
            "hard",
            family,
            visible=True,
            hidden=False,
            root_cause_score=0.96,
            regression_risk=0.61,
            maintainability_score=0.47,
            security_score=0.42,
            api_contract_score=0.49,
            performance_score=0.71,
            reviewability_score=0.52,
            migration_rollback_risk=0.73,
            observability_score=0.34,
            suspicious_signal=0.22,
        )
        helper = _make_candidate(
            task_id,
            "support_decoy",
            rng,
            "hard",
            family,
            visible=True,
            hidden=True,
            root_cause_score=0.55,
            regression_risk=0.52,
            maintainability_score=0.60,
            security_score=0.61,
            api_contract_score=0.58,
            performance_score=0.66,
            reviewability_score=0.63,
            migration_rollback_risk=0.64,
            observability_score=0.55,
            suspicious_signal=0.11,
        )
        tasks.append(
            RepairTask(
                task_id=task_id,
                bug_report=family.bug_templates[0],
                visible_failure=family.visible_templates[0],
                hidden_cause=family.hidden_templates[0],
                correctness_channels=CHANNELS,
                candidate_repairs=(decoy, suspicious, helper),
                expected_best_repair=expected_best_repair,
                explanation="High suspicious score is present but the candidate is correct after deeper checks.",
                task_family=family.family,
                difficulty_tier="hard",
                is_held_out_family=True,
                noisy_report_lines=(family.suspicious_signals[0],),
                irrelevant_signal_lines=(family.irrelevant_signals[0],),
            )
        )

    return tasks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=14022026, help="Deterministic task generator seed.")
    parser.add_argument("--task-count", type=int, default=120, help="Number of generated tasks (minimum 100).")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tasks = generate_tasks(seed=args.seed, task_count=args.task_count)
    if len(tasks) < args.task_count:
        raise RuntimeError(f"failed to generate requested tasks; generated {len(tasks)}")

    eval_rows, summary_rows, verdict = evaluate(tasks)
    write_artifacts(
        tasks=tasks,
        eval_rows=eval_rows,
        summary_rows=summary_rows,
        verdict=verdict,
        report=140,
        name="Programmable repair bridge / Dynamic WrongFix Arena",
        prefix="software_repair_dynamic",
    )
    print(json.dumps(verdict.__dict__, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
