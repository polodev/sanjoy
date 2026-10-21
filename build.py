"""Builds the whole site (static HTML in english/, japanese/, index.html).   python3 build.py

Content lives in english101.py and japanese101.py; engine.py has the HTML pieces; assets/ holds CSS and JS.
Relative links everywhere, so it works at https://<user>.github.io/sanjoy/ and later at https://sanjoy.cloud/."""
import shutil
import sys

from engine import ROOT, bn, esc, page, write
import english101 as E
import japanese101 as J
import site_english
import site_japanese

LANGS = {
    "english": dict(mod=E, name="English", bn_name="ইংরেজি", badge="A", theme="en", builder=site_english.build_day,
                    intro="গল্পে গল্পে ইংরেজি — প্রতিটি Day-তে একটা ছোট গল্প, ১০টি নতুন শব্দ আর ২০টি বাক্য।",
                    meta="১০ Day · ১০০ শব্দ · ২০০ বাক্য", n_days=10),
    "japanese": dict(mod=J, name="Japanese", bn_name="জাপানি", badge="あ", theme="ja", builder=site_japanese.build_day,
                     intro="হিরাগানা দিয়ে জাপানি লেখা শিখুন — প্রতিটি Day-তে একটি সারির অক্ষর, পড়ার অনুশীলন আর কুইজ।",
                     meta="১০ Day · ৭১ অক্ষর · প্রথম বাক্য", n_days=10),
}


def home():
    cards = "".join(
        f'<a class="card lang {v["theme"]}" href="{k}/index.html"><div class="badge">{v["badge"]}</div><div><b>{v["name"]} — {v["bn_name"]}</b>'
        f'<span>{v["intro"]}</span><br><span style="font-size:14px">{v["meta"]}</span></div></a>' for k, v in LANGS.items())
    body = (f'<header class="hero"><div class="in"><h1>সঞ্জয়ের ভাষা শেখার ঘর</h1><p>ইংরেজি আর জাপানি — বাংলায়, গল্পে গল্পে, মোবাইলে সহজে পড়ার মতো। রোজ একটা Day, রোজ একটু একটু।</p></div></header>'
            f'<main class="wrap">{cards}<p class="note">🔊 প্রতিটি শব্দ আর বাক্য শুনতে পাবেন · 👆 স্লাইডে বাঁ-ডানে swipe করুন · ✅ আপনার অগ্রগতি এই ফোনেই জমা থাকে</p></main>')
    write("index.html", page("সঞ্জয়ের ভাষা শেখার ঘর — English ও Japanese", body, 0, "home",
                             "ইংরেজি আর জাপানি শিখুন বাংলায়: গল্পে গল্পে ইংরেজি, হিরাগানা দিয়ে জাপানি।"))


def language_page(k, v):
    c = v["mod"].COURSE
    body = (f'<header class="hero"><div class="in"><a class="back" href="../index.html">← হোম</a><h1>{v["name"]} — {v["bn_name"]}</h1><p>{v["intro"]}</p></div></header>'
            f'<main class="wrap"><a class="card course" href="101/index.html"><span class="tag">101</span><b>{c["title"]} — {c["tag"]}</b>'
            f'<span class="sub">{c["sub"]}</span><span class="sub">{v["meta"]}</span></a>'
            f'<div class="card course locked"><span class="tag">102</span><b>{v["name"]} 102</b><span class="sub">🔒 শীঘ্রই আসছে</span></div></main>')
    write(f"{k}/index.html", page(f"{v['name']} — সঞ্জয়ের ভাষা শেখার ঘর", body, 1, v["theme"]))


def course_page(k, v):
    c = v["mod"].COURSE
    days = []
    for n in range(1, v["n_days"] + 1):
        if k == "english":
            d = E.DAYS[n - 1]
            title, sub = d["en"], f'{d["bn"]} · ১০ শব্দ · ২০ বাক্য'
        else:
            t, s = J.TITLES[n]
            title, sub = t, s
        days.append(f'<a class="day" data-deckkey="{k}/101/day-{n:02d}" href="day-{n:02d}/index.html"><span class="n">Day<b>{bn(n)}</b></span>'
                    f'<span class="t"><b>{esc(title)}</b><span>{esc(sub)}</span></span><span class="tick">✓</span></a>')
    body = (f'<header class="hero"><div class="in"><a class="back" href="../index.html">← {v["name"]}</a><h1>{c["title"]}</h1><p>{c["lead"]}</p></div></header>'
            f'<main class="wrap"><div class="card"><div class="bar"><i id="progress"></i></div>'
            f'<p class="note" id="progress-text">০ / {bn(v["n_days"])} দিন শেষ</p>'
            f'<p style="text-align:center;margin-top:10px"><a class="btn" id="continue" href="day-01/index.html">▶ শুরু করুন</a></p></div>'
            f'<div class="days">{"".join(days)}</div></main>')
    write(f"{k}/101/index.html", page(f"{c['title']} — {c['tag']}", body, 2, v["theme"]))


def not_found():
    body = ('<header class="hero"><div class="in"><h1>পাতাটি পাওয়া যায়নি</h1><p>ঠিকানাটা ভুল হতে পারে।</p></div></header>'
            '<main class="wrap"><a class="card" href="/" style="text-align:center"><b>🏠 হোমে ফিরে যান</b></a></main>')
    html = page("404 — পাতা নেই", body, 0, "home")
    # 404.html is served from any depth, so work out the site root at run time (project page vs custom domain)
    html = html.replace('<link rel="stylesheet" href="assets/app.css">', "").replace('<script src="assets/app.js"></script>', "")
    html = html.replace('href="/"', 'href="/" id="home404"').replace("</body>", """<script>
var root = /\\.github\\.io$/.test(location.hostname) ? '/' + location.pathname.split('/')[1] + '/' : '/';
document.getElementById('home404').href = root;
var l = document.createElement('link'); l.rel = 'stylesheet'; l.href = root + 'assets/app.css'; document.head.appendChild(l);
</script></body>""")
    write("404.html", html)


if __name__ == "__main__":
    for k in LANGS:
        shutil.rmtree(ROOT / k, ignore_errors=True)
    home()
    for k, v in LANGS.items():
        language_page(k, v)
        course_page(k, v)
        for n in range(1, v["n_days"] + 1):
            v["builder"](E.DAYS[n - 1] if k == "english" else n)
    not_found()
    pages = sum(1 for _ in ROOT.rglob("index.html"))
    print(f"built {pages} pages")
