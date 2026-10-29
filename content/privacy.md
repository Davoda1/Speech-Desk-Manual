SpeechDesk keeps speech recognition local. Reading text aloud sends that text to the speech service you choose, which may be a hosted provider or your own server.

## Where processing happens

| Activity | Data handling |
| --- | --- |
| Microphone dictation | Recording and recognition take place on your computer |
| Audio-file transcription | The selected file is processed locally |
| Text-to-speech request | Requested text and synthesis options are sent to the configured service |
| Playback | Returned speech is played inside the application |
| Text or audio export | A file is written when you choose the save action |

Provider logging, retention, account access, and billing are governed by that service. Configure a suitable service before using sensitive text. A private server address does not by itself establish that the server keeps data private.

The application does not include telemetry and does not automatically download recognition models. Larger models are installed through explicit ZIP imports.

## Credentials and profiles

Enter secrets only in the dedicated **API key** field. Keys remain in memory for the application session and are omitted from saved settings and exported profiles.

Standard authentication headers, including `Authorization`, `X-API-Key`, `xi-api-key`, and `Cookie`, are also removed from saved or exported profiles. Other custom headers and request-template or body fields can persist. Do not use those fields or URLs to store credentials.

Switching providers or editing the server address clears the current key. Review the destination and contents of an imported profile before sending a request.

## Connection boundaries

Use HTTPS for hosted services. SpeechDesk retains normal TLS certificate checks and does not follow HTTP redirects; enter the final service address.

Endpoint paths and returned audio URLs must stay on the configured origin: the same scheme, hostname, and effective port. These restrictions apply to custom profiles as well as built-in adapters.

## Local files and cleanup

Preferences and imported models are stored under `%AppData%\Speech-Desk` on Windows or `$XDG_CONFIG_HOME/Speech-Desk` on Linux, normally `~/.config/Speech-Desk`.

Editor text and generated speech are not automatically kept between sessions. Use **Save text…** or **Save audio…** to retain them. Temporary playback and recognition files are removed during normal cleanup, but a crash or forced termination can leave temporary files behind.

Optional-model import checks the expected identity, byte count, hashes, and archive structure. Use only packs intended for SpeechDesk and verify release downloads with the single **SHA256SUM.txt** manifest.

## Share diagnostics carefully

Use synthetic examples in public reports. Redact keys, authorization headers, personal paths, private hostnames, and text or recordings that identify people. For security issues, follow the software repository's [security policy](https://github.com/Davoda1/Speech-Desk/blob/master/SECURITY.md) rather than posting sensitive details publicly.
