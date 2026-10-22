"""English Sentence Builder (A1–B1): content/english-builder/ch-NN.json -> deck pages.
One builder per slide: the sentence grows step by step and the words each step adds are highlighted."""
import json

from builder_check import step_diff
from engine import DECK_BASE, FULL_NAME, avatar, bn, cover, deck_page, esc, finish_slide, mcq, quiz_slide, seeded, slide, write
from tools.gen_builder import CHAPTERS

TTS = "en-US"
KEY = "english/builder"


def ready(n):
    from engine import ROOT
    return (ROOT / "content" / "english-builder" / f"ch-{n:02d}.json").exists()


def load(n):
    from engine import ROOT
    return json.loads((ROOT / "content" / "english-builder" / f"ch-{n:02d}.json").read_text(encoding="utf-8"))


def marked(prev, cur):
    if prev is None:
        return esc(cur)
    out, run = [], []
    for tok, new in step_diff(prev, cur) + [("", False)]:
        if new:
            run.append(esc(tok))
            continue
        if run:
            out.append(f'<mark class="add">{" ".join(run)}</mark>')
            run = []
        if tok:
            out.append(esc(tok))
    return " ".join(out)


def builder_slide(i, b):
    rows, prev = [], None
    for k, st in enumerate(b["steps"], 1):
        rows.append(f'<div class="bstep" data-say="{esc(st["text"], quote=True)}" data-lang="{TTS}" role="button" tabindex="0">'
                    f'<span class="bn-no">{k}</span><div class="b-body"><p class="b-tx">{marked(prev, st["text"])}</p>'
                    f'<div class="b-more"><p class="pr">{esc(st["pron_bn"])}</p><p class="bn">{esc(st["bn"])}</p></div></div><span class="chev">›</span></div>')
        prev = st["text"]
    size = sum(len(st["text"]) for st in b["steps"])
    dens = "tight" if size > 430 else "dense" if size > 280 else ""
    return slide(f'<span class="chip">🧱 বাক্য {bn(i)} / ১০</span><div class="bld {dens}">{"".join(rows)}</div>'
                 f'<p class="hint b-note">💡 {esc(b["note_bn"])}</p>', "", f"বাক্য {i}")


def quiz_for(n, d):
    rng = seeded("builder", n)
    finals = [b["steps"][-1] for b in d["builders"]]
    qs = []
    for st in rng.sample(finals, 8):
        opts, a = mcq(rng, st["bn"], [x["bn"] for x in finals])
        qs.append(dict(q=f"“{st['text']}” — এর মানে কী?", say=st["text"], lang=TTS, o=opts, a=a, why=f'{st["text"]} = {st["bn"]}'))
    for b in rng.sample(d["builders"], 2):
        st = b["steps"]
        k = rng.randrange(len(st) - 1)
        others = [x["steps"][min(k + 1, len(x["steps"]) - 1)]["text"] for x in d["builders"] if x is not b]
        opts, a = mcq(rng, st[k + 1]["text"], others)
        qs.append(dict(q=f"“{st[k]['text']}” — এর পরের ধাপ কোনটা?", o=opts, a=a, why=f'{st[k + 1]["text"]} = {st[k + 1]["bn"]}'))
    return qs


def build_day(n):
    level, title_bn, _focus = CHAPTERS[n - 1]
    d = load(n)
    key = f"{KEY}/day-{n:02d}"
    steps = sum(len(b["steps"]) for b in d["builders"])
    S = [cover(f"অধ্যায় {bn(n)} · {level}", esc(title_bn), esc(d["intro_bn"]),
               [f"🧱 ১০টি বাক্য, ধাপে ধাপে বড় করা ({bn(steps)} ধাপ)", "🟩 প্রতি ধাপে নতুন অংশটা সবুজ", "🔊 ধাপে ট্যাপ করলে শুনবে আর বাংলা দেখবে", "📝 ১০ প্রশ্নের কুইজ"])]
    S += [builder_slide(i, b) for i, b in enumerate(d["builders"], 1)]
    S.append(slide(f'<span class="chip">💡 টিপস</span><div class="callout">{esc(d["tip_bn"])}</div>'
                   '<div class="callout warn">🎯 আজকের কাজ: যেকোনো একটা ছোট বাক্য নিয়ে নিজে তিন ধাপে বড় করে বলো।</div>', "", "টিপস"))
    S.append(quiz_slide(quiz_for(n, d)))
    chips = [esc(b["steps"][0]["text"]) for b in d["builders"][:6]]
    if n < len(CHAPTERS) and ready(n + 1):
        S.append(finish_slide(key, f"অধ্যায় {bn(n)} শেষ!", "আজকের বড় বাক্যগুলো থেকে দুটো মুখস্থ করে দিনে কয়েকবার বলো।", chips,
                              f"../day-{n + 1:02d}/index.html", f"অধ্যায় {bn(n + 1)}: {esc(CHAPTERS[n][1])}"))
    elif n < len(CHAPTERS):
        S.append(finish_slide(key, f"অধ্যায় {bn(n)} শেষ!", "পরের অধ্যায় শীঘ্রই আসছে।", chips))
    else:
        S.append(finish_slide(key, "Sentence Builder সম্পূর্ণ! 🏆", "A1 থেকে B1 — ছোট বাক্য থেকে বড় বাক্য। দারুণ কাজ!", chips))
    html = deck_page(f"অধ্যায় {n} · {title_bn} — Sentence Builder", key, "en", S, back_href="../index.html",
                     crumb=f"অধ্যায় {bn(n)} · {level} · {title_bn}", home_href="../../../index.html", has_bn=True, back_label="সব অধ্যায়")
    write(f"{KEY}/day-{n:02d}/index.html", html)
