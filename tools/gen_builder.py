"""Generate Sentence Builder chapters with muse.   python3 tools/gen_builder.py [--only N,N] [--force] [-j 5]
Output: content/english-builder/ch-NN.json = {title, intro_bn, tip_bn, builders: [{note_bn, steps: [{text, pron_bn, bn}]}]}"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from builder_check import check_builder  # noqa: E402

CHAPTERS = [
    ("A1", "শুরুর বাক্য: কে কী করে", "subject + verb + object; add an object or an adjective"),
    ("A1", "কোথায় আর কখন", "add place (at home, in Hajiganj) and time (every day, at night)"),
    ("A1", "and আর but দিয়ে জোড়া", "join two short ideas with and / but; add adjectives"),
    ("A1", "পরিবার আর বন্ধু", "family and friends: have / has, my / his / her, adjectives"),
    ("A1", "দোকান আর কেনাকাটা", "shopping and prices: want / need / buy, numbers, quantities"),
    ("A1", "দিনের রুটিন", "daily routine with time phrases (at six, in the morning, after work)"),
    ("A2", "কত ঘন ঘন", "adverbs of frequency and time phrases (always, twice a week, on Fridays)"),
    ("A2", "গতকালের গল্প", "past simple; add when, where, with whom"),
    ("A2", "কারণ আর ফল", "because / so / to (purpose)"),
    ("A2", "তুলনা", "comparatives and superlatives growing a description"),
    ("A2", "ফার্মেসি আর স্বাস্থ্য", "health and the pharmacy: should, have to, can"),
    ("A2", "ভবিষ্যতের পরিকল্পনা", "going to / will plus time and place"),
    ("A2", "পথ আর যাতায়াত", "directions and transport with prepositions"),
    ("B1", "অভিজ্ঞতা", "present perfect with for / since / ever / already / yet"),
    ("B1", "who, which, that দিয়ে বর্ণনা", "relative clauses that add detail to a noun"),
    ("B1", "যদি…", "first and second conditionals (if + result)"),
    ("B1", "কাজের উদ্দেশ্য আর পছন্দ", "gerunds and infinitives (enjoy doing, decide to do, in order to)"),
    ("B1", "কাজটা করা হয়", "passive voice with agent, time and place"),
    ("B1", "কে কী বলল", "reported speech with said / told / asked"),
    ("B1", "স্বপ্ন আর লক্ষ্য", "future plans and goals: hope to, plan to, would like to, by next year"),
]
SCHEMA = ROOT / "tools" / "builder.schema.json"
MODEL = "muse-spark-1.3"

PROMPT = """You are writing one chapter of a "Sentence Builder" course for an adult Bangladeshi learner of English
(native language Bangla). Answer with the JSON object only. Do not use any tools.

Chapter {n} of 20, CEFR level {level} (the course runs A1 to B1). Focus: {focus}.

A builder starts from a short, simple core sentence and grows it in steps. Every step repeats the previous sentence
and ADDS one new chunk (a word, a phrase or a clause) that practises the focus; change an existing word only when the
grammar requires it (e.g. like tea -> like drinking tea). Example builder:
  1. I like tea.
  2. I like tea with milk.
  3. I like drinking tea with milk every morning.

Write exactly 10 builders. Each builder has 3 to 5 steps (use 4-5 at B1). The final sentence must sound
natural and match level {level}{level_note}. Vary the core sentences (family, work at the pharmacy, friends, travel,
study, health, shopping, weather, phone and internet, village and town life in Bangladesh). The learner is Sanjoy (Sanjoy Dev Shuvo), a graduate from Hajiganj, Chandpur who works at Medicine Corner, a pharmacy in Hajiganj Bazar; use "Sanjoy" as the main character often and Hajiganj / Chandpur / Dhaka / Medicine Corner naturally. Other names: Rahim, Nusrat, Sukumar, Rajib.
Culturally safe for Bangladeshi Muslims and Hindus: no alcohol, pork, beef, dating, gambling or religious rituals.

For every step: "text" (English), "bn" (natural Bangla meaning in standard চলিত Bangla, not word-by-word),
"pron_bn" ({pron_rule}).
For every builder: "note_bn" = one short Bangla sentence saying what the steps added (address the learner as তুমি).
Chapter: "title" (short English title), "intro_bn" (1-2 Bangla sentences, তুমি), "tip_bn" (2 Bangla sentences, তুমি).
"""

LEVEL_NOTE = {"A1": " (very short and simple)", "A2": " (simple, everyday)", "B1": ""}


def run(n, force=False):
    out_f = ROOT / "content" / "english-builder" / f"ch-{n:02d}.json"
    if out_f.exists() and not force:
        return f"skip {n}"
    out_f.parent.mkdir(parents=True, exist_ok=True)
    level, _title, focus = CHAPTERS[n - 1]
    pron_rule = "English pronunciation in Bangla script, e.g. 'I like tea.' -> 'আই লাইক টি।'"
    prompt = PROMPT.format(n=n, level=level, focus=focus, level_note=LEVEL_NOTE[level], pron_rule=pron_rule)
    last = ""
    for _ in range(3):
        with tempfile.TemporaryDirectory() as tmp:
            pf = Path(tmp) / "p.txt"
            pf.write_text(prompt, encoding="utf-8")
            r = subprocess.run(["muse", "exec", "--model", MODEL, "--reasoning-effort", "max", "--output-schema", str(SCHEMA),
                                "--prompt-file", str(pf), "--workspace", tmp], cwd=tmp, capture_output=True, text=True, timeout=1800)
        out = r.stdout.strip()
        try:
            d = json.loads(out[out.find("{"):out.rfind("}") + 1])
        except ValueError:
            last = "bad json"
            continue
        for b in d["builders"]:
            for st in b["steps"]:
                st["pron_bn"] = re.sub(r"\.(?=\s|$)", "।", st["pron_bn"].strip())
        probs = check_builder(n, d)
        if not probs:
            out_f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            return f"ok   {n}"
        last = "; ".join(probs[:5])
        prompt += f"\n\nThe previous answer had problems, fix them: {last}"
    return f"FAIL {n}: {last}"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("-j", type=int, default=5)
    a = ap.parse_args()
    nums = [int(x) for x in a.only.split(",") if x] or list(range(1, 21))
    with ThreadPoolExecutor(a.j) as ex:
        for msg in ex.map(lambda n: run(n, a.force), nums):
            print(msg, flush=True)
