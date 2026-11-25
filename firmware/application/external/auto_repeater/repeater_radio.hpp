// SPDX-License-Identifier: GPL-2.0-or-later
#pragma once
namespace ui::external_app::auto_repeater {
// Caller must shut down the previous baseband before loading another image.
bool load_repeater_radio(bool capture);
}  // namespace ui::external_app::auto_repeater
