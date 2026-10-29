Set up a speech provider and use a short paragraph for your first reading. SpeechDesk plays the generated audio directly in the application.

## 1. Choose a service

Open **Settings → Servers**. In **Provider**, choose **OpenAI**, **ElevenLabs**, **OpenRouter**, or **Local / remote private server**.

For a hosted provider, enter that provider's API key in the dedicated **API key** field. For your own server, enter its **Server address** and choose the appropriate **Connection type**. Add a key only if the server requires one.

> Text requested for speech is sent to this service. Hosted API requests may incur charges. Dictation remains local.

API keys are retained for the current application session only. You will need to enter them again after restarting SpeechDesk.

## 2. Select a speech model and voice

Use **Detect capabilities** to request the service's model and voice information. Review the **Model / voice** fields and enter IDs supported by the selected provider.

Discovery does not generate a sample or prove that speech synthesis will succeed. If a provider does not return useful discovery information, you can enter the documented model and voice IDs manually. A model that supports ordinary chat is not necessarily a speech model.

For OpenRouter, voices can depend on the selected model. Review the voice whenever you change models. For ElevenLabs, use the voice's ID rather than its display name.

Choose **Save** to apply the profile. The [provider guide](providers.html) explains the available connection choices.

## 3. Add text

Type or paste a short paragraph into the editor. You can also choose **Open TXT…** to open a UTF-8 `.txt` or `.md` file. Markdown is treated as plain text, including its markup.

For example:

> Welcome to SpeechDesk. This short reading checks the selected voice and the playback volume.

Choose **Speak** to read the editor's text. To read only an excerpt, select that passage before pressing Speak.

## 4. Listen and adjust

Use **Pause** and **Resume** to control local playback, or **Stop** to end it. Adjust **Volume** if needed. The position slider moves within the currently playing section.

Speech is prepared in sections, so there may be a wait before playback begins. The active passage is highlighted. Individual words are highlighted only when the service returns usable timing data.

## 5. Save what you need

After the whole reading completes, choose **Save audio…** to export one WAV file. Use **Save text…** to keep the editor's text separately. Neither is saved automatically.

Continue with [Playback and audio export](playback.html), or see [Troubleshooting](troubleshooting.html) if the first request fails.
