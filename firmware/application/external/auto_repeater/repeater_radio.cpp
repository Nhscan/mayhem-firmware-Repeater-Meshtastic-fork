// SPDX-License-Identifier: GPL-2.0-or-later
#include "repeater_radio.hpp"
#include "repeater_radio_image.hpp"
#include "repeater_images.hpp"
#include "standalone_app.hpp"
#include "external_app.hpp"
#include "baseband_api.hpp"
#include "file.hpp"
#include "memory_map.hpp"

extern "C" application_information_t _application_information_auto_repeater;

namespace ui::external_app::auto_repeater {
bool load_repeater_radio(bool capture) {
    if (baseband::is_image_running()) return false;
    const auto base = portapack::memory::map::m4_code.base();
    const auto end = reinterpret_cast<uintptr_t>(_application_information_auto_repeater.memory_location);
    if (end <= base || end > base + portapack::memory::map::m4_code.size()) return false;
    File image;
    const auto* path = capture ? u"BASEBAND/PRCP.bin" : u"BASEBAND/PRAT.bin";
    if (image.open(path)) return false;
    const auto expected = capture ? capture_radio_image : audio_radio_image;
    if (!copy_radio_image(image, reinterpret_cast<uint8_t*>(base), end - base, expected)) return false;
    baseband::run_prepared_image(base, true, capture ? portapack::spi_flash::image_tag_capture : portapack::spi_flash::image_tag_none);
    return true;
}
}  // namespace ui::external_app::auto_repeater
