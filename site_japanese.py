"""Turns japanese101 into deck pages."""
from engine import (DECK_BASE, FULL_NAME, avatar, bn, chunks, cover, deck_page, esc, finish_slide, mcq, quiz_slide, say_btn, seeded, slide, write)
import japanese101 as J

LANG = "ja-JP"
K = J.K


def kcell(c):
    r, b = K[c]
    return (f'<button class="kcell" data-say="{c}" data-lang="{LANG}"><span class="jp">{c}</span><b>{r}</b><small>{b}</small></button>')


def krow(letters):
    return '<div class="krow">' + "".join(kcell(c) for c in letters) + "</div>"


def exword(word, meaning):
    return (f'<div class="exword">{say_btn(word.replace(" ", ""), LANG)}<div><div class="jp">{esc(word)}</div>'
            f'<small>{esc(J.romaji(word))} · {esc(meaning)}</small></div></div>')


def rcard(word, meaning):
    return (f'<div class="rcard" role="button" tabindex="0"><div class="top"><span class="jp">{esc(word)}</span>'
            f'{say_btn(word.replace(" ", ""), LANG)}<span class="tap">ট্যাপ করুন</span></div>'
            f'<div class="more"><b>{esc(J.romaji(word))}</b> · {esc(meaning)}</div></div>')


def sent_card(jp, meaning):
    return (f'<div class="rcard sent" role="button" tabindex="0"><div class="top"><span class="jp">{esc(jp)}</span>'
            f'{say_btn(jp.replace(" ", ""), LANG)}</div>'
            f'<div class="more"><b>{esc(J.romaji(jp))}</b><br>{esc(meaning)}</div></div>')


NOTES = {
    "し": "‘সি’ নয় — ‘শি’ (sh)।", "ち": "‘চি’ (chi) — ‘টি’ নয়।", "つ": "‘ৎসু’ (tsu): জিভ দাঁতের পেছনে ছুঁয়ে ‘ৎস’ বলুন।",
    "ふ": "হু আর ফু-র মাঝামাঝি — ঠোঁট একটু গোল করে আলতো ফুঁ।", "は": "শব্দের শুরুতে ‘হা’। কিন্তু আলাদা চিহ্ন হিসেবে (わたし は) পড়া হয় ‘ওয়া’।",
    "へ": "আলাদা চিহ্ন হিসেবে (দিক বোঝাতে) পড়া হয় ‘এ’।", "を": "উচ্চারণ ‘ও’ (お-র মতোই)। শুধু কর্ম বোঝানোর চিহ্ন: ほん を よむ = বই পড়ি।",
    "ん": "আলাদা ধ্বনি: নাকের টানসহ ‘ন্’ (বাংলা ‘ং’-এর কাছাকাছি)। শব্দের শেষে বা মাঝে বসে, কখনো শুরুতে না।",
    "ら": "জাপানি ‘র’ — বাংলা র আর ড়-এর মাঝামাঝি, জিভের ডগা আলতো ছুঁয়ে।", "り": "জিভের ডগা আলতো ছুঁয়ে ‘রি’ (বাংলা র আর ড়-এর মাঝামাঝি)।",
    "る": "আলতো ‘রু’ — জিভের ডগা আলতো ছুঁয়ে।", "れ": "আলতো ‘রে’।", "ろ": "আলতো ‘রো’।", "や": "‘ইয়া’ — য় + আ।", "ゆ": "‘ইউ’ — য় + উ।", "よ": "‘ইয়ো’ — য় + ও।",
    "わ": "‘ওয়া’ — ও + আ দ্রুত।", "じ": "ぢ-ও একই ‘জি’ পড়া হয়, তবে ぢ খুব কম লেখা হয়।", "ず": "づ-ও একই ‘জু’, তবে づ খুব কম লেখা হয়।",
    "ぢ": "じ-র মতোই ‘জি’; ব্যবহার খুব কম।", "づ": "ず-র মতোই ‘জু’; ব্যবহার খুব কম।",
}

