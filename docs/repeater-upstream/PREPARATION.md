# Auto Repeater integration and validation

Status: software validation passed; hardware validation pending. This branch is for preparation only and has not been submitted upstream.

Validated source: `d24764597b3496fafde86f21a911e9c2dc2cbfb6`. Baseline: Mayhem next at `5bc230848cb17c666f34d07b70062bed682da1a2`. Repeater source was separated from Nhscan's combined fork at `d2113491810f9877a087c0d43bea785d93bfecbd`.

## Final integration

- External Transceiver UI with automatic/manual recording and playback, RX/TX frequencies, timing, gain, retention, status and file controls.
- Main-firmware engine and file workers retain prebuffer handling, capture quality, metadata, RAW/BinRAW SUB conversion and playback scheduling.
- CaptureThread gains explicit stop/join while retaining counters and an optional writer stack size. Existing upstream termination/wakeup fixes and the default 1024-byte stack remain intact for other callers.
- Normal PCAP excludes the repeater recognizers. Optional recognition runs in the separate PRCP SD module; recorded AM/FM/SSB TX runs in PRAT.
- The app-scoped loader checks file size, available reserve space, read completion and a build-generated FNV-1a integrity value before starting M4. Missing/mismatched modules return an app error before RX/TX enable.
- ARSV reserves the largest radio image beneath the external UI. CMake dependencies generate this reserve and the matching radio manifest before app compilation.
- Normal built-in baseband SPI images and the global loader remain intact. One existing prepared-image API is declared in the public header for the scoped loader; its implementation is unchanged.
- The updater archive adds only PRCP/PRAT under BASEBAND and uses USTAR. Apps and SD modules precede the firmware entry.
- An uninitialized array in the existing Security+ v1 decoder is initialized because resetting its object exposed an uninitialized-copy warning. No new protocol is added.

Meshtastic, global SD-loader fallback, updater implementation changes, combined-fork release downloads and project README replacements are excluded.

## Evidence

[Passing GNU Arm GCC 9.2.1 / Ninja build](https://github.com/Nhscan/mayhem-firmware-Repeater-Meshtastic-fork/actions/runs/45519543490). Build identifier `rpt_d247645`.

Six regression programs pass locally and on Linux: control (including 1,000 automatic cycles), SUB parsing, actual IQ envelope recognition, capture quality/UI repaint logic, real file conversion routines and SD radio copy/integrity failure handling.

The known digest fixture also passed for the Python radio-manifest generator; unaligned image input was rejected.

| Check | Result |
| --- | ---: |
| Remaining 1 MiB flash | 1,280 bytes |
| External UI | 15,572 bytes |
| Largest reserved radio image | 23,220 bytes |
| Combined code use / limit | 38,792 / 40,960 bytes |
| M0 linked static RAM use | 21,024 / 65,536 bytes |
| Normal capture known heap headroom | 6,140 bytes |
| Repeater capture known heap headroom | 5,504 bytes |
| Recorded audio known heap headroom | 45,948 bytes |

The layout checker validates actual app relocation, checksum, reserve content, overlap limits and retained built-in SPI images. The memory checker reads linked ELF types and heap symbols and accounts for processor/stream objects, buffers, DMA and allocator slack. It is a static budget check, not a hardware fragmentation/timing measurement.

The install checker validates the exact 1 MiB firmware checksum and the USTAR archive, verifies packaged app/radio/firmware bytes against the build outputs and checks that SD assets precede firmware.

## Remaining work before submission

1. Physically test this exact candidate: UI, repeated automatic IQ/audio cycles, real RF peers, gain, stop/cancel and app exit/re-entry.
2. Test saved files, missing/mismatched SD modules, SD errors and normal Capture/Replay/Audio RX after the integration.
3. Collect exact settings, hardware model, screenshots/video and source/build identification.
4. Review final code, licensing/attribution, contribution guidelines and wiki commitments with the contributor.
5. Obtain Craig's explicit instruction before any upstream interaction; current instruction is preparation only.

The 1,280-byte flash margin is small. A future upstream rebase may exceed it and requires a fresh build. Earlier combined-fork hardware tests do not validate this isolated candidate.

## Initial measurement that motivated SD modules

The first isolated version kept the extra radio modules in SPI. It compiled/linked but needed 1,066,628 bytes against the 1,048,576-byte limit, an 18,052-byte overflow. A decoder-initialization follow-up required 1,066,684 bytes. These failed measurements are superseded by the passing SD-module revision above; they were never flashable candidates.
