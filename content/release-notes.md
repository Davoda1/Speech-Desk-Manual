SpeechDesk 2.0.0 adds built-in offline speech through the existing provider and playback controls. The manual and its application screenshots cover this release in both light and dark themes.

## Changes in 2.0.0

- **Built-in / Offline provider:** generate speech locally with Pocket TTS or Kokoro, using the CPU and the included runtimes. No account, API key, separate server, GPU, system Python installation, or runtime model download is required.
- **34 English voice presets:** Pocket TTS includes six voices with its standard English 100M model; Kokoro includes 28 American and British voices with its v1.0 82M full-precision ONNX model.
- **Existing playback workflow:** type, paste, open a text file, or dictate into the editor; choose a model and voice; read everything or a selection; pause, resume, stop, follow the passage, and save the completed reading as WAV.
- **Bundled runtime packages:** Windows ZIP, Linux tar.gz, and Debian packages include the TTS models, runtime dependencies, and license notices alongside the existing dictation assets. Download sizes increase accordingly.
- **Updated documentation:** setup, privacy, provider catalogs, troubleshooting, release links, package examples, and the website edition are updated for 2.0.0. All application screenshots have been refreshed, including the offline provider settings.

## Included functionality

SpeechDesk continues to support OpenAI, ElevenLabs, OpenRouter, and local or remote compatible speech servers, with per-profile optional encrypted API keys. Existing saved service profiles remain available after upgrading. Dictation stays in the same editor and runs locally with Whistle and multilingual Whisper Tiny, Base, and Small. Whisper Large v3 Turbo and Large v3 remain separate, complete ZIP add-ons.

Portable packages start the real top-level executable; the Debian package installs the real binary at `/usr/bin/speechdesk`. The release includes source archives, documentation, and a single **SHA256SUM.txt** manifest. Models and generated runtime assets are reconstructed from pinned acquisition manifests when building from source.

## Compatibility and verification

Built-in speech is intended for English and uses passage highlighting. Word highlighting for service profiles still requires supported timing data. Synthesis speed depends on the local CPU and available memory; audio is prepared in sections before playback.

Encrypted credentials protect the saved file while locked. They do not protect a key from software that can inspect the application after it has been unlocked. Passphrases are never stored, and there is no recovery feature.

OpenAI Realtime transcript matching remains conservative: punctuation and numeric-format differences can reject a section even when its spoken rendering might be acceptable. The check uses the service's reported transcript, not an independent analysis of the audio. Provider availability, model access, retention, and billing remain subject to the selected service.

Build and test results are recorded in the [software repository's workflows](https://github.com/Davoda1/Speech-Desk/actions). Automated checks do not establish physical microphone or speaker behavior on every desktop.

[Download SpeechDesk 2.0.0](https://github.com/Davoda1/Speech-Desk/releases/tag/v2.0.0).
