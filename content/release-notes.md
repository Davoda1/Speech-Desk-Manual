SpeechDesk 1.1.1 corrects text visibility in speech and dictation selectors and the alignment of dictation controls. This manual also adds refreshed application screenshots that follow its selected theme.

## Changes in 1.1.1

- **Full selector text:** speech and dictation selectors keep their complete text visible as the window width changes.
- **Dictation layout:** an inset panel adapts to the application's light or dark theme. Model, language, and microphone selectors expand across the available width, while action buttons form a compact, centered group on a separate row below. Labels remain fully visible, with consistent button heights and a clear Live text state.
- **Updated manual screenshots:** the editor, dictation panel, Servers tab, and About tab are illustrated in both themes. Each page shows the screenshot matching the website's current theme, including Follow system.
- **Documentation tooling:** the manual build now uses Markdown 3.8.1.

## Features introduced in 1.1.0

- **Optional encrypted API keys:** save a key separately for each server profile using a passphrase. Session-only keys remain the default; no operating-system keychain is required.
- **Explicit credential controls:** unlock a saved key on demand, lock the selected profile immediately, or replace a credential when its passphrase is forgotten. New saves, replacements, and removals are committed with Settings Save.
- **OpenAI Realtime:** the OpenAI preset defaults to `gpt-realtime-2.1-mini` with voice `marin`. Each text section is buffered and its reported transcript is checked before playback. Microphone audio is not sent to OpenAI.
- **Legacy OpenAI model handling:** the retired Speech API model families are hidden and rejected on the official OpenAI service from 6 January 2027 (UTC). Self-hosted compatible endpoints are not subject to that rule.
- **Microphone feedback:** a centered meter in the bottom status row expands outward with the mono input level. The Live text toggle now sits at the same height as the recording buttons, with a visible pressed state.
- **Reading progress:** “Reading part N of M” and the paused equivalent identify the current part. The position slider and time display remain specific to that part.

See [Saved API keys](settings.html#saved-api-keys), [OpenAI compatibility](providers.html#openai-realtime-and-legacy-models), and [Dictation](dictation.html) for the updated instructions.

## Included functionality

SpeechDesk continues to support ElevenLabs, OpenRouter, local or remote compatible speech servers, local microphone and audio-file recognition, selected-passage reading, and complete-reading WAV export.

Whistle and multilingual Whisper Tiny, Base, and Small are bundled. Whisper Large v3 Turbo and Large v3 remain separate, complete ZIP add-ons. Windows and Linux runtime packages include Qt and required recognition assets. Portable packages start the real top-level executable; the Debian package installs the real binary at `/usr/bin/speechdesk`.

## Compatibility and verification

Encrypted credentials protect the saved file while locked. They do not protect a key from software that can inspect the application after it has been unlocked. Passphrases are never stored, and there is no recovery feature.

OpenAI Realtime transcript matching is intentionally conservative: punctuation and numeric-format differences can reject a section even when its spoken rendering might be acceptable. The check uses the service's reported transcript, not an independent analysis of the audio. Word highlighting still requires supported timing data; Realtime uses section highlighting.

Build and test results are recorded in the [software repository's workflows](https://github.com/Davoda1/Speech-Desk/actions). Automated checks do not establish physical microphone or speaker behavior on every desktop. Direct OpenAI account integration has not been tested live for this release. Provider availability, model access, retention, and billing remain subject to the selected service.

[Download SpeechDesk 1.1.1](https://github.com/Davoda1/Speech-Desk/releases/tag/v1.1.1).