WRITE_TIP = ('<span class="chip">✍️ লেখার অভ্যাস</span><h2>হাতে লিখলে মনে থাকে</h2>'
             '<ul class="pts"><li>কাগজে প্রতিটি অক্ষর <b>১০ বার</b> লিখুন, লেখার সময় জোরে উচ্চারণ করুন।</li>'
             '<li>নিয়ম: <b>ওপর থেকে নিচে</b>, <b>বাঁ থেকে ডানে</b>। প্রতিটি দাগ আলাদা করে — আঁকার মতো করে নয়।</li>'
             '<li>ছবি না দেখে মনে করে লিখুন, তারপর মিলিয়ে নিন।</li>'
             '<li>প্রতিদিন নতুন অক্ষরের সাথে <b>আগের দিনের অক্ষরও</b> একবার লিখুন।</li></ul>'
             '<div class="callout">💡 ১০ মিনিট রোজ, ঘণ্টার পর ঘণ্টা একদিনে নয় — এতেই দ্রুত শেখা হয়।</div>')


def letters_of(n):
    return [c for row in J.ROWS[n] for c in row]


def look_slide(n):
    known = J.learned_upto(n)
    today = set(letters_of(n))
    pairs = [(a, b, why) for a, b, why in J.LOOK if a in known and b in known and (a in today or b in today)]
    if not pairs:
        return None
    rows = "".join(f'<div class="line"><div class="chips"><span class="kchip">{a}</span><span class="kchip">{b}</span></div>'
                   f'<div><p>{esc(why)}</p></div></div>' for a, b, why in pairs)
    return slide(f'<span class="chip">🔍 সাবধান</span><h2>একই রকম দেখতে অক্ষর</h2>'
                 f'<p class="lead">এই জোড়াগুলো সবাই গুলিয়ে ফেলে। পার্থক্যটা মনে রাখুন:</p>{rows}', "", "একই রকম অক্ষর")


def letter_slides(n):
    letters = letters_of(n)
    out = []
    for i, c in enumerate(letters, 1):
        r, b = K[c]
        ex = J.EX.get(c)
        extra = NOTES.get(c)
        body = (f'<span class="chip">Day {bn(n)} · অক্ষর {bn(i)}/{bn(len(letters))}</span>'
                f'<div class="kana-box"><div class="kana-big">{c}</div><div class="k-ro">{r}</div><div class="k-bn">{b}</div>{say_btn(c, LANG, big=True)}</div>')
        if extra:
            body += f'<div class="callout">💡 {esc(extra)}</div>'
        if ex:
            body += f'<p class="hint">এই অক্ষর দিয়ে একটি শব্দ:</p>{exword(*ex)}'
        out.append(slide(body, "", c))
    return out


def quiz_for(n):
    rng = seeded("ja", n)
    today = letters_of(n)
    earlier = [c for d in range(1, n) for row in J.ROWS[d] for c in row]
    pool = today + earlier
    words_pool = [w for d in range(1, n + 1) for w in J.WORDS[d]]
    qs = []

    def pick(k):
        pri = rng.sample(today, min(len(today), k))
        if n > 1 and k >= 3:
            pri = pri[:k - 1] + [rng.choice(earlier)]
        return pri if len(pri) == k else (pri + rng.sample(pool, k - len(pri)))

    def sounds_options(c):
        others = [x for x in pool if K[x][1] != K[c][1]]
        sounds = list(dict.fromkeys(K[x][1] for x in others))
        return mcq(rng, K[c][1], sounds)

    def kana_options(c):
        others, seen = [], {K[c][1]}
        for x in rng.sample(pool, len(pool)):
            if K[x][1] not in seen and x != c:
                others.append(x)
                seen.add(K[x][1])
        opts = others[:3] + [c]
        rng.shuffle(opts)
        return opts, opts.index(c)

    for c in pick(4):
        opts, a = sounds_options(c)
        qs.append(dict(q="এই অক্ষরের উচ্চারণ কী?", big=c, o=opts, a=a, say=c, lang=LANG, why=f"{c} = {K[c][0]} ({K[c][1]})"))
    for c in pick(3):
        opts, a = kana_options(c)
        qs.append(dict(q=f"‘{K[c][1]}’ ({K[c][0]}) — কোন অক্ষর?", o=opts, a=a, ko=True, why=f"{c} = {K[c][0]}"))
    for w, m in rng.sample(words_pool, 3):
        opts, a = mcq(rng, m, [x[1] for x in words_pool], n=4)
        qs.append(dict(q="এই শব্দের মানে কী?", big=w, o=opts, a=a, say=w, lang=LANG, why=f"{w} ({J.romaji(w)}) = {m}"))
    c = rng.choice(today)
    opts, a = kana_options(c)
    qs.append(dict(q="শুনুন — কোন অক্ষরটা বলল? (🔊 চাপুন)", o=opts, a=a, ko=True, say=c, lang=LANG, auto=True, why=f"{c} = {K[c][0]} ({K[c][1]})"))
    return qs


