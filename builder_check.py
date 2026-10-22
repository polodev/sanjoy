"""Checks for generated Sentence Builder chapters (a copy of the checks used in ~/sites/language)."""
import json
import re

BN = re.compile(r"[\u0980-\u09FF]")
FORBIDDEN = re.compile(r"\b(beer|wine|alcohol|whisk(?:e)?y|vodka|pork|bacon|ham|beef|steak|sausage)\b|(?<![\u0980-\u09FF])(?:মদ|শূকর|বিয়ার|ওয়াইন)(?![\u0980-\u09FF])|গরুর মাংস", re.I)
RELIGION = re.compile(r"নামাজ|সালাম|প্রার্থনা|মসজিদ|মন্দির|\b(?:pray(?:er|ers|ing)?|mosque|temple|church)\b", re.I)
FORMAL = re.compile(r"আপনি|আপনার|করুন|বলুন|রাখুন|বসান|দেখুন|পারবেন|ভুলবেন|শিখবেন|নিন\b|লিখুন|পড়ুন|শুনুন")

# ------------------------------------------------------------------ Sentence Builder
_TOKEN = re.compile(r"[^\w']+")


def _norm(tok):
    return _TOKEN.sub("", tok.lower())


def step_diff(prev, cur):
    """[(token, is_new)] for cur: words not carried over from prev are new (highlighted on the slide)."""
    from difflib import SequenceMatcher
    a, b = [_norm(t) for t in prev.split()], cur.split()
    out = [(t, True) for t in b]
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, a, [_norm(t) for t in b], autojunk=False).get_opcodes():
        if tag == "equal":
            for j in range(j1, j2):
                out[j] = (b[j], False)
    return out


def check_builder(n, d):
    p = []
    bs = d["builders"]
    if len(bs) != 10:
        p.append(f"{len(bs)} builders, want 10")
    for f in ("intro_bn", "tip_bn"):
        if not BN.search(d[f]):
            p.append(f"{f} is not Bangla")
    finals = set()
    for i, b in enumerate(bs, 1):
        st = b["steps"]
        if not 3 <= len(st) <= 5:
            p.append(f"builder {i} has {len(st)} steps, want 3-5")
        if not BN.search(b["note_bn"]):
            p.append(f"builder {i} note_bn is not Bangla")
        for k, x in enumerate(st):
            if not BN.search(x["bn"]) or BN.search(x["text"]):
                p.append(f"builder {i} step {k + 1}: text must be English and bn Bangla")
            if not BN.search(x["pron_bn"]):
                p.append(f"builder {i} step {k + 1}: pron_bn missing")
            if k:
                prev, cur = st[k - 1]["text"], x["text"]
                kept = sum(1 for _, new in step_diff(prev, cur) if not new)
                if len(cur.split()) <= len(prev.split()):
                    p.append(f"builder {i} step {k + 1} does not grow: {cur}")
                elif kept < 0.6 * len(prev.split()):
                    p.append(f"builder {i} step {k + 1} rewrites instead of adding: {prev} -> {cur}")
        if st and st[-1]["text"].lower() in finals:
            p.append(f"builder {i} repeats another builder")
        finals.add(st[-1]["text"].lower() if st else "")
    teacher = [d["intro_bn"], d["tip_bn"]] + [b["note_bn"] for b in bs]
    for t in teacher:
        m = FORMAL.search(t)
        if m:
            p.append(f"formal Bangla ({m.group(0)}): {t[:40]}")
    blob = json.dumps(d, ensure_ascii=False)
    if re.search(r"[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af]", blob):
        p.append("foreign script (Chinese/Japanese/Korean) in the text")
    for w in sorted({m.group(0) for m in FORBIDDEN.finditer(blob)} | {m.group(0) for m in RELIGION.finditer(blob)}):
        p.append(f"culturally unsuitable or religious word: {w}")
    return p
