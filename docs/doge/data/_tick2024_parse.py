# ephemeral parse tick2024 candidates
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2024")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()


def parse_amount(s):
    s = s.strip().replace("\xa0", " ").replace(" ", "")
    if "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) >= 2 and all(len(p) == 3 for p in parts[1:]):
            s = s.replace(",", "")
        elif len(parts) == 2 and len(parts[1]) <= 2:
            s = s.replace(",", ".")
        else:
            s = s.replace(",", "")
    elif "," in s and "." in s:
        if s.rfind(",") > s.rfind("."):
            s = s.replace(".", "").replace(",", ".")
        else:
            s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    return float(s)


def analyze(path_or_text, label):
    if isinstance(path_or_text, Path):
        t = path_or_text.read_text(encoding="utf-8", errors="replace")
        label = str(path_or_text)
    else:
        t = path_or_text
    title = re.search(r"<title>([^<]+)</title>", t)
    print("==", label, (title.group(1)[:100] if title else None))
    year = None
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = t.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", t[i : i + 220])
            if m:
                year = m.group(1)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print(" year", year, "nblocks", len(blocks))
    nums = re.findall(r"/(0\d{9})/", t[:8000])
    print(" pathnums", list(dict.fromkeys(nums))[:5])
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0 w/eq/br/om", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(f"  {n} {a:.0f} vs {b:.0f} {pct:+.2f}%")
    m2 = re.search(r'Employees\s*=\s*"([^"]+)"', t)
    print(" emp", m2.group(1) if m2 else None)
    for lab in ["filed on", "neergelegd op", "déposés le"]:
        j = t.lower().find(lab.lower())
        if j >= 0:
            print(" filed", t[j : j + 55])
            break
    return year, blocks


for p in [
    Path("docs/doge/data/raw/tick2020/multiversum_en.html"),
    Path("docs/doge/data/raw/tick2020/multiversum_nl.html"),
    Path("docs/doge/data/raw/tick2020/kbo_search_multiversum_vzw.html"),
]:
    if p.exists():
        analyze(p, p.name)

# fetch Evara + Multiversum correct IDs + carolus/zilverbos search
urls = [
    ("evara_en", "https://www.companyweb.be/en/0406633304/evara"),
    ("evara_nl", "https://www.companyweb.be/nl/0406633304/evara"),
    ("evara_fr", "https://www.companyweb.be/fr/0406633304/evara"),
    (
        "multiversum_jv",
        "https://multiversum.be/jaarverslag-2025/",
    ),
]

# get enterprise number from prior multiversum html
mv = Path("docs/doge/data/raw/tick2020/multiversum_en.html")
if mv.exists():
    t = mv.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"BE0?(\d{3})[.\s]?(\d{3})[.\s]?(\d{3})", t[:3000])
    nums = re.findall(r"/(0\d{9})/", t[:5000])
    print("MV BE", m.groups() if m else None, "nums", nums[:3])
    if nums:
        n = nums[0]
        urls.extend(
            [
                ("multiversum_en2", f"https://www.companyweb.be/en/{n}/multiversum"),
                ("multiversum_nl2", f"https://www.companyweb.be/nl/{n}/multiversum"),
                ("multiversum_fr2", f"https://www.companyweb.be/fr/{n}/multiversum"),
            ]
        )

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        if "jaarverslag" in name:
            print("JV ok", len(html))
            continue
        analyze(html, name)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
