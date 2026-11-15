Open Settings to adjust appearance, manage speech profiles, and configure local recognition. Choose **Save** to apply preference changes or **Cancel** to discard them.

Choose **Settings → About → Manual** to open this online manual in your browser.

## Appearance

| Setting | Effect |
| --- | --- |
| **Theme** | Choose Follow system, Light, or Dark |
| **Editor text size** | Set the editor text between 11 and 28 px |
| **Highlight the text being read** | Show the active words or passage during playback |
| **Keep the current sentence in view** | Follow the active passage as playback advances |

Built-in speech uses passage highlighting. Word highlighting depends on timing information supplied by a speech service. Without usable word timings, SpeechDesk highlights the current sentence or section. See [Playback](playback.html) for details.

## Server profiles

The **Servers** tab manages built-in and service profiles. Use **Add** to create a profile or **Remove** to delete one. At least one profile remains. Select **Built-in / Offline** to use the included Pocket TTS or Kokoro model without a service address or key.

Give each profile a useful **Profile name**, then select its provider, model, and voice. The main window also lets you select the current profile, model, and voice. Network, credential, and Advanced fields are disabled for built-in speech; its model and voice use dropdown catalogs. Service profiles additionally use an address; hosted presets use fixed provider addresses. The [provider guide](providers.html) describes the built-in catalogs and service setup.

For service profiles, **Detect capabilities** requests discovery information. Built-in catalogs are available locally. **Advanced…** opens the JSON profile for custom endpoints and mappings. **Import…** and **Export…** work with profile configuration files. Review an imported profile before using it.

Enter credentials in the dedicated **API key** field. Keys are session-only unless you explicitly enable encrypted saving for that profile. Plaintext keys are excluded from settings and profile exports. Changing providers or editing the service address prevents reuse of the current key for the new destination. Custom headers and request-body fields may be saved; keep credentials out of them.

<figure class="theme-screenshot">
<img class="screenshot-light" src="assets/settings-servers-light.png" alt="SpeechDesk Settings on the Servers tab, showing provider fields and encrypted API-key controls without credentials." loading="lazy" decoding="async">
<img class="screenshot-dark" src="assets/settings-servers-dark.png" alt="SpeechDesk Settings on the Servers tab, showing provider fields and encrypted API-key controls without credentials." loading="lazy" decoding="async">
<figcaption>The Servers tab combines connection details and per-profile key protection.</figcaption>
</figure>

## Saved API keys

Encrypted saving is optional and separate for each server profile. Leave **Save API key encrypted** off to keep a key for the current session only.

To save a key, enter it in **API key**, enable **Save API key encrypted**, and provide a passphrase of at least **12 characters** and confirmation when prompted. Choose **Save** in Settings to commit the encrypted credential. The passphrase is never stored.

After restarting SpeechDesk, the saved key remains locked. Choose **Unlock…** and enter that profile's passphrase, or unlock when prompted to use it. **Lock now** immediately removes only the selected profile's unlocked key from use. It does not delete the encrypted file or affect other profiles. This explicit lock still applies if you later cancel Settings.

A wrong passphrase or a damaged credential file does not overwrite or delete the saved key. There is no passphrase reset or key recovery. Use **Replace saved key…** to enter a valid API key, which can be the same key or a replacement from your provider, and a new passphrase with confirmation. Choose Settings **Save** to replace only that profile's credential.

Turning **Save API key encrypted** off and choosing **Save** removes the profile's stored key. A session-only key can still be used. New saves, replacements, and removals are pending until Settings Save; **Cancel** discards these pending changes. A failed save preserves the previous saved credential.

Profile exports contain no API keys, encrypted credential files, or passphrases. Encrypted files are stored in the `credentials` subdirectory of SpeechDesk's configuration directory. This feature works without an operating-system keychain. Read [Privacy and data](privacy.html#encrypted-key-storage) for its protection and limitations.

## Request limits

Two controls set how SpeechDesk prepares speech sections and how long it allows generation or a service request to take:

- **Timeout:** 10–1,800 seconds, with a default of 180 seconds.
- **Characters per section:** normally 80–8,000, with a default of 500. The OpenAI preset limits this field to 4,096.

For service profiles, follow the service's own limits. Increasing a timeout does not speed up synthesis, and increasing section size may increase the wait before playback. SpeechDesk divides text at sentence and paragraph boundaries where possible.

## Dictation

**Recognition CPU threads** can be set from 1 to 32. The initial value uses up to four available processor threads. More threads do not guarantee better performance on every computer.

**Import model pack…** installs an optional local model. This action takes effect when the import finishes; choosing Cancel in Settings afterwards does not uninstall it. See [Model packs](model-packs.html).

## Saved preferences

Preferences and installed models use `%AppData%\Speech-Desk` on Windows or `$XDG_CONFIG_HOME/Speech-Desk` on Linux, normally `~/.config/Speech-Desk`.

The editor's text and generated audio are not automatically retained. Use their explicit save actions for anything you want to keep. Session-only API keys must be entered again after a restart. Encrypted keys require their passphrase before use.

## About and online help

The **About** tab shows the installed application version and a **Manual** button. Choose Manual to open the online documentation in your default browser.

<figure class="theme-screenshot">
<img class="screenshot-light" src="assets/settings-about-light.png" alt="SpeechDesk Settings on the About tab, showing version information and the Manual button." loading="lazy" decoding="async">
<img class="screenshot-dark" src="assets/settings-about-dark.png" alt="SpeechDesk Settings on the About tab, showing version information and the Manual button." loading="lazy" decoding="async">
<figcaption>The About tab provides the application version and a direct link to the manual.</figcaption>
</figure>
