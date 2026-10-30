Read the whole editor or a selected passage, control playback in SpeechDesk, and export a completed reading as one audio file.

## Prepare the text

Type or paste into the editor, or use **Open TXT…** for a UTF-8 `.txt` or `.md` file. Input files are limited to **2 MiB**, and a reading may contain up to **200,000 characters**. Markdown is read as plain text.

Choose **Speak** to read all text. Select an excerpt first to read only that selection. Text used by an active task is protected against simultaneous editing.

**Save text…** writes the editor's contents as a UTF-8 TXT file. It does not save the generated speech.

## Follow reading progress

SpeechDesk divides a reading at sentence and paragraph boundaries. Long sentences are split at the profile's section limit, which defaults to **500 characters**. This can affect pauses and phrasing.

Each section is buffered before it plays. The application prepares the next section ahead of playback where possible. This is not immediate playback of every arriving audio fragment.

**Reading part N of M** identifies the part currently playing and the total number of parts in this reading. Pausing changes the label to **Paused · part N of M**. The position slider and time display apply to the current part; they are not a position within the complete reading. The part count is hidden when idle.

OpenAI Realtime also waits for a final transcript and compares it with the requested text before playing the section. A mismatch, including a punctuation or number-format difference, produces an error. See [Provider setup](providers.html#openai-realtime-and-legacy-models).

The section size and request timeout are available in **Settings → Servers → Request limits**. Smaller sections may help with provider limits or long waits; they also create more separate requests.

## Control playback

| Control | What it does |
| --- | --- |
| **Speak** | Starts reading the text or selection |
| **Pause / Resume** | Pauses or resumes audio already being played |
| **Stop** | Ends playback and cancels pending work in SpeechDesk |
| Position slider | Seeks within the current section |
| **Volume** | Adjusts playback volume |

Pausing playback does not pause generation on the server. Stopping cannot guarantee that a remote provider cancels a request it has already accepted or stops charging for it.

After completion, Speak can reuse the cached reading while the text, selection, and effective speech profile remain unchanged. Starting another reading replaces that cache. Save audio before closing the application if you want to keep it.

## Follow the text

SpeechDesk uses word timings supplied by the service when they can be matched to the requested text. Otherwise, it highlights the current sentence or section for the duration of that audio. It does not estimate a moving word highlight.

In **Settings → Appearance**, you can turn off **Highlight the text being read** or **Keep the current sentence in view** independently.

## Export audio

**Save audio…** becomes available after every section has completed. It combines the reading into a WAV file with **48 kHz, mono, 16-bit PCM** audio.

Export requires a working decoder for the service's returned format. If conversion fails, check that the provider is returning a supported audio format. A partially completed reading cannot be exported as the complete reading.

See [Keyboard shortcuts](shortcuts.html) for quick access to playback and save actions.
