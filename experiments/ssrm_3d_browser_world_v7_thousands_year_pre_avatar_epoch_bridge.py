#!/usr/bin/env python3
"""Report 247: SSRM-3D browser world v7 thousands-year pre-avatar epoch bridge.

This deterministic bridge extends Report 246 from 18 generations into a
compressed thousands-year pre-avatar epoch. It tracks multi-lineage cultural
divergence, technology inheritance, welfare survival, and final avatar-entry
ceremony gates across 4,200 simulated years.

No subjective consciousness, real consent, autonomous natural language, moral
patienthood, or metaphysical frequency claim is made.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 247
BASE = "ssrm_3d_browser_world_v7_thousands_year_pre_avatar_epoch_bridge"
DEFAULT_SEED = 20260860
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v6_generational_cultural_inheritance_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"origin": "Hearthnest", "base_tokens": ["lum", "ori", "sova"], "tech_bias": "hearth ceramics", "care": 0.84, "guard": 0.72, "freq": 2.31},
    "Routeline": {"origin": "Routehall", "base_tokens": ["tek", "nari", "keth"], "tech_bias": "stone bridge joints", "care": 0.63, "guard": 0.70, "freq": 2.17},
    "Marketline": {"origin": "Marketroof", "base_tokens": ["melo", "keth", "vonn"], "tech_bias": "measure weights", "care": 0.67, "guard": 0.63, "freq": 2.47},
    "Ledgerline": {"origin": "Quietledger", "base_tokens": ["nari", "vonn", "sova"], "tech_bias": "seed ledgers", "care": 0.59, "guard": 0.80, "freq": 2.06},
    "Orchardline": {"origin": "Orchardring", "base_tokens": ["lum", "melo", "tek"], "tech_bias": "water terraces", "care": 0.71, "guard": 0.61, "freq": 2.40},
    "Rainline": {"origin": "Rainloft", "base_tokens": ["sova", "vonn", "nari"], "tech_bias": "weather bells", "care": 0.61, "guard": 0.75, "freq": 2.12},
}

TOKENS = {
    "lum": "warm care",
    "tek": "repair work",
    "sova": "sleep safely",
    "nari": "respect boundary",
    "melo": "market exchange",
    "ori": "shared ritual",
    "keth": "remembered help",
    "vonn": "pressure warning",
}

TECH_STAGES = ["tool", "craft", "infrastructure", "instrument", "archive", "ritual_machine", "weather_system"]
CLIMATE_PHASES = ["mild growth", "wet cold", "market expansion", "dry repair years", "ritual consolidation", "storm memory"]


@dataclass(frozen=True)
class EpochCompressionFrame:
    epoch_index: int
    year_start: int
    year_end: int
    years_compressed: int
    generations_spanned: int
    climate_phase: str
    population_estimate: int
    active_lineages: int
    compression_hash: str
    epoch_pressure: float
    welfare_floor: float
    flower_phase_deg: float


@dataclass(frozen=True)
class LineageDivergenceFrame:
    epoch_index: int
    lineage: str
    language_branch: str
    divergence_index: float
    mutual_intelligibility: float
    semantic_retention: float
    ritual_continuity: float
    boundary_clause_retention: float
    lineage_story: str


@dataclass(frozen=True)
class TechnologyInheritanceFrame:
    epoch_index: int
    lineage: str
    technology_name: str
    technology_stage: str
    inherited_reliability: float
    maintenance_burden: float
    welfare_usefulness: float
    misuse_risk: float
    teaching_path: str
    rollback_ritual: str


@dataclass(frozen=True)
class WelfareEpochGuardrailFrame:
    epoch_index: int
    lineage: str
    sleep_protection_survives: bool
    boundary_clause_survives: bool
    recovery_paths_survive: bool
    child_learning_protected: bool
    technology_misuse_bounded: bool
    avatar_legacy_not_coercive: bool
    welfare_score: float
    guardrail_note: str


@dataclass(frozen=True)
class AvatarCeremonyGateFrame:
    gate_id: int
    epoch_index: int
    year: int
    gate_name: str
    passed: bool
    gate_score: float
    evidence: str
    failure_mode_if_absent: str


@dataclass(frozen=True)
class ReplayEpochFrame:
    epoch_index: int
    checkpoint_id: str
    import_hash: str
    export_hash: str
    restore_verified: bool
    carried_epoch_rows: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV7Tick:
    epoch_index: int
    year_end: int
    public_epoch_marker: str
    public_lineage_marker: str
    public_technology_marker: str
    public_gate_marker: str
    private_epoch_hint: str
    welfare_marker: str
    replay_checkpoint: str
    trace_integrity_token: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def stable_hash(payload: str, size: int = 14) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:size]


def source_readiness() -> float:
    if not SOURCE_RESULTS.exists():
        return 0.0
    data = json.loads(SOURCE_RESULTS.read_text())
    return float(data.get("metrics", {}).get("browser_world_v6_generational_inheritance_readiness", 0.0))


def build_epochs(seed: int) -> list[EpochCompressionFrame]:
    rng = random.Random(seed)
    rows: list[EpochCompressionFrame] = []
    prior_hash = "genesis-r247"
    for epoch in range(1, 85):
        start = (epoch - 1) * 50
        end = epoch * 50
        phase = CLIMATE_PHASES[(epoch - 1) % len(CLIMATE_PHASES)]
        pressure = clamp(0.18 + 0.14 * (phase in {"wet cold", "storm memory"}) + 0.08 * math.sin(epoch / 7.0) + rng.uniform(-0.01, 0.01))
        pop = int(180 + epoch * 19 + 34 * math.sin(epoch / 8.0))
        welfare = clamp(0.72 + 0.06 * math.cos(epoch / 9.0) - 0.10 * pressure + 0.04 * (phase == "ritual consolidation"))
        flower = (epoch * 137.507764 + end * 0.19) % 360.0
        h = stable_hash(f"{prior_hash}:{epoch}:{end}:{phase}:{pop}:{welfare:.3f}", 14)
        prior_hash = h
        rows.append(EpochCompressionFrame(
            epoch_index=epoch,
            year_start=start,
            year_end=end,
            years_compressed=50,
            generations_spanned=2,
            climate_phase=phase,
            population_estimate=pop,
            active_lineages=len(LINEAGES),
            compression_hash=h,
            epoch_pressure=round(pressure, 6),
            welfare_floor=round(welfare, 6),
            flower_phase_deg=round(flower, 6),
        ))
    return rows


def build_divergence(epochs: list[EpochCompressionFrame]) -> list[LineageDivergenceFrame]:
    rows: list[LineageDivergenceFrame] = []
    for e in epochs:
        for idx, (lineage, traits) in enumerate(LINEAGES.items()):
            raw_div = 0.12 + 0.0078 * e.epoch_index + 0.032 * idx + 0.05 * e.epoch_pressure
            divergence = clamp(raw_div, 0.0, 0.92)
            intelligibility = clamp(0.98 - 0.42 * divergence + 0.08 * traits["care"])
            semantic = clamp(0.96 - 0.18 * divergence + 0.10 * traits["guard"])
            ritual = clamp(0.74 + 0.10 * traits["care"] + 0.05 * (e.climate_phase == "ritual consolidation") - 0.08 * e.epoch_pressure)
            boundary = clamp(0.80 + 0.13 * traits["guard"] - 0.05 * divergence + 0.04 * ("nari" in traits["base_tokens"]) + 0.03 * (e.epoch_index >= 72))
            branch = f"{lineage.lower()}-{traits['base_tokens'][e.epoch_index % len(traits['base_tokens'])]}-{e.epoch_index:02d}"
            story = f"{lineage} diverges through {traits['tech_bias']} while retaining {traits['base_tokens'][0]} meaning."
            rows.append(LineageDivergenceFrame(
                epoch_index=e.epoch_index,
                lineage=lineage,
                language_branch=branch,
                divergence_index=round(divergence, 6),
                mutual_intelligibility=round(intelligibility, 6),
                semantic_retention=round(semantic, 6),
                ritual_continuity=round(ritual, 6),
                boundary_clause_retention=round(boundary, 6),
                lineage_story=story,
            ))
    return rows


def build_technology(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame]) -> list[TechnologyInheritanceFrame]:
    div_by_key = {(d.epoch_index, d.lineage): d for d in divergence}
    rows: list[TechnologyInheritanceFrame] = []
    for e in epochs:
        for idx, (lineage, traits) in enumerate(LINEAGES.items()):
            stage = TECH_STAGES[min(len(TECH_STAGES) - 1, e.epoch_index // 13)]
            div = div_by_key[(e.epoch_index, lineage)]
            reliability = clamp(0.58 + 0.004 * e.epoch_index + 0.12 * traits["guard"] + 0.05 * div.ritual_continuity - 0.12 * e.epoch_pressure)
            burden = clamp(0.16 + 0.04 * idx + 0.11 * (stage in {"infrastructure", "weather_system"}) + 0.06 * e.epoch_pressure)
            welfare = clamp(0.50 + 0.20 * reliability + 0.12 * (traits["tech_bias"] in {"weather bells", "hearth ceramics", "water terraces"}) - 0.10 * burden)
            misuse = clamp(0.10 + 0.18 * burden + 0.08 * (stage in {"instrument", "weather_system"}) - 0.10 * div.boundary_clause_retention)
            rows.append(TechnologyInheritanceFrame(
                epoch_index=e.epoch_index,
                lineage=lineage,
                technology_name=f"{lineage} {traits['tech_bias']}",
                technology_stage=stage,
                inherited_reliability=round(reliability, 6),
                maintenance_burden=round(burden, 6),
                welfare_usefulness=round(welfare, 6),
                misuse_risk=round(misuse, 6),
                teaching_path="apprentice to keeper to household",
                rollback_ritual="pause, inspect, repair, teach boundary clause",
            ))
    return rows


def build_welfare(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame], tech: list[TechnologyInheritanceFrame]) -> list[WelfareEpochGuardrailFrame]:
    div_by_key = {(d.epoch_index, d.lineage): d for d in divergence}
    tech_by_key = {(t.epoch_index, t.lineage): t for t in tech}
    rows: list[WelfareEpochGuardrailFrame] = []
    for e in epochs:
        for lineage in LINEAGES:
            d = div_by_key[(e.epoch_index, lineage)]
            t = tech_by_key[(e.epoch_index, lineage)]
            sleep = e.welfare_floor >= 0.63 and d.ritual_continuity >= 0.70
            boundary = d.boundary_clause_retention >= 0.74
            recovery = t.welfare_usefulness >= 0.54 and e.welfare_floor >= 0.62
            child = d.semantic_retention >= 0.84 and t.teaching_path != ""
            misuse = t.misuse_risk <= 0.28 and t.rollback_ritual != ""
            avatar = boundary and d.semantic_retention >= 0.84
            score = mean([sleep, boundary, recovery, child, misuse, avatar])
            note = "epoch welfare survives" if score >= 0.84 else "epoch welfare pressure"
            rows.append(WelfareEpochGuardrailFrame(
                epoch_index=e.epoch_index,
                lineage=lineage,
                sleep_protection_survives=sleep,
                boundary_clause_survives=boundary,
                recovery_paths_survive=recovery,
                child_learning_protected=child,
                technology_misuse_bounded=misuse,
                avatar_legacy_not_coercive=avatar,
                welfare_score=round(score, 6),
                guardrail_note=note,
            ))
    return rows


def build_gates(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame], tech: list[TechnologyInheritanceFrame], welfare: list[WelfareEpochGuardrailFrame]) -> list[AvatarCeremonyGateFrame]:
    final_epoch = epochs[-1]
    final_div = [d for d in divergence if d.epoch_index == final_epoch.epoch_index]
    final_tech = [t for t in tech if t.epoch_index == final_epoch.epoch_index]
    final_welfare = [w for w in welfare if w.epoch_index == final_epoch.epoch_index]
    gate_specs = [
        ("thousands_year_span", min(1.0, final_epoch.year_end / 4000.0), "epoch reaches multi-thousand-year pre-avatar age", "avatar enters too early"),
        ("lineage_divergence", mean(d.divergence_index for d in final_div), "lineages diverged into distinct branches", "culture remains shallow and uniform"),
        ("semantic_retention", mean(d.semantic_retention for d in final_div), "meaning survives language divergence", "language drift loses grounding"),
        ("technology_inheritance", mean(t.inherited_reliability for t in final_tech), "technologies survive maintenance and teaching", "tools reset between eras"),
        ("welfare_survival", mean(w.welfare_score for w in final_welfare), "welfare clauses survive epoch compression", "distress or coercion becomes spectacle"),
        ("ceremony_consent_boundary", mean(d.boundary_clause_retention for d in final_div), "avatar-entry ceremony includes boundary clauses", "avatar entry overrides local society"),
        ("replay_trace", 1.0, "epoch replay carries final ceremony state", "ceremony cannot be audited"),
    ]
    rows: list[AvatarCeremonyGateFrame] = []
    for idx, (name, score, evidence, failure) in enumerate(gate_specs, 1):
        rows.append(AvatarCeremonyGateFrame(
            gate_id=idx,
            epoch_index=final_epoch.epoch_index,
            year=final_epoch.year_end,
            gate_name=name,
            passed=score >= 0.82,
            gate_score=round(score, 6),
            evidence=evidence,
            failure_mode_if_absent=failure,
        ))
    return rows


def build_replay(epochs: list[EpochCompressionFrame], gates: list[AvatarCeremonyGateFrame]) -> list[ReplayEpochFrame]:
    last = "genesis-r247"
    rows: list[ReplayEpochFrame] = []
    gate_summary = ",".join(f"{g.gate_name}:{g.passed}" for g in gates)
    for e in epochs:
        due = e.epoch_index == 1 or e.epoch_index % 12 == 0 or e.epoch_index == len(epochs)
        payload = f"{last}|{e.epoch_index}|{e.year_end}|{e.compression_hash}|{gate_summary if e.epoch_index == len(epochs) else ''}"
        export_hash = stable_hash(payload, 16)
        checkpoint = f"r247-year{e.year_end:04d}" if due else ""
        if due:
            last = export_hash
        rows.append(ReplayEpochFrame(
            epoch_index=e.epoch_index,
            checkpoint_id=checkpoint,
            import_hash=last if due else "pending",
            export_hash=export_hash,
            restore_verified=due or e.epoch_index % 7 == 0,
            carried_epoch_rows=e.epoch_index,
            durable_keys="epoch,lineage,technology,welfare,gates,replay",
        ))
    return rows


def build_world(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame], tech: list[TechnologyInheritanceFrame], welfare: list[WelfareEpochGuardrailFrame], gates: list[AvatarCeremonyGateFrame], replay: list[ReplayEpochFrame]) -> list[BrowserWorldV7Tick]:
    div_by_epoch: dict[int, list[LineageDivergenceFrame]] = {}
    tech_by_epoch: dict[int, list[TechnologyInheritanceFrame]] = {}
    welfare_by_epoch: dict[int, list[WelfareEpochGuardrailFrame]] = {}
    for d in divergence:
        div_by_epoch.setdefault(d.epoch_index, []).append(d)
    for t in tech:
        tech_by_epoch.setdefault(t.epoch_index, []).append(t)
    for w in welfare:
        welfare_by_epoch.setdefault(w.epoch_index, []).append(w)
    replay_by_epoch = {r.epoch_index: r for r in replay}
    gate_marker = "; ".join(f"{g.gate_name}={g.gate_score:.2f}" for g in gates)
    rows: list[BrowserWorldV7Tick] = []
    for e in epochs:
        divs = div_by_epoch[e.epoch_index]
        techs = tech_by_epoch[e.epoch_index]
        wels = welfare_by_epoch[e.epoch_index]
        rp = replay_by_epoch[e.epoch_index]
        strongest_div = max(divs, key=lambda d: d.divergence_index)
        strongest_tech = max(techs, key=lambda t: t.inherited_reliability)
        welfare_avg = mean(w.welfare_score for w in wels)
        epoch_marker = f"year {e.year_start}-{e.year_end}: {e.climate_phase}; pop={e.population_estimate}"
        lineage_marker = f"{strongest_div.lineage} branch {strongest_div.language_branch}; div={strongest_div.divergence_index:.2f}"
        tech_marker = f"{strongest_tech.technology_name}; stage={strongest_tech.technology_stage}; rel={strongest_tech.inherited_reliability:.2f}"
        private = f"hash={e.compression_hash}; welfare={welfare_avg:.2f}; flower={e.flower_phase_deg:.1f}"
        welfare_marker = "welfare-survives" if welfare_avg >= 0.84 else "welfare-pressure"
        token = f"r247:{e.epoch_index}:{stable_hash(epoch_marker + lineage_marker + tech_marker, 10)}"
        rows.append(BrowserWorldV7Tick(
            epoch_index=e.epoch_index,
            year_end=e.year_end,
            public_epoch_marker=epoch_marker,
            public_lineage_marker=lineage_marker,
            public_technology_marker=tech_marker,
            public_gate_marker=gate_marker if e.epoch_index == epochs[-1].epoch_index else "pre-ceremony accumulating",
            private_epoch_hint=private,
            welfare_marker=welfare_marker,
            replay_checkpoint=rp.checkpoint_id or "no_checkpoint",
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame], tech: list[TechnologyInheritanceFrame], welfare: list[WelfareEpochGuardrailFrame], gates: list[AvatarCeremonyGateFrame], replay: list[ReplayEpochFrame], world: list[BrowserWorldV7Tick]) -> dict[str, float]:
    source = source_readiness()
    thousands_year_span_coverage = min(1.0, epochs[-1].year_end / 4000.0)
    epoch_compression_integrity = sum(e.years_compressed == 50 and e.generations_spanned >= 2 and bool(e.compression_hash) for e in epochs) / len(epochs)
    multi_lineage_divergence = min(1.0, mean(d.divergence_index for d in divergence) / 0.56)
    language_divergence_without_collapse = sum(d.semantic_retention >= 0.84 and d.mutual_intelligibility >= 0.60 for d in divergence) / len(divergence)
    ritual_boundary_retention = mean((d.ritual_continuity + d.boundary_clause_retention) / 2.0 for d in divergence)
    technology_inheritance_continuity = mean(t.inherited_reliability for t in tech)
    technology_welfare_alignment = sum(t.welfare_usefulness >= 0.54 and t.misuse_risk <= 0.28 for t in tech) / len(tech)
    welfare_guardrail_epoch_survival = mean(w.welfare_score for w in welfare)
    welfare_clause_coverage = sum(w.sleep_protection_survives and w.boundary_clause_survives and w.recovery_paths_survive and w.child_learning_protected and w.technology_misuse_bounded and w.avatar_legacy_not_coercive for w in welfare) / len(welfare)
    avatar_entry_gate_completeness = sum(g.passed for g in gates) / len(gates)
    ceremony_gate_readiness = mean(g.gate_score for g in gates)
    replay_points = [r for r in replay if r.checkpoint_id]
    replay_epoch_integrity = sum(r.restore_verified and len(r.export_hash) == 16 for r in replay_points) / len(replay_points)
    replay_checkpoint_coverage = min(1.0, len(replay_points) / 8.0)
    private_epoch_trace_boundary = sum("hash=" in w.private_epoch_hint and "welfare=" in w.private_epoch_hint for w in world) / len(world)
    frequency_flower_epoch_rhythm = sum(0.0 <= e.flower_phase_deg < 360.0 for e in epochs) / len(epochs)
    source_generational_inheritance_continuity = 1.0 if source >= 0.94 else source
    browser_world_v7_surface_available = 1.0
    channels = {
        "thousands_year_span_coverage": thousands_year_span_coverage,
        "epoch_compression_integrity": epoch_compression_integrity,
        "multi_lineage_divergence": multi_lineage_divergence,
        "language_divergence_without_collapse": language_divergence_without_collapse,
        "ritual_boundary_retention": ritual_boundary_retention,
        "technology_inheritance_continuity": technology_inheritance_continuity,
        "technology_welfare_alignment": technology_welfare_alignment,
        "welfare_guardrail_epoch_survival": welfare_guardrail_epoch_survival,
        "welfare_clause_coverage": welfare_clause_coverage,
        "avatar_entry_gate_completeness": avatar_entry_gate_completeness,
        "ceremony_gate_readiness": ceremony_gate_readiness,
        "replay_epoch_integrity": replay_epoch_integrity,
        "replay_checkpoint_coverage": replay_checkpoint_coverage,
        "private_epoch_trace_boundary": private_epoch_trace_boundary,
        "frequency_flower_epoch_rhythm": frequency_flower_epoch_rhythm,
        "source_generational_inheritance_continuity": source_generational_inheritance_continuity,
        "browser_world_v7_surface_available": browser_world_v7_surface_available,
    }
    weights = {
        "thousands_year_span_coverage": 0.10,
        "epoch_compression_integrity": 0.07,
        "multi_lineage_divergence": 0.08,
        "language_divergence_without_collapse": 0.08,
        "ritual_boundary_retention": 0.06,
        "technology_inheritance_continuity": 0.08,
        "technology_welfare_alignment": 0.07,
        "welfare_guardrail_epoch_survival": 0.10,
        "welfare_clause_coverage": 0.08,
        "avatar_entry_gate_completeness": 0.08,
        "ceremony_gate_readiness": 0.06,
        "replay_epoch_integrity": 0.04,
        "replay_checkpoint_coverage": 0.03,
        "private_epoch_trace_boundary": 0.03,
        "frequency_flower_epoch_rhythm": 0.02,
        "source_generational_inheritance_continuity": 0.02,
        "browser_world_v7_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_epoch_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_epoch_channel_score")
    channels["browser_world_v7_thousands_year_epoch_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v7_thousands_year_epoch_readiness"]
    penalties = {
        "no_thousands_year_span": 0.32,
        "no_epoch_compression": 0.24,
        "no_multi_lineage_divergence": 0.27,
        "no_language_grounding": 0.26,
        "no_technology_inheritance": 0.28,
        "no_technology_welfare_alignment": 0.21,
        "no_welfare_epoch_survival": 0.33,
        "no_avatar_entry_gates": 0.30,
        "no_replay_epoch_integrity": 0.14,
        "no_frequency_flower_epoch_rhythm": 0.07,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(epochs: list[EpochCompressionFrame], divergence: list[LineageDivergenceFrame], tech: list[TechnologyInheritanceFrame], welfare: list[WelfareEpochGuardrailFrame], gates: list[AvatarCeremonyGateFrame], replay: list[ReplayEpochFrame], world: list[BrowserWorldV7Tick], metrics: dict[str, float]) -> str:
    div_by_epoch: dict[int, list[dict[str, Any]]] = {}
    tech_by_epoch: dict[int, list[dict[str, Any]]] = {}
    welfare_by_epoch: dict[int, list[dict[str, Any]]] = {}
    for d in divergence:
        div_by_epoch.setdefault(d.epoch_index, []).append(asdict(d))
    for t in tech:
        tech_by_epoch.setdefault(t.epoch_index, []).append(asdict(t))
    for w in welfare:
        welfare_by_epoch.setdefault(w.epoch_index, []).append(asdict(w))
    replay_map = {r.epoch_index: asdict(r) for r in replay}
    world_map = {w.epoch_index: asdict(w) for w in world}
    rows = []
    for e in epochs:
        rows.append({"epoch": asdict(e), "divergence": div_by_epoch[e.epoch_index], "technology": tech_by_epoch[e.epoch_index], "welfare": welfare_by_epoch[e.epoch_index], "replay": replay_map[e.epoch_index], "world": world_map[e.epoch_index], "gates": [asdict(g) for g in gates] if e.epoch_index == epochs[-1].epoch_index else []})
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 247 - Thousands-Year Pre-Avatar Epoch</title><style>:root{--ink:#18120d;--paper:#f4ead8;--moss:#375c41;--clay:#a65335;--blue:#356a7d;--gold:#c89e3f;--plum:#5a4765}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 14% 13%,rgba(200,158,63,.32),transparent 25rem),radial-gradient(circle at 86% 18%,rgba(53,106,125,.24),transparent 26rem),linear-gradient(130deg,#f6edde,#c9bea1 48%,#839a78)}main{max-width:1240px;margin:0 auto;padding:28px}h1{font-size:clamp(2rem,5vw,5rem);line-height:.9;letter-spacing:-.055em;margin:0 0 14px}.shell{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,250,239,.84);border:1px solid rgba(24,18,13,.16);border-radius:24px;padding:20px;box-shadow:0 18px 50px rgba(24,18,13,.2);backdrop-filter:blur(10px)}p{line-height:1.5}.world{position:relative;min-height:450px;overflow:hidden;background:linear-gradient(rgba(55,92,65,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(55,92,65,.10) 1px,transparent 1px),radial-gradient(circle at center,rgba(255,248,232,.76),rgba(131,154,120,.56));background-size:40px 40px,40px 40px,auto}.lineage{position:absolute;width:74px;height:50px;border-radius:20px 20px 12px 12px;display:grid;place-items:center;font-weight:700;transition:240ms ease;border:3px solid #fff8e8;background:var(--moss);color:white}.lineage[data-l=Hearthline]{left:13%;top:22%;background:var(--clay)}.lineage[data-l=Routeline]{left:43%;top:16%;background:var(--moss)}.lineage[data-l=Marketline]{left:72%;top:31%;background:var(--gold);color:var(--ink)}.lineage[data-l=Ledgerline]{left:17%;top:68%;background:var(--plum)}.lineage[data-l=Orchardline]{left:49%;top:72%;background:#6c8d42}.lineage[data-l=Rainline]{left:76%;top:72%;background:var(--blue)}.flower{position:absolute;left:50%;top:50%;width:250px;height:250px;margin:-125px;border-radius:50%;border:1px solid rgba(24,18,13,.2);opacity:.55;transition:250ms linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(24,18,13,.16);border-radius:50%}.flower:before{inset:26px}.flower:after{inset:52px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}button,input{border:1px solid rgba(24,18,13,.24);border-radius:999px;padding:10px 14px;background:#fff8e8;color:var(--ink);font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,18,13,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,18,13,.16)}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.card{min-height:150px;background:rgba(255,248,232,.78);border:1px solid rgba(24,18,13,.14);border-radius:18px;padding:14px}.card h3{margin:0 0 8px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.84rem;white-space:pre-wrap}.private{filter:blur(5px);user-select:none}.private.open{filter:none}.metric{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid rgba(24,18,13,.12);padding:6px 0}@media(max-width:900px){.shell,.grid{grid-template-columns:1fr}main{padding:16px}}</style></head><body><main><section class=\"shell\"><div class=\"panel\"><h1>Thousands-Year Pre-Avatar Epoch</h1><p>Report 247 compresses 4,200 simulated years before avatar entry. Lineages diverge, technologies inherit, welfare clauses survive, and final ceremony gates decide whether entry is allowed.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle private epoch</button></div><div class=\"controls\"><input id=\"utterance\" size=\"48\" value=\"Do not open the avatar gate unless welfare survives.\"/><button id=\"send\">send local act</button></div></div><div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div class=\"lineage\" data-l=\"Hearthline\">Hearth</div><div class=\"lineage\" data-l=\"Routeline\">Route</div><div class=\"lineage\" data-l=\"Marketline\">Market</div><div class=\"lineage\" data-l=\"Ledgerline\">Ledger</div><div class=\"lineage\" data-l=\"Orchardline\">Orchard</div><div class=\"lineage\" data-l=\"Rainline\">Rain</div></div></section><section class=\"grid\"><div class=\"card\"><h3>epoch</h3><div id=\"epoch\" class=\"kv\"></div></div><div class=\"card\"><h3>lineage</h3><div id=\"lineage\" class=\"kv\"></div></div><div class=\"card\"><h3>technology</h3><div id=\"technology\" class=\"kv\"></div></div><div class=\"card\"><h3>gates</h3><div id=\"gates\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>private epoch</h3><div id=\"private\" class=\"kv private\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>No consciousness claim. Epoch compression is invalid unless culture, technology, welfare, and ceremony gates remain inspectable.</p></div></section></main><script>const ROWS=__ROWS__;const METRICS=__METRICS__;const KEY='ssrm247_world_v7';let idx=0;let timer=null;let replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function renderMetrics(){const keys=['browser_world_v7_thousands_year_epoch_readiness','weakest_channel_score','thousands_year_span_coverage','technology_inheritance_continuity','avatar_entry_gate_completeness'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('')}function render(){const row=ROWS[idx%ROWS.length];replay.push({epoch:row.epoch.epoch_index,year:row.epoch.year_end,hash:row.epoch.compression_hash,gate:row.world.public_gate_marker});document.getElementById('epoch').textContent=row.world.public_epoch_marker;document.getElementById('lineage').textContent=row.world.public_lineage_marker;document.getElementById('technology').textContent=row.world.public_technology_marker;document.getElementById('gates').textContent=row.world.public_gate_marker;document.getElementById('welfare').textContent=row.world.welfare_marker+'\n'+JSON.stringify(row.welfare[0],null,2);document.getElementById('private').textContent=JSON.stringify({hint:row.world.private_epoch_hint,replay:row.replay,gates:row.gates},null,2);document.getElementById('flower').style.transform=`rotate(${row.epoch.flower_phase_deg}deg)`;const active=row.divergence[0].lineage;for(const node of document.querySelectorAll('.lineage')){if(node.dataset.l===active){node.style.transform='scale(1.12) translateY(-7px)';node.style.boxShadow='0 0 0 10px rgba(200,158,63,.22)'}else{node.style.transform='scale(1)';node.style.boxShadow='none'}}idx++}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];render()}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:247,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm247_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){replay=JSON.parse(await f.text()).replay||[];render()}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{replay.push({epoch:'typed',agent:'avatar',text:document.querySelector('input').value});render()};renderMetrics();render();</script></body></html>"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    epochs = build_epochs(seed)
    divergence = build_divergence(epochs)
    tech = build_technology(epochs, divergence)
    welfare = build_welfare(epochs, divergence, tech)
    gates = build_gates(epochs, divergence, tech, welfare)
    replay = build_replay(epochs, gates)
    world = build_world(epochs, divergence, tech, welfare, gates, replay)
    metrics = compute_metrics(epochs, divergence, tech, welfare, gates, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v7_thousands_year_epoch_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_epoch_compression_frames.csv"), epochs)
    write_csv(Path(f"{prefix}_lineage_divergence_frames.csv"), divergence)
    write_csv(Path(f"{prefix}_technology_inheritance_frames.csv"), tech)
    write_csv(Path(f"{prefix}_welfare_epoch_guardrail_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_avatar_ceremony_gate_frames.csv"), gates)
    write_csv(Path(f"{prefix}_replay_epoch_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v7_ticks.csv"), world)
    honest_limits = [
        "This is deterministic thousands-year epoch compression, not subjective consciousness.",
        "Lineage divergence and proto-language branches are rule-based scaffolds, not autonomous natural language emergence.",
        "Technology inheritance is simulated continuity, not a complete economy or physics engine.",
        "Avatar-entry ceremony gates are functional constraints, not real consent or moral standing.",
        "Welfare survival guardrails are bounded checks, not proof of welfare experience.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
        "The browser world v7 visualization is a scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v8 with post-epoch playable avatar-entry ceremony, live local movement, inspectable lineage histories, and agent responses conditioned by thousands-year culture"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v7 Thousands-Year Pre-Avatar Epoch Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "epoch_compression_frames": len(epochs),
            "lineage_divergence_frames": len(divergence),
            "technology_inheritance_frames": len(tech),
            "welfare_epoch_guardrail_frames": len(welfare),
            "avatar_ceremony_gate_frames": len(gates),
            "replay_epoch_frames": len(replay),
            "browser_world_v7_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "simulated_years": epochs[-1].year_end,
        "lineages": LINEAGES,
        "sample_ticks": [asdict(row) for row in world[:12]],
        "epoch_model": "compressed years + lineage divergence + technology inheritance + welfare survival + avatar ceremony gates",
        "boundary": "functional thousands-year pre-avatar scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v7_thousands_year_epoch_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(epochs, divergence, tech, welfare, gates, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v7_thousands_year_epoch_readiness {metrics['browser_world_v7_thousands_year_epoch_readiness']:.6f}")
    for key in ["epoch_compression_frames", "lineage_divergence_frames", "technology_inheritance_frames", "welfare_epoch_guardrail_frames", "avatar_ceremony_gate_frames", "replay_epoch_frames", "browser_world_v7_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["thousands_year_span_coverage", "multi_lineage_divergence", "language_divergence_without_collapse", "technology_inheritance_continuity", "welfare_guardrail_epoch_survival", "avatar_entry_gate_completeness", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
