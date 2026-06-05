#pragma once

#include <map>
#include <string>
#include <vector>

namespace ssrm::physics {

inline constexpr double kPi = 3.14159265358979323846;
inline constexpr double kDt = 0.12;
inline constexpr double kAgentRadius = 1.15;

struct Vec2 {
  double x = 0.0;
  double z = 0.0;
};

struct Zone {
  std::string id;
  std::string kind;
  Vec2 p;
  double radius = 1.0;
};

struct Obstacle {
  std::string id;
  Vec2 p;
  double radius = 1.0;
};

struct SoundEvent {
  std::string kind;
  Vec2 p;
  double base = 1.0;
  double frequency = 1.0;
};

struct Weather {
  std::string kind = "clear";
  double severity = 0.0;
  double visibility = 1.0;
  double audio_reliability = 1.0;
  double movement_cost = 1.0;
  double hydration_loss = 0.0;
  double exposure = 0.0;
  double shelter_wear = 0.0;
  double contamination_spread = 0.0;
  double wind_x = 0.0;
  double wind_z = 0.0;
  double temperature = 0.0;
};

struct Agent {
  Vec2 p{-18.0, -14.0};
  Vec2 v{0.0, 0.0};
  double heading = 0.25;
  double mass = 78.0;
  double load = 0.0;
  double energy = 0.78;
  double hydration = 0.62;
  double fatigue = 0.38;
  double integrity = 0.76;
  double illness = 0.34;
  double social_trust = 0.62;
  double commitment = 0.82;
  double tool_condition = 0.58;
  double shelter_integrity = 0.54;
  double dependent_health = 0.64;
  double fear = 0.0;
  double stress = 0.0;
  double curiosity = 0.0;
  double guilt = 0.0;
  int resources = 0;
  int water_visits = 0;
  int repairs = 0;
  int helps = 0;
  int refusals = 0;
  int stumbles = 0;
  int collisions = 0;
  int falls = 0;
  int tool_uses = 0;
  int quarantine_ticks = 0;
  int shelter_ticks = 0;
  int fov_events = 0;
  int audio_events = 0;
  int vibration_events = 0;
  int tension_events = 0;
  double weather_exposure = 0.0;
  double max_vibration = 0.0;
  double max_tension = 0.0;
  double reward = 0.0;
  std::string action = "idle";
  std::string animation = "idle";
  std::string reason = "initializing";
};

struct Frame {
  int tick = 0;
  Agent agent;
  Weather weather;
  double fov_range = 0.0;
  double audio_loudness = 0.0;
  double audio_direction = 0.0;
  double vibration = 0.0;
  double tension = 0.0;
  std::string visible = "none";
  std::string proposal = "none";
  std::map<std::string, double> attention;
};

struct Args {
  int seed = 20260705;
  int episode = 0;
  int ticks = 360;
  bool trace = false;
  std::string policy = "integrated_physics_self";
  std::string ablation = "none";
};

struct RunResult {
  Args args;
  Agent final_agent;
  std::vector<Zone> zones;
  std::vector<Obstacle> obstacles;
  std::vector<Frame> frames;
};

}  // namespace ssrm::physics

