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

Enter secrets only in the dedicated **API key** field. By default, a key is kept for the application session only. You can opt in to encrypted storage separately for each profile. Plaintext keys are omitted from ordinary settings and profile exports.

Standard authentication headers, including `Authorization`, `X-API-Key`, `xi-api-key`, and `Cookie`, are also removed from saved or exported profiles. Other custom headers and request-template or body fields can persist. Do not use those fields or URLs to store credentials.

Switching providers or editing the server address prevents the current credential from being reused for another destination. Review the destination and contents of an imported profile before sending a request.

## Encrypted key storage

A saved key is protected with a passphrase that SpeechDesk never stores. Encryption uses libsodium: **Argon2id** derives the encryption key with its moderate work factor and **256 MiB of memory**, and **XChaCha20-Poly1305** provides authenticated encryption. No operating-system keychain is required.

Unlocking makes the API key available in the running application so it can authenticate requests. **Lock now** immediately removes the selected profile's unlocked credential from use without locking other profiles or deleting its saved file. This lock remains effective if you later cancel Settings. Encryption protects the saved file while locked; it does not protect a key from software that can inspect the application while that key is unlocked. Choose a strong passphrase of at least **12 characters**; longer, unpredictable passphrases provide better protection than meeting the minimum alone.

Wrong-passphrase and damaged-file errors preserve the existing credential file. SpeechDesk has no passphrase recovery. If you cannot unlock a key, use **Replace saved key…** for that profile with a valid API key and a new passphrase, then choose Settings **Save**. Replacement is atomic: a failed write leaves the previous encrypted record intact.

Turning **Save API key encrypted** off and saving Settings deletes that profile's saved credential. New saves, replacements, and deletions are pending until Save; cancelling Settings discards those changes. Exported profiles contain neither API keys nor encrypted credential records, so sharing a profile does not transfer its saved key.

See [Saved API keys](settings.html#saved-api-keys) for the controls.

## Connection boundaries

Use HTTPS for hosted services. SpeechDesk retains normal TLS certificate checks and does not follow HTTP redirects; enter the final service address.

Endpoint paths and returned audio URLs must stay on the configured origin: the same scheme, hostname, and effective port. These restrictions apply to custom profiles as well as built-in adapters.

## Local files and cleanup

Encrypted key files use a `credentials` subdirectory in the application configuration directory. Preferences and imported models are stored under `%AppData%\Speech-Desk` on Windows or `$XDG_CONFIG_HOME/Speech-Desk` on Linux, normally `~/.config/Speech-Desk`.

Editor text and generated speech are not automatically kept between sessions. Use **Save text…** or **Save audio…** to retain them. Temporary playback and recognition files are removed during normal cleanup, but a crash or forced termination can leave temporary files behind.

Optional-model import checks the expected identity, byte count, hashes, and archive structure. Use only packs intended for SpeechDesk and verify release downloads with the single **SHA256SUM.txt** manifest.

## Share diagnostics carefully

Use synthetic examples in public reports. Redact keys, authorization headers, personal paths, private hostnames, and text or recordings that identify people. For security issues, follow the software repository's [security policy](https://github.com/Davoda1/Speech-Desk/blob/master/SECURITY.md) rather than posting sensitive details publicly.
