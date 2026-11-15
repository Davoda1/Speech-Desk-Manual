SpeechDesk is a Windows and Linux desktop application for reading text aloud and turning recorded speech into editable text. This manual covers version **2.0.0**.

## Start here

<ul class="chapter-list">
<li><a href="installation.html">Install SpeechDesk →</a><span>Choose a package and start the application.</span></li>
<li><a href="first-reading.html">Your first reading →</a><span>Choose a built-in or hosted voice and listen.</span></li>
<li><a href="dictation.html">Local dictation →</a><span>Turn recordings into text on your computer.</span></li>
</ul>

<figure class="theme-screenshot">
<img class="screenshot-light" src="assets/speechdesk-light.png" alt="SpeechDesk editor with text selection, speech provider choices, and playback controls." loading="eager" decoding="async">
<img class="screenshot-dark" src="assets/speechdesk-dark.png" alt="SpeechDesk editor with text selection, speech provider choices, and playback controls." loading="eager" decoding="async">
<figcaption>The SpeechDesk editor, with text selection and playback controls.</figcaption>
</figure>

## Two ways to work with speech

**Text to speech** can run entirely on your computer with the bundled Pocket TTS and Kokoro models. You can also use OpenAI, ElevenLabs, OpenRouter, or a compatible local or remote speech server. Enter text, select a model and voice, and play the generated audio inside SpeechDesk. You can save a completed reading as one WAV file.

**Speech to text** runs on your computer. Record from a microphone or open a supported audio file, then insert the recognized words into the editor. Whistle and three Whisper models are included. Two larger Whisper models are available as [separate add-ons](model-packs.html).

Built-in speech and local dictation need no account or speech server. Hosted providers require a configured speech-capable service; a general chat model or chat endpoint cannot necessarily generate speech.

## New in 2.0.0

Version 2.0.0 adds **Built-in / Offline** speech with Pocket TTS and Kokoro: 34 English voice presets in total, CPU inference, and all required models and runtimes included in the application packages. Choose the model and voice with the existing controls, then use the same playback and WAV export actions. The manual includes fresh screenshots in both themes. See the [release notes](release-notes.html) for the changes.

## Find an answer

The [playback guide](playback.html) explains selection reading, pause, highlighting, and audio export. [Provider setup](providers.html) covers built-in voices, hosted accounts, model IDs, and self-hosted connections. Use [troubleshooting](troubleshooting.html) for connection, playback, microphone, and model-import problems.

For downloads, see the [SpeechDesk 2.0.0 release](https://github.com/Davoda1/Speech-Desk/releases/tag/v2.0.0). Read [privacy and data handling](privacy.html) before sending confidential text to a speech provider.
