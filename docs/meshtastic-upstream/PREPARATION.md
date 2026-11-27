# PortaMeshRF upstream preparation

PortaMeshRF is the name of this fork's messaging app. References to Meshtastic below identify protocol compatibility, source attribution or the historical upstream review. The rename does not resolve the previously measured upstream integration size limit.

Target: portapack-mayhem/mayhem-firmware, next.
Clean upstream baseline: c27dcfceaddab8cddfb341c787018d26f5136e92.
Existing fork next: 36740da8f0a67a22fae46a83e102fc55e528d564.
Newest tested-source candidate: d2113491810f9877a087c0d43bea785d93bfecbd, fix/meshtastic-rx-window. This incorporates the ar10 meter work and later LongFast receive fixes.
This preparation branch contains a review plan, not an integrated firmware change.

## Required source separation

The fork comparison contains 105 changed files, including Auto Repeater, release ZIPs, project README replacements and release workflows. Those must not all enter the Meshtastic PR.

Meshtastic candidates:
- firmware/application/apps/ui_meshtastic.cpp and .hpp, including ar10 RF meter.
- firmware/application/apps/mesh protocol, crypto, PKI, router, node database, region and key code.
- firmware/baseband/proc_lora.cpp/.hpp, proc_lora_tx.cpp/.hpp and lora_taps.hpp.
- firmware/common/lora_framing.hpp and the LoRa IPC messages.
- Meshtastic launcher, build registration and linker integration.
- Relevant protocol, crypto, key, region, telemetry, partial-packet and LoRa regression tests.
- User instructions and preserved import attribution.

## Integration issues found

1. The external Meshtastic launcher currently constructs a view compiled into the main application. The full UI and mesh code are in main firmware. Upstream AGENT.md requires new apps to use the external app structure. Resolve storage/namespace/linker placement while measuring M0 RAM and flash.
2. LoRa RX and TX are separate M4 images. The fork uses an MSRV reserve image and loads LoRa images from SPI. Determine an app-scoped image loading design without changing how all other apps obtain baseband code.
3. The fork disables normal built-in baseband SPI inclusion and adds a global SD fallback in baseband_api.cpp. Separate that architectural change from this app, or obtain maintainer guidance after a concrete, measured proposal.
4. Auto Repeater capture-thread, capture DSP, OOK, engine and reserve-image changes should be excluded.
5. Retain only genuinely needed SettingsManager, IPC and baseband API changes. Recheck all existing callers and default behavior.
6. Run formatter and host tests, build against the clean baseline, capture final size/memory output and test this exact build physically.
7. Verify the original software-LoRa attribution and GPL-compatible import notices. The upstream template asks for GPL-3.0-compatible contribution rights. Do not claim sole authorship of imported code.

## Hardware evidence already available

Craig flashed ar05 successfully after the USTAR packaging fix. An imported 256-bit Base64 channel PSK allowed text reception in both directions with a LILYGO T3 running Meshtastic 2.7.26. Existing test used Short Fast at 433.125 MHz.
Later conversations report five messages each direction and a three-screen test with the home node and OpenWebRX. Retrieve the original image and exact firmware version before adding that proof to the PR.
The current next tree includes earlier screenshots under docs/h4m/media. The newer three-screen image is not in that directory on next.
Historical screenshots establish testing of the fork, not automatically the final isolated branch.

## Submission readiness

No upstream PR has been opened. Review branch preparation can proceed under Craig's instruction.
Upstream AGENT.md requires human review/approval and physical testing of the submitted code.
Its PR template requires compile size output, physical PortaPack evidence, RF peer evidence, wiki commitment and licensing confirmation.
Prepare the final description and validated build first, then present the exact diff and evidence to Craig for submission approval.

## Validation still to do

- Isolate implementation with app-scoped integration.
- Host protocol/crypto/LoRa regression tests.
- ARM build and M0/M4 memory budgets on current upstream.
- Verify SD update archive and matching external apps.
- Physical UI, send/receive, encrypted channels and startup/exit stability on final build.
- Clarify current DM PKC and supported SF limitations from current source/tests.

## Work completed in the preparation branch

Extracted Meshtastic protocol, crypto, node database, routing, key handling, LoRa framing and existing host tests, excluding repeater files. UI/DSP/build integration is still pending.
Nine host test programs passed with MinGW GCC (C++17, -O2, -Wall -Wextra; _USE_MATH_DEFINES enables the Windows math constants used by test_lora_ref).
After finding the newer RX-window branch, updated framing and its regression fixture and repeated that test.
The three-screen image was read from the saved original. It labels n_261121_rxwin and LongFast broadcast, and shows HackRF test 01 through 05 received by Mesh A with OpenWebRX decoding. It identifies the PortaPack panel as H2, so verify the actual device model with Craig before stating H4M-only hardware evidence.

## Prior upstream review discovered during integration

Original app PR: https://github.com/portapack-mayhem/mayhem-firmware/pull/3306
Author: verhogladov. Closed without merge.
Maintainer zxkmm requested a narrower, less mixed change and invited developer discussion on Discord.
Maintainer htotoo's closing comment says the app changes too much base firmware and should remain separate firmware.
The original PR also discusses the external-app limit and the application's much larger size.
Do not submit an equivalent full-app PR while ignoring that decision. Craig has been asked whether to explore a smaller external app or prepare a full-feature proposal for maintainer feedback.

## Current integration measurement

A separate build/meshtastic-upstream-measurement branch restores the latest tested UI/DSP onto current upstream, then applies a narrowly scoped integration patch.
It preserves existing built-in baseband inclusion and omits the global SD-loader fallback and all repeater changes.
Only the Meshtastic RX/TX images are read from SD through an app-scoped loader.
The existing internal UI placement is temporarily retained to measure its real flash cost. This is explicitly not the final external-app implementation.
New LoRa IPC IDs were moved to 128/129/130 to avoid upstream Horus IDs 126/127.
Initial compilation found the new loader needed native UTF-16 paths. That was corrected.
RX M4 code linked at 30904 bytes and TX at 11128 bytes in the first measurement run.
All nine host test programs passed on the Linux runner.
A subsequent local adjustment defers TX enable until image load and clears TX flags on failure; it is not yet in the active hosted measurement run.
The measurement candidate compiled the M0 application and M4 radio code, but final SPI image generation failed:
- Required image size: 1,158,152 bytes.
- HackRF firmware limit: 1,048,576 bytes.
- Excess: 109,576 bytes (about 107 KiB).
- Run: https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45275799111

This is a size failure, not a passing firmware package. No flashable image from this candidate is offered.
The candidate retains the full internal UI for measurement, excludes the repeater and global baseband relocation, and places LoRa RX/TX on SD.
The result supports the maintainer's prior concern about full-app integration. Further implementation depends on Craig choosing a smaller external feature set or a full-feature maintainer proposal.


