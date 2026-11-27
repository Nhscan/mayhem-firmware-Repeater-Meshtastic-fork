# Changelog

## Unreleased: PortaMeshRF branding

- Renamed the mesh app's menu entry and title to PortaMeshRF; added an original three-node icon.
- Updated project branding and setup/key instructions, with descriptive protocol references and preserved attribution.
- Retained internal filenames, settings keys and node identity for migration compatibility.
- New firmware requires exact-build physical testing; previous release artifacts are unchanged.


## LongFast receive window fix - 2026-11-21

Test firmware `n_261121_rxwin`, based on the ar10 RF meter build.

- Spread the LoRa header search across DMA buffers to reduce missed samples during decoding.
- Recover the receive cursor when its samples have been overwritten. Allow late windows whose samples are still available.
- Add LoRa payload CRC diagnostics and counters for receive stages, header rejects, stale windows, and missed sample buffers.

The host tests and firmware layout, runtime memory, install, and Flash Utility archive checks passed. The bench test received 10 of 10 LongFast broadcasts from Mesh A at `L:16 V:14 A:0`. In a separate two-way test, the HackRF received 5 of 5 from Mesh A, and Mesh A received 4 of 5 from the HackRF. OpenWebRX decoded all 10 transmissions.

## ar09 - 2026-11-21

Meshtastic now reserves chat rows across display filters, restores recent messages when switching conversations with SD saving off, and keeps message-detail links aligned as the session buffer rolls over. The compose bar has a wide Write message button and a separate Clear confirmation. Radio uses the native frequency keypad with Load and an explicit Auto reset. Settings pages include a focusable Back button. The H4M build and archive checks passed. Physical-device testing is pending.

## ar08 - 2026-11-21

H4M community test firmware `n_261121_ar08` incorporates the upstream November 21 nightly and the ar07 Meshtastic chat-history change. In Msg view, hidden status lines are discarded first when the history buffer is full. The ar06 Settings memory fix is included. Auto Repeater retains its record-only and automatic repeat modes.

GitHub Actions passed the firmware layout, runtime memory, installation, and Flash Utility archive checks. On-device verification of this nightly build is pending. [Firmware and checksum](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/releases/tag/ar08).

## ar06 - 2026-11-19

Fixed an out-of-memory crash when opening Meshtastic Settings pages, including Profile. The map now checks for memory when opened, leaving approximately 3.7 KB available to other pages. If memory is fragmented, opening the map can require reopening Meshtastic.

The owner confirmed the fix on a HackRF One + PortaPack H4M. The build passed layout, runtime memory, install and update archive checks, including checksums for the firmware and all 104 matching external apps.

## ar05 - 2026-11-13

Test firmware `n_261109_ar05` for HackRF One + PortaPack H4M.

- Synced Mayhem upstream through 2b7e3b4023b46d4e2c557ffa205a1e02a8caef12.
- Fixed custom channels with empty keys using synthetic encryption instead of plaintext.
- Added custom channel support for raw 128-bit/256-bit hexadecimal keys and padded Base64 PSKs.
- Added an Import key button for a key-only SD-card .TXT file and expanded typed key entry to 64 characters.
- Preserved the existing custom passphrase format and primary-channel default key behavior.
- Added rate-limited receive decode failure diagnostics.
- Corrected the updater package to USTAR with explicit directories, matching APPS/BASEBAND files, and the firmware image last.
- Included the matching firmware .bin, Windows USB tools/drivers, backup and read-back verification launcher, instructions and SHA-256 checksums.

Validation: ARM build, layout, runtime memory, installation and update-archive checks passed.
Craig successfully flashed the corrected archive. In a bench test with LILYGO T3 Meshtastic 2.7.26, the PortaPack imported a 256-bit Base64 key and received the LILYGO test text. The LILYGO received "256" from the PortaPack. A subsequent reply was not observed, so repeated-delivery reliability remains under investigation. This test covered the secondary test channel on Short Fast at 433.125 MHz. Other presets, direct-message PKC, arbitrary keys and manual 256-bit typing require further hardware testing.


## v0.3.1 — 2026-11-09

Community test build `n_261109_ar04`, based on Mayhem nightly `n_261109`.

- Stabilized START AUTO / STOP AUTO captions and limited redundant display repainting.
- Restricted capture loss checks to the retained prebuffer and current recording.
- Joined the capture worker before reading final counters and buffer state.
- Ended captures on silence below Trigger without the rearm margin holding them open.
- Preserved damaged captures, incremented SKIP, and automatically rearmed after cooldown. Clean captures continue to delayed transmit; genuine file errors still stop.
- Packaged matching firmware, 104 PPMA apps, two standalone apps and 70 baseband images.
- Added a screen-only interface walkthrough and screenshots for community testers.

Owner reports the repeater working well so far. Meshtastic opens; message exchange remains unverified. This is not an official Mayhem or Meshtastic release.

## v0.3.0 — 2026-11-09

- Rebased on the November 9 Mayhem nightly and rebuilt matching SD applications.
- Fixed Meshtastic startup/RAM handling and restored the PFUT internal flashing component.
- Cached the custom version to keep application compatibility stable across regeneration.

## v0.2.1 / v0.2.0 — development builds

- Expanded repeater controls, modes, automatic operation and file support.
- Added the experimental Meshtastic app under Transceivers.
- These builds omitted the internal flash writer; updating from them requires the packaged USB procedure.

## v0.1.0 — initial development build

- Introduced the H4M Auto Repeater application.

See the README and packaged documentation for mode, file and radio limitations.
