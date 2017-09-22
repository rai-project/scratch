#ifndef __UTILS_HPP__
#define __UTILS_HPP__

#include <iomanip>
#include <random>
#include <sstream>
#include <string>

static inline std::string uuid4() {
  static std::random_device rd;
  static std::uniform_int_distribution<uint64_t> dist(0, (uint64_t)(~0));

  const auto ab = (dist(rd) & 0xFFFFFFFFFFFF0FFFULL) | 0x0000000000004000ULL;
  const auto cd = (dist(rd) & 0x3FFFFFFFFFFFFFFFULL) | 0x8000000000000000ULL;

  std::stringstream ss;
  ss << std::hex << std::nouppercase << std::setfill('0');

  uint32_t a = (ab >> 32);
  uint32_t b = (ab & 0xFFFFFFFF);
  uint32_t c = (cd >> 32);
  uint32_t d = (cd & 0xFFFFFFFF);

  ss << std::setw(8) << (a) << '-';
  ss << std::setw(4) << (b >> 16) << '-';
  ss << std::setw(4) << (b & 0xFFFF) << '-';
  ss << std::setw(4) << (c >> 16) << '-';
  ss << std::setw(4) << (c & 0xFFFF);
  ss << std::setw(8) << d;

  return ss.str();
}

#endif // __UTILS_HPP__
