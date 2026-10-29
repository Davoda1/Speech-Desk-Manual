Download the package for your operating system, keep its included files together, and start the real application executable. The runtime packages already include Qt and the four default dictation models.

## Choose a package

All downloads are attached to the [SpeechDesk 1.0.0 release](https://github.com/Davoda1/Speech-Desk/releases/tag/v1.0.0).

| System | Package |
| --- | --- |
| Windows 10/11, x64 | `SpeechDesk-1.0.0-Windows-x64.zip` |
| Linux, amd64, portable | `SpeechDesk-1.0.0-Linux-amd64.tar.gz` |
| Debian-family Linux, amd64 | `SpeechDesk-1.0.0-Linux-amd64.deb` |

The source archives are for building the application. They do not contain the downloaded recognition models or generated native engines.

## Windows

1. Download the Windows ZIP and extract the entire archive into a folder.
2. Open **SpeechDesk.exe** at the root of that folder.
3. Keep the executable beside its libraries, plugins, and `resources` directory. Moving the EXE on its own will leave required files behind.

No separate Python or Qt installation is required. Recognition paths containing Unicode characters require Windows 10 version 1903 or newer.

When Windows requests microphone permission, allow it if you intend to use dictation. Text-to-speech playback does not require microphone access.

## Linux

For the portable package, extract the archive and run the top-level `speechdesk` executable. Keep the accompanying directories in place. Run it as your normal desktop user.

For the Debian package, open it with your package manager or run this command from the download directory:

```sh
sudo apt install ./SpeechDesk-1.0.0-Linux-amd64.deb
```

The package installs the real executable at `/usr/bin/speechdesk`. Launch SpeechDesk from your application menu or run `speechdesk` in a terminal.

Linux still needs a graphical desktop, working audio services, and the system dependencies required by the package. Bundled Qt libraries do not make the application independent of the operating system. Older distributions may not meet its runtime requirements.

## Verify a download

The release provides one **SHA256SUM.txt** file covering the downloadable assets. Compare the package's SHA-256 hash with its entry in that file.

On Windows, PowerShell can calculate the hash:

```powershell
Get-FileHash .\SpeechDesk-1.0.0-Windows-x64.zip -Algorithm SHA256
```

On Linux:

```sh
sha256sum SpeechDesk-1.0.0-Linux-amd64.tar.gz
```

Do not install a file whose hash differs. Download it again from the release page.

## Next steps

Follow [First reading](first-reading.html) to set up speech playback, or [Dictation](dictation.html) to begin using local recognition. Larger recognition models are optional; see [Model packs](model-packs.html).
