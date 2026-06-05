#pragma once

#include <vector>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

std::vector<Zone> build_zones();
std::vector<Obstacle> build_obstacles();
Weather weather_at(int tick, int episode);

}  // namespace ssrm::physics

