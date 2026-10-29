SpeechDesk is a Windows and Linux desktop application for reading text aloud and turning recorded speech into editable text. This manual covers version **1.0.0**.

## Start here

<ul class="chapter-list">
<li><a href="installation.html">Install SpeechDesk →</a><span>Choose a package and start the application.</span></li>
<li><a href="first-reading.html">Your first reading →</a><span>Connect a service, choose a voice, and listen.</span></li>
<li><a href="dictation.html">Local dictation →</a><span>Turn recordings into text on your computer.</span></li>
</ul>

<figure>
<img src="assets/speechdesk-light.png" alt="SpeechDesk in the light theme, showing the editor and speech playback controls">
<figcaption>The SpeechDesk editor, with text selection and playback controls.</figcaption>
</figure>

## Two ways to work with speech

**Text to speech** uses a service you configure: OpenAI, ElevenLabs, OpenRouter, or a compatible local or remote speech server. Enter text, select a model and voice, and play the generated audio inside SpeechDesk. You can save a completed reading as one WAV file.

**Speech to text** runs on your computer. Record from a microphone or open a supported audio file, then insert the recognized words into the editor. Whistle and three Whisper models are included. Two larger Whisper models are available as [separate add-ons](model-packs.html).

A speech service is needed for reading aloud, but it is not needed for local dictation. A general chat model or chat endpoint cannot necessarily generate speech.

## Find an answer

The [playback guide](playback.html) explains selection reading, pause, highlighting, and audio export. [Provider setup](providers.html) covers accounts, model IDs, and self-hosted connections. Use [troubleshooting](troubleshooting.html) for connection, playback, microphone, and model-import problems.

For downloads, see the [SpeechDesk 1.0.0 release](https://github.com/Davoda1/Speech-Desk/releases/tag/v1.0.0). Read [privacy and data handling](privacy.html) before sending confidential text to a speech provider.
