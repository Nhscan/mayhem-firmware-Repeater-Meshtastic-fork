# Auto Repeater preparation branch

> [!WARNING]
> **Before transmitting (TX):** check the radio rules for your country, state/province and local area. Make sure the frequency, power, mode and antenna setup are permitted, and obtain any required licence or authorization. You are responsible for lawful operation; this experimental firmware does not guarantee regulatory compliance.

The repeater-only candidate now builds and passes software validation on the 1 MiB HackRF One target. It has not been flashed or physically tested. No upstream issue, message or pull request has been sent. Craig explicitly requested preparation only.

- Validated source: `d24764597b3496fafde86f21a911e9c2dc2cbfb6`.
- Firmware identifier: `rpt_d247645`.
- Upstream baseline: `5bc230848cb17c666f34d07b70062bed682da1a2`.
- [Passing build and validation logs](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45519543490).
- [Download unflashed test candidate](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45519543490/artifacts/14980265350) (GitHub sign-in may be required).

The candidate artifact includes `build/firmware/portapack-mayhem_OCI.ppfw.tar`, the matching 1 MiB `portapack-mayhem-firmware.bin`, a source-commit text file and the guide. The USTAR updater archive contains APPS, the repeater-specific BASEBAND files and the firmware image. It is a repeater-only test build; PortaMeshRF is excluded.

| Validation | Result |
| --- | --- |
| Portable regression programs | All six passed |
| Remaining flash | 1,280 bytes (0.1%) |
| External UI plus largest radio image | 15,572 + 23,220 = 38,792 / 40,960 bytes |
| Normal capture known heap headroom | 6,140 bytes |
| Repeater capture known heap headroom | 5,504 bytes |
| Recorded audio known heap headroom | 45,948 bytes |
| Update archive | USTAR, matching files, correct order, 1 MiB firmware checksum passed |

The flash margin is small: future upstream changes may require further size work. The heap figures account for known allocations and allocator slack; they do not establish fragmentation behavior or RF timing on hardware.

## What is external

The UI and its radio-file loader are in the external app. Only optional repeater capture recognition (`PRCP.bin`) and recorded-audio TX (`PRAT.bin`) load from SD. Their exact size and build-generated integrity hash are checked before startup, and loading is bounded below the external UI's memory address. Normal Capture, Replay and Audio RX stay built into SPI and retain the existing global loader.

The repeater engine and file workers still use main firmware. This is not a drop-in app for arbitrary stock firmware. Install/test only a complete matching candidate when ready.

## Review and testing handoff

- [Controls and file formats](USER-GUIDE-DRAFT.md)
- [Integration and validation details](PREPARATION.md)
- [Maintainer discussion draft](MAINTAINER-PROPOSAL.md)
- [PR description and hardware test plan](PR-DRAFT.md)

Next: review the code, test this exact build on physical PortaPack hardware and real RF peers, collect screenshots/video and review licensing/documentation commitments. Do not submit upstream without Craig's further instruction and review. The passing build is not a claim that physical testing has happened.
