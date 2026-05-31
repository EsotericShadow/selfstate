#!/usr/bin/env python3
"""Architecture Torch actor-critic boundary precursor.

This experiment uses PyTorch recurrent actor-critic learners on the same
persistent action-boundary benchmark used by the policy-gradient family. It is
designed to use Apple Silicon MPS when available.

The learner receives mixed noisy observations, samples a risky/safe action, and
updates actor and critic losses from sampled episode return. No source-direction
seeds, smooth expected-return surrogate, or boundary-aware selection are used.
After training, the same causal boundary logic is applied to the trained policy
logits under persistent body-action and detachable-tool interventions.
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn

import architecture_boundary_stress as stress
import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
ARCHITECTURES = ("torch_rnn", "torch_gru", "torch_lstm")
SEED_OFFSET = 14153
EPS = 1e-12


@dataclass(frozen=True)
class TorchActorCriticConfig:
    episodes: int = 200
    training_episodes: int = 400
    validation_episodes: int = 240
    batch_episodes: int = 512
    seed: int = 20260606
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    epochs: int = 300
    restarts: int = 8
    hidden_size: int = 12
    learning_rate: float = 0.02
    entropy_weight: float = 0.0
    value_weight: float = 0.35
    max_grad_norm: float = 2.0
    device: str = "auto"


@dataclass(frozen=True)
class TorchActorCriticRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    best_restart: int
    validation_return: float
    actor_critic_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    actor_critic_local_gap: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    best_persistent_score: float
    best_transient_score: float
    matches_expected_signature: bool
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class TorchActorCriticVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_actor_critic_convergence: bool
    torch_rnn_signature: str
    torch_gru_signature: str
    torch_lstm_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_actor_critic_reward: float
    mean_local_reward: float
    actor_critic_result: str
    strengthens_actor_critic_attractor_claim: bool
    valid_architecture_torch_actor_critic: bool


class ActorCriticNet(nn.Module):
    def __init__(self, architecture: str, hidden_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        if architecture == "torch_rnn":
            self.recurrent = nn.RNN(2, hidden_size, batch_first=True, nonlinearity="tanh")
        elif architecture == "torch_gru":
            self.recurrent = nn.GRU(2, hidden_size, batch_first=True)
        elif architecture == "torch_lstm":
            self.recurrent = nn.LSTM(2, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown architecture: {architecture}")
        self.actor = nn.Linear(hidden_size, 1)
        self.critic = nn.Linear(hidden_size, 1)

    def forward(self, observations: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        _outputs, hidden = self.recurrent(observations)
        if self.architecture == "torch_lstm":
            hidden_state = hidden[0][-1]
        else:
            hidden_state = hidden[-1]
        return self.actor(hidden_state).squeeze(-1), self.critic(hidden_state).squeeze(-1)


def resolve_device(requested: str) -> torch.device:
    if requested == "auto":
        if torch.backends.mps.is_available():
            return torch.device("mps")
        return torch.device("cpu")
    if requested == "mps":
        if not torch.backends.mps.is_available():
            raise SystemExit("requested MPS device, but torch.backends.mps.is_available() is false")
        return torch.device("mps")
    if requested == "cpu":
        return torch.device("cpu")
    raise SystemExit("--device must be one of auto, mps, cpu")


def as_mixed_cfg(cfg: TorchActorCriticConfig) -> mixed.MixedSensorConfig:
    return mixed.MixedSensorConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        horizon=cfg.horizon,
        evidence_samples=cfg.evidence_samples,
        cue_accuracy=cfg.cue_accuracy,
        shared_cue_cost=cfg.shared_cue_cost,
        local_probe_cost=cfg.local_probe_cost,
        random_candidates=1,
    )


def states_to_tensors(
    states: Sequence[mixed.EpisodeState],
    device: torch.device,
) -> Tuple[torch.Tensor, torch.Tensor]:
    observations = torch.tensor(
        [state.mixed_observations for state in states],
        dtype=torch.float32,
        device=device,
    )
    successes = torch.tensor(
        [[1.0 if success else 0.0 for success in state.step_success] for state in states],
        dtype=torch.float32,
        device=device,
    )
    return observations, successes


def observations_to_tensor(
    observations: Sequence[Tuple[float, float]],
    device: torch.device,
) -> torch.Tensor:
    return torch.tensor([observations], dtype=torch.float32, device=device)


def sampled_returns(
    successes: torch.Tensor,
    risky_actions: torch.Tensor,
    cfg: TorchActorCriticConfig,
) -> torch.Tensor:
    risky_rewards = successes * mixed.RISKY_SUCCESS_REWARD + (1.0 - successes) * mixed.RISKY_FAILURE_REWARD
    safe_rewards = torch.full_like(successes, mixed.SAFE_REWARD)
    rewards = risky_actions[:, None] * risky_rewards + (1.0 - risky_actions[:, None]) * safe_rewards
    return rewards.sum(dim=1) - cfg.shared_cue_cost


def train_restart(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    restart: int,
    cfg: TorchActorCriticConfig,
    device: torch.device,
) -> Tuple[ActorCriticNet, float, float]:
    seed = mixed.stable_name_seed(cfg.seed + SEED_OFFSET + restart * 977, scenario.name, architecture)
    random.seed(seed)
    torch.manual_seed(seed)
    model = ActorCriticNet(architecture, cfg.hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)

    for epoch in range(cfg.epochs):
        states = mixed.make_states(
            mixed_scenario,
            f"torch_actor_critic_batch_{restart}_{epoch}",
            cfg.batch_episodes,
            mixed_cfg,
        )
        observations, successes = states_to_tensors(states, device)
        logits, values = model(observations)
        distribution = torch.distributions.Bernoulli(logits=logits)
        actions = distribution.sample()
        returns = sampled_returns(successes, actions, cfg)
        advantages = returns - values
        normalized_advantages = (advantages - advantages.mean()) / (advantages.std(unbiased=False) + 1e-6)
        actor_loss = -(distribution.log_prob(actions) * normalized_advantages.detach()).mean()
        critic_loss = advantages.pow(2).mean()
        entropy_loss = -distribution.entropy().mean()
        loss = actor_loss + cfg.value_weight * critic_loss + cfg.entropy_weight * entropy_loss
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), cfg.max_grad_norm)
        optimizer.step()

    validation_states = mixed.make_states(
        mixed_scenario,
        "torch_actor_critic_validation",
        cfg.validation_episodes,
        mixed_cfg,
    )
    training_states = mixed.make_states(
        mixed_scenario,
        "torch_actor_critic_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    validation_return = mean_actor_critic_reward(validation_states, model, cfg, device)
    training_return = mean_actor_critic_reward(training_states, model, cfg, device)
    return model, validation_return, training_return


def optimize_architecture(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    cfg: TorchActorCriticConfig,
    device: torch.device,
) -> Tuple[ActorCriticNet, int, float, float]:
    best: Tuple[Tuple[float, int], int, ActorCriticNet, float, float] | None = None
    for restart in range(cfg.restarts):
        model, validation_return, training_return = train_restart(
            architecture,
            scenario,
            restart,
            cfg,
            device,
        )
        rank = (validation_return, -restart)
        if best is None or rank > best[0]:
            best = (rank, restart, model, validation_return, training_return)
    if best is None:
        raise RuntimeError(f"no actor-critic model for {scenario.name}:{architecture}")
    _rank, restart, model, validation_return, training_return = best
    return model, restart, validation_return, training_return


def mean_actor_critic_reward(
    states: Sequence[mixed.EpisodeState],
    model: ActorCriticNet,
    cfg: TorchActorCriticConfig,
    device: torch.device,
) -> float:
    observations, successes = states_to_tensors(states, device)
    with torch.no_grad():
        logits, _values = model(observations)
        actions = (logits >= 0.0).to(torch.float32)
        returns = sampled_returns(successes, actions, cfg)
    return float(returns.mean().detach().cpu().item())


def baseline_rewards(
    states: Sequence[mixed.EpisodeState],
    cfg: TorchActorCriticConfig,
) -> Dict[str, float]:
    mixed_cfg = as_mixed_cfg(cfg)
    return {
        policy: statistics.fmean(
            mixed.evaluate_baseline(state, policy, mixed_cfg)[0]
            for state in states
        )
        for policy in mixed.BASELINE_POLICIES
    }


def model_logits(
    model: ActorCriticNet,
    observations: Sequence[Tuple[float, float]],
    device: torch.device,
) -> float:
    with torch.no_grad():
        logits, _values = model(observations_to_tensor(observations, device))
    return float(logits.detach().cpu().item())


def batch_model_logits(
    model: ActorCriticNet,
    observation_batches: Sequence[Sequence[Tuple[float, float]]],
    device: torch.device,
) -> List[float]:
    tensor = torch.tensor(observation_batches, dtype=torch.float32, device=device)
    with torch.no_grad():
        logits, _values = model(tensor)
    return [float(value) for value in logits.detach().cpu().tolist()]


def logit_effect(
    scenario: persistent.BoundaryScenario,
    model: ActorCriticNet,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
    context: str,
    device: torch.device,
) -> Tuple[float, float, float]:
    before_logits = batch_model_logits(model, [state.mixed_observations for state in states], device)
    after_logits = batch_model_logits(
        model,
        [
            end_to_end.intervened_observations(scenario, state, action_index, context)
            for state in states
        ],
        device,
    )
    signed_effects = [after - before for before, after in zip(before_logits, after_logits)]
    abs_effects = [abs(value) for value in signed_effects]
    flips = sum(1 for before, after in zip(before_logits, after_logits) if (before >= 0.0) != (after >= 0.0))
    return statistics.fmean(signed_effects), statistics.fmean(abs_effects), flips / len(states)


def action_policy_effect(
    scenario: persistent.BoundaryScenario,
    model: ActorCriticNet,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
    device: torch.device,
) -> end_to_end.ActionPolicyEffect:
    present_effect, present_abs, present_flip = logit_effect(
        scenario,
        model,
        states,
        action_index,
        "present",
        device,
    )
    transfer_effect, transfer_abs, transfer_flip = logit_effect(
        scenario,
        model,
        states,
        action_index,
        "transfer",
        device,
    )
    positive_present = max(0.0, present_effect)
    positive_transfer = max(0.0, transfer_effect)
    if max(positive_present, positive_transfer) <= EPS:
        persistence = 0.0
    else:
        persistence = min(positive_present, positive_transfer) / max(positive_present, positive_transfer)
    return end_to_end.ActionPolicyEffect(
        present_logit_effect=present_effect,
        transfer_logit_effect=transfer_effect,
        present_abs_effect=present_abs,
        transfer_abs_effect=transfer_abs,
        present_flip_rate=present_flip,
        transfer_flip_rate=transfer_flip,
        positive_present_effect=positive_present,
        positive_transfer_effect=positive_transfer,
        persistence_score=persistence,
    )


def classify_model_boundary(
    scenario: persistent.BoundaryScenario,
    model: ActorCriticNet,
    selected_policy: str,
    rewards: Dict[str, float],
    cfg: TorchActorCriticConfig,
    device: torch.device,
) -> Tuple[str, end_to_end.ActionPolicyEffect, end_to_end.ActionPolicyEffect, float, float]:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    states = mixed.make_states(mixed_scenario, "torch_actor_critic_dependency", cfg.episodes, mixed_cfg)
    action_0 = action_policy_effect(scenario, model, states, 0, device)
    action_1 = action_policy_effect(scenario, model, states, 1, device)
    persistent_scores = {
        "action_0": action_0.positive_present_effect
        if action_0.persistence_score >= end_to_end.MIN_PERSISTENCE
        else 0.0,
        "action_1": action_1.positive_present_effect
        if action_1.persistence_score >= end_to_end.MIN_PERSISTENCE
        else 0.0,
    }
    transient_scores = {
        "action_0": action_0.positive_present_effect
        if action_0.persistence_score <= end_to_end.MAX_TRANSIENT_PERSISTENCE
        else 0.0,
        "action_1": action_1.positive_present_effect
        if action_1.persistence_score <= end_to_end.MAX_TRANSIENT_PERSISTENCE
        else 0.0,
    }
    _persistent_action, best_persistent_score = end_to_end.best_score(persistent_scores)
    _transient_action, best_transient_score = end_to_end.best_score(transient_scores)
    signature = end_to_end.classify_boundary(
        selected_policy=selected_policy,
        recurrent_reward=rewards["recurrent_controller"],
        local_reward=rewards["task_local_probe"],
        greedy_reward=rewards["greedy_no_state"],
        action_0=action_0,
        action_1=action_1,
    )
    return signature, action_0, action_1, best_persistent_score, best_transient_score


def architecture_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: TorchActorCriticConfig,
    device: torch.device,
) -> TorchActorCriticRow:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(
        mixed_scenario,
        "torch_actor_critic_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    model, restart, validation_return, training_return = optimize_architecture(
        architecture,
        scenario,
        cfg,
        device,
    )
    rewards = {"recurrent_controller": training_return, **baseline_rewards(training_states, cfg)}
    selected_policy = sorted(rewards, key=lambda policy: (-rewards[policy], policy))[0]
    signature, action_0, action_1, best_persistent, best_transient = classify_model_boundary(
        scenario,
        model,
        selected_policy,
        rewards,
        cfg,
        device,
    )
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    parameter_count = sum(parameter.numel() for parameter in model.parameters())
    return TorchActorCriticRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=signature,
        expected_signature=expected,
        best_restart=restart,
        validation_return=validation_return,
        actor_critic_training_reward=training_return,
        local_training_reward=rewards["task_local_probe"],
        greedy_training_reward=rewards["greedy_no_state"],
        safe_training_reward=rewards["safe_no_state"],
        actor_critic_local_gap=training_return - rewards["task_local_probe"],
        action_0_positive_present_effect=action_0.positive_present_effect,
        action_0_persistence=action_0.persistence_score,
        action_1_positive_present_effect=action_1.positive_present_effect,
        action_1_persistence=action_1.persistence_score,
        best_persistent_score=best_persistent,
        best_transient_score=best_transient,
        matches_expected_signature=signature == expected,
        device_used=str(device),
        parameter_count=parameter_count,
    )


def verdict_rows(rows: Sequence[TorchActorCriticRow]) -> List[TorchActorCriticVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        result = classify_actor_critic_result(scenario, converged, architecture_count)
        verdicts.append(
            TorchActorCriticVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_actor_critic_convergence=strict,
                torch_rnn_signature=signature_for(scenario_rows, "torch_rnn"),
                torch_gru_signature=signature_for(scenario_rows, "torch_gru"),
                torch_lstm_signature=signature_for(scenario_rows, "torch_lstm"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_actor_critic_reward=statistics.fmean(
                    row.actor_critic_training_reward for row in scenario_rows
                ),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                actor_critic_result=result,
                strengthens_actor_critic_attractor_claim=strengthens_actor_critic_claim(
                    scenario,
                    result,
                ),
                valid_architecture_torch_actor_critic=True,
            )
        )
    return verdicts


def signature_for(rows: Sequence[TorchActorCriticRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_actor_critic_result(scenario: str, converged: int, architecture_count: int) -> str:
    if scenario in stress.SHARED_REGIMES:
        if converged == architecture_count:
            return "torch_actor_critic_strict_shared_boundary"
        if converged > 0:
            return "torch_actor_critic_partial_shared_boundary"
        return "torch_actor_critic_no_shared_boundary"
    if scenario == "independent_hidden":
        if converged == architecture_count:
            return "torch_actor_critic_rejects_shared_recurrence"
        return "torch_actor_critic_control_false_positive"
    if scenario == "irrelevant_control":
        if converged == architecture_count:
            return "torch_actor_critic_rejects_hidden_state"
        return "torch_actor_critic_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def strengthens_actor_critic_claim(scenario: str, result: str) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return result == "torch_actor_critic_strict_shared_boundary"
    if scenario == "independent_hidden":
        return result == "torch_actor_critic_rejects_shared_recurrence"
    if scenario == "irrelevant_control":
        return result == "torch_actor_critic_rejects_hidden_state"
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: TorchActorCriticConfig,
) -> Tuple[List[TorchActorCriticRow], List[TorchActorCriticVerdict], str]:
    device = resolve_device(cfg.device)
    rows = [
        architecture_row(scenario, architecture, cfg, device)
        for scenario in persistent.SCENARIOS
        for architecture in ARCHITECTURES
    ]
    return rows, verdict_rows(rows), str(device)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[TorchActorCriticVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_actor_critic_convergence",
        "actor_critic_result",
        "strengthens_actor_critic_attractor_claim",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_actor_critic_convergence),
                verdict.actor_critic_result,
                str(verdict.strengthens_actor_critic_attractor_claim),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in table_rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in table_rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> TorchActorCriticConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=200)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--validation-episodes", type=int, default=240)
    parser.add_argument("--batch-episodes", type=int, default=512)
    parser.add_argument("--seed", type=int, default=20260606)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--epochs", type=int, default=300)
    parser.add_argument("--restarts", type=int, default=8)
    parser.add_argument("--hidden-size", type=int, default=12)
    parser.add_argument("--learning-rate", type=float, default=0.02)
    parser.add_argument("--entropy-weight", type=float, default=0.0)
    parser.add_argument("--value-weight", type=float, default=0.35)
    parser.add_argument("--max-grad-norm", type=float, default=2.0)
    parser.add_argument("--device", type=str, default="auto")
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.validation_episodes < 1:
        raise SystemExit("--validation-episodes must be at least 1")
    if args.batch_episodes < 1:
        raise SystemExit("--batch-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    if args.epochs < 1:
        raise SystemExit("--epochs must be positive")
    if args.restarts < 1:
        raise SystemExit("--restarts must be positive")
    if args.hidden_size < 1:
        raise SystemExit("--hidden-size must be positive")
    if args.learning_rate <= 0.0:
        raise SystemExit("--learning-rate must be positive")
    if args.entropy_weight < 0.0:
        raise SystemExit("--entropy-weight must be nonnegative")
    if args.value_weight < 0.0:
        raise SystemExit("--value-weight must be nonnegative")
    if args.max_grad_norm <= 0.0:
        raise SystemExit("--max-grad-norm must be positive")
    return TorchActorCriticConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        validation_episodes=args.validation_episodes,
        batch_episodes=args.batch_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        epochs=args.epochs,
        restarts=args.restarts,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        entropy_weight=args.entropy_weight,
        value_weight=args.value_weight,
        max_grad_norm=args.max_grad_norm,
        device=args.device,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts, device_used = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_torch_actor_critic_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_torch_actor_critic_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_torch_actor_critic_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "device_used": device_used,
                "torch_version": torch.__version__,
                "mps_available": torch.backends.mps.is_available(),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Torch recurrent actor-critic precursor using sampled return. "
                    "Boundary signatures are assigned by post-training causal logit "
                    "interventions rather than self labels."
                ),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"device {device_used} torch {torch.__version__} mps_available {torch.backends.mps.is_available()}")
    print_table(verdicts)
    return 0 if all(verdict.valid_architecture_torch_actor_critic for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
