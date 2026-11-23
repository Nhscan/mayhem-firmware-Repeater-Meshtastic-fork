# Maintainer discussion proposal: Meshtastic on PortaPack
Prepared 23 November 2026 by Nhscan. Draft for human review before sharing upstream.

## Request
Would the Mayhem maintainers consider a smaller, external Meshtastic app, or another explicitly supported integration approach? I would like guidance on an acceptable scope before preparing a new pull request.

I understand that [the original PR #3306](https://github.com/portapack-mayhem/mayhem-firmware/pull/3306) was closed because the full implementation changed too much of the base firmware. This proposal acknowledges [that decision](https://github.com/portapack-mayhem/mayhem-firmware/pull/3306#issuecomment-6414594620); it is not a request to merge the same broad change again. The earlier [invitation to discuss the design](https://github.com/portapack-mayhem/mayhem-firmware/pull/3306#issuecomment-5479880314) is useful context, rather than an indication that the current design is approved.

## Existing work and evidence
My [separate fork](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork) builds on the original software-LoRa/Meshtastic work by Alexey Verhogladov (verhogladov), with attribution retained. AI assistance has been used for development, investigation and documentation.

I have tested text transmission and reception between my HackRF/PortaPack and a LILYGO Meshtastic node. An imported 256-bit channel PSK worked for text in both directions on an earlier fork build. Later LongFast testing on n_261121_rxwin produced a three-screen screenshot showing five HackRF messages received by the home node and decoded by OpenWebRX.

These are tests of the existing fork. They do not establish that a new upstream integration works, that every device or modem preset is compatible, or that encrypted direct messages have passed. Channel PSK encryption and direct-message public-key encryption are separate features.

## Measured integration limit
I prepared an isolated measurement against upstream next at c27dcfceaddab8cddfb341c787018d26f5136e92, using Meshtastic source from d2113491810f9877a087c0d43bea785d93bfecbd.

The measurement excludes Auto Repeater, preserves upstream's normal built-in baseband storage, and loads only the LoRa RX/TX images from SD through an app-scoped loader. It temporarily leaves the full Meshtastic UI in the main application to measure its flash cost; it is not a completed external-app port.

| Measurement | Result |
| --- | ---: |
| Host regression programs | 9 passed |
| LoRa RX M4 linked image | 30,904 bytes |
| LoRa TX M4 linked image | 11,128 bytes |
| Required final SPI image | 1,158,152 bytes |
| Firmware image limit | 1,048,576 bytes |
| Overflow | 109,576 bytes, about 107 KiB |

[Diagnostic build and logs](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/actions/runs/45275799111).

The M0 application and M4 radio code compiled and linked, but final image generation failed on size. This was not a successful firmware build, and there is no flashable package from that candidate. A small external launcher by itself does not solve the footprint when the implementation remains in main flash.

## Possible directions for discussion
1. **A smaller external app.** Start with short channel text TX/RX, essential radio configuration and channel-key entry/import. Reduce UI and optional functions as necessary, then measure whether the result actually fits. Fit and final feature scope are not yet established.
2. **A maintainer-approved architecture for the full app.** Explore conditional builds or another supported loading arrangement only if maintainers want that work. I would not treat relocating other applications' baseband images or raising size limits as an assumed solution.
3. **Continue as separate firmware.** If the prior decision remains the preferred outcome, keep the full app in the fork and discuss only independently useful, narrowly scoped fixes where maintainers see value.

My preferred next step is agreement on scope, not another full-app PR. Which approach, if any, would you be willing to review? For a smaller external app, which features and core changes would be acceptable?

## Before any implementation PR
- Agree on scope and storage/loading design.
- Separate unrelated repeater, packaging and platform changes.
- Preserve original authorship and verify contribution/licensing requirements.
- Follow external-app, namespace and existing UI conventions.
- Provide flash/RAM measurements and host regression results.
- Build and physically test the exact final candidate, including startup/exit, RF interoperability and supported encryption behavior.
- Supply screenshots, reproducible peer settings, limitations and user documentation.
- Have the contributor review and take responsibility for the submitted code.

No new upstream PR or issue has been opened for this proposal.
