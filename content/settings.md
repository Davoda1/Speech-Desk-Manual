Open Settings to adjust appearance, manage speech profiles, and configure local recognition. Choose **Save** to apply preference changes or **Cancel** to discard them.

## Appearance

| Setting | Effect |
| --- | --- |
| **Theme** | Choose Follow system, Light, or Dark |
| **Editor text size** | Set the editor text between 11 and 28 px |
| **Highlight the text being read** | Show the active words or passage during playback |
| **Keep the current sentence in view** | Follow the active passage as playback advances |

Word highlighting depends on timing information supplied by the speech service. Without usable word timings, SpeechDesk highlights the current sentence or section. See [Playback](playback.html) for details.

## Server profiles

The **Servers** tab stores connection settings. Use **Add** to create a profile or **Remove** to delete one. At least one profile remains; its address can be left empty if you do not want to configure speech playback yet.

Give each profile a useful **Profile name**, then select its provider, address, model, and voice. Hosted presets use fixed provider addresses. The [provider guide](providers.html) explains the differences between hosted and self-hosted services.

**Detect capabilities** requests discovery information. **Advanced…** opens the JSON profile for custom endpoints and mappings. **Import…** and **Export…** work with profile configuration files. Review an imported profile before using it.

The dedicated **API key** field is session-only and is excluded from saved settings and exported profiles. Changing providers or editing the service address clears the current key. Custom headers and request-body fields may be saved; keep credentials out of them.

## Request limits

Two controls set how SpeechDesk sends text to a speech service:

- **Timeout:** 10–1,800 seconds, with a default of 180 seconds.
- **Characters per section:** normally 80–8,000, with a default of 500. The OpenAI preset limits this field to 4,096.

Follow the service's own limits. Increasing a timeout does not make a server faster, and increasing section size may increase the wait before playback. SpeechDesk divides text at sentence and paragraph boundaries where possible.

## Dictation

**Recognition CPU threads** can be set from 1 to 32. The initial value uses up to four available processor threads. More threads do not guarantee better performance on every computer.

**Import model pack…** installs an optional local model. This action takes effect when the import finishes; choosing Cancel in Settings afterwards does not uninstall it. See [Model packs](model-packs.html).

## Saved preferences

Preferences and installed models use `%AppData%\Speech-Desk` on Windows or `$XDG_CONFIG_HOME/Speech-Desk` on Linux, normally `~/.config/Speech-Desk`.

The editor's text and generated audio are not automatically retained. Use their explicit save actions for anything you want to keep. API keys must be entered again after an application restart.

## Appearance example

![SpeechDesk using the dark appearance](assets/speechdesk-dark.png)

The application can use a light appearance, a dark appearance, or follow the operating system.
