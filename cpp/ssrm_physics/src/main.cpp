#include <iostream>
#include <string>

#include "ssrm_physics/json_writer.hpp"
#include "ssrm_physics/simulation.hpp"

namespace ssrm::physics {

Args parse_args(int argc, char** argv) {
  Args args;
  for (int i = 1; i < argc; ++i) {
    const std::string key = argv[i];
    auto read = [&](const std::string& fallback) {
      if (i + 1 >= argc) return fallback;
      ++i;
      return std::string(argv[i]);
    };
    if (key == "--seed") args.seed = std::stoi(read("20260705"));
    else if (key == "--episode") args.episode = std::stoi(read("0"));
    else if (key == "--ticks") args.ticks = std::stoi(read("360"));
    else if (key == "--policy") args.policy = read(args.policy);
    else if (key == "--ablation") args.ablation = read(args.ablation);
    else if (key == "--trace") args.trace = true;
  }
  return args;
}

}  // namespace ssrm::physics

int main(int argc, char** argv) {
  const auto args = ssrm::physics::parse_args(argc, argv);
  const auto result = ssrm::physics::run_simulation(args);
  ssrm::physics::write_result_json(std::cout, result);
  return 0;
}

