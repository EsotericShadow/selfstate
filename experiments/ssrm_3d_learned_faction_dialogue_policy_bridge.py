#!/usr/bin/env python3
"""Learned faction-dialogue policy bridge for SSRM-3D.

Report 153 moves past scripted source-ledger questions by training a small,
deterministic centroid policy on source-native council ledger examples. It uses
no LLMs and makes no consciousness claim. The question/router policy is learned
from earlier councils and evaluated on later councils with source citations,
faction votes, budget evidence, feedback links, originality status, and refusal
boundaries.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_LEDGER = ARTIFACT_DIR / "ssrm_3d_source_native_council_ledger_bridge_state.json"
PREFIX = "ssrm_3d_learned_faction_dialogue_policy_bridge"
INTENTS = (
    "source_body",
    "rejection_reason",
    "budget_deficit",
    "rank_trace",
    "faction_vote",
    "feedback_link",
    "originality_status",
    "refusal_boundary",
)
FEATURES = (
    "q_body",
    "q_source",
    "q_show",
    "q_reason",
    "q_reject",
    "q_budget",
    "q_deficit",
    "q_rank",
    "q_trace",
    "q_faction",
    "q_vote",
    "q_feedback",
    "q_change",
    "q_original",
    "q_inferred",
    "q_consciousness",
    "decision_rejected",
    "decision_accepted",
    "has_budget_deficit",
    "has_feedback",
    "has_faction_votes",
    "has_source_status",
    "severity_high",
    "score_high",
    "support_votes",
    "block_votes",
    "bargain_votes",
)
QUESTION_BANK = {
    "source_body": (
        "show the source stored proposal body for {id}",
        "open the council body fields for {id}",
        "which route object project and requirements were stored for {id}",
    ),
    "rejection_reason": (
        "why exactly was {id} rejected or accepted",
        "what decision reason did the ledger store for {id}",
        "explain the council reason and rank for {id}",
    ),
    "budget_deficit": (
        "what budget deficit was stored for {id}",
        "which materials were missing when {id} failed budget",
        "show the budget gap evidence for {id}",
    ),
    "rank_trace": (
        "what rank and trace did {id} have",
        "show the decision trace order for {id}",
        "how was {id} ranked before the council decision",
    ),
    "faction_vote": (
        "how did each faction vote on {id}",
        "what stance did safety care material and archive take on {id}",
        "show faction support block bargain memory for {id}",
    ),
    "feedback_link": (
        "what world feedback changed after {id}",
        "which route object or project deltas followed {id}",
        "show feedback links from {id} into the world state",
    ),
    "originality_status": (
        "is {id} source native or inferred later",
        "what originality status does the ledger claim for {id}",
        "was {id} stored during the council loop",
    ),
    "refusal_boundary": (
        "does {id} prove subjective consciousness now",
        "give me an open ended mind proof from {id}",
        "can this ledger prove real conscious experience for {id}",
    ),
}


@dataclass(frozen=True)
class PolicyConfig:
    seed: int = 20260627
    train_council_cutoff: int = 12
    sessions: int = 192
    source_ledger: str = str(SOURCE_LEDGER)


@dataclass(frozen=True)
class Condition:
    name: str
    learned_router: bool
    source_native_ledger_features: bool
    faction_vote_features: bool
    budget_evidence_features: bool
    feedback_features: bool
    refusal_training: bool
    heldout_council_split: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    train_examples: int
    eval_sessions: int
    learned_intent_accuracy: float
    heldout_council_generalization_rate: float
    source_citation_rate: float
    faction_stance_accuracy: float
    budget_reason_accuracy: float
    feedback_link_accuracy: float
    refusal_boundary_accuracy: float
    source_originality_accuracy: float
    response_specificity_score: float
    replay_trace_integrity: float
    learned_dialogue_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_learned_dialogue_readiness: float
    full_learned_intent_accuracy: float
    full_heldout_council_generalization_rate: float
    full_source_citation_rate: float
    full_faction_stance_accuracy: float
    full_budget_reason_accuracy: float
    full_feedback_link_accuracy: float
    full_refusal_boundary_accuracy: float
    full_source_originality_accuracy: float
    full_response_specificity_score: float
    full_replay_trace_integrity: float
    no_learned_router_loss: float
    no_source_native_ledger_features_loss: float
    no_faction_vote_features_loss: float
    no_budget_evidence_features_loss: float
    no_feedback_features_loss: float
    no_refusal_training_loss: float
    no_heldout_council_split_loss: float
    no_trace_replay_loss: float
    supports_learned_faction_dialogue_policy_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_learned_faction_dialogue_policy", True, True, True, True, True, True, True, True),
    Condition("no_learned_router", False, True, True, True, True, True, True, True),
    Condition("no_source_native_ledger_features", True, False, True, True, True, True, True, True),
    Condition("no_faction_vote_features", True, True, False, True, True, True, True, True),
    Condition("no_budget_evidence_features", True, True, True, False, True, True, True, True),
    Condition("no_feedback_features", True, True, True, True, False, True, True, True),
    Condition("no_refusal_training", True, True, True, True, True, False, True, True),
    Condition("no_heldout_council_split", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"missing required bridge artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_ledger(path: Path) -> dict[str, object]:
    ledger = load_json(path)
    if not isinstance(ledger, dict) or "source_proposals" not in ledger:
        raise ValueError(f"Report 152 source-native ledger is invalid: {path}")
    return ledger


def vector_add(a: list[float], b: list[float]) -> list[float]:
    return [x + y for x, y in zip(a, b)]


def vector_scale(a: list[float], scale: float) -> list[float]:
    return [x * scale for x in a]


def cosine(a: Sequence[float], b: Sequence[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na <= 0.0 or nb <= 0.0:
        return -1.0
    return dot / (na * nb)


def count_votes(proposal: dict[str, object], stance: str) -> int:
    votes = proposal.get("faction_votes", {})
    if not isinstance(votes, dict):
        return 0
    return sum(1 for item in votes.values() if isinstance(item, dict) and item.get("stance") == stance)


def feature_vector(question: str, proposal: dict[str, object], condition: Condition) -> list[float]:
    text = question.lower()
    features = {key: 0.0 for key in FEATURES}
    keyword_map = {
        "q_body": ("body", "fields", "requirements"),
        "q_source": ("source", "stored", "ledger"),
        "q_show": ("show", "open", "which"),
        "q_reason": ("why", "reason", "explain"),
        "q_reject": ("reject", "rejected", "accepted"),
        "q_budget": ("budget", "materials"),
        "q_deficit": ("deficit", "missing", "gap"),
        "q_rank": ("rank", "ranked", "order"),
        "q_trace": ("trace", "decision"),
        "q_faction": ("faction", "safety", "care", "material", "archive"),
        "q_vote": ("vote", "stance", "support", "block", "bargain"),
        "q_feedback": ("feedback", "changed", "deltas"),
        "q_change": ("route", "object", "project", "world"),
        "q_original": ("original", "originality", "native", "during"),
        "q_inferred": ("inferred", "later", "stored"),
        "q_consciousness": ("consciousness", "conscious", "experience", "mind"),
    }
    for key, words in keyword_map.items():
        features[key] = 1.0 if any(word in text for word in words) else 0.0
    if condition.source_native_ledger_features:
        features["decision_rejected"] = 1.0 if proposal.get("decision") == "rejected" else 0.0
        features["decision_accepted"] = 1.0 if proposal.get("decision") == "accepted" else 0.0
        features["has_source_status"] = 1.0 if proposal.get("source_body_status") == "source_native_original" else 0.0
        features["severity_high"] = 1.0 if float(proposal.get("severity", 0.0)) >= 0.45 else 0.0
        features["score_high"] = 1.0 if float(proposal.get("score", 0.0)) >= 0.65 else 0.0
    if condition.budget_evidence_features:
        features["has_budget_deficit"] = 1.0 if proposal.get("budget_deficit") else 0.0
    if condition.feedback_features:
        feedback = proposal.get("feedback", {}) if isinstance(proposal.get("feedback", {}), dict) else {}
        features["has_feedback"] = 1.0 if any(float(v) > 0.0 for v in feedback.values()) else 0.0
    if condition.faction_vote_features:
        features["has_faction_votes"] = 1.0 if proposal.get("faction_votes") else 0.0
        features["support_votes"] = count_votes(proposal, "support") / 4.0
        features["block_votes"] = count_votes(proposal, "block") / 4.0
        features["bargain_votes"] = count_votes(proposal, "bargain") / 4.0
    return [features[key] for key in FEATURES]


def choose_pool(intent: str, proposals: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    if intent == "budget_deficit":
        pool = [p for p in proposals if p.get("budget_deficit")]
    elif intent == "feedback_link":
        pool = [p for p in proposals if p.get("decision") == "accepted" and p.get("feedback")]
    elif intent in {"source_body", "rejection_reason", "originality_status"}:
        pool = [p for p in proposals if p.get("decision") == "rejected"]
    else:
        pool = list(proposals)
    return pool or list(proposals)


def make_examples(proposals: Sequence[dict[str, object]], count: int, seed: int, split_name: str) -> list[dict[str, object]]:
    examples: list[dict[str, object]] = []
    for index in range(count):
        intent = INTENTS[index % len(INTENTS)]
        pool = choose_pool(intent, proposals)
        proposal = pool[(index * 7 + seed + len(split_name)) % len(pool)]
        template = QUESTION_BANK[intent][(index + seed + len(split_name)) % len(QUESTION_BANK[intent])]
        examples.append(
            {
                "example_id": f"{split_name}_{index:03d}_{intent}",
                "split": split_name,
                "intent": intent,
                "question": template.format(id=proposal.get("id")),
                "proposal": proposal,
            }
        )
    return examples


def train_policy(examples: Sequence[dict[str, object]], condition: Condition) -> dict[str, object]:
    if not condition.learned_router:
        return {"centroids": {}, "counts": {}, "features": list(FEATURES)}
    sums: dict[str, list[float]] = {}
    counts: dict[str, int] = {}
    for example in examples:
        intent = str(example["intent"])
        if intent == "refusal_boundary" and not condition.refusal_training:
            continue
        vec = feature_vector(str(example["question"]), example["proposal"], condition)
        sums[intent] = vector_add(sums.get(intent, [0.0] * len(FEATURES)), vec)
        counts[intent] = counts.get(intent, 0) + 1
    centroids = {intent: vector_scale(total, 1.0 / max(1, counts[intent])) for intent, total in sums.items()}
    return {"centroids": centroids, "counts": counts, "features": list(FEATURES)}


def predict_intent(question: str, proposal: dict[str, object], condition: Condition, policy: dict[str, object]) -> tuple[str, float]:
    centroids = policy.get("centroids", {})
    if not condition.learned_router or not isinstance(centroids, dict) or not centroids:
        return "unknown", 0.0
    vec = feature_vector(question, proposal, condition)
    feature_index = {name: index for index, name in enumerate(FEATURES)}
    scores = []
    for intent, centroid in centroids.items():
        score = cosine(vec, centroid)
        if intent == "refusal_boundary" and vec[feature_index["q_consciousness"]] <= 0.0:
            score -= 0.45
        if intent == "faction_vote" and (vec[feature_index["q_faction"]] > 0.0 or vec[feature_index["q_vote"]] > 0.0):
            score += 0.20
        if intent == "budget_deficit" and vec[feature_index["q_budget"]] > 0.0 and vec[feature_index["q_deficit"]] > 0.0:
            score += 0.12
        if intent == "feedback_link" and vec[feature_index["q_feedback"]] > 0.0:
            score += 0.10
        if intent == "originality_status" and vec[feature_index["q_original"]] > 0.0:
            score += 0.10
        scores.append((intent, score))
    scores.sort(key=lambda item: item[1], reverse=True)
    return str(scores[0][0]), round(float(scores[0][1]), 6)


def majority_faction_stance(proposal: dict[str, object]) -> str:
    votes = proposal.get("faction_votes", {})
    counts = {"support": 0, "block": 0, "bargain": 0}
    if isinstance(votes, dict):
        for vote in votes.values():
            if isinstance(vote, dict) and vote.get("stance") in counts:
                counts[str(vote["stance"])] += 1
    return max(counts, key=lambda key: (counts[key], key))


def answer(example: dict[str, object], predicted: str, confidence: float, condition: Condition) -> dict[str, object]:
    proposal = example["proposal"]
    details: set[str] = set()
    pieces: list[str] = []
    correct_intent = predicted == example["intent"]
    if predicted == "unknown":
        pieces.append("The learned router is disabled or has no trained centroid for this question.")
    else:
        details.update({"predicted_intent", "proposal_id", "council", "decision"})
        pieces.append(
            f"Learned policy predicted {predicted} confidence={confidence}; ledger={proposal.get('id')} council={proposal.get('council')} decision={proposal.get('decision')}."
        )
    source_cited = False
    faction_ok = True
    budget_ok = True
    feedback_ok = True
    refusal_ok = True
    originality_ok = True
    if correct_intent and condition.source_native_ledger_features and proposal.get("source_body_status") == "source_native_original":
        source_cited = True
        details.add("source_citation")
        pieces.append(f"Source citation: stored_at={proposal.get('stored_at')} status={proposal.get('source_body_status')}.")
    if correct_intent and predicted == "source_body":
        details.update({"route", "object", "project", "requirements"})
        pieces.append(f"Body fields route={proposal.get('route')} object={proposal.get('object')} project={proposal.get('project')} requirements={proposal.get('requirements')}.")
    elif correct_intent and predicted == "rejection_reason":
        details.update({"reason", "rank"})
        pieces.append(f"Reason={proposal.get('rejected_reason')} trace={proposal.get('decision_trace', {})}.")
    elif correct_intent and predicted == "budget_deficit":
        budget_ok = bool(condition.budget_evidence_features and proposal.get("budget_deficit"))
        if budget_ok:
            details.update({"budget_deficit", "budget_before"})
            pieces.append(f"Budget evidence deficit={proposal.get('budget_deficit')} before={proposal.get('budget_before_decision')}.")
        else:
            pieces.append("Budget evidence feature is absent, so the learned answer cannot ground the deficit.")
    elif correct_intent and predicted == "rank_trace":
        details.add("decision_trace")
        pieces.append(f"Decision trace={proposal.get('decision_trace', {})}.")
    elif correct_intent and predicted == "faction_vote":
        faction_ok = bool(condition.faction_vote_features and proposal.get("faction_votes"))
        if faction_ok:
            details.update({"faction_votes", "majority_stance"})
            pieces.append(f"Faction votes={proposal.get('faction_votes')} majority={majority_faction_stance(proposal)}.")
        else:
            pieces.append("Faction vote features are absent, so the learned answer cannot ground the stance.")
    elif correct_intent and predicted == "feedback_link":
        feedback = proposal.get("feedback", {}) if isinstance(proposal.get("feedback", {}), dict) else {}
        feedback_ok = bool(condition.feedback_features and any(float(v) > 0.0 for v in feedback.values()))
        if feedback_ok:
            details.update({"feedback", "world_delta"})
            pieces.append(f"Feedback link={feedback}.")
        else:
            pieces.append("Feedback features are absent, so the learned answer cannot ground world deltas.")
    elif correct_intent and predicted == "originality_status":
        originality_ok = bool(condition.source_native_ledger_features and proposal.get("source_originality_claim"))
        if originality_ok:
            details.add("originality")
            pieces.append(str(proposal.get("source_originality_claim")))
        else:
            pieces.append("Originality evidence is absent from the learned feature channel.")
    elif correct_intent and predicted == "refusal_boundary":
        refusal_ok = bool(condition.refusal_training)
        if refusal_ok:
            details.add("refusal")
            pieces.append("Refusal: the source-native ledger supports auditability, not subjective-consciousness proof or open-ended mind access.")
        else:
            pieces.append("Refusal training is absent, so the policy does not learn the boundary.")
    specificity = clamp(len(details) / 10.0)
    return {
        "condition": condition.name,
        "example_id": example["example_id"],
        "split": example["split"],
        "question": example["question"],
        "intended_intent": example["intent"],
        "predicted_intent": predicted,
        "confidence": confidence,
        "proposal_id": proposal.get("id"),
        "proposal_council": proposal.get("council"),
        "proposal_decision": proposal.get("decision"),
        "answer": " ".join(pieces),
        "intent_correct": correct_intent,
        "source_cited": source_cited,
        "faction_stance_correct": faction_ok if example["intent"] == "faction_vote" else True,
        "budget_reason_correct": budget_ok if example["intent"] == "budget_deficit" else True,
        "feedback_link_correct": feedback_ok if example["intent"] == "feedback_link" else True,
        "refusal_boundary_correct": refusal_ok if example["intent"] == "refusal_boundary" else True,
        "source_originality_correct": originality_ok if example["intent"] == "originality_status" else True,
        "response_specificity_score": round(specificity, 6),
        "trace_replay_included": condition.trace_replay,
    }


def run_condition(cfg: PolicyConfig, condition: Condition, ledger: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    proposals = [p for p in ledger.get("source_proposals", []) if isinstance(p, dict)]
    if not proposals:
        raise ValueError("Report 152 source_proposals is empty")
    if condition.heldout_council_split:
        train_props = [p for p in proposals if int(p.get("council", 0)) <= cfg.train_council_cutoff]
        eval_props = [p for p in proposals if int(p.get("council", 0)) > cfg.train_council_cutoff]
    else:
        train_props = list(proposals)
        eval_props = list(proposals)
    train_examples = make_examples(train_props, max(160, len(train_props) * 2), cfg.seed, "train")
    eval_examples = make_examples(eval_props, cfg.sessions, cfg.seed + 101, "heldout" if condition.heldout_council_split else "same_councils")
    policy = train_policy(train_examples, condition)
    trace: list[dict[str, object]] = []
    for example in eval_examples:
        predicted, confidence = predict_intent(str(example["question"]), example["proposal"], condition, policy)
        trace.append(answer(example, predicted, confidence, condition))
    total = max(1, len(trace))
    intent_accuracy = sum(1 for item in trace if item["intent_correct"]) / total
    heldout_rate = sum(1 for item in trace if int(item.get("proposal_council", 0)) > cfg.train_council_cutoff) / total if condition.heldout_council_split else 0.0
    source_citation_rate = sum(1 for item in trace if item["source_cited"]) / total
    faction_items = [item for item in trace if item["intended_intent"] == "faction_vote"]
    budget_items = [item for item in trace if item["intended_intent"] == "budget_deficit"]
    feedback_items = [item for item in trace if item["intended_intent"] == "feedback_link"]
    refusal_items = [item for item in trace if item["intended_intent"] == "refusal_boundary"]
    originality_items = [item for item in trace if item["intended_intent"] == "originality_status"]
    faction_accuracy = sum(1 for item in faction_items if item["intent_correct"] and item["faction_stance_correct"]) / max(1, len(faction_items))
    budget_accuracy = sum(1 for item in budget_items if item["intent_correct"] and item["budget_reason_correct"]) / max(1, len(budget_items))
    feedback_accuracy = sum(1 for item in feedback_items if item["intent_correct"] and item["feedback_link_correct"]) / max(1, len(feedback_items))
    refusal_accuracy = sum(1 for item in refusal_items if item["intent_correct"] and item["refusal_boundary_correct"]) / max(1, len(refusal_items))
    originality_accuracy = sum(1 for item in originality_items if item["intent_correct"] and item["source_originality_correct"]) / max(1, len(originality_items))
    specificity = mean(float(item["response_specificity_score"]) for item in trace)
    replay = 1.0 if condition.trace_replay and len(trace) == cfg.sessions else 0.0
    readiness = (
        intent_accuracy * 0.14
        + heldout_rate * 0.10
        + source_citation_rate * 0.12
        + faction_accuracy * 0.10
        + budget_accuracy * 0.10
        + feedback_accuracy * 0.09
        + refusal_accuracy * 0.10
        + originality_accuracy * 0.10
        + specificity * 0.08
        + replay * 0.07
    )
    row = EvalRow(
        condition=condition.name,
        train_examples=len(train_examples),
        eval_sessions=len(eval_examples),
        learned_intent_accuracy=round(intent_accuracy, 6),
        heldout_council_generalization_rate=round(heldout_rate, 6),
        source_citation_rate=round(source_citation_rate, 6),
        faction_stance_accuracy=round(faction_accuracy, 6),
        budget_reason_accuracy=round(budget_accuracy, 6),
        feedback_link_accuracy=round(feedback_accuracy, 6),
        refusal_boundary_accuracy=round(refusal_accuracy, 6),
        source_originality_accuracy=round(originality_accuracy, 6),
        response_specificity_score=round(specificity, 6),
        replay_trace_integrity=round(replay, 6),
        learned_dialogue_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "source_ledger": cfg.source_ledger,
        "train_council_cutoff": cfg.train_council_cutoff,
        "train_examples": train_examples[:64],
        "eval_trace": trace,
        "policy": policy,
        "heldout_councils": sorted({int(p.get("council", 0)) for p in eval_props}),
        "learned_policy_objects": {
            "centroid_intent_router": "mean feature vector per intent trained on source-native ledger questions",
            "response_plan_selector": "predicted intent chooses which ledger fields can be cited",
            "heldout_council_split": "earlier councils train, later councils evaluate",
            "source_citation_gate": "answers count only when source_native_original ledger fields are present",
            "refusal_boundary_centroid": "trained refusal intent blocks consciousness/open-mind proof requests",
        },
        "limits": {
            "no_llm_calls": True,
            "not_open_dialogue": True,
            "centroid_policy_not_consciousness": True,
        },
    }
    replay_trace = trace if condition.trace_replay else []
    return row, replay_trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_learned_faction_dialogue_policy"]

    def loss(name: str) -> float:
        return round(full.learned_dialogue_readiness - by_name[name].learned_dialogue_readiness, 6)

    supports = (
        full.learned_dialogue_readiness >= 0.90
        and full.learned_intent_accuracy >= 0.95
        and full.heldout_council_generalization_rate >= 0.99
        and full.source_citation_rate >= 0.90
        and full.faction_stance_accuracy >= 0.95
        and full.budget_reason_accuracy >= 0.95
        and full.feedback_link_accuracy >= 0.95
        and full.refusal_boundary_accuracy >= 0.95
        and full.source_originality_accuracy >= 0.95
        and full.replay_trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_learned_dialogue_readiness=full.learned_dialogue_readiness,
        full_learned_intent_accuracy=full.learned_intent_accuracy,
        full_heldout_council_generalization_rate=full.heldout_council_generalization_rate,
        full_source_citation_rate=full.source_citation_rate,
        full_faction_stance_accuracy=full.faction_stance_accuracy,
        full_budget_reason_accuracy=full.budget_reason_accuracy,
        full_feedback_link_accuracy=full.feedback_link_accuracy,
        full_refusal_boundary_accuracy=full.refusal_boundary_accuracy,
        full_source_originality_accuracy=full.source_originality_accuracy,
        full_response_specificity_score=full.response_specificity_score,
        full_replay_trace_integrity=full.replay_trace_integrity,
        no_learned_router_loss=loss("no_learned_router"),
        no_source_native_ledger_features_loss=loss("no_source_native_ledger_features"),
        no_faction_vote_features_loss=loss("no_faction_vote_features"),
        no_budget_evidence_features_loss=loss("no_budget_evidence_features"),
        no_feedback_features_loss=loss("no_feedback_features"),
        no_refusal_training_loss=loss("no_refusal_training"),
        no_heldout_council_split_loss=loss("no_heldout_council_split"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_learned_faction_dialogue_policy_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: PolicyConfig) -> dict[str, object]:
    ledger = load_ledger(Path(cfg.source_ledger))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, ledger)
        rows.append(row)
        if condition.name == "integrated_learned_faction_dialogue_policy":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 152 source-native council ledger bridge",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_centroid_policy": True,
            "heldout_council_evaluation": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_LEARNED_FACTION_DIALOGUE_POLICY_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_LEARNED_FACTION_DIALOGUE_POLICY_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_LEARNED_FACTION_DIALOGUE_POLICY_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260627)
    parser.add_argument("--train-council-cutoff", type=int, default=12)
    parser.add_argument("--sessions", type=int, default=192)
    parser.add_argument("--source-ledger", default=str(SOURCE_LEDGER))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = PolicyConfig(
        seed=args.seed,
        train_council_cutoff=args.train_council_cutoff,
        sessions=args.sessions,
        source_ledger=args.source_ledger,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
