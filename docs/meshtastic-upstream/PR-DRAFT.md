# Add experimental Meshtastic software-LoRa transceiver

This draft follows the current upstream PR template. It is preparation material and is not ready for submission.

## Brief description

Add a Meshtastic transceiver under TRX for HackRF One + PortaPack H4M, using software LoRa without an external LoRa module. The app provides chat, node information, radio setup, channel PSK entry/import and RF status. Preserve upstream attribution for the imported implementation and describe subsequent changes.

Final scope and supported presets must be confirmed after integration. Exclude Auto Repeater and fork-specific download/release infrastructure.

## Proof it compiles

Pending a build of the final isolated branch. Attach the final flash size summary and M0/M4 memory checks from that build.

## Proof of testing on a real device

Historical fork testing was performed by Craig on physical HackRF One + PortaPack H4M. Final isolated-branch test is pending. Insert exact version, test results and screenshots after validation. Do not mark this section complete based solely on historical builds.

## Proof against a real emitter/receiver

Historical evidence includes two-way text with a LILYGO T3 and an imported 256-bit channel key. Retrieve the newer home-node/OpenWebRX five-message tests, screenshot and exact firmware identity. Repeat against the final isolated build.

## Known limitations

Confirm limits against current source and tests, including SF support, packet buffering, repeated delivery, DM PKC and hardware coverage. Avoid claims of universal node/preset compatibility.

## Wiki documentation commitment

The draft user guide should describe setup, TX/RX controls, PSK import, encryption versus DM PKC and known limitations. Craig must review the template's wiki-maintenance commitment before submission.

## AI assistance and attribution

AI assisted implementation, debugging, test preparation and documentation. Imported software-LoRa implementation is credited to Alexey Verhogladov / mamapapa1, with its original notices retained. Craig remains the human maintainer and hardware tester.

## Checklist

- [ ] Changes limited to Meshtastic and necessary integration
- [ ] Final ARM build and size evidence
- [ ] Physical PortaPack test of final branch
- [ ] RF peer test of final branch
- [ ] Screenshot evidence matched to firmware version
- [ ] Licensing and source notices verified
- [ ] Human code review and maintenance ownership
- [ ] Wiki documentation commitment reviewed
- [ ] Explicit approval to submit the final branch

