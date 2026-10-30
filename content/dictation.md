Dictation turns microphone recordings or audio files into text on your own computer. It does not require a hosted recognition account, and the recording is not sent to your text-to-speech provider.

## Record into the editor

1. Place the cursor where the text should be inserted, or select text to replace.
2. Choose **Dictate** to open the dictation controls.
3. Select a recognition model, language, and microphone. Use the refresh control to update the microphone list.
4. Choose **Record** and speak clearly.
5. Choose **Stop recording** to finish capture and obtain the final transcription.

Allow microphone access in your operating system if permission is requested. Playback and dictation cannot run at the same time.

Dictation selectors and action buttons form separate centered groups that adapt to the window width. The selectors keep their full text visible. The button always reads **Live text**. When enabled, it uses a light blue fill in light mode and a dark blue fill in dark mode; when disabled, its fill is neutral. With Live text enabled, SpeechDesk periodically inserts provisional words while you speak. The final result after Stop recording may change them. With Live text disabled, recognition begins after recording stops.

Choose **Cancel** to discard the current dictation and restore the previous text and selection. An error or an empty final result also preserves the original text. After successful insertion, **Ctrl+Z** undoes that dictation in one action.

## Dictation controls

<figure class="theme-screenshot">
<img class="screenshot-light" src="assets/dictation-light.png" alt="SpeechDesk with the dictation panel open, showing recognition model, language, microphone, recording controls, and the centered level meter." loading="lazy" decoding="async">
<img class="screenshot-dark" src="assets/dictation-dark.png" alt="SpeechDesk with the dictation panel open, showing recognition model, language, microphone, recording controls, and the centered level meter." loading="lazy" decoding="async">
<figcaption>Dictation selectors and action buttons are centered in separate groups. The microphone meter sits in the bottom status row.</figcaption>
</figure>

## Read the microphone meter

When the dictation panel is open, a microphone level meter is centered in the bottom status row. During recording it expands outward from the middle as the input level rises. The two halves mirror one mono input level; they do not represent separate left and right channels.

Use the meter to see whether sound is reaching the selected microphone. It is a level indicator, not a measure of transcription accuracy. If it stays still while you speak, check the device selection and microphone permission.

## Choose a model

The normal application packages include four models:

| Model | When to consider it |
| --- | --- |
| Whistle | Compact recognition for English, German, French, Spanish, Italian, Dutch, and Polish |
| Whisper Tiny Q5_1 | A small multilingual model, including Hungarian |
| Whisper Base Q5_1 | Another multilingual option |
| Whisper Small Q5_1 | A larger multilingual model |

These model files total approximately **299 MB**. They run on the CPU. Recording quality, language, model choice, and hardware all affect accuracy and processing time.

Start with a smaller model if recognition is slow. For larger models or a less powerful computer, turn **Live text** off and record first. **Settings → Dictation → Recognition CPU threads** controls the worker thread count.

Two larger Whisper models are available as [optional model packs](model-packs.html). They are not required for ordinary dictation.

## Transcribe an audio file

Choose **Audio file…** in the dictation controls, then select a **WAV, MP3, or FLAC** file. The limit is **one hour** and **1 GiB** per file.

The recognized text is inserted at the current cursor position or replaces the selection, just as with microphone dictation. Check and correct the result before using it elsewhere.

Dictation does not start text-to-speech automatically. You can edit the result, save it with **Save text…**, or choose **Speak** separately.

## If recording does not work

Check the selected microphone, operating-system permission, and whether another application is using the device. Refresh the device list after connecting a microphone. See [Troubleshooting](troubleshooting.html) for recording and recognition errors.
