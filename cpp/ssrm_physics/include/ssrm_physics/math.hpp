#pragma once

#include <algorithm>
#include <cmath>
#include <cstdint>
#include <string>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

inline double clamp(double value, double low, double high) {
  return std::max(low, std::min(high, value));
}

inline double length(Vec2 v) {
  return std::sqrt(v.x * v.x + v.z * v.z);
}

inline double dist(Vec2 a, Vec2 b) {
  return length({a.x - b.x, a.z - b.z});
}

inline Vec2 normalize(Vec2 v) {
  const double n = length(v);
  if (n < 1e-9) return {0.0, 0.0};
  return {v.x / n, v.z / n};
}

inline double dot(Vec2 a, Vec2 b) {
  return a.x * b.x + a.z * b.z;
}

inline double terrain_height(Vec2 p) {
  return 1.2 * std::sin(p.x * 0.075) + 0.9 * std::cos(p.z * 0.069) +
         0.6 * std::sin((p.x + p.z) * 0.041);
}

inline Vec2 terrain_gradient(Vec2 p) {
  constexpr double e = 0.35;
  const double dx = (terrain_height({p.x + e, p.z}) - terrain_height({p.x - e, p.z})) / (2.0 * e);
  const double dz = (terrain_height({p.x, p.z + e}) - terrain_height({p.x, p.z - e})) / (2.0 * e);
  return {dx, dz};
}

inline uint32_t stable_seed(int seed, int episode, const std::string& policy, const std::string& ablation) {
  uint32_t value = static_cast<uint32_t>(seed * 2654435761u + episode * 97u);
  for (char c : policy + ablation) value = value * 131u + static_cast<uint32_t>(c);
  return value;
}

}  // namespace ssrm::physics

