#pragma once

#include <string>
#include <utility>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

std::pair<std::string, Vec2> choose_action(const Args& args, const Agent& agent, const Weather& real_weather,
                                           const std::string& visible, double audio_loudness,
                                           double vibration, double tension, int tick);
void update_affect(Agent& agent, const Weather& weather, double audio_loudness, double vibration, double tension);
std::string animation_for(const Agent& agent, const std::string& action, double slope, double vibration);

}  // namespace ssrm::physics

