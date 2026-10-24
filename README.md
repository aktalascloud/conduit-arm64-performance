# Conduit · ARM64 Performance

[English](README.md) · [Русский](README.ru.md)

Experimental builds for personal compatibility and performance testing. Upstream application names and interface branding are retained.

[Upstream project](https://github.com/cogwheel0/conduit) · [Packages](https://github.com/aktalascloud/conduit-arm64-performance/releases)

Download the **single APK** from the latest release and install it on Android ARM64. It combines the latest main-branch source with reviewed fork patches. A permanent application ID and signing key support upgrades. Releases contain no ZIP, CMD, LLM weights or personal settings. The original 2.3 MB Silero VAD speech detector remains bundled; its exact v5.1 source and MIT notice are recorded in `.avx1/native-arm64.json`.

Extended Russian UI and menu translation; interpolation parameters are checked in every build.

## Patches

| ID | Change | Source |
|---|---|---|
| APK-001 | ARM64-only Flutter release AOT with icon tree shaking, Dart obfuscation and existing R8/resource shrinking. | `.avx1/PATCHES.json` |
| APK-002 | One permanent fork application ID and a persistent private signing key; one latest APK. | `.avx1/PATCHES.json` |
| APK-003 | Use stable Flutter 3.47.8 and latest stable Android SDK 37.2/build-tools 37.0.0; verify exact SDK pins, ARM64 ABI, persistent APK signature and 5004 Flutter tests. | `.avx1/PATCHES.json` |
| APK-004 | Complete Russian workspace and MCP dialogs, preserve credential-warning meaning and interpolation; restore Russian ARB parameter metadata. | `.avx1/PATCHES.json` |
| APK-005 | Source-built SQLite, Dart JNI and ONNX Runtime/JNI: O3 ARMv8-A ThinLTO; verify actual C/C++ commands, exports and Android 16 KiB alignment. | `.avx1/native-arm64.json` |

Source-built SQLite 3.53.4, dartjni 1.0.3 and ONNX Runtime/JNI 1.22.0 use NDK Clang O3, ARMv8-A and ThinLTO. Public/JNI exports, packaged build IDs and Android 16 KiB page alignment are checked. CPU, NNAPI and XNNPACK providers are preserved. Flutter engine, WebRTC, PDFium and AndroidX vendor binaries are identified separately; no C/C++ O3 claim is made for unchanged binaries or Dart AOT. Physical-phone runtime speed has not been measured. See `.avx1/native-arm64.json` for pinned sources and compatibility requirements.

ThinLTO is verified for 486 ONNX core C/C++ files and 17 JNI files. The 21 handwritten MLAS assembly files remain native objects; bitcode LTO does not apply to assembly. Upstream CPU feature dispatch is preserved.

## Measurements

The 2026-10-24 ARM64 APK (`316e124d`) is 92,667,875 bytes: **4.78% smaller** than the official v4.2.1 ARM64 APK (97,324,692 bytes), and 1.21% larger than our 2026-10-23 APK. This measures download/storage size across different toolchains; it is not a runtime-speed benchmark. [Exact library inventory, hashes and checks](.avx1/measurements/native-release-316e124d.json). [Official comparison artifact](https://github.com/cogwheel0/conduit/releases/tag/v4.2.1).

Runtime performance has not been measured on a physical phone.

## Licensing and compatibility

Original licenses, notices and license history are preserved. Exact corresponding source, build instructions and pinned third-party source are available through the release tag and its links. Private signing keys stay outside the repository. APKs use a separate application ID.

Local deployment additionally checks the owner's private filter and Telegram bridge. Their source, settings and data are not published. Unreviewed PR/fork changes remain candidates; accepted upstream fixes arrive through merges of official branches.
