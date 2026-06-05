#pragma once

#include <random>
#include <vector>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

void step_physics(const Args& args, Agent& agent, const Weather& weather, const std::vector<Zone>& zones,
                  const std::vector<Obstacle>& obstacles, std::mt19937& rng, int tick,
                  double audio_loudness, double vibration, double tension);
RunResult run_simulation(const Args& args);

}  // namespace ssrm::physics

