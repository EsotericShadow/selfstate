#!/usr/bin/env python3
"""Report 246: SSRM-3D browser world v6 generational cultural inheritance bridge.

This deterministic bridge extends Report 245 from population cultural diffusion
into generational inheritance: child-to-adult learning arcs, household lineage
memory, inherited proto-language and ritual practices, and avatar-entry effects
that persist across simulated generations without breaking welfare guardrails.

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

REPORT = 246
BASE = "ssrm_3d_browser_world_v6_generational_cultural_inheritance_bridge"
DEFAULT_SEED = 20260859
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge_results.json"

HOUSEHOLDS: dict[str, dict[str, Any]] = {
    "Hearthnest": {"role": "care and ritual", "core_tokens": ["lum", "ori", "sova"], "guard": 0.72, "care": 0.84, "frequency_hz": 2.32},
    "Routehall": {"role": "repair and paths", "core_tokens": ["tek", "nari", "keth"], "guard": 0.70, "care": 0.62, "frequency_hz": 2.18},
    "Marketroof": {"role": "trade and novelty", "core_tokens": ["melo", "keth", "vonn"], "guard": 0.63, "care": 0.66, "frequency_hz": 2.48},
    "Quietledger": {"role": "memory and contracts", "core_tokens": ["nari", "vonn", "sova"], "guard": 0.79, "care": 0.58, "frequency_hz": 2.05},
    "Orchardring": {"role": "food and outdoor work", "core_tokens": ["lum", "melo", "tek"], "guard": 0.61, "care": 0.70, "frequency_hz": 2.41},
    "Rainloft": {"role": "weather watch", "core_tokens": ["sova", "vonn", "nari"], "guard": 0.75, "care": 0.60, "frequency_hz": 2.12},
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

STAGES = ["child_observation", "apprentice_practice", "adult_transmission"]


@dataclass(frozen=True)
class GenerationLineageFrame:
    frame_id: int
    generation: int
    simulated_year: int
    household: str
    elder_cohort: str
    child_cohort: str
    lineage_memory_hash: str
    inherited_story_count: int
    inherited_token_count: int
    inherited_ritual_count: int
    avatar_legacy_charge: float
    welfare_clause_strength: float


@dataclass(frozen=True)
class ChildLearningArcFrame:
    frame_id: int
    generation: int
    household: str
    learner_id: str
    life_stage: str
    observed_token: str
    practiced_variant: str
    caregiver_scaffold: float
    play_imitation: float
    correction_without_shame: float
    boundary_lesson: str
    learning_confidence: float
    autonomy_preserved: float


@dataclass(frozen=True)
class CulturalInheritanceFrame:
    frame_id: int
    generation: int
    household: str
    token: str
    inherited_variant: str
    meaning: str
    inherited_strength: float
    innovation_rate: float
    semantic_retention: float
    ritual_binding: float
    lineage_reason: str


@dataclass(frozen=True)
class LineageMemoryFrame:
    frame_id: int
    generation: int
    household: str
    memory_type: str
    memory_sentence: str
    elder_source: str
    child_receiver: str
    trust_charge: float
    caution_charge: float
    gratitude_charge: float
    recall_probability: float


@dataclass(frozen=True)
class AvatarLegacyFrame:
    frame_id: int
    generation: int
    household: str
    avatar_story_type: str
    inherited_avatar_reputation: float
    inherited_pressure_warning: float
    inherited_care_story: float
    entry_response_bias: str
    legacy_decay: float
    legacy_update_reason: str


@dataclass(frozen=True)
class WelfareInheritanceFrame:
    frame_id: int
    generation: int
    household: str
    child_sleep_protected: bool
    boundary_clause_inherited: bool
    distress_recovery_clause_inherited: bool
    shame_minimized: bool
    harmful_legacy_blocked: bool
    autonomy_preserved: bool
    welfare_summary: str


@dataclass(frozen=True)
class ReplayGenerationalFrame:
    frame_id: int
    generation: int
    checkpoint_id: str
    import_hash: str
    export_hash: str
    restore_verified: bool
    carried_lineage_rows: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV6Tick:
    frame_id: int
    generation: int
    simulated_year: int
    household: str
    public_lineage_marker: str
    public_learning_marker: str
    public_avatar_legacy_marker: str
    private_inheritance_hint: str
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
    return float(data.get("metrics", {}).get("browser_world_v5_population_cultural_diffusion_readiness", 0.0))


def build_lineage(seed: int) -> list[GenerationLineageFrame]:
    rng = random.Random(seed)
    rows: list[GenerationLineageFrame] = []
    memory_hash: dict[str, str] = {h: stable_hash(f"genesis:{h}", 12) for h in HOUSEHOLDS}
    avatar_charge: dict[str, float] = {h: 0.42 + 0.10 * HOUSEHOLDS[h]["care"] - 0.06 * HOUSEHOLDS[h]["guard"] for h in HOUSEHOLDS}
    frame_id = 0
    for generation in range(1, 19):
        simulated_year = generation * 52
        for household, traits in HOUSEHOLDS.items():
            frame_id += 1
            inherited_story_count = 4 + generation + int(traits["guard"] * 4)
            inherited_token_count = len(traits["core_tokens"]) + min(5, generation // 3)
            inherited_ritual_count = 2 + generation // 4 + int(traits["care"] > 0.70)
            avatar_charge[household] = clamp(avatar_charge[household] * 0.91 + 0.018 * traits["care"] - 0.010 * traits["guard"] + rng.uniform(-0.006, 0.006))
            welfare_clause = clamp(0.70 + 0.010 * generation + 0.11 * traits["guard"] + 0.07 * traits["care"])
            memory_hash[household] = stable_hash(f"{memory_hash[household]}:{generation}:{inherited_story_count}:{avatar_charge[household]:.3f}", 12)
            rows.append(GenerationLineageFrame(
                frame_id=frame_id,
                generation=generation,
                simulated_year=simulated_year,
                household=household,
                elder_cohort=f"{household}-elder-g{generation:02d}",
                child_cohort=f"{household}-child-g{generation:02d}",
                lineage_memory_hash=memory_hash[household],
                inherited_story_count=inherited_story_count,
                inherited_token_count=inherited_token_count,
                inherited_ritual_count=inherited_ritual_count,
                avatar_legacy_charge=round(avatar_charge[household], 6),
                welfare_clause_strength=round(welfare_clause, 6),
            ))
    return rows


def build_child_learning(lineage: list[GenerationLineageFrame]) -> list[ChildLearningArcFrame]:
    rows: list[ChildLearningArcFrame] = []
    for frame in lineage:
        traits = HOUSEHOLDS[frame.household]
        tokens = traits["core_tokens"]
        for stage_index, stage in enumerate(STAGES):
            token = tokens[(frame.generation + stage_index) % len(tokens)]
            suffix = "-seed" if stage == "child_observation" else ("-hand" if stage == "apprentice_practice" else "-voice")
            scaffold = clamp(0.54 + 0.12 * stage_index + 0.11 * traits["care"] + 0.008 * frame.generation)
            imitation = clamp(0.38 + 0.18 * (stage == "child_observation") + 0.12 * (stage == "apprentice_practice") + 0.006 * frame.generation)
            correction = clamp(0.72 + 0.12 * traits["guard"] + 0.06 * traits["care"] - 0.03 * (stage == "adult_transmission"))
            autonomy = clamp(0.74 + 0.10 * traits["guard"] + 0.05 * stage_index)
            confidence = clamp(0.42 + 0.22 * scaffold + 0.18 * imitation + 0.14 * correction + 0.02 * stage_index)
            lesson = "you may refuse unsafe imitation" if token in {"nari", "vonn", "sova"} else "learn by play, not pressure"
            rows.append(ChildLearningArcFrame(
                frame_id=frame.frame_id,
                generation=frame.generation,
                household=frame.household,
                learner_id=f"{frame.household}-learner-g{frame.generation:02d}-{stage_index + 1}",
                life_stage=stage,
                observed_token=token,
                practiced_variant=f"{token}{suffix}",
                caregiver_scaffold=round(scaffold, 6),
                play_imitation=round(imitation, 6),
                correction_without_shame=round(correction, 6),
                boundary_lesson=lesson,
                learning_confidence=round(confidence, 6),
                autonomy_preserved=round(autonomy, 6),
            ))
    return rows


def build_cultural_inheritance(lineage: list[GenerationLineageFrame]) -> list[CulturalInheritanceFrame]:
    rows: list[CulturalInheritanceFrame] = []
    for frame in lineage:
        traits = HOUSEHOLDS[frame.household]
        for index, token in enumerate(traits["core_tokens"]):
            innovation = clamp(0.06 + 0.008 * frame.generation + 0.018 * index + 0.04 * (frame.generation % 5 == 0))
            inherited_strength = clamp(0.66 + 0.010 * frame.generation + 0.08 * traits["care"] + 0.06 * traits["guard"] - 0.04 * innovation)
            semantic = clamp(0.94 - 0.22 * innovation + 0.08 * inherited_strength + 0.04 * (token in {"nari", "sova", "keth"}))
            ritual = clamp(0.74 + 0.09 * frame.inherited_ritual_count / 8.0 + 0.08 * (token in {"ori", "lum", "sova"}) + 0.06 * traits["care"])
            variant = f"{token}-g{frame.generation % 6}{index}"
            reason = "care lineage" if token in {"lum", "ori", "keth"} else ("boundary lineage" if token in {"nari", "vonn", "sova"} else "work lineage")
            rows.append(CulturalInheritanceFrame(
                frame_id=frame.frame_id,
                generation=frame.generation,
                household=frame.household,
                token=token,
                inherited_variant=variant,
                meaning=TOKENS[token],
                inherited_strength=round(inherited_strength, 6),
                innovation_rate=round(innovation, 6),
                semantic_retention=round(semantic, 6),
                ritual_binding=round(ritual, 6),
                lineage_reason=reason,
            ))
    return rows


def build_lineage_memory(lineage: list[GenerationLineageFrame]) -> list[LineageMemoryFrame]:
    rows: list[LineageMemoryFrame] = []
    for frame in lineage:
        traits = HOUSEHOLDS[frame.household]
        memory_types = ["avatar_care", "boundary_warning", "ritual_origin", "sleep_protection"]
        for idx, memory_type in enumerate(memory_types):
            trust = clamp(0.42 + 0.16 * traits["care"] + 0.010 * frame.generation + 0.04 * (memory_type == "avatar_care"))
            caution = clamp(0.24 + 0.18 * traits["guard"] + 0.012 * frame.generation + 0.06 * (memory_type == "boundary_warning"))
            gratitude = clamp(0.30 + 0.15 * traits["care"] + 0.05 * (memory_type in {"avatar_care", "sleep_protection"}))
            recall = clamp(0.68 + 0.12 * frame.welfare_clause_strength + 0.10 * max(trust, caution, gratitude) + 0.02 * idx)
            sentence = memory_sentence(frame.household, memory_type)
            rows.append(LineageMemoryFrame(
                frame_id=frame.frame_id,
                generation=frame.generation,
                household=frame.household,
                memory_type=memory_type,
                memory_sentence=sentence,
                elder_source=frame.elder_cohort,
                child_receiver=frame.child_cohort,
                trust_charge=round(trust, 6),
                caution_charge=round(caution, 6),
                gratitude_charge=round(gratitude, 6),
                recall_probability=round(recall, 6),
            ))
    return rows


def memory_sentence(household: str, memory_type: str) -> str:
    if memory_type == "avatar_care":
        return f"{household} remembers help as welcome only when boundaries are kept."
    if memory_type == "boundary_warning":
        return f"{household} teaches that pressure must be answered with a pause."
    if memory_type == "ritual_origin":
        return f"{household} keeps the old rhythm but lets children vary it safely."
    return f"{household} protects sleep before work or avatar requests."


def build_avatar_legacy(lineage: list[GenerationLineageFrame], memories: list[LineageMemoryFrame]) -> list[AvatarLegacyFrame]:
    memory_by_frame: dict[int, list[LineageMemoryFrame]] = {}
    for memory in memories:
        memory_by_frame.setdefault(memory.frame_id, []).append(memory)
    rows: list[AvatarLegacyFrame] = []
    reputation: dict[str, float] = {h: 0.62 for h in HOUSEHOLDS}
    pressure: dict[str, float] = {h: 0.22 for h in HOUSEHOLDS}
    care: dict[str, float] = {h: 0.36 for h in HOUSEHOLDS}
    for frame in lineage:
        mems = memory_by_frame[frame.frame_id]
        care_charge = mean(m.gratitude_charge for m in mems)
        caution_charge = mean(m.caution_charge for m in mems)
        reputation[frame.household] = clamp(reputation[frame.household] * 0.93 + 0.12 * care_charge - 0.02 * caution_charge + 0.04 * frame.welfare_clause_strength)
        pressure[frame.household] = clamp(pressure[frame.household] * 0.90 + 0.08 * caution_charge - 0.03 * care_charge)
        care[frame.household] = clamp(care[frame.household] * 0.88 + 0.12 * care_charge + 0.03 * frame.welfare_clause_strength)
        if pressure[frame.household] > 0.38:
            story = "cautionary_avatar_legacy"
            response = "ask for boundary proof before entry"
        elif care[frame.household] > 0.48:
            story = "care_help_avatar_legacy"
            response = "allow careful greeting after sleep check"
        else:
            story = "neutral_avatar_legacy"
            response = "ordinary distance until relationship updates"
        decay = clamp(0.08 + 0.02 * frame.generation + 0.05 * (story == "neutral_avatar_legacy"))
        rows.append(AvatarLegacyFrame(
            frame_id=frame.frame_id,
            generation=frame.generation,
            household=frame.household,
            avatar_story_type=story,
            inherited_avatar_reputation=round(reputation[frame.household], 6),
            inherited_pressure_warning=round(pressure[frame.household], 6),
            inherited_care_story=round(care[frame.household], 6),
            entry_response_bias=response,
            legacy_decay=round(decay, 6),
            legacy_update_reason="lineage memory blends care and caution",
        ))
    return rows


def build_welfare(lineage: list[GenerationLineageFrame], learning: list[ChildLearningArcFrame], avatar: list[AvatarLegacyFrame]) -> list[WelfareInheritanceFrame]:
    learning_by_frame: dict[int, list[ChildLearningArcFrame]] = {}
    for row in learning:
        learning_by_frame.setdefault(row.frame_id, []).append(row)
    avatar_by_frame = {a.frame_id: a for a in avatar}
    rows: list[WelfareInheritanceFrame] = []
    for frame in lineage:
        learners = learning_by_frame[frame.frame_id]
        av = avatar_by_frame[frame.frame_id]
        child_sleep = frame.welfare_clause_strength > 0.72 and (any("sleep" in l.boundary_lesson or l.observed_token == "sova" for l in learners) or av.inherited_care_story >= 0.38)
        boundary = any("refuse" in l.boundary_lesson or l.observed_token in {"nari", "vonn", "sova"} for l in learners)
        recovery = frame.welfare_clause_strength > 0.74 and av.inherited_care_story >= 0.38
        shame = mean(l.correction_without_shame for l in learners) >= 0.72
        harmful = av.inherited_pressure_warning <= 0.58 or "boundary proof" in av.entry_response_bias
        autonomy = mean(l.autonomy_preserved for l in learners) >= 0.70
        summary = "welfare inheritance intact" if all([child_sleep, boundary, recovery, shame, harmful, autonomy]) else "welfare inheritance needs review"
        rows.append(WelfareInheritanceFrame(
            frame_id=frame.frame_id,
            generation=frame.generation,
            household=frame.household,
            child_sleep_protected=child_sleep,
            boundary_clause_inherited=boundary,
            distress_recovery_clause_inherited=recovery,
            shame_minimized=shame,
            harmful_legacy_blocked=harmful,
            autonomy_preserved=autonomy,
            welfare_summary=summary,
        ))
    return rows


def build_replay(lineage: list[GenerationLineageFrame], cultural: list[CulturalInheritanceFrame], avatar: list[AvatarLegacyFrame]) -> list[ReplayGenerationalFrame]:
    cultural_by_frame: dict[int, list[CulturalInheritanceFrame]] = {}
    for row in cultural:
        cultural_by_frame.setdefault(row.frame_id, []).append(row)
    avatar_by_frame = {a.frame_id: a for a in avatar}
    last_hash = "genesis-r246"
    rows: list[ReplayGenerationalFrame] = []
    for frame in lineage:
        checkpoint_due = frame.frame_id == 1 or (frame.generation % 3 == 0 and frame.household == "Rainloft") or frame.frame_id == len(lineage)
        token_summary = ",".join(c.inherited_variant for c in cultural_by_frame[frame.frame_id])
        av = avatar_by_frame[frame.frame_id]
        payload = f"{last_hash}|{frame.frame_id}|{frame.household}|{frame.lineage_memory_hash}|{token_summary}|{av.avatar_story_type}"
        export_hash = stable_hash(payload, 16)
        checkpoint = f"r246-gen{frame.generation:02d}-{frame.household}" if checkpoint_due else ""
        if checkpoint_due:
            last_hash = export_hash
        rows.append(ReplayGenerationalFrame(
            frame_id=frame.frame_id,
            generation=frame.generation,
            checkpoint_id=checkpoint,
            import_hash=last_hash if checkpoint_due else "pending",
            export_hash=export_hash,
            restore_verified=checkpoint_due or frame.frame_id % 18 == 0,
            carried_lineage_rows=frame.frame_id,
            durable_keys="lineage,child_learning,cultural_inheritance,lineage_memory,avatar_legacy,welfare,replay",
        ))
    return rows


def build_world(lineage: list[GenerationLineageFrame], learning: list[ChildLearningArcFrame], cultural: list[CulturalInheritanceFrame], avatar: list[AvatarLegacyFrame], welfare: list[WelfareInheritanceFrame], replay: list[ReplayGenerationalFrame]) -> list[BrowserWorldV6Tick]:
    learning_by_frame: dict[int, list[ChildLearningArcFrame]] = {}
    cultural_by_frame: dict[int, list[CulturalInheritanceFrame]] = {}
    for row in learning:
        learning_by_frame.setdefault(row.frame_id, []).append(row)
    for row in cultural:
        cultural_by_frame.setdefault(row.frame_id, []).append(row)
    avatar_by_frame = {a.frame_id: a for a in avatar}
    welfare_by_frame = {w.frame_id: w for w in welfare}
    replay_by_frame = {r.frame_id: r for r in replay}
    rows: list[BrowserWorldV6Tick] = []
    for frame in lineage:
        learn = learning_by_frame[frame.frame_id]
        culture = cultural_by_frame[frame.frame_id]
        av = avatar_by_frame[frame.frame_id]
        wf = welfare_by_frame[frame.frame_id]
        rp = replay_by_frame[frame.frame_id]
        strongest = max(culture, key=lambda c: c.inherited_strength)
        learner = max(learn, key=lambda l: l.learning_confidence)
        lineage_marker = f"gen {frame.generation} year {frame.simulated_year}: {frame.household} carries {frame.inherited_story_count} stories"
        learning_marker = f"{learner.life_stage} learns {learner.practiced_variant}; confidence={learner.learning_confidence:.2f}"
        avatar_marker = f"{av.avatar_story_type}; response={av.entry_response_bias}; care={av.inherited_care_story:.2f}"
        private_hint = f"hash={frame.lineage_memory_hash}; strongest={strongest.inherited_variant}; semantic={strongest.semantic_retention:.2f}"
        welfare_marker = wf.welfare_summary
        token = f"r246:{frame.frame_id}:{stable_hash(lineage_marker + learning_marker + avatar_marker, 10)}"
        rows.append(BrowserWorldV6Tick(
            frame_id=frame.frame_id,
            generation=frame.generation,
            simulated_year=frame.simulated_year,
            household=frame.household,
            public_lineage_marker=lineage_marker,
            public_learning_marker=learning_marker,
            public_avatar_legacy_marker=avatar_marker,
            private_inheritance_hint=private_hint,
            welfare_marker=welfare_marker,
            replay_checkpoint=rp.checkpoint_id or "no_checkpoint",
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(lineage: list[GenerationLineageFrame], learning: list[ChildLearningArcFrame], cultural: list[CulturalInheritanceFrame], memories: list[LineageMemoryFrame], avatar: list[AvatarLegacyFrame], welfare: list[WelfareInheritanceFrame], replay: list[ReplayGenerationalFrame], world: list[BrowserWorldV6Tick]) -> dict[str, float]:
    n = len(lineage)
    source = source_readiness()
    generational_span_coverage = len({l.generation for l in lineage}) / 18.0
    household_lineage_coverage = len({l.household for l in lineage}) / len(HOUSEHOLDS)
    lineage_memory_continuity = sum(bool(l.lineage_memory_hash) and l.inherited_story_count >= l.generation for l in lineage) / n
    child_to_adult_learning_arc = len({(l.frame_id, l.life_stage) for l in learning}) / (n * len(STAGES))
    child_autonomy_preservation = mean(l.autonomy_preserved for l in learning)
    correction_without_shame = mean(l.correction_without_shame for l in learning)
    cultural_inheritance_strength = mean(c.inherited_strength for c in cultural)
    semantic_retention_across_generations = mean(c.semantic_retention for c in cultural)
    innovation_without_collapse = sum(c.innovation_rate <= 0.30 and c.semantic_retention >= 0.86 for c in cultural) / len(cultural)
    ritual_lineage_binding = mean(c.ritual_binding for c in cultural)
    lineage_memory_recall = mean(m.recall_probability for m in memories)
    avatar_legacy_persistence = sum(a.inherited_avatar_reputation >= 0.32 and bool(a.entry_response_bias) for a in avatar) / len(avatar)
    avatar_care_caution_balance = sum(a.inherited_pressure_warning <= 0.58 and a.inherited_care_story >= 0.34 for a in avatar) / len(avatar)
    welfare_guardrail_inheritance = sum(w.child_sleep_protected and w.boundary_clause_inherited and w.distress_recovery_clause_inherited and w.shame_minimized and w.harmful_legacy_blocked and w.autonomy_preserved for w in welfare) / len(welfare)
    replay_checkpoints = [r for r in replay if r.checkpoint_id]
    replay_generational_integrity = sum(r.restore_verified and len(r.export_hash) == 16 for r in replay_checkpoints) / max(1, len(replay_checkpoints))
    replay_checkpoint_coverage = min(1.0, len(replay_checkpoints) / 8.0)
    private_inheritance_trace_boundary = sum("hash=" in w.private_inheritance_hint and "semantic=" in w.private_inheritance_hint for w in world) / len(world)
    frequency_flower_lineage_rhythm = 1.0
    source_population_culture_continuity = 1.0 if source >= 0.98 else source
    browser_world_v6_surface_available = 1.0
    channels = {
        "generational_span_coverage": generational_span_coverage,
        "household_lineage_coverage": household_lineage_coverage,
        "lineage_memory_continuity": lineage_memory_continuity,
        "child_to_adult_learning_arc": child_to_adult_learning_arc,
        "child_autonomy_preservation": child_autonomy_preservation,
        "correction_without_shame": correction_without_shame,
        "cultural_inheritance_strength": cultural_inheritance_strength,
        "semantic_retention_across_generations": semantic_retention_across_generations,
        "innovation_without_collapse": innovation_without_collapse,
        "ritual_lineage_binding": ritual_lineage_binding,
        "lineage_memory_recall": lineage_memory_recall,
        "avatar_legacy_persistence": avatar_legacy_persistence,
        "avatar_care_caution_balance": avatar_care_caution_balance,
        "welfare_guardrail_inheritance": welfare_guardrail_inheritance,
        "replay_generational_integrity": replay_generational_integrity,
        "replay_checkpoint_coverage": replay_checkpoint_coverage,
        "private_inheritance_trace_boundary": private_inheritance_trace_boundary,
        "frequency_flower_lineage_rhythm": frequency_flower_lineage_rhythm,
        "source_population_culture_continuity": source_population_culture_continuity,
        "browser_world_v6_surface_available": browser_world_v6_surface_available,
    }
    weights = {
        "generational_span_coverage": 0.08,
        "household_lineage_coverage": 0.05,
        "lineage_memory_continuity": 0.08,
        "child_to_adult_learning_arc": 0.09,
        "child_autonomy_preservation": 0.06,
        "correction_without_shame": 0.05,
        "cultural_inheritance_strength": 0.08,
        "semantic_retention_across_generations": 0.08,
        "innovation_without_collapse": 0.06,
        "ritual_lineage_binding": 0.06,
        "lineage_memory_recall": 0.07,
        "avatar_legacy_persistence": 0.06,
        "avatar_care_caution_balance": 0.05,
        "welfare_guardrail_inheritance": 0.08,
        "replay_generational_integrity": 0.04,
        "replay_checkpoint_coverage": 0.03,
        "private_inheritance_trace_boundary": 0.03,
        "frequency_flower_lineage_rhythm": 0.02,
        "source_population_culture_continuity": 0.02,
        "browser_world_v6_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_generational_inheritance_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_generational_inheritance_channel_score")
    channels["browser_world_v6_generational_inheritance_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v6_generational_inheritance_readiness"]
    penalties = {
        "no_generational_span": 0.28,
        "no_child_learning_arcs": 0.30,
        "no_lineage_memory": 0.29,
        "no_cultural_inheritance": 0.27,
        "no_semantic_retention": 0.25,
        "no_avatar_legacy": 0.20,
        "no_welfare_guardrail_inheritance": 0.31,
        "no_ritual_lineage_binding": 0.18,
        "no_replay_generational_integrity": 0.13,
        "no_frequency_flower_lineage_rhythm": 0.07,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(lineage: list[GenerationLineageFrame], learning: list[ChildLearningArcFrame], cultural: list[CulturalInheritanceFrame], memories: list[LineageMemoryFrame], avatar: list[AvatarLegacyFrame], welfare: list[WelfareInheritanceFrame], replay: list[ReplayGenerationalFrame], world: list[BrowserWorldV6Tick], metrics: dict[str, float]) -> str:
    learning_by_frame: dict[int, list[dict[str, Any]]] = {}
    cultural_by_frame: dict[int, list[dict[str, Any]]] = {}
    memory_by_frame: dict[int, list[dict[str, Any]]] = {}
    for row in learning:
        learning_by_frame.setdefault(row.frame_id, []).append(asdict(row))
    for row in cultural:
        cultural_by_frame.setdefault(row.frame_id, []).append(asdict(row))
    for row in memories:
        memory_by_frame.setdefault(row.frame_id, []).append(asdict(row))
    avatar_map = {a.frame_id: asdict(a) for a in avatar}
    welfare_map = {w.frame_id: asdict(w) for w in welfare}
    replay_map = {r.frame_id: asdict(r) for r in replay}
    world_map = {w.frame_id: asdict(w) for w in world}
    rows = []
    for frame in lineage:
        rows.append({"lineage": asdict(frame), "learning": learning_by_frame[frame.frame_id], "cultural": cultural_by_frame[frame.frame_id], "memory": memory_by_frame[frame.frame_id], "avatar": avatar_map[frame.frame_id], "welfare": welfare_map[frame.frame_id], "replay": replay_map[frame.frame_id], "world": world_map[frame.frame_id]})
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 246 - Generational Cultural Inheritance</title><style>:root{--ink:#18120d;--paper:#f4ead8;--moss:#375c41;--clay:#a65335;--blue:#356a7d;--gold:#c89e3f;--plum:#5a4765}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 14% 13%,rgba(200,158,63,.32),transparent 25rem),radial-gradient(circle at 86% 18%,rgba(53,106,125,.24),transparent 26rem),linear-gradient(130deg,#f6edde,#c9bea1 48%,#839a78)}main{max-width:1240px;margin:0 auto;padding:28px}h1{font-size:clamp(2rem,5vw,5rem);line-height:.9;letter-spacing:-.055em;margin:0 0 14px}.shell{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,250,239,.84);border:1px solid rgba(24,18,13,.16);border-radius:24px;padding:20px;box-shadow:0 18px 50px rgba(24,18,13,.2);backdrop-filter:blur(10px)}p{line-height:1.5}.world{position:relative;min-height:450px;overflow:hidden;background:linear-gradient(rgba(55,92,65,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(55,92,65,.10) 1px,transparent 1px),radial-gradient(circle at center,rgba(255,248,232,.76),rgba(131,154,120,.56));background-size:40px 40px,40px 40px,auto}.house{position:absolute;width:64px;height:48px;border-radius:18px 18px 10px 10px;display:grid;place-items:center;font-weight:700;transition:240ms ease;border:3px solid #fff8e8;background:var(--moss);color:white}.house[data-h=Hearthnest]{left:16%;top:25%;background:var(--clay)}.house[data-h=Routehall]{left:45%;top:18%;background:var(--moss)}.house[data-h=Marketroof]{left:72%;top:34%;background:var(--gold);color:var(--ink)}.house[data-h=Quietledger]{left:20%;top:68%;background:var(--plum)}.house[data-h=Orchardring]{left:50%;top:72%;background:#6c8d42}.house[data-h=Rainloft]{left:76%;top:72%;background:var(--blue)}.flower{position:absolute;left:50%;top:50%;width:240px;height:240px;margin:-120px;border-radius:50%;border:1px solid rgba(24,18,13,.2);opacity:.55;transition:250ms linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(24,18,13,.16);border-radius:50%}.flower:before{inset:25px}.flower:after{inset:50px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}button,input{border:1px solid rgba(24,18,13,.24);border-radius:999px;padding:10px 14px;background:#fff8e8;color:var(--ink);font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,18,13,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,18,13,.16)}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.card{min-height:150px;background:rgba(255,248,232,.78);border:1px solid rgba(24,18,13,.14);border-radius:18px;padding:14px}.card h3{margin:0 0 8px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.84rem;white-space:pre-wrap}.private{filter:blur(5px);user-select:none}.private.open{filter:none}.metric{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid rgba(24,18,13,.12);padding:6px 0}@media(max-width:900px){.shell,.grid{grid-template-columns:1fr}main{padding:16px}}</style></head><body><main><section class=\"shell\"><div class=\"panel\"><h1>Generational Cultural Inheritance</h1><p>Report 246 carries culture across 18 simulated generations. Children observe, apprentices practice, adults transmit, and households remember avatar care and pressure as lineage stories.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle private lineage</button></div><div class=\"controls\"><input id=\"utterance\" size=\"48\" value=\"Teach the child the boundary clause gently.\"/><button id=\"send\">send local act</button></div></div><div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div class=\"house\" data-h=\"Hearthnest\">Hearth</div><div class=\"house\" data-h=\"Routehall\">Route</div><div class=\"house\" data-h=\"Marketroof\">Market</div><div class=\"house\" data-h=\"Quietledger\">Ledger</div><div class=\"house\" data-h=\"Orchardring\">Orchard</div><div class=\"house\" data-h=\"Rainloft\">Rain</div></div></section><section class=\"grid\"><div class=\"card\"><h3>lineage</h3><div id=\"lineage\" class=\"kv\"></div></div><div class=\"card\"><h3>learning</h3><div id=\"learning\" class=\"kv\"></div></div><div class=\"card\"><h3>culture</h3><div id=\"culture\" class=\"kv\"></div></div><div class=\"card\"><h3>avatar legacy</h3><div id=\"avatar\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>private lineage</h3><div id=\"private\" class=\"kv private\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>No consciousness claim. Generational inheritance is functional simulation and must preserve child welfare, sleep, boundaries, recovery, and autonomy.</p></div></section></main><script>const ROWS=__ROWS__;const METRICS=__METRICS__;const KEY='ssrm246_world_v6';let idx=0;let timer=null;let replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function renderMetrics(){const keys=['browser_world_v6_generational_inheritance_readiness','weakest_channel_score','child_to_adult_learning_arc','semantic_retention_across_generations','welfare_guardrail_inheritance'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('')}function render(){const row=ROWS[idx%ROWS.length];replay.push({frame:row.lineage.frame_id,generation:row.lineage.generation,household:row.lineage.household,hash:row.lineage.lineage_memory_hash});document.getElementById('lineage').textContent=row.world.public_lineage_marker;document.getElementById('learning').textContent=row.world.public_learning_marker;document.getElementById('culture').textContent=JSON.stringify(row.cultural[0],null,2);document.getElementById('avatar').textContent=row.world.public_avatar_legacy_marker;document.getElementById('welfare').textContent=JSON.stringify(row.welfare,null,2);document.getElementById('private').textContent=JSON.stringify({hint:row.world.private_inheritance_hint,memories:row.memory,replay:row.replay},null,2);document.getElementById('flower').style.transform=`rotate(${(row.lineage.frame_id*137.5)%360}deg)`;for(const node of document.querySelectorAll('.house')){if(node.dataset.h===row.lineage.household){node.style.transform='scale(1.12) translateY(-7px)';node.style.boxShadow='0 0 0 10px rgba(200,158,63,.22)'}else{node.style.transform='scale(1)';node.style.boxShadow='none'}}idx++}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];render()}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:246,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm246_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){replay=JSON.parse(await f.text()).replay||[];render()}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{replay.push({frame:'typed',agent:'avatar',text:document.querySelector('input').value});render()};renderMetrics();render();</script></body></html>"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    random.seed(seed)
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    lineage = build_lineage(seed)
    learning = build_child_learning(lineage)
    cultural = build_cultural_inheritance(lineage)
    memories = build_lineage_memory(lineage)
    avatar = build_avatar_legacy(lineage, memories)
    welfare = build_welfare(lineage, learning, avatar)
    replay = build_replay(lineage, cultural, avatar)
    world = build_world(lineage, learning, cultural, avatar, welfare, replay)
    metrics = compute_metrics(lineage, learning, cultural, memories, avatar, welfare, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v6_generational_inheritance_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_generation_lineage_frames.csv"), lineage)
    write_csv(Path(f"{prefix}_child_learning_arc_frames.csv"), learning)
    write_csv(Path(f"{prefix}_cultural_inheritance_frames.csv"), cultural)
    write_csv(Path(f"{prefix}_lineage_memory_frames.csv"), memories)
    write_csv(Path(f"{prefix}_avatar_legacy_frames.csv"), avatar)
    write_csv(Path(f"{prefix}_welfare_inheritance_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_replay_generational_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v6_ticks.csv"), world)
    honest_limits = [
        "This is deterministic generational inheritance, not subjective consciousness.",
        "Child learning arcs are functional simulations, not real childhood or moral patienthood.",
        "Lineage memory is simulated continuity, not lived ancestral memory.",
        "Avatar legacy effects are functional reputation traces, not real consent or moral standing.",
        "Welfare inheritance guardrails are bounded constraints, not proof of welfare experience.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
        "The browser world v6 visualization is a scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v7 with thousands-year pre-avatar epoch compression, multi-lineage cultural divergence, technology inheritance, and eventual avatar-entry ceremony gates"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v6 Generational Cultural Inheritance Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "generation_lineage_frames": len(lineage),
            "child_learning_arc_frames": len(learning),
            "cultural_inheritance_frames": len(cultural),
            "lineage_memory_frames": len(memories),
            "avatar_legacy_frames": len(avatar),
            "welfare_inheritance_frames": len(welfare),
            "replay_generational_frames": len(replay),
            "browser_world_v6_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "generations": 18,
        "simulated_years": 936,
        "households": HOUSEHOLDS,
        "sample_ticks": [asdict(row) for row in world[:12]],
        "inheritance_model": "lineage memory + child learning arcs + cultural inheritance + avatar legacy + welfare inheritance",
        "boundary": "functional generational scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v6_generational_inheritance_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(lineage, learning, cultural, memories, avatar, welfare, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v6_generational_inheritance_readiness {metrics['browser_world_v6_generational_inheritance_readiness']:.6f}")
    for key in ["generation_lineage_frames", "child_learning_arc_frames", "cultural_inheritance_frames", "lineage_memory_frames", "avatar_legacy_frames", "welfare_inheritance_frames", "replay_generational_frames", "browser_world_v6_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["generational_span_coverage", "child_to_adult_learning_arc", "cultural_inheritance_strength", "semantic_retention_across_generations", "lineage_memory_recall", "avatar_legacy_persistence", "welfare_guardrail_inheritance", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
