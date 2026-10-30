Two optional ZIP packs add larger Whisper models to local dictation. The four bundled models remain available without either pack.

## Available packs

Download the complete ZIP from the [SpeechDesk 1.1.0 release](https://github.com/Davoda1/Speech-Desk/releases/tag/v1.1.0).

| Model | Download | Model weight size |
| --- | --- | --- |
| Whisper Large v3 Turbo | `SpeechDesk-1.1.0-Whisper-Large-v3-Turbo-Expansion.zip` | 574,041,195 bytes |
| Whisper Large v3 | `SpeechDesk-1.1.0-Whisper-Large-v3-Expansion.zip` | 1,081,140,203 bytes |

Each download is **one complete ZIP**. These weights are not included in the ordinary application or source archives. The same pack can be imported on Windows and Linux, but each computer needs its own installation.

## Import a pack

1. Download the desired ZIP and compare its hash with the release's **SHA256SUM.txt** entry.
2. Open **Settings → Dictation → Import model pack…**.
3. Select the ZIP directly. Do not extract it first.
4. Wait for validation and import to complete.
5. Close Settings and select the new model in **Dictate**.

SpeechDesk checks the expected model identity, file size, hashes, and archive structure. Unrelated model files or arbitrary ZIP archives cannot be installed through this importer.

A successfully imported model remains installed even if you then choose **Cancel** in Settings. Model import is a separate operation from saving the other preferences.

After a successful import, you may remove the downloaded ZIP to recover its disk space. The installed model is retained in the application configuration directory.

## Storage locations

| System | Installed model directory |
| --- | --- |
| Windows | `%AppData%\Speech-Desk\models` |
| Linux | `$XDG_CONFIG_HOME/Speech-Desk/models`, normally `~/.config/Speech-Desk/models` |

Allow free disk space for the download, installed weights, and temporary import data. Use Cancel while an import is running to stop it. An import that has already completed remains installed.

## Performance expectations

Both models use the local CPU; a dedicated GPU is not required. Large v3 Turbo is intended to reduce processing time, while full Large v3 offers another accuracy and performance tradeoff. Neither is guaranteed to produce the best result for every recording.

File size is not the same as peak memory use. Allow several gigabytes of free memory. **8 GB of total RAM is a planning allowance, not a measured minimum or a promise of real-time recognition.**

Start with **Live text** disabled on modest hardware. If processing takes too long, switch to one of the bundled models. See [Dictation](dictation.html) for recording and file-transcription instructions.
