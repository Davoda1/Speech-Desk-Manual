Set up a speech provider and use a short paragraph for your first reading. SpeechDesk plays the generated audio directly in the application.

## 1. Choose built-in speech or a service

For offline speech, open **Settings → Servers**, select **Built-in / Offline** in **Provider**, choose the model and voice from its dropdowns, and choose **Save**. New installations start with Pocket and Alba. No server address or API key is needed. The bundled models run on your computer's CPU.

To use a service, choose **OpenAI**, **ElevenLabs**, **OpenRouter**, or **Local / remote private server** instead. Enter a hosted provider's API key in the dedicated **API key** field. For your own server, enter its **Server address** and choose the appropriate **Connection type**; add a key only if the server requires one.

> Built-in speech processes text locally. A hosted or private-server profile sends requested text to that service, and hosted API requests may incur charges. Dictation remains local with every provider.

API keys are session-only by default. You can optionally save a service profile's key encrypted with a passphrase; after restarting, unlock it when needed. The passphrase is never stored. See [Saved API keys](settings.html#saved-api-keys).

## 2. Select a speech model and voice

For **Built-in / Offline**, choose **pocket** or **kokoro** in the main window's model selector, then choose one of that model's English voices. Pocket includes Alba, Marius, Javert, Anna, Charles, and Vera. Kokoro includes 28 American and British English presets. The [provider guide](providers.html#built-in-offline-speech) lists the choices. The installed catalogs are available without a network request.

For a service, use **Detect capabilities** to request its model and voice information. Review the **Model / voice** fields and enter IDs supported by that provider. Discovery does not generate a sample or prove that synthesis will succeed; manually entered IDs are supported when discovery is unavailable.

For OpenRouter, review the voice whenever you change models. For ElevenLabs, use the voice's ID rather than its display name. Choose **Save** to apply a changed profile.

## 3. Add text

Type or paste a short paragraph into the editor. You can also choose **Open TXT…** to open a UTF-8 `.txt` or `.md` file. Markdown is treated as plain text, including its markup.

For example:

> Welcome to SpeechDesk. This short reading checks the selected voice and the playback volume.

Choose **Speak** to read the editor's text. To read only an excerpt, select that passage before pressing Speak.

## 4. Listen and adjust

Use **Pause** and **Resume** to control local playback, or **Stop** to end it. Adjust **Volume** if needed. The position slider moves within the currently playing section.

Speech is prepared in sections, so there may be a wait before playback begins. **Reading part N of M** shows which part is playing; the position slider and time display refer to that part. The active passage is highlighted. Built-in models use passage highlighting. Individual words are highlighted only when a service returns usable timing data.

## 5. Save what you need

After the whole reading completes, choose **Save audio…** to export one WAV file. Use **Save text…** to keep the editor's text separately. Neither is saved automatically.

Continue with [Playback and audio export](playback.html), or see [Troubleshooting](troubleshooting.html) if the first request fails.
