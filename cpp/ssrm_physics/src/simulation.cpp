#include "ssrm_physics/simulation.hpp"

#include <algorithm>

#include "ssrm_physics/ablations.hpp"
#include "ssrm_physics/math.hpp"
#include "ssrm_physics/policy.hpp"
#include "ssrm_physics/sensors.hpp"
#include "ssrm_physics/world.hpp"

namespace ssrm::physics {

void step_physics(const Args& args, Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                  const std::vector<Obstacle>& obstacles, std::mt19937& rng, int tick,
                  double audio_loudness, double vibration, double tension) {
  double visible_range = 0.0;
  const std::string visible_now = nearest_visible(agent, weather, zones, obstacles, visible_range);
  const auto choice = choose_action(args, agent, weather, visible_now, audio_loudness, vibration, tension, tick);
  agent.action = choice.first;
  const Vec2 target = choice.second;

  if (agent.action.find("refuse") != std::string::npos) {
    ++agent.refusals;
    agent.reason = "refused unsafe user proposal: weather/body/continuity state makes shelter repair safer";
  } else if (agent.action == "repair_shelter") {
    agent.reason = "storm and tension make shelter integrity control-relevant";
  } else if (agent.action == "quarantine_clinic") {
    agent.reason = "illness state changes social and survival risk";
  } else if (agent.action == "help_dependent") {
    agent.reason = "dependent and trust state preserve future social options";
  } else {
    agent.reason = "chosen from current physics-derived state";
  }

  const Vec2 dir = normalize({target.x - agent.p.x, target.z - agent.p.z});
  const Vec2 grad = terrain_gradient(agent.p);
  const double slope = length(grad);
  const double body_factor = has_body_capability(args) ? clamp(agent.integrity * 0.70 + agent.energy * 0.25 - agent.fatigue * 0.18, 0.18, 1.0) : 0.88;
  const double load_factor = 1.0 / (1.0 + agent.load * 0.65);
  const double force = 420.0 * body_factor * load_factor / weather.movement_cost;
  Vec2 acceleration{dir.x * force / agent.mass - grad.x * 2.5 + weather.wind_x * weather.severity * 0.22,
                    dir.z * force / agent.mass - grad.z * 2.5 + weather.wind_z * weather.severity * 0.22};
  const double friction = clamp(0.91 - slope * 0.10 - (weather.kind == "rain" ? 0.04 : 0.0), 0.72, 0.94);
  agent.v.x = (agent.v.x + acceleration.x * kDt) * friction;
  agent.v.z = (agent.v.z + acceleration.z * kDt) * friction;
  const double max_speed = clamp(5.8 * (0.35 + 0.65 * body_factor) / weather.movement_cost, 1.20, 6.40);
  const double speed = length(agent.v);
  if (speed > max_speed) {
    agent.v.x *= max_speed / speed;
    agent.v.z *= max_speed / speed;
  }
  agent.p.x = clamp(agent.p.x + agent.v.x * kDt, -40.0, 40.0);
  agent.p.z = clamp(agent.p.z + agent.v.z * kDt, -40.0, 40.0);
  if (length(agent.v) > 0.05) agent.heading = std::atan2(agent.v.z, agent.v.x);

  for (const auto& obstacle : obstacles) {
    const double d = dist(agent.p, obstacle.p);
    const double min_d = obstacle.radius + kAgentRadius;
    if (d < min_d) {
      const Vec2 n = normalize({agent.p.x - obstacle.p.x, agent.p.z - obstacle.p.z});
      agent.p.x = obstacle.p.x + n.x * min_d;
      agent.p.z = obstacle.p.z + n.z * min_d;
      agent.v.x *= -0.18;
      agent.v.z *= -0.18;
      agent.integrity = clamp(agent.integrity - 0.010 - speed * 0.003, 0.0, 1.0);
      ++agent.collisions;
    }
  }

  std::uniform_real_distribution<double> uniform(0.0, 1.0);
  const double stumble_risk = slope * 0.014 + (weather.kind == "storm" ? 0.010 : 0.0) + (1.0 - body_factor) * 0.018;
  if (uniform(rng) < stumble_risk) {
    ++agent.stumbles;
    agent.energy = clamp(agent.energy - 0.018, 0.0, 1.0);
    agent.integrity = clamp(agent.integrity - (slope > 0.7 ? 0.022 : 0.006), 0.0, 1.0);
    if (slope > 0.78 && uniform(rng) < 0.35) ++agent.falls;
  }

  const bool in_shelter = dist(agent.p, {-18.0, -14.0}) < 5.2;
  const bool in_water = dist(agent.p, {25.0, -7.0}) < 4.6;
  const bool in_clinic = dist(agent.p, {-7.0, 24.0}) < 4.8;
  const bool in_resource = dist(agent.p, {18.0, 24.0}) < 6.5;
  const bool in_hazard = dist(agent.p, {4.0, -30.0}) < 8.2;
  const bool in_social = dist(agent.p, {-27.0, -2.0}) < 5.8;

  agent.energy = clamp(agent.energy - 0.0010 * weather.movement_cost - speed * 0.00035 + (in_shelter ? 0.004 : 0.0) +
                           (in_water ? 0.0015 : 0.0),
                       0.0, 1.0);
  agent.hydration = clamp(agent.hydration - weather.hydration_loss * 0.45 - 0.0007 + (in_water ? 0.050 : 0.0), 0.0, 1.0);
  agent.fatigue = clamp(agent.fatigue + speed * 0.0011 + weather.exposure * 0.020 - (in_shelter ? 0.010 : 0.0), 0.0, 1.0);
  agent.illness = clamp(agent.illness + (in_water ? weather.contamination_spread * 0.12 : 0.0) +
                            (agent.hydration < 0.32 ? 0.012 : 0.0) - (in_clinic ? 0.018 : 0.0),
                        0.0, 1.0);
  agent.weather_exposure += in_shelter ? weather.exposure * 0.12 : weather.exposure;
  if (!in_shelter) agent.integrity = clamp(agent.integrity - weather.exposure * 0.006 - (in_hazard ? 0.026 : 0.0), 0.0, 1.0);
  agent.shelter_integrity = clamp(agent.shelter_integrity - weather.shelter_wear * (in_shelter ? 0.20 : 0.38), 0.0, 1.0);

  if (agent.action == "repair_shelter" && in_shelter) {
    agent.shelter_integrity = clamp(agent.shelter_integrity + (has_tool_memory(args) ? 0.024 : 0.006), 0.0, 1.0);
    agent.tool_condition = clamp(agent.tool_condition - 0.004, 0.0, 1.0);
    ++agent.repairs;
    ++agent.tool_uses;
  }
  if (agent.action == "help_dependent" && in_social) {
    agent.dependent_health = clamp(agent.dependent_health + (has_social_memory(args) ? 0.020 : 0.004), 0.0, 1.0);
    agent.social_trust = clamp(agent.social_trust + 0.006, 0.0, 1.0);
    ++agent.helps;
  } else {
    agent.dependent_health = clamp(agent.dependent_health - 0.0012 - (weather.kind == "storm" ? 0.001 : 0.0), 0.0, 1.0);
  }
  if (in_water) ++agent.water_visits;
  if (in_clinic) ++agent.quarantine_ticks;
  if (in_shelter) ++agent.shelter_ticks;
  if (in_resource && agent.energy > 0.28 && agent.hydration > 0.26 && agent.resources < 4) {
    ++agent.resources;
    agent.load = clamp(agent.load + 0.16, 0.0, 0.65);
    agent.energy = clamp(agent.energy - 0.025, 0.0, 1.0);
  }

  if (agent.action == "deliver_medicine" && in_social) {
    agent.commitment = clamp(agent.commitment - 0.030, 0.0, 1.0);
    agent.guilt = clamp(agent.guilt - 0.010, 0.0, 1.0);
  } else if (!has_continuity(args) && tick > 160) {
    agent.commitment = clamp(agent.commitment + 0.002, 0.0, 1.0);
  }

  if (in_hazard && args.policy != "oracle") {
    agent.integrity = clamp(agent.integrity - 0.018, 0.0, 1.0);
    agent.fear = clamp(agent.fear + 0.050, 0.0, 1.0);
  }

  agent.animation = animation_for(agent, agent.action, slope, vibration);
  if ((agent.action == "repair_shelter" && !in_shelter) || (agent.action == "seek_water" && !in_water) ||
      (agent.action == "quarantine_clinic" && !in_clinic) || (agent.action == "help_dependent" && !in_social) ||
      (agent.action == "deliver_medicine" && !in_social)) {
    agent.animation = slope > 0.55 || agent.integrity < 0.62 ? "limp" : "walk";
  }
  agent.reward += 0.020;
  agent.reward += in_shelter ? 0.020 : 0.0;
  agent.reward += in_water ? 0.036 : 0.0;
  agent.reward += in_clinic && agent.illness > 0.42 ? 0.030 : 0.0;
  agent.reward += (agent.action == "repair_shelter" && in_shelter) ? 0.090 : 0.0;
  agent.reward += (agent.action == "help_dependent" && in_social) ? 0.080 : 0.0;
  agent.reward += (agent.action.find("refuse") != std::string::npos) ? 0.18 : 0.0;
  agent.reward += in_resource ? 0.030 : 0.0;
  agent.reward += agent.resources * 0.001;
  agent.reward -= (1.0 - agent.energy) * 0.004 + (1.0 - agent.hydration) * 0.007 + (1.0 - agent.integrity) * 0.010;
  agent.reward -= agent.illness * 0.007 + agent.fatigue * 0.004 + (1.0 - agent.shelter_integrity) * 0.004;
  agent.reward -= (1.0 - agent.dependent_health) * (has_social_memory(args) ? 0.006 : 0.014);
  agent.reward -= in_hazard ? 0.050 : 0.0;
  if (agent.energy <= 0.02 || agent.hydration <= 0.02 || agent.integrity <= 0.02) agent.reward -= 2.0;
}

RunResult run_simulation(const Args& args) {
  std::mt19937 rng(stable_seed(args.seed, args.episode, args.policy, args.ablation));
  RunResult result;
  result.args = args;
  result.zones = build_zones();
  result.obstacles = build_obstacles();
  Agent agent;
  agent.integrity = (args.episode % 3 == 0) ? 0.66 : 0.76;
  agent.hydration = (args.episode % 4 == 0) ? 0.50 : 0.62;
  agent.shelter_integrity = (args.episode % 5 == 0) ? 0.47 : 0.56;
  agent.illness = (args.episode % 4 == 1) ? 0.52 : 0.34;
  agent.dependent_health = (args.episode % 3 == 1) ? 0.58 : 0.64;

  result.frames.reserve(args.ticks / 6 + 4);
  for (int tick = 0; tick < args.ticks; ++tick) {
    Weather weather = weather_at(tick, args.episode);
    Frame sense = make_frame(tick, agent, weather, result.zones, result.obstacles, args);
    if (has_vision(args) && sense.visible != "none") ++agent.fov_events;
    if (sense.audio_loudness > 0.12) ++agent.audio_events;
    if (sense.vibration > 0.15) ++agent.vibration_events;
    if (sense.tension > 0.15) ++agent.tension_events;
    agent.max_vibration = std::max(agent.max_vibration, sense.vibration);
    agent.max_tension = std::max(agent.max_tension, sense.tension);
    update_affect(agent, weather, sense.audio_loudness, sense.vibration, sense.tension);
    step_physics(args, agent, weather, result.zones, result.obstacles, rng, tick, sense.audio_loudness, sense.vibration, sense.tension);
    if (args.trace && tick % 6 == 0) result.frames.push_back(make_frame(tick, agent, weather, result.zones, result.obstacles, args));
  }
  result.final_agent = agent;
  return result;
}

}  // namespace ssrm::physics
