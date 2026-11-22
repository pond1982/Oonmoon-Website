#!/usr/bin/env python3
"""One-off content update for Oonmoon 1.1 (22 November 2026).

The published pages carry hand edits made after scripts/build.py last ran, so
this patches the pages in place instead of regenerating them: three languages,
the pop-up book, the new set of included stories, and a "watch a story" section.
content.json, privacy-support.json (support answers only) and build.py get the
same wording so the sources do not drift further.
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHANNEL = "https://www.youtube.com/@oonmoonstories"

# (old, new) pairs applied to every page and to the JSON sources.
TEXT = [
    # English
    ("listen in Thai or English", "listen in English, Thai or Mandarin"),
    ("Thai and English recorded narration", "English, Thai and Mandarin recorded narration"),
    ("Oonmoon’s Thai and English narration", "Oonmoon’s English, Thai and Mandarin narration"),
    ("Ten familiar tales, Thai and English narration,", "Ten familiar tales, English, Thai and Mandarin narration,"),
    ("recorded narration and character choices. Available", "narration in three languages, a 3D pop-up book view and character choices. Available"),
    ("English and Thai recordings are bundled with the app.", "English, Thai and Mandarin recordings are bundled with the app."),
    ("Can I switch between Thai and English?", "Can I switch between English, Thai and Mandarin?"),
    ("Yes. Choose the story language in the app to use the matching captions and recorded narration.",
     "Yes. Tap the flag on the bookshelf or in the reader to move between English, Thai and Mandarin captions and recorded narration."),
    ("Little Red Riding Hood, The Tortoise and the Hare, and The Three Little Pigs are included.",
     "The Tortoise and the Hare, The Three Little Pigs and The Ugly Duckling are included."),
    ("The first three stories are included.", "Three stories are included."),
    ("The app is coming soon; the actual storefront price and listing will be shown when they are available.",
     "The price is shown in the app before you buy."),
    # Thai
    ("ฟังเสียงบรรยายภาษาไทยหรือภาษาอังกฤษ", "ฟังเสียงบรรยายภาษาไทย อังกฤษ หรือจีนกลาง"),
    ("พร้อมเสียงบรรยายภาษาไทยและภาษาอังกฤษที่บันทึกไว้", "พร้อมเสียงบรรยายภาษาไทย อังกฤษ และจีนกลางที่บันทึกไว้"),
    ("ทั้งเสียงบรรยายภาษาไทยและภาษาอังกฤษ", "ทั้งเสียงบรรยายภาษาไทย อังกฤษ และจีนกลาง"),
    ("พร้อมเสียงบรรยายภาษาไทยและอังกฤษ", "พร้อมเสียงบรรยายภาษาไทย อังกฤษ และจีนกลาง"),
    ("ไฟล์เสียงภาษาไทยและภาษาอังกฤษมาพร้อมกับแอป", "ไฟล์เสียงภาษาไทย อังกฤษ และจีนกลางมาพร้อมกับแอป"),
    ("สลับภาษาไทยกับภาษาอังกฤษได้ไหม?", "สลับภาษาไทย อังกฤษ และจีนกลางได้ไหม?"),
    ("ได้ เลือกภาษาของนิทานในแอปเพื่อใช้ข้อความและเสียงบรรยายที่ตรงกับภาษานั้น",
     "ได้ แตะธงบนชั้นหนังสือหรือในหน้าที่อ่านเพื่อสลับข้อความและเสียงบรรยายระหว่างภาษาไทย อังกฤษ และจีนกลาง"),
    ("รวมหนูน้อยหมวกแดง เต่าและกระต่าย และหมูน้อยสามตัวไว้ให้แล้ว", "รวมเต่าและกระต่าย หมูน้อยสามตัว และลูกเป็ดขี้เหร่ไว้ให้แล้ว"),
    ("หนูน้อยหมวกแดง เต่าและกระต่าย และหมูน้อยสามตัวเป็นสามเรื่องที่รวมไว้ให้แล้ว",
     "เต่าและกระต่าย หมูน้อยสามตัว และลูกเป็ดขี้เหร่เป็นสามเรื่องที่รวมไว้ให้แล้ว"),
    ("รวมสามเรื่องแรกไว้ให้แล้ว", "รวมนิทานสามเรื่องไว้ให้แล้ว"),
    ("ไม่มีค่าสมาชิก Oonmoon กำลังจะเปิดให้บริการ", "ไม่มีค่าสมาชิก ดาวน์โหลด Oonmoon ได้แล้วบน App Store"),
    ("แอปกำลังจะเปิดให้บริการ โดยจะแสดงราคาจริงและหน้าร้านเมื่อพร้อม", "แอปจะแสดงราคาก่อนยืนยันการซื้อ"),
]

CARDS = {
    "en": [
        ["Three languages, one adventure", "Listen to recorded English, Thai or Mandarin narration and read along with the story text. One tap on the flag switches language."],
        ["A pop-up book in 3D", "Turn on Pop-up and every page stands up like a real pop-up book, folding flat and springing open as you turn it."],
        ["A character of their own", "Choose a character and make its appearance your own."],
        ["Little things to discover", "Tap the characters and watch them jump, spin and dance."],
        ["Let the story turn the page", "Press Play and the story reads to the end, turning each page after its narration finishes. You can also turn pages yourself."],
        ["A shelf that can grow", "Three stories are included. A one-time full-library unlock covers the other seven and future completed books added to Oonmoon. No subscription."],
    ],
    "th": [
        ["สามภาษา หนึ่งการผจญภัย", "ฟังเสียงบรรยายภาษาไทย อังกฤษ หรือจีนกลางที่บันทึกไว้ และอ่านตามข้อความในนิทาน แตะธงครั้งเดียวเพื่อเปลี่ยนภาษา"],
        ["หนังสือป๊อปอัปสามมิติ", "เปิดโหมดป๊อปอัป แล้วทุกหน้าจะตั้งขึ้นเหมือนหนังสือป๊อปอัปจริง พับราบและกางขึ้นใหม่เมื่อพลิกหน้า"],
        ["เลือกตัวละครในแบบของตัวเอง", "เลือกตัวละครและปรับรูปลักษณ์ในแบบของตัวเอง"],
        ["สิ่งเล็ก ๆ ที่รอให้ค้นพบ", "แตะตัวละครแล้วดูมันกระโดด หมุน และเต้น"],
        ["ให้นิทานพาไปยังหน้าถัดไป", "กดปุ่มเล่น แล้วนิทานจะอ่านไปจนจบ โดยพลิกหน้าให้เมื่อเสียงบรรยายของแต่ละหน้าเล่นจบ หรือจะพลิกหน้าเองก็ได้"],
        ["ชั้นหนังสือที่เติบโตได้", "รวมนิทานสามเรื่องไว้ให้แล้ว ซื้อคลังนิทานครั้งเดียวเพื่อปลดล็อกอีกเจ็ดเรื่อง รวมถึงนิทานใหม่ที่เสร็จสมบูรณ์และเพิ่มเข้า Oonmoon ในอนาคต ไม่มีค่าสมาชิก"],
    ],
}

VIDEOS = {
    "en": {
        "heading": "Watch a story come to life.",
        "intro": "Full read-throughs in the 3D pop-up view, on our YouTube channel. Narrated in Thai for now.",
        "channel": "Visit the Oonmoon story channel on YouTube ↗",
        "items": [
            ("video-tortoise-hare-th.jpg", "The Tortoise and the Hare", "Watch now · Thai narration", "https://youtu.be/KBSWmVoIdcg"),
            ("video-three-pigs-th.jpg", "The Three Little Pigs", "Coming 29 November", CHANNEL),
            ("video-ugly-duckling-th.jpg", "The Ugly Duckling", "Coming 6 December", CHANNEL),
        ],
    },
    "th": {
        "heading": "ดูนิทานแบบป๊อปอัป",
        "intro": "ชมนิทานเต็มเรื่องในมุมมองหนังสือป๊อปอัปสามมิติ พร้อมเสียงบรรยายภาษาไทย บนช่อง YouTube ของเรา",
        "channel": "ไปที่ช่อง อุ่นมูน นิทานก่อนนอน บน YouTube ↗",
        "items": [
            ("video-tortoise-hare-th.jpg", "กระต่ายกับเต่า", "ดูได้แล้ว", "https://youtu.be/KBSWmVoIdcg"),
            ("video-three-pigs-th.jpg", "ลูกหมูสามตัว", "พบกัน 29 พฤศจิกายน", CHANNEL),
            ("video-ugly-duckling-th.jpg", "ลูกเป็ดขี้เหร่", "พบกัน 6 ธันวาคม", CHANNEL),
        ],
    },
}

def cards(lang, limit, level):
    return '<div class="feature-grid">' + ''.join(
        f'<article class="feature-card"><span class="number">0{i + 1}</span><h{level}>{html.escape(h)}</h{level}><p>{html.escape(t)}</p></article>'
        for i, (h, t) in enumerate(CARDS[lang][:limit])) + '</div>'

def videos(lang):
    v = VIDEOS[lang]
    items = ''.join(
        f'<a class="video-card" href="{href}"><img src="../assets/{image}" width="1280" height="720" alt="{html.escape(title)}" loading="lazy" decoding="async">'
        f'<span class="video-title">{html.escape(title)}</span><span class="video-meta">{html.escape(meta)}</span></a>'
        for image, title, meta, href in v["items"])
    return (f'<section class="paper videos" id="videos"><div class="wrap"><div class="section-heading"><h2>{v["heading"]}</h2><p>{v["intro"]}</p></div>'
            f'<div class="video-grid">{items}</div><p class="library-note"><a href="{CHANNEL}">{v["channel"]}</a></p></div></section>')

counts = {old: 0 for old, _ in TEXT}
def replace_text(text, escaped):
    for old, new in TEXT:
        a, b = (html.escape(old, quote=True), html.escape(new, quote=True)) if escaped else (old, new)
        for x, y in ((a, b), (old, new)):
            if x in text:
                counts[old] += text.count(x); text = text.replace(x, y)
    return text

pages = sorted(ROOT.glob("index.html")) + sorted(ROOT.glob("en/**/index.html")) + sorted(ROOT.glob("th/**/index.html"))
for page in pages:
    text = page.read_text(encoding="utf-8")
    if "/privacy/" in str(page):
        continue  # the privacy policy is owner-approved wording; left exactly as it is
    lang = "th" if "/th/" in str(page) else "en"
    text = replace_text(text, escaped=True)
    relative = page.relative_to(ROOT).as_posix()
    if relative in ("en/index.html", "th/index.html", "en/features/index.html", "th/features/index.html"):
        home = "features" not in relative
        new, n = re.subn(r'<div class="feature-grid">.*?</div>', lambda m: cards(lang, 3 if home else 6, 3 if home else 2), text, count=1, flags=re.S)
        assert n == 1, relative
        text = new
        if home and 'id="videos"' not in text:
            anchor = '<section class="forest-section"><div class="wrap split">'
            assert text.count(anchor) == 1, relative
            text = text.replace(anchor, videos(lang) + "\n" + anchor)
    if relative.endswith("stories/index.html"):
        included, full = ("Included", "Full library") if lang == "en" else ("รวมไว้ให้แล้ว", "คลังนิทานทั้งหมด")
        def badge(book, free):
            global text
            pattern = re.compile(r'(assets/' + book + r'-primary\.png"[^>]*>)<span class="access [^"]*">[^<]*</span>')
            text, n = pattern.subn(lambda m: m.group(1) + (f'<span class="access ">{included}</span>' if free else f'<span class="access full">{full}</span>'), text)
            assert n == 1, (relative, book)
        badge("red", False); badge("duckling", True)
    page.write_text(text, encoding="utf-8")

# The same wording in the sources.
content = json.loads((ROOT / "content.json").read_text(encoding="utf-8"))
content = json.loads(replace_text(json.dumps(content, ensure_ascii=False), escaped=False))
for lang in ("en", "th"):
    content[lang]["featureCards"] = CARDS[lang]
    content[lang]["videos"] = {k: v for k, v in VIDEOS[lang].items() if k != "items"}
    content[lang]["videos"]["items"] = [list(item) for item in VIDEOS[lang]["items"]]
(ROOT / "content.json").write_text(json.dumps(content, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

support = json.loads((ROOT / "privacy-support.json").read_text(encoding="utf-8"))
for lang in ("en", "th"):
    for row in support[lang]["support"]:
        row["question"] = replace_text(row["question"], escaped=False)
        row["answer"] = replace_text(row["answer"], escaped=False)
(ROOT / "privacy-support.json").write_text(json.dumps(support, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for old, n in counts.items():
    print(f"{n:3d}  {old[:70]}")
