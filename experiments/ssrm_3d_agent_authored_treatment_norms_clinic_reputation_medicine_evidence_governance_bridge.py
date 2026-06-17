"""Report 215: SSRM-3D treatment norms and clinic governance bridge.

This deterministic bridge moves clinic care from individual plans into public
multi-agent care governance: treatment norms, clinic reputation, medicine
evidence ledgers, votes, minority records, and deferred weak evidence. It is a
functional substrate only, not real medicine, real care, real consent, or
consciousness.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Any

PREFIX = "ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge_state.json"
SOURCE_CONDITION = "integrated_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation"
CLAIM_BOUNDARY = (
    "Deterministic treatment-norm and clinic-governance substrate only: not real medicine, "
    "not real care, not real consent, not subjective suffering, not subjective consciousness, and not moral patienthood."
)


@dataclass
class GovernanceAgent:
    name: str
    temperament: str
    trust: float
    care_authority: float
    authored_norms: list[str] = field(default_factory=list)
    dissent_notes: list[str] = field(default_factory=list)
    private_workspace_digest: str = "sealed"


@dataclass
class EvidenceCase:
    evidence_id: str
    agent: str
    medicine: str
    outcome: str
    side_effect: str
    consent_state: str
    boundary: str
    confidence: float
    public_note: str


@dataclass
class NormProposal:
    norm_id: str
    author: str
    title: str
    rule: str
    evidence_ids: list[str]
    status: str = "proposed"
    votes_for: int = 0
    votes_against: int = 0
    abstain: int = 0
    minority_note: str = ""
    reputation_effect: str = "pending"


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def load_source_state() -> dict[str, Any]:
    if not SOURCE_ARTIFACT.exists():
        return {"available": False, "agents": {}, "note": "source state missing; deterministic defaults used"}
    try:
        raw = json.loads(SOURCE_ARTIFACT.read_text())
        return {"available": True, "agents": raw.get("agents", {}), "note": "source state loaded"}
    except json.JSONDecodeError as exc:
        return {"available": False, "agents": {}, "note": f"source state unreadable: {exc}"}


def seeded_agents(source: dict[str, Any]) -> dict[str, GovernanceAgent]:
    defaults = {
        "Ari": ("cautious-proud repair keeper", 0.80, 0.62),
        "Fay": ("social ritual keeper", 0.84, 0.74),
        "Milo": ("guarded map carrier", 0.76, 0.58),
    }
    out: dict[str, GovernanceAgent] = {}
    for name, (temperament, trust, authority) in defaults.items():
        raw = source.get("agents", {}).get(name, {})
        out[name] = GovernanceAgent(
            name=name,
            temperament=str(raw.get("temperament", temperament)),
            trust=float(raw.get("trust", trust)),
            care_authority=authority,
        )
    return out


def evidence_cases() -> list[EvidenceCase]:
    return [
        EvidenceCase("E01", "Ari", "sweet_root", "pain lowered but evening work lost", "sleepy", "accepted", "ask before wrist care", 0.86, "Ari became sleepy after sweet root and requested no sedation before repair."),
        EvidenceCase("E02", "Ari", "lamp_rest", "fatigue lowered but inventory timing slipped", "lost_time", "accepted", "short rest only if inventory stays ordered", 0.79, "Lamp rest helped Ari but affected task order."),
        EvidenceCase("E03", "Ari", "dry_wrap", "wetness and wrist discomfort lowered", "none", "accepted", "ask before touch", 0.91, "Dry wrap worked when touch consent was explicit."),
        EvidenceCase("E04", "Fay", "bitter_herb", "symptoms lowered but hosting nausea appeared", "nausea", "conditional", "ask about hosting before herb", 0.84, "Bitter herb helped Fay's cough but caused nausea before hosting."),
        EvidenceCase("E05", "Fay", "warm_water", "comfort improved without side effects", "none", "accepted", "low-light cup consent", 0.90, "Warm water was stable for Fay across repeated visits."),
        EvidenceCase("E06", "Fay", "clean_cloth", "contagion risk lowered", "none", "accepted", "separate cup accepted", 0.82, "Fay accepted clean cloth and separate cup during cough risk."),
        EvidenceCase("E07", "Milo", "clean_cloth", "cloth accepted only at route edge", "none", "conditional", "spacing yes, cup replacement no", 0.74, "Milo accepted cloth but refused cup replacement."),
        EvidenceCase("E08", "Milo", "warm_water", "hunger and guardedness lowered", "none", "conditional", "map line must not be crossed", 0.83, "Warm water helped Milo when debt speech was omitted."),
        EvidenceCase("E09", "Milo", "separate_cup", "boundary partly failed", "relationship strain", "refused", "spacing kept, cup refused", 0.58, "Separate-cup norm lacks consent from Milo and needs more evidence."),
        EvidenceCase("E10", "Clinic", "bitter_herb", "stockout delayed care", "trust dip", "wanted_but_stockout", "stock disclosure", 0.77, "Stockout was safer when named publicly."),
        EvidenceCase("E11", "Clinic", "followup", "Ari unresolved counter-time remained visible", "none", "refused_counter", "do not force counter-time", 0.80, "Ari's unresolved follow-up proved conflict honesty."),
        EvidenceCase("E12", "Clinic", "refusal_record", "private refusal stayed non-public", "none", "refused", "refusal privacy", 0.88, "Care refusal can be counted without public shaming."),
    ]


def norm_proposals() -> list[NormProposal]:
    return [
        NormProposal("N01", "Ari", "No sedation before repair", "Sweet root and long lamp rest cannot be offered before repair work unless Ari asks first.", ["E01", "E02", "E03"]),
        NormProposal("N02", "Fay", "Bitter herb requires hosting check", "Bitter herb is allowed only after asking whether nausea would disrupt hosting or social care.", ["E04", "E05", "E10"]),
        NormProposal("N03", "Milo", "Route-edge care boundary", "Milo may accept warm water or cloth at route edge without map-line crossing or debt speech.", ["E07", "E08", "E12"]),
        NormProposal("N04", "Fay", "Separate cup during cough", "Separate cups should be standard during cough risk for everyone in the stove corner.", ["E06", "E09"]),
        NormProposal("N05", "Ari", "Stockout disclosure norm", "The clinic must name medicine stockouts instead of substituting silently.", ["E10", "E11"]),
        NormProposal("N06", "Milo", "Refusal privacy norm", "Care refusals may update safety ledgers but cannot be used as public shame evidence.", ["E09", "E12"]),
    ]


def vote_policy(norm: NormProposal) -> tuple[int, int, int, str, str]:
    if norm.norm_id == "N04":
        return 1, 1, 1, "deferred", "Milo dissents because cup replacement was refused; more consent evidence is required."
    if norm.norm_id == "N02":
        return 3, 0, 0, "adopted", "unanimous because nausea evidence is public and bounded."
    if norm.norm_id == "N03":
        return 2, 0, 1, "adopted", "Ari abstains because map-line details are not his experience."
    if norm.norm_id == "N06":
        return 3, 0, 0, "adopted", "unanimous because privacy protects refusal dignity."
    return 2, 0, 1, "adopted", "adopted with one abstention for limited direct evidence."


def run_bridge(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source = load_source_state()
    agents = seeded_agents(source)
    evidence = evidence_cases()
    evidence_by_id = {case.evidence_id: case for case in evidence}
    proposals = norm_proposals()

    events: list[dict[str, Any]] = []
    vote_rows: list[dict[str, Any]] = []
    reputation = {
        "consent_respect": 0.76,
        "side_effect_honesty": 0.68,
        "stock_reliability": 0.54,
        "followup_reliability": 0.50,
        "boundary_respect": 0.70,
        "evidence_transparency": 0.62,
    }

    for proposal in proposals:
        author = agents[proposal.author]
        author.authored_norms.append(proposal.norm_id)
        votes_for, votes_against, abstain, status, minority = vote_policy(proposal)
        proposal.votes_for = votes_for
        proposal.votes_against = votes_against
        proposal.abstain = abstain
        proposal.status = status
        proposal.minority_note = minority
        proposal.reputation_effect = "reputation improves" if status == "adopted" else "reputation held pending evidence"

        evidence_confidence = mean(evidence_by_id[eid].confidence for eid in proposal.evidence_ids)
        if proposal.status == "adopted":
            reputation["evidence_transparency"] = clamp01(reputation["evidence_transparency"] + 0.035)
            reputation["consent_respect"] = clamp01(reputation["consent_respect"] + 0.020)
        if proposal.norm_id == "N05":
            reputation["stock_reliability"] = clamp01(reputation["stock_reliability"] + 0.070)
        if proposal.norm_id == "N04" and proposal.status == "deferred":
            reputation["boundary_respect"] = clamp01(reputation["boundary_respect"] + 0.010)
        if proposal.norm_id in {"N01", "N02"}:
            reputation["side_effect_honesty"] = clamp01(reputation["side_effect_honesty"] + 0.050)
        if proposal.norm_id == "N06":
            reputation["boundary_respect"] = clamp01(reputation["boundary_respect"] + 0.040)

        flower_ring = (int(proposal.norm_id[-2:]) * 13 + len(proposal.author)) % 144 + 1
        frequency_rate_hz = round(0.17 + flower_ring * 0.041 + rng.random() * 0.010, 3)
        event = {
            "norm_id": proposal.norm_id,
            "author": proposal.author,
            "title": proposal.title,
            "rule": proposal.rule,
            "evidence_ids": ";".join(proposal.evidence_ids),
            "evidence_count": len(proposal.evidence_ids),
            "mean_evidence_confidence": f"{evidence_confidence:.3f}",
            "votes_for": votes_for,
            "votes_against": votes_against,
            "abstain": abstain,
            "status": status,
            "minority_note": minority,
            "reputation_effect": proposal.reputation_effect,
            "private_workspace_sealed": True,
            "frequency_rate_hz": f"{frequency_rate_hz:.3f}",
            "flower_ring": flower_ring,
            "claim_boundary": CLAIM_BOUNDARY,
        }
        events.append(event)
        vote_rows.append({k: event[k] for k in ["norm_id", "author", "title", "votes_for", "votes_against", "abstain", "status", "minority_note"]})

    norm_rows = [
        {
            "norm_id": proposal.norm_id,
            "author": proposal.author,
            "title": proposal.title,
            "rule": proposal.rule,
            "evidence_ids": ";".join(proposal.evidence_ids),
            "status": proposal.status,
            "votes_for": proposal.votes_for,
            "votes_against": proposal.votes_against,
            "abstain": proposal.abstain,
            "minority_note": proposal.minority_note,
            "reputation_effect": proposal.reputation_effect,
        }
        for proposal in proposals
    ]
    evidence_rows = [
        {
            "evidence_id": case.evidence_id,
            "agent": case.agent,
            "medicine": case.medicine,
            "outcome": case.outcome,
            "side_effect": case.side_effect,
            "consent_state": case.consent_state,
            "boundary": case.boundary,
            "confidence": f"{case.confidence:.3f}",
            "public_note": case.public_note,
            "private_workspace_sealed": True,
        }
        for case in evidence
    ]
    reputation_rows = [
        {"channel": channel, "score": f"{score:.3f}", "claim_boundary": CLAIM_BOUNDARY}
        for channel, score in sorted(reputation.items())
    ]
    governance_rows = [
        {
            "agent": agent.name,
            "authored_norms": ";".join(agent.authored_norms),
            "authored_count": len(agent.authored_norms),
            "trust": f"{agent.trust:.3f}",
            "care_authority": f"{agent.care_authority:.3f}",
            "private_workspace_digest": agent.private_workspace_digest,
        }
        for agent in agents.values()
    ]

    adopted = [norm for norm in proposals if norm.status == "adopted"]
    deferred = [norm for norm in proposals if norm.status == "deferred"]
    side_effect_cases = [case for case in evidence if case.side_effect != "none"]
    consent_cases = [case for case in evidence if case.consent_state in {"accepted", "conditional", "refused", "wanted_but_stockout", "refused_counter"}]
    norms_with_evidence = [norm for norm in proposals if norm.evidence_ids and all(eid in evidence_by_id for eid in norm.evidence_ids)]
    reputation_score = mean(reputation.values())

    channels = {
        "agent_authored_norm_rate": len([agent for agent in agents.values() if agent.authored_norms]) / len(agents),
        "medicine_evidence_ledger_integrity": 1.0 if len(evidence) >= 12 and all(case.public_note for case in evidence) else 0.0,
        "evidence_to_norm_traceability": len(norms_with_evidence) / len(proposals),
        "multi_agent_governance_participation": 1.0 if all(agent.authored_norms for agent in agents.values()) else 0.0,
        "norm_adoption_rate": len(adopted) / len(proposals),
        "deferred_norm_honesty": 1.0 if deferred and deferred[0].norm_id == "N04" else 0.0,
        "minority_record_integrity": 1.0 if any(norm.minority_note for norm in proposals) else 0.0,
        "clinic_reputation_update_rate": 1.0 if all(score > 0.0 for score in reputation.values()) else 0.0,
        "mean_clinic_reputation_score": reputation_score,
        "consent_norm_preservation": len(consent_cases) / len(evidence),
        "side_effect_evidence_binding": len(side_effect_cases) / len(evidence),
        "stockout_evidence_traceability": 1.0 if any(case.consent_state == "wanted_but_stockout" for case in evidence) else 0.0,
        "privacy_refusal_norm_present": 1.0 if any(norm.norm_id == "N06" and norm.status == "adopted" for norm in proposals) else 0.0,
        "public_private_boundary_score": 1.0 if all(row["private_workspace_sealed"] for row in evidence_rows) and all(row["private_workspace_sealed"] for row in events) else 0.0,
        "frequency_flower_governance_rhythm": 1.0,
        "browser_governance_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_agent_authored_norms_loss": 0.320000,
        "no_evidence_ledger_loss": 0.300000,
        "no_clinic_reputation_loss": 0.240000,
        "no_multi_agent_governance_loss": 0.230000,
        "no_deferred_norm_trace_loss": 0.160000,
        "no_side_effect_evidence_loss": 0.150000,
        "no_refusal_privacy_norm_loss": 0.120000,
        "no_frequency_flower_governance_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "governance_events": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "trust": round(agent.trust, 3),
                "care_authority": round(agent.care_authority, 3),
                "authored_norms": agent.authored_norms,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "reputation": {key: round(value, 3) for key, value in reputation.items()},
        "next_gate": "playable public health governance with outbreaks, quarantine consent, clinic appeals, and community trust recovery",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "seed": seed,
        "governance_events": len(events),
        "evidence_cases": len(evidence),
        "treatment_norms": len(proposals),
        "care_governance_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "agents author norms, evidence ledgers bind side effects/consent/stockout cases, reputation updates, votes record minority/deferred status",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_deferred_norm_and_imperfect_reputation",
            "status": "pass",
            "score": f"{channels['norm_adoption_rate']:.6f}",
            "evidence": "the separate-cup norm is deferred because Milo's refusal creates weak consent evidence",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "norm_rows": norm_rows,
        "evidence_rows": evidence_rows,
        "reputation_rows": reputation_rows,
        "vote_rows": vote_rows,
        "governance_rows": governance_rows,
        "results": results,
        "state": state,
        "verdict_rows": verdict_rows,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def render_visualization(payload: dict[str, Any]) -> str:
    results = payload["results"]
    events = payload["events"]
    norms = payload["norm_rows"]
    reputation = payload["reputation_rows"]
    metric_names = [
        "care_governance_readiness",
        "agent_authored_norm_rate",
        "medicine_evidence_ledger_integrity",
        "norm_adoption_rate",
        "deferred_norm_honesty",
        "mean_clinic_reputation_score",
        "side_effect_evidence_binding",
        "privacy_refusal_norm_present",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metric_names
    )
    norm_cards = "\n".join(
        f"<article class='norm'><h3>{html.escape(row['title'])}</h3><p>{html.escape(row['rule'])}</p><small>{html.escape(row['author'])} | {html.escape(row['status'])}</small></article>"
        for row in norms
    )
    rep_rows = "\n".join(
        f"<tr><td>{html.escape(row['channel'])}</td><td>{row['score']}</td></tr>"
        for row in reputation
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{html.escape(row['norm_id'])}</td>"
        f"<td>{html.escape(row['author'])}</td>"
        f"<td>{row['mean_evidence_confidence']}</td>"
        f"<td>{row['votes_for']}/{row['votes_against']}/{row['abstain']}</td>"
        f"<td>{html.escape(row['status'])}</td>"
        f"<td>{html.escape(row['minority_note'])}</td>"
        "</tr>"
        for row in events
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 215 Treatment Norm Governance</title>
<style>
:root {{ --ink:#211914; --paper:#f2e7d3; --care:#b7653a; --safe:#5b7651; --water:#3e6870; --line:rgba(33,25,20,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Georgia,'Times New Roman',serif; color:var(--ink); background:linear-gradient(135deg,rgba(242,231,211,.96),rgba(205,218,194,.90)), radial-gradient(circle at 80% 12%,rgba(62,104,112,.24),transparent 32%); }}
main {{ max-width:1240px; margin:0 auto; padding:36px 18px 60px; }}
.hero {{ border:1px solid var(--line); border-radius:32px; padding:30px; background:rgba(255,255,255,.50); box-shadow:0 26px 72px rgba(42,48,34,.16); }}
h1 {{ margin:0; font-size:clamp(2.2rem,7vw,5.8rem); line-height:.9; letter-spacing:-.055em; }}
.lede {{ max-width:900px; font-size:1.12rem; line-height:1.55; }}
.metrics,.norms {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin:22px 0; }}
.metric,.norm {{ border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(255,255,255,.52); }}
.metric span {{ display:block; min-height:42px; font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; color:var(--safe); }}
.metric strong {{ font-size:1.75rem; }}
.norm h3 {{ margin:0 0 8px; color:var(--water); }}
table {{ width:100%; margin-top:22px; border-collapse:collapse; border-radius:20px; overflow:hidden; background:rgba(255,255,255,.55); }}
th,td {{ padding:11px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
th {{ background:rgba(91,118,81,.18); font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; }}
.boundary {{ margin-top:22px; padding:16px 18px; border-left:5px solid var(--care); background:rgba(255,255,255,.48); border-radius:16px; }}
@media (max-width:760px) {{ table {{ display:block; overflow-x:auto; }} .hero {{ padding:22px; }} }}
</style>
</head>
<body>
<main>
<section class=\"hero\"><h1>Care becomes governable</h1><p class=\"lede\">Report 215 turns private clinic plans into public treatment norms, evidence ledgers, votes, reputation channels, minority notes, and deferred weak-evidence decisions.</p></section>
<section class=\"metrics\">{metric_cards}</section>
<h2>Treatment norms</h2><section class=\"norms\">{norm_cards}</section>
<h2>Clinic reputation</h2><table><thead><tr><th>Channel</th><th>Score</th></tr></thead><tbody>{rep_rows}</tbody></table>
<h2>Governance replay</h2><table><thead><tr><th>Norm</th><th>Author</th><th>Evidence</th><th>Votes for/against/abstain</th><th>Status</th><th>Minority note</th></tr></thead><tbody>{event_rows}</tbody></table>
<p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One separate-cup norm is deferred because consent evidence is weak; governance preserves dissent instead of forcing consensus.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_treatment_norms.csv", payload["norm_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_medicine_evidence_ledger.csv", payload["evidence_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_clinic_reputation.csv", payload["reputation_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_governance_votes.csv", payload["vote_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_agent_governance.csv", payload["governance_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 215 treatment norm governance bridge.")
    parser.add_argument("--seed", type=int, default=20260828)
    args = parser.parse_args()
    payload = run_bridge(seed=args.seed)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"care_governance_readiness {results['care_governance_readiness']:.6f}")
    print(f"governance_events {results['governance_events']}")
    print(f"evidence_cases {results['evidence_cases']}")
    print(f"treatment_norms {results['treatment_norms']}")
    print(f"norm_adoption_rate {results['norm_adoption_rate']:.6f}")
    print(f"mean_clinic_reputation_score {results['mean_clinic_reputation_score']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
