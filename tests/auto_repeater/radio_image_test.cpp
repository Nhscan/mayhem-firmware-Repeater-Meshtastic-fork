#include "../../firmware/application/external/auto_repeater/repeater_radio_image.hpp"
#include <array>
#include <cassert>
#include <cstdio>
#include <cstring>
using namespace ui::external_app::auto_repeater;
struct Source {
    std::array<uint8_t, 600> bytes{};
    size_t position{0}, length{600};
    bool fail{false}, short_read{false};
    size_t size() const { return length; }
    struct Result {
        bool error;
        size_t count;
        bool is_error() const { return error; }
        size_t value() const { return count; }
    };
    Result read(void* p, size_t n) {
        if (fail) return {true, 0};
        if (short_read) --n;
        std::memcpy(p, bytes.data() + position, n);
        position += n;
        return {false, n};
    }
};
int main() {
    Source source;
    for (size_t i = 0; i < source.bytes.size(); ++i) source.bytes[i] = uint8_t(i);
    // Independent known FNV-1a fixture for bytes 0..255 repeated, truncated to 600.
    const RadioImage expected{600, 0xbc485d2dU};
    std::array<uint8_t, 608> destination;
    destination.fill(0xa5);
    assert(copy_radio_image(source, destination.data(), 600, expected));
    assert(std::memcmp(source.bytes.data(), destination.data(), 600) == 0);
    for (size_t i = 600; i < destination.size(); ++i) assert(destination[i] == 0xa5);
    source.position = 0;
    assert(!copy_radio_image(source, destination.data(), 599, expected));
    assert(source.position == 0);
    source.length = 599;
    assert(!copy_radio_image(source, destination.data(), 600, expected));
    source.length = 600;
    source.fail = true;
    assert(!copy_radio_image(source, destination.data(), 600, expected));
    source.fail = false;
    source.short_read = true;
    assert(!copy_radio_image(source, destination.data(), 600, expected));
    source.short_read = false;
    source.position = 0;
    source.bytes[299] ^= 1;
    assert(!copy_radio_image(source, destination.data(), 600, expected));
    assert(!copy_radio_image(source, destination.data(), 600, RadioImage{0, 0}));
    std::puts("PASS SD radio: multi-block copy, bounds, wrong size, read error, short read and corrupt image rejection");
}
