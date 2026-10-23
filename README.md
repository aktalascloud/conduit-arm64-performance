# Conduit · ARM64 Performance

[English](README.md) · [Русский](README.ru.md)

Experimental builds for personal compatibility and performance testing. Upstream application names and interface branding are retained.

[Upstream project](https://github.com/cogwheel0/conduit) · [Packages](https://github.com/aktalascloud/conduit-arm64-performance/releases)

Download the **single APK** from the latest release and install it on Android ARM64. It combines the latest main-branch source with reviewed fork patches. A permanent application ID and signing key support upgrades. Releases contain no ZIP, CMD, models or personal settings.

Extended Russian UI and menu translation; interpolation parameters are checked in every build.

## Patches

| ID | Change | Source |
|---|---|---|
| APK-001 | ARM64-only Flutter release AOT with icon tree shaking, Dart obfuscation and existing R8/resource shrinking. | `.avx1/PATCHES.json` |
| APK-002 | One permanent fork application ID and a persistent private signing key; one latest APK. | `.avx1/PATCHES.json` |
| APK-003 | Use stable Flutter 3.47.7 and latest stable Android SDK 37.2/build-tools 37.0.0; verify exact SDK pins, ARM64 ABI, persistent APK signature and 5004 Flutter tests. | `.avx1/PATCHES.json` |
| APK-004 | Complete Russian workspace and MCP dialogs, preserve credential-warning meaning and interpolation; restore Russian ARB parameter metadata. | `.avx1/PATCHES.json` |

## Measurements

The earlier 2026-10-23 stable ARM64 experiment was 91,561,648 bytes, versus 97,324,692 bytes for the official v4.2.1 ARM64 APK: **5.92% smaller**. This compares different toolchains and package IDs; it is a download/storage measurement, not a runtime speed claim. [Official comparison artifact](https://github.com/cogwheel0/conduit/releases/tag/v4.2.1).

Runtime performance has not been measured on a physical phone.

## Licensing and compatibility

Original licenses, notices and license history are preserved. Exact corresponding source, build instructions and pinned third-party source are available through the release tag and its links. Private signing keys stay outside the repository. APKs use a separate application ID.

Local deployment additionally checks the owner's private filter and Telegram bridge. Their source, settings and data are not published. Unreviewed PR/fork changes remain candidates; accepted upstream fixes arrive through merges of official branches.