def reading_slides(n, per=4):
    words = J.WORDS[n]
    parts = chunks(words, per)
    return [slide(f'<span class="chip">📖 পড়ার অনুশীলন {bn(i)}/{bn(len(parts))}</span><h2>শব্দ পড়ুন</h2>'
                  '<p class="hint">আগে নিজে পড়ার চেষ্টা করুন, তারপর কার্ডে ট্যাপ করে উত্তর মিলিয়ে নিন। শুধু শেখা অক্ষরই আছে!</p>'
                  + "".join(rcard(*w) for w in grp), "", "পড়া") for i, grp in enumerate(parts, 1)]


def chart_slide():
    cells = []
    for row in J.CHART_ROWS:
        for c in row:
            cells.append(kcell(c) if c else '<div class="kcell empty"></div>')
    return slide('<span class="chip">🏆 মাইলফলক</span><h2>পুরো হিরাগানা ছক</h2>'
                 '<p class="lead">৪৬টি মূল অক্ষর — আপনি সবই শিখেছেন! ট্যাপ করে শুনুন, ফাঁকা ঘরে অক্ষর নেই।</p>'
                 f'<div class="chart">{"".join(cells)}</div>', "", "পুরো ছক")


def day1_intro():
    return [slide('<span class="chip">🗾 শুরুর কথা</span><h2>জাপানি লেখা কেমন?</h2>'
                  '<table class="tbl"><tr><th>লেখা</th><th>কী</th><th>কখন</th></tr>'
                  '<tr><td><b class="jp">ひらがな</b></td><td>হিরাগানা — ৪৬ অক্ষর</td><td>জাপানি শব্দ, ব্যাকরণ <b>(এখন এটা)</b></td></tr>'
                  '<tr><td><b class="jp">カタカナ</b></td><td>কাতাকানা — ৪৬ অক্ষর</td><td>বিদেশি শব্দ (コーヒー = কফি)</td></tr>'
                  '<tr><td><b class="jp">漢字</b></td><td>কাঞ্জি — চীনা অক্ষর</td><td>অর্থবহ অক্ষর (山 = পাহাড়)</td></tr></table>'
                  '<div class="callout">প্রথমে হিরাগানা শিখলেই জাপানি পড়া শুরু করা যায় — কাঞ্জির উপরেও ছোট করে হিরাগানায় উচ্চারণ লেখা থাকে।</div>', "", "জাপানি লেখা"),
            slide('<span class="chip">✨ সুখবর</span><h2>হিরাগানা শেখা সহজ</h2>'
                  '<ul class="pts"><li><b>প্রতিটি অক্ষর = একটি নির্দিষ্ট ধ্বনি।</b> ইংরেজির মতো বানানের ঝামেলা নেই — যা লেখা, তাই পড়া।</li>'
                  '<li>প্রায় প্রতিটি অক্ষর <b>ব্যঞ্জন + স্বর</b>: か = ক + আ = <b>কা</b>। বাংলা বর্ণমালার সাথে অনেক মিল।</li>'
                  '<li>মোট <b>৪৬টি</b> মূল অক্ষর, তারপর দুটো চিহ্ন দিয়ে আরও কিছু। আমরা <b>১০ দিনে</b> সব শিখব।</li>'
                  '<li>পাঁচটি স্বর: <b>あ い う え お</b> (আ ই উ এ ও) — সব সারির শেষে এই স্বরগুলোই ঘুরে ঘুরে আসে।</li></ul>'
                  '<div class="callout">🔊 প্রতিটি অক্ষর ট্যাপ করলে শুনতে পাবেন। জাপানি voice না পেলে ফোনের Settings → Text-to-speech থেকে Japanese যোগ করুন।</div>', "", "সহজ")]


