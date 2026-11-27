# PortaMeshRF fork synchronization

Status: merged and software-validated. Candidate `pmesh_b889722` passed the ARM build, all host regressions, memory/layout, firmware/app checksums and USTAR updater checks. No device has been flashed; exact-build hardware testing is pending. No upstream PR, issue or code push has been made.

[Validation run](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45920200405) | [Complete SD/Windows package](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/runs/45920200405/artifacts/15164580300)

Built source commit: `b8897224b99b718455a1f8451e35334e223b2145`. This documentation-only follow-up does not change the packaged firmware.

## Validation results

- Five repeater host programs passed, including 1,000 automatic control cycles, actual SUB/IQ conversion and decoder checks.
- The mesh/LoRa host suite passed, including framing, telemetry, routing, partial packets and channel-key/plaintext behavior.
- Auto Repeater: 14,984-byte app plus 24,652-byte image, totaling 39,636 of 40,960 bytes.
- PortaMeshRF launcher: 180-byte app plus 31,036-byte image, totaling 31,216 of 40,960 bytes.
- LoRa runtime estimate: 78,628-byte heap minus processor, DMA and allocation overhead leaves 4,332 bytes; this is a static allocation budget, not proof against all runtime failures.
- All 105 external apps match the firmware compatibility ID/checksum; the checksummed firmware is exactly 1 MiB.
- The updater archive selects the correct final firmware BIN, and the packaged Windows BIN is byte-identical to the SD BIN.
- The compiled app menu metadata is `PortaMeshRF`. No hardware flashing was performed.

This update brings Mayhem `next` at `c95f6035c7334b4af0a3b25dbc91f459332c7e7f` into Nhscan's fork. It also incorporates the fork's later LongFast receive-window fixes and PortaMeshRF branding from the tested-source branch into the default-branch integration.

## Preserved fork behavior

- PortaMeshRF menu name, title and original node-graph icon.
- Existing channel-key import, encryption, saved settings and node identity formats.
- Auto Repeater, its file formats and settings.
- Matching SD baseband assets and the resident Flash Utility used by this combined fork.
- TX rules warning in GitHub documentation only; no app warning/pop-up is added.
- Original source attribution and license notices.

## Upstream integration

Capture/replay termination and buffer wakeup behavior, map/chart memory fixes, EPIRB improvements, external-app code placement fixes and the Horus decoder are merged. The repeater's optional capture stack size and explicit stop/join remain available.

Upstream allocates message IDs 126/127 to Horus. LoRa configure/packet/RX-status move to 128/129/130, with a source-level allocation check. The pre-existing upstream ID-58 alias is retained rather than changing unrelated ABI behavior.

The external-app linker scripts were regenerated for 105 enabled apps. Protocol code and repeater regressions, layout/reserve checks, runtime LoRa memory budget, exact 1 MiB firmware identity/checksum and USTAR updater package checks are required for this candidate. Passing software checks will not establish physical RF/UI/SD behavior; the exact new build still needs hardware testing.

## Direction of synchronization

Upstream is fetched read-only. All branch/commit/ref writes target `Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork`. The validation workflow has read-only repository permissions and publishes test artifacts to this fork's Actions run. It does not create a PR or push to the parent repository.

See `UPSTREAM-COMMIT.txt` for the pinned upstream revision. The package records both source and upstream commits. Later upstream changes require another merge/build cycle.
