#pragma once

#include <map>
#include <string>
#include <vector>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

bool line_blocked(Vec2 from, Vec2 to, const std::vector<Obstacle>& obstacles);
std::vector<SoundEvent> sound_sources(const Agent& agent, const Weather& weather);
std::string nearest_visible(const Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                            const std::vector<Obstacle>& obstacles, double& range_out);
double perceived_audio(const Agent& agent, const Weather& weather, double& direction_out, int& count_out);
double vibration_signal(const Agent& agent, const Weather& weather);
double tension_signal(const Agent& agent, const Weather& weather);
std::map<std::string, double> attention_for(const Frame& frame);
Frame make_frame(int tick, const Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                 const std::vector<Obstacle>& obstacles, const Args& args);

}  // namespace ssrm::physics

