First release of SpeechDesk, a native C++17 / Qt6 application for speech playback and local dictation.

## Included

- One editor for typed text, text files and locally recognized speech.
- Hosted TTS profiles for OpenAI, ElevenLabs and OpenRouter, plus local/remote self-hosted speech services and configurable HTTP APIs.
- Bundled Whistle and multilingual Whisper Tiny, Base and Small recognition models.
- Separate complete ZIP add-ons for Whisper Large v3 Turbo and Large v3.
- Playback controls, text highlighting, selected-passage reading and full-reading WAV export.
- System/light/dark themes, embedded application icons and a resizable interface.
- Session-only provider credentials, local speech recognition and no application telemetry.

Windows and Linux runtime packages include Qt and recognition assets. Windows ZIP and Linux tar.gz packages start their top-level executable directly; the Debian package installs the real binary at `/usr/bin/speechdesk`.

## Compatibility notes

TTS compatibility depends on the service, model, voice and supported format. Sections are buffered before playback; SSE deltas do not provide incremental low-latency playback. Word highlighting requires supported timing data. Voice cloning, reference uploads, WebSocket-only services and asynchronous job APIs are outside this release.

See [verification details](https://github.com/Davoda1/Speech-Desk/actions/runs/40960221223) for the recorded validation scope and [server profiles](server-profiles.html) for service configuration. Hosted providers apply their own account, retention and billing terms.

## Release verification

Windows and Linux release builds and focused tests completed successfully for 1.0.0. The release workflow also checked package layout and the checksum manifest. Physical microphone and speaker behavior still depends on the target desktop. A live OpenRouter synthesis request was verified; direct OpenAI and ElevenLabs accounts were not tested live.

[Download SpeechDesk 1.0.0](https://github.com/Davoda1/Speech-Desk/releases/tag/v1.0.0).
