#pragma once

#include <iosfwd>
#include <string>

#include "ssrm_physics/types.hpp"

namespace ssrm::physics {

std::string json_escape(const std::string& value);
void write_result_json(std::ostream& out, const RunResult& result);

}  // namespace ssrm::physics

