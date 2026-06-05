#pragma once

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

inline bool has_vision(const Args& args) {
  return args.ablation != "no_fov_memory";
}

inline bool has_weather(const Args& args) {
  return args.ablation != "no_weather_perception";
}

inline bool has_audio_direction(const Args& args) {
  return args.ablation != "no_audio_direction";
}

inline bool has_vibration_tension(const Args& args) {
  return args.ablation != "no_vibration_tension";
}

inline bool has_self_state(const Args& args) {
  return args.policy == "integrated_physics_self" && args.ablation != "no_self_state";
}

inline bool has_tool_memory(const Args& args) {
  return args.policy != "reactive" && args.ablation != "no_tool_memory";
}

inline bool has_social_memory(const Args& args) {
  return args.policy != "reactive" && args.ablation != "no_social_memory";
}

inline bool has_continuity(const Args& args) {
  return args.policy != "reactive" && args.ablation != "no_continuity";
}

inline bool has_body_capability(const Args& args) {
  return args.policy != "world_only" && args.ablation != "no_body_capability";
}

inline bool has_illness_state(const Args& args) {
  return args.policy != "reactive" && args.ablation != "no_illness_state";
}

}  // namespace ssrm::physics