def day10_extras():
    s = []
    pairs = "".join(f'<div class="exword"><div class="chips"><span class="kchip">{a}</span><span class="kchip">＋{"゛" if b in "がざだば" else "゜"}</span><span class="kchip">{b}</span></div>'
                    f'<div><small>{K[a][0]} → {K[b][0]} · {K[a][1]} → {K[b][1]}</small></div></div>' for a, b in J.DAKU_PAIRS)
    s.append(slide('<span class="chip">゛ ゜</span><h2>দুটো ছোট চিহ্ন, ২৫টি নতুন ধ্বনি</h2>'
                   '<p class="lead">অক্ষরের কোনায় <b>゛ (দুই ফোঁটা)</b> বা <b>゜ (বৃত্ত)</b> বসালে ধ্বনি ভারী (ঘোষ) হয়ে যায়। নতুন করে মুখস্থ করার কিছু নেই!</p>' + pairs, "", "゛ ゜"))
    groups = J.ROWS[10]
    names = ["が行 (গ)", "ざ行 (জ)", "だ行 (দ)", "ば行 (ব)", "ぱ行 (প)"]
    for g, name in zip(groups, names):
        body = f'<span class="chip">{name}</span><h2>{g[0]} {g[1]} {g[2]} {g[3]} {g[4]}</h2>{krow(g)}'
        if g[0] == "だ":
            body += '<div class="callout">💡 ぢ ও づ প্রায় ব্যবহার হয় না — じ ও ず-এর মতোই উচ্চারণ।</div>'
        body += "".join(exword(*J.EX[c]) for c in g if J.EX.get(c))
        s.append(slide(body, "", name))
    s.append(slide('<span class="chip">っ ছোট তসু</span><h2>ছোট っ = ক্ষণিক থামা</h2>'
                   '<p class="lead">পরের ব্যঞ্জনটা দ্বিগুণ হয়ে যায় — যেন একটা ছোট বিরতি নিয়ে তারপর বলা।</p>'
                   + exword("きって", "ডাকটিকিট") + exword("がっこう", "স্কুল") + exword("ざっし", "ম্যাগাজিন")
                   + '<div class="callout">が<b>っ</b>こう = gak<b>k</b>ou — ‘গাক্কো’। ছোট っ ছাড়া きて (kite = এসো), ছোট っ দিয়ে きって (kitte = ডাকটিকিট) — অর্থই আলাদা!</div>', "", "ছোট っ"))
    combos = [("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"), ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"),
              ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"), ("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo")]
    for c, r in combos:
        assert J.romaji(c) == r, (c, J.romaji(c), r)
    cells = "".join(f'<button class="kcell" data-say="{c}" data-lang="{LANG}"><span class="jp">{c}</span><b>{r}</b><small>{J.SMALL_SOUND[c]}</small></button>' for c, r in combos)
    s.append(slide('<span class="chip">ゃ ゅ ょ</span><h2>ছোট や ゆ よ = এক ধ্বনি</h2>'
                   '<p class="lead">i-কারের অক্ষরের পাশে ছোট ゃ ゅ ょ বসলে দুই অক্ষর মিলে <b>একটাই ধ্বনি</b> হয়।</p>'
                   f'<div class="chart" style="grid-template-columns:repeat(3,1fr)">{cells}</div>'
                   + exword("しゃしん", "ছবি") + exword("おちゃ", "চা") + exword("びょういん", "হাসপাতাল") + exword("べんきょう", "পড়াশোনা"), "", "ゃ ゅ ょ"))
    s.append(slide('<span class="chip">টান</span><h2>লম্বা স্বর</h2>'
                   '<p class="lead">একই স্বর (বা お-এর পরে う) পরপর এলে টেনে লম্বা করে পড়তে হয়। টান ছাড়লে অর্থ বদলে যায়।</p>'
                   + exword("おかあさん", "মা") + exword("おにいさん", "বড় ভাই") + exword("ありがとう", "ধন্যবাদ") + exword("おはよう", "শুভ সকাল")
                   + '<div class="callout">romaji-তে অনেকে ō লেখে (arigatō); আমরা যেমন লেখা তেমনই দেখাচ্ছি: arigatou।</div>', "", "লম্বা স্বর"))
    return s


def sentence_slides():
    parts = chunks(J.SENTENCES, 4)
    out = [slide('<span class="chip">🧩 বাক্য গঠন</span><h2>প্রথম তিনটি শব্দ-চিহ্ন</h2>'
                 '<table class="tbl"><tr><th>শব্দ</th><th>উচ্চারণ</th><th>কাজ</th></tr>'
                 '<tr><td class="jp"><b>は</b></td><td>wa</td><td>বিষয়: <b>わたし は</b> = আমি (হলাম)</td></tr>'
                 '<tr><td class="jp"><b>です</b></td><td>desu</td><td>= হয়/আছি (ভদ্র): <b>…です</b></td></tr>'
                 '<tr><td class="jp"><b>これ / あれ</b></td><td>kore / are</td><td>এটা (কাছে) / ওটা (দূরে)</td></tr></table>'
                 '<div class="callout">গঠন: <b>[কী] は [কী] です</b> = [কী] হলো [কী]। ক্রিয়া সবার শেষে — বাংলার মতোই!</div>', "", "বাক্য গঠন")]
    for i, grp in enumerate(parts, 1):
        out.append(slide(f'<span class="chip">🗣️ প্রথম বাক্য {bn(i)}/{bn(len(parts))}</span><h2>বাক্য পড়ুন</h2>'
                         '<p class="hint">বিরতি (ফাঁকা জায়গা) শুধু শেখার সুবিধার জন্য। আগে পড়ুন, তারপর ট্যাপ করুন।</p>'
                         + "".join(sent_card(*x) + (f'<div class="you-card">{avatar(DECK_BASE, "ava")}<div><b>👆 এটা তুমি!</b><br><span>{FULL_NAME} = <span class="jp">さんじょい</span> (Sanjoy)।</span></div></div>' if x[0].startswith("わたし は さんじょい") else "") for x in grp), "", "বাক্য"))
    return out


def build_day(n):
    key = f"japanese/101/day-{n:02d}"
    title, sub = J.TITLES[n]
    letters = letters_of(n)
    learn = [f"✏️ {bn(len(letters))}টি নতুন অক্ষর", "🔊 প্রতিটির উচ্চারণ শুনুন", "📖 ছোট ছোট শব্দ পড়া", "📝 ১১টি প্রশ্নের কুইজ"]
    chips = "".join(f'<button class="kchip" data-say="{c}" data-lang="{LANG}">{c}</button>' for c in letters)
    first = cover(f"Day {n}", esc(title), esc(J.INTRO_LINES[n]), learn)
    first = first.replace('<p class="hint">', f'<div class="chips">{chips}</div><p class="hint">', 1)
    S = [first]
    if n == 1:
        S += day1_intro()
    if n < 10:
        S.append(slide(f'<span class="chip">ছক</span><h2>আজকের অক্ষর</h2><p class="hint">ট্যাপ করলে উচ্চারণ শুনবেন।</p>'
                       + "".join(krow(row) for row in J.ROWS[n]), "", "ছক"))
        S += letter_slides(n)
        ls = look_slide(n)
        if ls:
            S.append(ls)
    else:
        S += day10_extras()
    if n == 9:
        S.append(chart_slide())
    S += reading_slides(n, per=5 if n == 10 else 4)
    if n == 10:
        S += sentence_slides()
    S.append(slide(WRITE_TIP, "", "লেখা"))
    S.append(quiz_slide(quiz_for(n)))
    words = [w for w, _ in J.WORDS[n]][:8]
    if n == 10:
        S.append(finish_slide(key, "Japanese 101 সম্পূর্ণ! 🏆", "৭১টি অক্ষর, ডজন ডজন শব্দ আর আপনার প্রথম জাপানি বাক্য — আপনি হিরাগানা পড়তে পারেন! জাপানের যেকোনো শিশুর বই এখন আপনার নাগালে।",
                              words, None, back_href="../index.html",
                              extra='<div class="callout"><b>এখন কী করবেন?</b><br>প্রতিদিন ৫ মিনিট পুরো ছক (Day 9) ট্যাপ করে পড়ুন। Japanese 102-তে আসছে: কাতাকানা ও প্রথম ব্যাকরণ।</div>'))
    else:
        S.append(finish_slide(key, f"Day {bn(n)} শেষ!", "আজকের অক্ষরগুলো আজ রাতে ঘুমানোর আগে আরেকবার কাগজে লিখুন।", words,
                              f"../day-{n + 1:02d}/index.html", f"Day {bn(n + 1)}: {esc(J.TITLES[n + 1][0])}"))
    html = deck_page(f"Day {n} · {title} — Japanese 101", key, "ja", S, back_href="../index.html",
                     crumb=f"Day {bn(n)} · {title}", home_href="../../../index.html", has_bn=False)
    write(f"japanese/101/day-{n:02d}/index.html", html)
