# Sanjoy — agent guide

Language-learning site: **English** and **Japanese**, taught in **Bangla**, mobile first.
Repo `polodev/sanjoy` → GitHub Pages `https://polodev.github.io/sanjoy/` (future custom domain `sanjoy.cloud`; add a `CNAME` file only after the domain is bought).

## Structure the owner asked for
Home → language (English / Japanese) → course (101; 102 shown as "coming soon") → chapters **Day 1 … Day 10**; each Day is one swipeable slide deck.
English teaches through stories ("গল্পে গল্পে"): per Day a story, **10 words, 20 sentences**. Japanese teaches letters (hiragana).

## Files
- `english101.py` — English days as data (`day(n, en, bn, intro, story, words, sentences, grammar)`); text blocks use `English | Bangla` lines, words use `English | Bangla pronunciation | Bangla meaning`. Asserts 8 story lines, 10 words, 20 sentences per day.
- `japanese101.py` — kana table `K`, example words `EX`, reading words `WORDS`, sentences, look-alike pairs, `romaji()` generator. `validate()` fails the build if a practice word uses a letter not yet taught that day. **Never type romaji by hand.**
- `site_english.py`, `site_japanese.py` — slide builders. `engine.py` — shared HTML. `build.py` — builds everything.
- `assets/app.css`, `assets/app.js` — the only CSS/JS (no frameworks). Generated pages link them relatively.

## Rules
- Bangla prose, English/Japanese examples. Keep slides small: one idea each, large text, nothing wider than a phone (390 px). Tables must not overflow.
- Mobile behaviour is a requirement: decks are pinned to the viewport; vertical drag scrolls inside a slide; horizontal swipe changes slide; tap targets ≥ 44 px.
- Speech uses `speechSynthesis` (`en-US`, `ja-JP`); 🐢 slows it; 👁 blurs Bangla (English only). No audio files.
- Cultural care: no alcohol or pork examples (Bangladeshi audience).
- Relative links only (works under `/sanjoy/` and at a domain root).
- Quizzes are generated at build time with a seeded RNG (stable diffs). English: 5 word + 3 sentence + 1 grammar. Japanese: 4 sound + 3 letter + 3 word + 1 listening.

## Build and verify
```bash
python3 build.py        # regenerates every page (25 pages today)
```
Check on an emulated phone (Playwright, 390×844, `isMobile`, `hasTouch`): no horizontal overflow, swipe works, quiz works, no console errors.
Reload the page between screenshots of different `#slide` hashes (a hash-only navigation does not reload).

## Publish
Commit generated files too. Commit messages: plain, **no AI/Claude mentions, no Co-Authored-By** (owner's rule). `git push` → Pages deploys from `main` `/`.

## Next ideas (queue)
- English 102 (new story days) and Japanese 102 (katakana, first grammar). Add a `courses` entry per language in `build.py` and a `COURSE` in the new content module; `build.py` currently builds course `101` only — generalise `course_page`/`language_page` when 102 is added.
- Stroke-order animations for kana; audio recorded by a native speaker; printable review sheets.
