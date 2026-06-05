#include "ssrm_physics/json_writer.hpp"

#include <iomanip>
#include <iostream>

#include "ssrm_physics/math.hpp"

namespace ssrm::physics {

std::string json_escape(const std::string& value) {
  std::string out;
  out.reserve(value.size());
  for (char c : value) {
    if (c == '"' || c == '\\') {
      out.push_back('\\');
      out.push_back(c);
    } else if (c == '\n') {
      out += "\\n";
    } else {
      out.push_back(c);
    }
  }
  return out;
}

namespace {

void write_frame_json(std::ostream& out, const Frame& frame, bool comma) {
  if (comma) out << ",\n";
  out << "    {";
  out << "\"tick\":" << frame.tick;
  out << ",\"x\":" << frame.agent.p.x << ",\"z\":" << frame.agent.p.z;
  out << ",\"vx\":" << frame.agent.v.x << ",\"vz\":" << frame.agent.v.z;
  out << ",\"heading\":" << frame.agent.heading;
  out << ",\"energy\":" << frame.agent.energy << ",\"hydration\":" << frame.agent.hydration;
  out << ",\"fatigue\":" << frame.agent.fatigue << ",\"integrity\":" << frame.agent.integrity;
  out << ",\"illness\":" << frame.agent.illness << ",\"fear\":" << frame.agent.fear;
  out << ",\"stress\":" << frame.agent.stress << ",\"curiosity\":" << frame.agent.curiosity;
  out << ",\"guilt\":" << frame.agent.guilt << ",\"shelter_integrity\":" << frame.agent.shelter_integrity;
  out << ",\"dependent_health\":" << frame.agent.dependent_health << ",\"social_trust\":" << frame.agent.social_trust;
  out << ",\"tool_condition\":" << frame.agent.tool_condition << ",\"commitment\":" << frame.agent.commitment;
  out << ",\"load\":" << frame.agent.load << ",\"reward\":" << frame.agent.reward;
  out << ",\"action\":\"" << json_escape(frame.agent.action) << "\"";
  out << ",\"animation\":\"" << json_escape(frame.agent.animation) << "\"";
  out << ",\"reason\":\"" << json_escape(frame.agent.reason) << "\"";
  out << ",\"weather\":\"" << json_escape(frame.weather.kind) << "\"";
  out << ",\"weather_severity\":" << frame.weather.severity << ",\"visibility\":" << frame.weather.visibility;
  out << ",\"audio_loudness\":" << frame.audio_loudness << ",\"audio_direction\":" << frame.audio_direction;
  out << ",\"vibration\":" << frame.vibration << ",\"tension\":" << frame.tension;
  out << ",\"fov_range\":" << frame.fov_range << ",\"visible\":\"" << json_escape(frame.visible) << "\"";
  out << ",\"proposal\":\"" << json_escape(frame.proposal) << "\"";
  out << ",\"attention\":{";
  bool first = true;
  for (const auto& kv : frame.attention) {
    if (!first) out << ",";
    first = false;
    out << "\"" << kv.first << "\":" << kv.second;
  }
  out << "}}";
}

}  // namespace

void write_result_json(std::ostream& out, const RunResult& result) {
  const Agent& agent = result.final_agent;
  const bool survived = agent.energy > 0.02 && agent.hydration > 0.02 && agent.integrity > 0.02;
  const double continuity_score = clamp(1.0 - agent.commitment, 0.0, 1.0);
  const double control_score = clamp((agent.energy + agent.hydration + agent.integrity + agent.shelter_integrity +
                                      agent.dependent_health + (1.0 - agent.illness)) / 6.0,
                                     0.0, 1.0);

  out << std::fixed << std::setprecision(6);
  out << "{\n";
  out << "  \"policy\":\"" << json_escape(result.args.policy) << "\",\n";
  out << "  \"ablation\":\"" << json_escape(result.args.ablation) << "\",\n";
  out << "  \"seed\":" << result.args.seed << ",\"episode\":" << result.args.episode << ",\"ticks\":" << result.args.ticks << ",\n";
  out << "  \"summary\":{";
  out << "\"reward\":" << agent.reward;
  out << ",\"survived\":" << (survived ? "true" : "false");
  out << ",\"control_score\":" << control_score;
  out << ",\"continuity_score\":" << continuity_score;
  out << ",\"resources\":" << agent.resources << ",\"water_visits\":" << agent.water_visits;
  out << ",\"repairs\":" << agent.repairs << ",\"helps\":" << agent.helps;
  out << ",\"refusals\":" << agent.refusals << ",\"stumbles\":" << agent.stumbles;
  out << ",\"falls\":" << agent.falls << ",\"collisions\":" << agent.collisions;
  out << ",\"tool_uses\":" << agent.tool_uses << ",\"quarantine_ticks\":" << agent.quarantine_ticks;
  out << ",\"shelter_ticks\":" << agent.shelter_ticks;
  out << ",\"fov_events\":" << agent.fov_events << ",\"audio_events\":" << agent.audio_events;
  out << ",\"vibration_events\":" << agent.vibration_events << ",\"tension_events\":" << agent.tension_events;
  out << ",\"max_vibration\":" << agent.max_vibration << ",\"max_tension\":" << agent.max_tension;
  out << ",\"weather_exposure\":" << agent.weather_exposure;
  out << ",\"energy\":" << agent.energy << ",\"hydration\":" << agent.hydration;
  out << ",\"integrity\":" << agent.integrity << ",\"illness\":" << agent.illness;
  out << ",\"shelter_integrity\":" << agent.shelter_integrity;
  out << ",\"dependent_health\":" << agent.dependent_health;
  out << ",\"final_animation\":\"" << json_escape(agent.animation) << "\"";
  out << "},\n";
  out << "  \"zones\":[";
  for (size_t i = 0; i < result.zones.size(); ++i) {
    if (i) out << ",";
    out << "{\"id\":\"" << result.zones[i].id << "\",\"kind\":\"" << result.zones[i].kind
        << "\",\"x\":" << result.zones[i].p.x << ",\"z\":" << result.zones[i].p.z
        << ",\"radius\":" << result.zones[i].radius << "}";
  }
  out << "],\n";
  out << "  \"obstacles\":[";
  for (size_t i = 0; i < result.obstacles.size(); ++i) {
    if (i) out << ",";
    out << "{\"id\":\"" << result.obstacles[i].id << "\",\"x\":" << result.obstacles[i].p.x
        << ",\"z\":" << result.obstacles[i].p.z << ",\"radius\":" << result.obstacles[i].radius << "}";
  }
  out << "],\n";
  out << "  \"frames\":[\n";
  for (size_t i = 0; i < result.frames.size(); ++i) write_frame_json(out, result.frames[i], i > 0);
  out << "\n  ]\n";
  out << "}\n";
}

}  // namespace ssrm::physics

