A server profile tells SpeechDesk how to request speech from a service. It does not install a model, start a server, or give a chat-only endpoint the ability to generate audio.

## Set up a hosted provider

Open **Settings → Servers** and select a **Provider**. Enter your own API key in **API key**, review the model and voice, then choose **Save**.

| Provider | Setup details |
| --- | --- |
| OpenAI | Uses the provider's HTTP speech API and a supported speech model and voice |
| ElevenLabs | Uses a speech model ID and a voice ID available to your account |
| OpenRouter | Lists speech-capable models; voice choices can differ between models |

The presets supply each provider's service address and connection type. Use a private-server profile if you need a different endpoint.

Provider accounts, API access, limits, billing, model availability, and retention policies are controlled by the provider. SpeechDesk sends the requested text and speech options to that service. Playback is AI-generated speech.

Keys remain available only for the current application session. Switching providers or editing the server address clears the current key so it is not reused for a different destination.

## Find models and voices

Choose **Detect capabilities** to request model and voice information. Detection does not generate speech or confirm that a complete request will work.

You can enter IDs manually if discovery is unavailable or incomplete. Use a model that actually supports speech output and a voice supported by that model. In particular, review the voice after changing an OpenRouter model. ElevenLabs expects a voice ID, not just a voice name.

Start with a short paragraph to check the configuration before submitting a long reading.

## Connect your own server

Choose **Local / remote private server** and enter its origin, for example `http://localhost:8000` or `https://speech.example.org`. These are examples; replace them with the address of your service.

Choose **Automatic / compatible speech API**, or select the connection type documented by your server. Available adapters include OpenAI-compatible speech, vLLM-Omni, Kokoro-FastAPI, and custom HTTP/JSON/SSE mappings.

Automatic discovery checks the server's API description and model/voice endpoints. If those endpoints are absent, enter the connection type, model, and voice manually. The server must already be running and reachable.

Use **Advanced…** only when the service requires custom paths, request fields, or response mappings. The [server profile reference](server-profiles.html) describes those options and their limits.

## API compatibility

SpeechDesk 1.0.0 implements OpenAI's HTTP speech endpoint. The documented retirement date for those Speech API models is **6 January 2027**; the replacement Realtime protocol needs a future adapter. Check the [official deprecation schedule](https://developers.openai.com/api/docs/deprecations) before relying on a model.

For any provider, service features outside the supported adapter—such as voice cloning or a different streaming protocol—are not enabled merely by entering the service address.

If a request fails, see [Troubleshooting](troubleshooting.html). Read [Privacy and data handling](privacy.html) before importing profiles or adding custom request fields.
