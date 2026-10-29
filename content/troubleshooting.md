Start with a short piece of non-sensitive text or a brief recording. Check the status message in SpeechDesk and use the matching guidance below.

## A speech request fails

| Symptom | Check |
| --- | --- |
| Authentication error | Enter the correct provider key again; keys are cleared when the application restarts |
| Access or credit error | Check the provider account's API access, available credit, and permitted model |
| Model or voice rejected | Use a speech-capable model and a voice supported by that exact model |
| Connection failure | Check the service address and whether the server is running and reachable |
| Request times out | Try a shorter passage or smaller section limit; adjust the timeout if appropriate |

Hosted presets use their provider's fixed address. For another endpoint, choose **Local / remote private server**. Do not put a key in the URL or in a custom request-body field.

If the address changed, re-enter the key in its dedicated field. SpeechDesk deliberately clears credentials when switching providers or editing the address.

## Detection returns no models

**Detect capabilities** uses discovery endpoints that a service may not provide. An empty result does not by itself mean that speech synthesis is impossible.

Select the documented connection type and enter the model and voice IDs manually. Then try a short reading. Detection alone does not prove that a synthesis request works.

## There is no playback sound

Check SpeechDesk's volume, the operating-system output device and application volume controls. Wait for the current speech section to finish downloading; each section is buffered before playback.

If the service returned an unsupported format or malformed audio, use a format documented by that service and supported by the adapter. Keep all bundled libraries and plugins beside the portable application; copying only the executable can break multimedia support.

**Save audio…** is unavailable until the whole reading completes. Stopping early does not produce an exportable complete reading.

## Recording or recognition fails

Check microphone permission, select the intended input device, and refresh the device list after connecting it. Confirm that the microphone works in the operating system. Stop speech playback before recording.

If recognition is slow, turn **Live text** off and use a smaller model. Provisional text can change when final recognition finishes; review the completed result before saving it.

Audio-file transcription accepts WAV, MP3, or FLAC, up to one hour and 1 GiB.

## A model pack is rejected

Import the complete release ZIP directly, without extracting it. Confirm its SHA-256 against **SHA256SUM.txt**, check available disk space, and download it again if the hash differs. The importer accepts only the catalogued SpeechDesk model packs.

## Report a reproducible problem

Open an issue in the [software repository](https://github.com/Davoda1/Speech-Desk/issues). Include the app version, operating system, steps to reproduce, and a redacted error message. Use synthetic text or audio. Remove API keys, authorization headers, private server names, full personal paths, and confidential content.

For sensitive security reports, follow the repository's [security policy](https://github.com/Davoda1/Speech-Desk/blob/master/SECURITY.md).
