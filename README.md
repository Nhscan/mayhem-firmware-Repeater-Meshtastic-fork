# Mayhem Firmware - Repeater + PortaMeshRF Fork

## PortaMeshRF branding update

The mesh messaging app is now **PortaMeshRF**, with a new Transceiver menu name, screen title and original three-node icon. Saved channel keys, node identity, internal settings identifiers and the `meshtastic.ppma` filename are retained for upgrade compatibility.

PortaMeshRF is independently developed and compatible with the Meshtastic® protocol. It is not affiliated with, sponsored by or endorsed by the Meshtastic project. Meshtastic® is a registered trademark of Meshtastic LLC. Protocol references and original copyright/license notices remain for compatibility and attribution.

- [Current setup and key-import instructions](docs/h4m/PORTAMESHRF.md)
- [Rebranding candidate with the later receive-window fixes](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/tree/build/portameshrf-branding)
- [PortaMeshRF build checks and matching test downloads](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/actions/workflows/portameshrf-branding.yml)

Existing releases and screenshots retain their original labels. The new candidate needs physical testing of that exact build; no flashing or upstream submission has been performed. The separate repeater-only preparation remains on [upstream/repeater-only](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/tree/upstream/repeater-only).

> [!WARNING]
> **Unofficial, independent project — not affiliated with or endorsed by Meshtastic.**
>
> This repository and the included firmware/app are **not an official Meshtastic app, firmware, client, or product**. Meshtastic® is a registered trademark of Meshtastic LLC. This project is independent and is not created, operated, sponsored, or endorsed by The Meshtastic Project.
>
> Use of the name “Meshtastic” here is for descriptive compatibility identification only. No affiliation or endorsement should be inferred.

A fork of [PortaPack Mayhem](https://github.com/portapack-mayhem/mayhem-firmware) with Auto Repeater and experimental PortaMeshRF apps compatible with the Meshtastic protocol for **HackRF One + PortaPack H4M**. The complete modified source, public test builds, and installation instructions are in this repository.

**Start here:** [Installation](docs/h4m/INSTALL.txt) | [PortaMeshRF setup and keys](docs/h4m/PORTAMESHRF.md) | [Full app guide](docs/h4m/MESHTASTIC.md)

**Previous H4M test firmware (old app label):** [Download H4M_AR09.ppfw.tar](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/download/ar09/H4M_AR09.ppfw.tar) · [Release notes and checksums](docs/h4m/AR09-RELEASE.md)

The [ar06 release](https://github.com/Nhscan/mayhem-firmware-Repeater-PortaMeshRF-fork/releases/tag/ar06) is the previous H4M build with a hardware-confirmed Meshtastic Settings fix.
