# Meshtastic upstream submission preparation

Target: portapack-mayhem/mayhem-firmware, next.
Clean upstream baseline: c27dcfceaddab8cddfb341c787018d26f5136e92.
Existing fork next: 36740da8f0a67a22fae46a83e102fc55e528d564.
Newest app source reviewed: fca5fd7218d5abc051a6b8efe1d8dea6e8a8e7c2, build/h4m-mesh-rf-meter-ar10.
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

