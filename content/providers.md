Choose a speech provider in **Settings → Servers**. **Built-in / Offline** uses the included models on your computer; other providers use a hosted or self-hosted speech service.

## Built-in / Offline speech

Select **Built-in / Offline**, choose a model and voice from its dropdowns, then save the profile. New installations start with Pocket and Alba. Upgrading keeps the selected existing profile and adds the built-in profile as another choice. The models and their runtimes are included in the application package. They run on the CPU without an account, API key, server, GPU, system Python installation, or runtime model download. Your text stays on your computer during built-in synthesis.

| Model selector | Included model | Voice presets |
| --- | --- | --- |
| `pocket` | Pocket TTS standard English 100M, float32 inference | 6 |
| `kokoro` | Kokoro v1.0 82M, full-precision ONNX | 28 |

Both models use the existing playback controls, selection reading, passage highlighting, and complete-reading WAV export. Speech is generated one section at a time. Model loading and CPU speed affect the wait before playback; a short first reading is a useful check. See [Playback](playback.html).

### Pocket voices

| Name | Voice ID |
| --- | --- |
| Alba | `alba` |
| Marius | `marius` |
| Javert | `javert` |
| Anna | `anna` |
| Charles | `charles` |
| Vera | `vera` |

### Kokoro voices

| English voice group | Voice IDs |
| --- | --- |
| American female | `af_heart`, `af_alloy`, `af_aoede`, `af_bella`, `af_jessica`, `af_kore`, `af_nicole`, `af_nova`, `af_river`, `af_sarah`, `af_sky` |
| American male | `am_adam`, `am_echo`, `am_eric`, `am_fenrir`, `am_liam`, `am_michael`, `am_onyx`, `am_puck`, `am_santa` |
| British female | `bf_alice`, `bf_emma`, `bf_isabella`, `bf_lily` |
| British male | `bm_daniel`, `bm_fable`, `bm_george`, `bm_lewis` |

Choose a voice from the selected model's catalog. These bundled presets are intended for English speech. Voice cloning and importing arbitrary TTS models are not exposed by this provider. The optional ZIP importer is for [dictation model packs](model-packs.html).

<figure class="theme-screenshot">
<img class="screenshot-light" src="assets/settings-offline-light.png" alt="SpeechDesk Settings with the Built-in / Offline provider selected and Pocket model and voice settings." loading="lazy" decoding="async">
<img class="screenshot-dark" src="assets/settings-offline-dark.png" alt="SpeechDesk Settings with the Built-in / Offline provider selected and Pocket model and voice settings." loading="lazy" decoding="async">
<figcaption>Built-in speech uses the bundled models without service credentials.</figcaption>
</figure>

## Set up a hosted provider

Open **Settings → Servers** and select a **Provider**. Enter your own API key in **API key**, review the model and voice, then choose **Save**.

| Provider | Setup details |
| --- | --- |
| OpenAI | Defaults to `gpt-realtime-2.1-mini` with the `marin` voice, using the Realtime speech connection |
| ElevenLabs | Uses a speech model ID and a voice ID available to your account |
| OpenRouter | Lists speech-capable models; voice choices can differ between models |

The presets supply each provider's service address and connection type. Use a private-server profile if you need a different endpoint.

Provider accounts, API access, limits, billing, model availability, and retention policies are controlled by the provider. SpeechDesk sends the requested text and speech options to that service. Playback is AI-generated speech.

Keys are session-only by default. Each profile can optionally keep an encrypted key, unlocked with a passphrase when needed. Saved settings and exported profiles never contain the plaintext key. Switching providers or editing the service address prevents the current key from being reused for the new destination. See [Saved API keys](settings.html#saved-api-keys).

## Find models and voices

Choose **Detect capabilities** to request model and voice information. Detection does not generate speech or confirm that a complete request will work.

You can enter IDs manually if discovery is unavailable or incomplete. Use a model that actually supports speech output and a voice supported by that model. In particular, review the voice after changing an OpenRouter model. ElevenLabs expects a voice ID, not just a voice name.

Start with a short paragraph to check the configuration before submitting a long reading.

## Connect your own server

Choose **Local / remote private server** and enter its origin, for example `http://localhost:8000` or `https://speech.example.org`. These are examples; replace them with the address of your service.

Choose **Automatic / compatible speech API**, or select the connection type documented by your server. Available adapters include OpenAI-compatible speech, vLLM-Omni, Kokoro-FastAPI, and custom HTTP/JSON/SSE mappings.

Automatic discovery checks the server's API description and model/voice endpoints. If those endpoints are absent, enter the connection type, model, and voice manually. The server must already be running and reachable.

Use **Advanced…** only when the service requires custom paths, request fields, or response mappings. The [server profile reference](server-profiles.html) describes those options and their limits.

## OpenAI Realtime and legacy models

SpeechDesk 2.0.0 uses OpenAI's Realtime API for supported `gpt-realtime-2.1` models, including the default `gpt-realtime-2.1-mini`. This connection sends the text to be read, not microphone audio. Dictation remains local.

Each speech section is buffered before playback. SpeechDesk compares the service's final transcript with the requested text, allowing differences in letter case, whitespace, and equivalent Unicode representation. If the transcript is missing or differs, that section is rejected with an error instead of being played. Punctuation or number-format changes can also cause rejection, even when the spoken wording might be acceptable. The check compares the reported transcript; it is not an independent analysis of the audio.

Legacy OpenAI models—`tts-1`, `tts-1-hd`, and `gpt-4o-mini-tts`, including their dated versions—use `/v1/audio/speech` until their retirement. From **6 January 2027 (UTC)**, SpeechDesk hides these models from discovery and rejects requests for them on the official OpenAI service. Choose a supported Realtime model or another provider. This retirement rule does not disable similarly named models on self-hosted compatible servers.

See [OpenAI's deprecation schedule](https://developers.openai.com/api/docs/deprecations) for provider changes and the [server profile reference](server-profiles.html#openai-realtime) for the transport details.

For any provider, service features outside the supported adapter—such as voice cloning or a different streaming protocol—are not enabled merely by entering the service address.

If a request fails, see [Troubleshooting](troubleshooting.html). Read [Privacy and data handling](privacy.html) before importing profiles or adding custom request fields.
