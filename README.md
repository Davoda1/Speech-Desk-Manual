# SpeechDesk Manual

The user manual for [SpeechDesk](https://github.com/Davoda1/Speech-Desk), a native Windows and Linux application for text-to-speech playback and local dictation.

The website covers installation, speech providers, playback, dictation, optional model packs, settings and troubleshooting. It uses ordinary HTML pages with a persistent chapter navigation, on-page contents and browser-only search. All fonts, images, styles and scripts are local; the site has no analytics, external embeds or runtime dependencies.

![SpeechDesk manual website](docs/extras/manual-preview.jpg)

## Build

Python 3.12 or later is recommended.

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
```

Open `dist/index.html` directly, or serve `dist/` with a static web server. The search index is a local script, so search also works when the files are opened from disk. The build works at a domain root or a subdirectory such as `/Speech-Desk-Manual/`.

## Edit the manual

Write article content in `content/`. Page order and titles live in `scripts/build.py`; site styling and behavior live in `assets/`. Rebuild after editing. Content describes SpeechDesk **1.0.0**; check instructions against the application before documenting a later version.

The included screenshots show the application, not a separate browser implementation. The website stores only its chosen color theme in the browser. Search queries stay in the browser.

## Hosting

The generated `dist/` folder can be deployed to any static host. The **Build manual** workflow validates the source on `master` and uploads a ready-to-host `speechdesk-manual` artifact. It does not change repository visibility or enable public hosting.

When public hosting is wanted, GitHub Pages can serve the generated files under `https://davoda1.github.io/Speech-Desk-Manual/`. Enable Pages with GitHub Actions as its source, then run the **Deploy manual to GitHub Pages** workflow. Pages availability for private repositories depends on the GitHub account plan. A Pages website can be public even when its source repository is private; choose the intended audience before enabling it.

The application repository can link to the deployed website once its address and audience are confirmed.

## License

MIT, copyright © 2026 davoda1. Application screenshots and icon are from SpeechDesk.
