// SPDX-License-Identifier: GPL-2.0-or-later
#include "ui.hpp"
#include "ui_navigation.hpp"
#include "external_app.hpp"
namespace ui::external_app::meshtastic {
void initialize_app(NavigationView&);
}
extern "C" {
__attribute__((section(".external_app.app_meshtastic.application_information"), used))
application_information_t _application_information_meshtastic = {
    (uint8_t*)0,
    ui::external_app::meshtastic::initialize_app,
    CURRENT_HEADER_VERSION,
    VERSION_MD5,
    "PortaMeshRF",
    {0x00, 0x00, 0x08, 0x10, 0x1c, 0x38, 0xfe, 0x7f, 0x1c, 0x38, 0x18, 0x18, 0x10, 0x04, 0x20, 0x04, 0x20, 0x02, 0x40, 0x02, 0xc0, 0x01, 0xc0, 0x01, 0xe0, 0x03, 0xc0, 0x01, 0x80, 0x00, 0x00, 0x00},
    ui::Color::green().v,
    app_location_t::TRX,
    -1,
    {'M', 'S', 'R', 'V'},
    0};
}
