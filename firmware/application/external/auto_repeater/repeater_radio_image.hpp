// SPDX-License-Identifier: GPL-2.0-or-later
#pragma once
#include <cstddef>
#include <cstdint>

namespace ui::external_app::auto_repeater {
struct RadioImage {
    uint32_t size;
    uint32_t hash;
};

// Source supplies size() and read(), with File's result interface.
// The expected hash comes from the same build as the external app.
template <typename Source>
bool copy_radio_image(Source& source, uint8_t* destination, size_t capacity, const RadioImage& expected) {
    if (!expected.size || expected.size > capacity || source.size() != expected.size) return false;
    uint32_t hash = 2166136261U;
    size_t offset = 0;
    while (offset < expected.size) {
        const size_t remaining = expected.size - offset;
        const size_t count = remaining < 256 ? remaining : 256;
        const auto result = source.read(destination + offset, count);
        if (result.is_error() || result.value() != count) return false;
        for (size_t i = 0; i < count; ++i) {
            hash ^= destination[offset + i];
            hash *= 16777619U;
        }
        offset += count;
    }
    return hash == expected.hash;
}
}  // namespace ui::external_app::auto_repeater
