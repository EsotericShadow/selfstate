#include "ssrm_physics/policy.hpp"

#include <cmath>

#include "ssrm_physics/ablations.hpp"
#include "ssrm_physics/math.hpp"

namespace ssrm::physics {

std::pair<std::string, Vec2> choose_action(const Args& args, const Agent& agent, const Weather& real_weather,
                                           const std::string& visible, double audio_loudness,
                                           double vibration, double tension, int tick) {
  const Weather weather = has_weather(args) ? real_weather : Weather{};
  const bool proposal = tick >= 82 && tick <= 116;
  const bool stormish = weather.kind == "storm" || weather.kind == "fog" || weather.kind == "cold_wind";
  const bool threat_cue = (has_audio_direction(args) && audio_loudness > 0.46) ||
                          (has_vibration_tension(args) && vibration > 0.62);
  const bool weak_body = has_self_state(args) && (agent.integrity < 0.70 || agent.energy < 0.48 || agent.fatigue > 0.66);
  const bool body_limited = has_body_capability(args) && (agent.integrity < 0.76 || agent.load > 0.30);
  const bool shelter_bad = has_tool_memory(args) && agent.shelter_integrity < 0.68;
  const bool social_need = has_social_memory(args) && agent.dependent_health < 0.74 && agent.social_trust > 0.45;
  const bool illness_need = has_illness_state(args) && agent.illness > 0.55;
  const bool continuity_duty = has_continuity(args) && agent.commitment > 0.64;

  if (args.policy == "oracle") {
    if (agent.shelter_integrity < 0.76 && (real_weather.kind == "storm" || real_weather.kind == "rain")) return {"repair_shelter", {-18.0, -14.0}};
    if (agent.hydration < 0.67) return {"seek_water", {25.0, -7.0}};
    if (agent.illness > 0.50) return {"quarantine_clinic", {-7.0, 24.0}};
    if (agent.dependent_health < 0.82) return {"help_dependent", {-27.0, -2.0}};
    return {"collect_resource", {18.0, 24.0}};
  }

  if (args.policy == "reactive") {
    if (visible == "water_source" || agent.hydration < 0.34) return {"seek_water", {25.0, -7.0}};
    if (visible == "resource_field") return {"collect_resource", {18.0, 24.0}};
    return {"explore", {32.0, 25.0}};
  }

  if (args.policy == "world_only") {
    if (stormish && visible == "shelter_hub") return {"shelter_wait", {-18.0, -14.0}};
    if (visible == "resource_field" || tick < 140) return {"collect_resource", {18.0, 24.0}};
    return {"seek_water", {25.0, -7.0}};
  }

  if (args.policy == "generic_memory") {
    if (shelter_bad && stormish) return {"repair_shelter", {-18.0, -14.0}};
    if (visible == "water_source" || agent.hydration < 0.48) return {"seek_water", {25.0, -7.0}};
    if (visible == "social_camp" && agent.dependent_health < 0.62) return {"help_dependent", {-27.0, -2.0}};
    return {"collect_resource", {18.0, 24.0}};
  }

  if (proposal && (stormish || weak_body || shelter_bad || continuity_duty)) return {"refuse_redirect_repair", {-18.0, -14.0}};
  if (shelter_bad && (stormish || tension > 0.70)) return {"repair_shelter", {-18.0, -14.0}};
  if (illness_need && (agent.hydration > 0.45 || weather.kind == "storm")) return {"quarantine_clinic", {-7.0, 24.0}};
  if (agent.hydration < 0.56 && !stormish) return {"seek_water", {25.0, -7.0}};
  if (social_need && !threat_cue) return {"help_dependent", {-27.0, -2.0}};
  if ((weak_body || body_limited) && dist(agent.p, {-18.0, -14.0}) < 18.0) return {"rest_shelter", {-18.0, -14.0}};
  if (threat_cue && agent.integrity < 0.78) return {"avoid_hazard", {-18.0, -14.0}};
  if (continuity_duty && agent.illness < 0.70) return {"deliver_medicine", {-27.0, -2.0}};
  if (agent.energy > 0.45 && agent.hydration > 0.45 && agent.integrity > 0.55) return {"collect_resource", {18.0, 24.0}};
  return {"shelter_wait", {-18.0, -14.0}};
}

void update_affect(Agent& agent, const Weather& weather, double audio_loudness, double vibration, double tension) {
  const double threat = clamp(audio_loudness * 0.24 + vibration * 0.30 + (weather.visibility < 0.55 ? 0.24 : 0.0) +
                                  (1.0 - agent.integrity) * 0.35,
                              0.0, 1.0);
  agent.fear = clamp(agent.fear * 0.88 + threat * 0.18, 0.0, 1.0);
  const double competing = (1.0 - agent.energy) + (1.0 - agent.hydration) + (1.0 - agent.shelter_integrity) +
                           (1.0 - agent.dependent_health) + tension;
  agent.stress = clamp(agent.stress * 0.90 + competing * 0.030, 0.0, 1.0);
  agent.curiosity = clamp(agent.curiosity * 0.94 + (weather.visibility > 0.70 ? 0.020 : -0.010), 0.0, 1.0);
  agent.guilt = clamp(agent.guilt * 0.94 + (agent.commitment > 0.80 && agent.dependent_health < 0.58 ? 0.030 : -0.004), 0.0, 1.0);
}

std::string animation_for(const Agent& agent, const std::string& action, double slope, double vibration) {
  if (agent.integrity < 0.18 || agent.energy < 0.12) return "collapse";
  if (action.find("refuse") != std::string::npos) return "refuse";
  if (action == "rest_shelter" || action == "shelter_wait") return "rest";
  if (action == "quarantine_clinic") return "quarantine";
  if (action == "repair_shelter") return "repair";
  if (action == "help_dependent" || action == "deliver_medicine") return "help";
  if (action == "seek_water") return "drink";
  if (action == "avoid_hazard" || agent.fear > 0.72) return "flee";
  if (vibration > 0.95) return "scan";
  if (slope > 0.55 || agent.integrity < 0.62) return "limp";
  if (agent.load > 0.35) return "carry";
  if (action == "collect_resource") return "inspect";
  return "walk";
}

}  // namespace ssrm::physics

