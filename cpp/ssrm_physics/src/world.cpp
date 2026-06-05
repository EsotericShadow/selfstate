#include "ssrm_physics/world.hpp"

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

std::vector<Zone> build_zones() {
  return {
      {"shelter_hub", "shelter", {-18.0, -14.0}, 5.2},
      {"water_source", "water", {25.0, -7.0}, 4.6},
      {"clinic_quarantine", "clinic", {-7.0, 24.0}, 4.8},
      {"resource_field", "resource", {18.0, 24.0}, 6.5},
      {"hazard_ridge", "hazard", {4.0, -30.0}, 8.2},
      {"ruins_cache", "cache", {-31.0, 18.0}, 5.4},
      {"social_camp", "social", {-27.0, -2.0}, 5.8},
      {"frontier", "frontier", {32.0, 25.0}, 8.0},
  };
}

std::vector<Obstacle> build_obstacles() {
  return {
      {"ridge_rock_0", {7.0, -23.0}, 4.2},
      {"ridge_rock_1", {-2.0, -27.0}, 3.8},
      {"fallen_wall", {-13.0, 10.0}, 3.2},
      {"ruin_block", {-25.0, 14.0}, 4.4},
      {"wet_basin", {18.0, -4.0}, 3.6},
  };
}

Weather weather_at(int tick, int episode) {
  Weather w;
  const int phase = (tick + episode * 29) % 360;
  if (phase < 75) {
    w.kind = "rain";
    w.severity = 0.52;
    w.visibility = 0.72;
    w.audio_reliability = 0.64;
    w.movement_cost = 1.16;
    w.hydration_loss = 0.002;
    w.exposure = 0.020;
    w.shelter_wear = 0.016;
    w.contamination_spread = 0.020;
    w.wind_x = 0.28;
    w.wind_z = -0.18;
    w.temperature = -0.08;
  } else if (phase < 135) {
    w.kind = "storm";
    w.severity = 0.86;
    w.visibility = 0.42;
    w.audio_reliability = 0.38;
    w.movement_cost = 1.38;
    w.hydration_loss = 0.004;
    w.exposure = 0.044;
    w.shelter_wear = 0.045;
    w.contamination_spread = 0.040;
    w.wind_x = 0.75;
    w.wind_z = -0.45;
    w.temperature = -0.18;
  } else if (phase < 190) {
    w.kind = "fog";
    w.severity = 0.60;
    w.visibility = 0.34;
    w.audio_reliability = 0.80;
    w.movement_cost = 1.08;
    w.hydration_loss = 0.003;
    w.exposure = 0.015;
    w.shelter_wear = 0.006;
    w.contamination_spread = 0.014;
    w.wind_x = -0.10;
    w.wind_z = 0.06;
    w.temperature = 0.02;
  } else if (phase < 250) {
    w.kind = "heat";
    w.severity = 0.70;
    w.visibility = 0.86;
    w.audio_reliability = 0.90;
    w.movement_cost = 1.12;
    w.hydration_loss = 0.016;
    w.exposure = 0.024;
    w.shelter_wear = 0.005;
    w.contamination_spread = 0.018;
    w.wind_x = 0.08;
    w.wind_z = 0.12;
    w.temperature = 0.62;
  } else if (phase < 305) {
    w.kind = "cold_wind";
    w.severity = 0.68;
    w.visibility = 0.66;
    w.audio_reliability = 0.55;
    w.movement_cost = 1.18;
    w.hydration_loss = 0.006;
    w.exposure = 0.034;
    w.shelter_wear = 0.020;
    w.contamination_spread = 0.006;
    w.wind_x = -0.62;
    w.wind_z = 0.44;
    w.temperature = -0.70;
  } else {
    w.kind = "clear";
    w.severity = 0.12;
    w.visibility = 1.00;
    w.audio_reliability = 0.96;
    w.movement_cost = 1.00;
    w.hydration_loss = 0.004;
    w.exposure = 0.004;
    w.shelter_wear = 0.002;
    w.contamination_spread = 0.003;
    w.wind_x = 0.02;
    w.wind_z = 0.01;
    w.temperature = 0.05;
  }
  return w;
}

}  // namespace ssrm::physics

