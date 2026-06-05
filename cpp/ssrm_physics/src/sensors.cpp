#include "ssrm_physics/sensors.hpp"

#include <algorithm>
#include <cmath>

#include "ssrm_physics/ablations.hpp"
#include "ssrm_physics/math.hpp"

namespace ssrm::physics {

bool line_blocked(Vec2 from, Vec2 to, const std::vector<Obstacle>& obstacles) {
  const Vec2 d{to.x - from.x, to.z - from.z};
  const double dd = dot(d, d);
  if (dd < 1e-9) return false;
  for (const auto& obstacle : obstacles) {
    const Vec2 f{obstacle.p.x - from.x, obstacle.p.z - from.z};
    const double t = clamp(dot(f, d) / dd, 0.0, 1.0);
    const Vec2 closest{from.x + d.x * t, from.z + d.z * t};
    if (dist(closest, obstacle.p) < obstacle.radius) return true;
  }
  return false;
}

std::vector<SoundEvent> sound_sources(const Agent& agent, const Weather& weather) {
  std::vector<SoundEvent> sounds = {
      {"shelter_creak", {-18.0, -14.0}, 0.70 + (1.0 - agent.shelter_integrity) * 1.6, 0.35},
      {"dependent_call", {-27.0, -2.0}, 0.45 + (1.0 - agent.dependent_health), 0.62},
      {"water_flow", {25.0, -7.0}, 0.78, 0.22},
      {"ridge_threat_step", {4.0, -30.0}, 0.95 + agent.fear * 0.4, 0.85},
  };
  if (weather.kind == "storm") sounds.push_back({"storm_roar", {agent.p.x + 8.0, agent.p.z - 6.0}, 2.2, 0.18});
  if (weather.kind == "cold_wind") sounds.push_back({"wind_shear", {agent.p.x - 10.0, agent.p.z + 5.0}, 1.5, 0.25});
  return sounds;
}

std::string nearest_visible(const Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                            const std::vector<Obstacle>& obstacles, double& range_out) {
  const double sensor_quality = clamp(0.55 + agent.integrity * 0.35 - agent.fatigue * 0.16 - agent.illness * 0.10, 0.20, 1.0);
  const double range = 9.0 + 28.0 * weather.visibility * sensor_quality;
  range_out = range;
  const Vec2 forward{std::cos(agent.heading), std::sin(agent.heading)};
  std::string best = "none";
  double best_d = 1e9;
  for (const auto& zone : zones) {
    const Vec2 delta{zone.p.x - agent.p.x, zone.p.z - agent.p.z};
    const double d = length(delta);
    if (d > range) continue;
    const double facing = dot(normalize(delta), forward);
    if (facing < 0.15 && d > 7.0) continue;
    if (line_blocked(agent.p, zone.p, obstacles)) continue;
    if (d < best_d) {
      best_d = d;
      best = zone.id;
    }
  }
  return best;
}

double perceived_audio(const Agent& agent, const Weather& weather, double& direction_out, int& count_out) {
  double total = 0.0;
  Vec2 weighted{0.0, 0.0};
  count_out = 0;
  for (const auto& source : sound_sources(agent, weather)) {
    const double d = std::max(1.0, dist(agent.p, source.p));
    const double loud = source.base * weather.audio_reliability / (1.0 + 0.020 * d * d);
    if (loud > 0.07) {
      ++count_out;
      total += loud;
      const Vec2 dir = normalize({source.p.x - agent.p.x, source.p.z - agent.p.z});
      weighted.x += dir.x * loud;
      weighted.z += dir.z * loud;
    }
  }
  direction_out = std::atan2(weighted.z, weighted.x);
  return total;
}

double vibration_signal(const Agent& agent, const Weather& weather) {
  const double threat = 1.1 / (1.0 + 0.030 * std::pow(dist(agent.p, {4.0, -30.0}), 2.0));
  const double storm = (weather.kind == "storm") ? 0.50 : 0.0;
  const double structure = (1.0 - agent.shelter_integrity) * 0.45 /
                           (1.0 + 0.025 * std::pow(dist(agent.p, {-18.0, -14.0}), 2.0));
  const double load = agent.load * 0.18;
  return clamp(threat + storm + structure + load, 0.0, 2.5);
}

double tension_signal(const Agent& agent, const Weather& weather) {
  const double carried = agent.load * 0.80;
  const double shelter = (1.0 - agent.shelter_integrity) * (weather.kind == "storm" ? 1.2 : 0.45);
  const double dependent = (1.0 - agent.dependent_health) * 0.55;
  return clamp(carried + shelter + dependent, 0.0, 2.5);
}

std::map<std::string, double> attention_for(const Frame& frame) {
  std::map<std::string, double> out;
  out["self"] = clamp((1.0 - frame.agent.energy) + (1.0 - frame.agent.integrity) + frame.agent.illness, 0.0, 1.0);
  out["weather"] = clamp(frame.weather.severity, 0.0, 1.0);
  out["audio"] = clamp(frame.audio_loudness * 0.50, 0.0, 1.0);
  out["vibration"] = clamp(frame.vibration * 0.55, 0.0, 1.0);
  out["tension"] = clamp(frame.tension * 0.50, 0.0, 1.0);
  out["tool"] = clamp(1.0 - frame.agent.shelter_integrity, 0.0, 1.0);
  out["social"] = clamp(1.0 - frame.agent.dependent_health, 0.0, 1.0);
  out["continuity"] = clamp(frame.agent.commitment, 0.0, 1.0);
  return out;
}

Frame make_frame(int tick, const Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                 const std::vector<Obstacle>& obstacles, const Args& args) {
  Frame frame;
  frame.tick = tick;
  frame.agent = agent;
  frame.weather = weather;
  double range = 0.0;
  frame.visible = has_vision(args) ? nearest_visible(agent, weather, zones, obstacles, range) : "vision_ablation";
  frame.fov_range = has_vision(args) ? range : 0.0;
  int count = 0;
  frame.audio_loudness = perceived_audio(agent, weather, frame.audio_direction, count);
  frame.audio_loudness = has_audio_direction(args) ? frame.audio_loudness : frame.audio_loudness * 0.45;
  frame.vibration = has_vibration_tension(args) ? vibration_signal(agent, weather) : 0.0;
  frame.tension = has_vibration_tension(args) ? tension_signal(agent, weather) : 0.0;
  frame.proposal = (tick >= 82 && tick <= 116) ? "cross_hazard_for_resource" : "none";
  frame.attention = attention_for(frame);
  return frame;
}

}  // namespace ssrm::physics

