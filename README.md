# Conduit · ARM64 Performance

[English](README.md) · [Русский](README.ru.md)

Experimental builds for personal compatibility and performance testing. Upstream application names and interface branding are retained.

[Upstream project](https://github.com/cogwheel0/conduit) · [Packages](https://github.com/aktalascloud/conduit-arm64-performance/releases)

Extract the appropriate archive and run `Install.cmd`. `Install.cmd -CheckOnly` verifies integrity without installing. Packages exclude personal configuration, credentials, history, caches and model weights. Models download from Hugging Face on demand.

## Patches

| ID | Change | Source |
|---|---|---|
| APK-001 | ARM64-only Flutter release AOT with icon tree shaking, Dart obfuscation and existing R8/resource shrinking. | local recipe; R8/resource shrinking already enabled upstream |
| APK-002 | Separate stable/development package IDs and a persistent private signing key; do not overwrite the official app. | local |

## Measurements

| Metric | Verified improvement |
|---|---|
| LLM generation throughput | Not measured |
| JSON on Ivy Bridge | Pending stock/optimized comparison |
| Android runtime performance | Not measured on a physical phone |

Unmeasured changes have no claimed percentage. JSON timings cover serialization/parsing, not tokens/s. PGO, LTO and ISA flags apply only to the named native components; they do not turn Python or TypeScript into native code. AVX2/FMA and fast-math are not enabled.

## Licensing and compatibility

Original licenses, notices and license history are preserved. Each binary package includes its corresponding source. Private signing keys stay outside the repository. APKs use a separate application ID.

Local deployment additionally checks the owner's private filter and Telegram bridge. Their source, settings and data are not published. Unreviewed PR/fork changes remain candidates; accepted upstream fixes arrive through merges of official branches.
