# সঞ্জয়ের ভাষা শেখার ঘর — Sanjoy's Language Corner

English and Japanese, taught in Bangla, built for reading on a phone.

- **English 101 — গল্পে গল্পে ইংরেজি:** 20 days. Each day = a short story about Sanjoy, 10 words (with Bangla pronunciation), 20 sentences, a grammar tip and a quiz.
- **Japanese 101:** 10 chapters. Each chapter opens with 5 survival sentences (Bangla pronunciation, Bangla meaning, today's letters highlighted), then the chapter's hiragana. Day titles are Bangla only. All 46 basic hiragana + the 25 voiced/semi-voiced sounds, small っ ゃ ゅ ょ, reading practice, and the first sentences.

Live: https://polodev.github.io/sanjoy/ (later: https://sanjoy.cloud/)

## How it works

Static HTML, no framework. `python3 build.py` regenerates every page from the content files.

```
english101.py / japanese101.py   the lessons (data only)
site_english.py / site_japanese.py   turn lessons into slides
engine.py                        HTML helpers (pages, slides, quiz data)
assets/app.css, assets/app.js    styles and behaviour (swipe, speech, quiz, progress)
index.html, english/, japanese/  generated output (committed, served by GitHub Pages)
```

Pronunciation uses the phone's own text-to-speech (no audio files). Progress is stored in the browser (`localStorage`).

## Custom domain (sanjoy.cloud) — when bought

1. Add a file named `CNAME` containing `sanjoy.cloud` to the repo root and push.
2. At the domain registrar: `A` records for the apex to GitHub Pages IPs `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   (and optionally `www` CNAME → `polodev.github.io`).
3. Repo → Settings → Pages → Custom domain `sanjoy.cloud`, tick *Enforce HTTPS*.

All links are relative, so nothing else changes.
