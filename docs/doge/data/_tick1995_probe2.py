# ephemeral tick1995 — fetch FARO/AIESH/REW + Haute Senne/CNDG/Verviers YE check
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick1995")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
            data = r.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, "OK", len(data))
        return dst / f"{name}.html"
    except Exception as e:
        print("FETCH", name, "FAIL", e)
        return None


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


def parse(path: Path):
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", path.name, "==")
    print(" title", (title.group(1)[:110] if title else None))
    print(" blocks raw", blocks[:3])
    parsed = []
    for a, b, c, d in blocks[:2]:
        try:
            parsed.append((parse_amount(a), parse_amount(b), parse_amount(c), parse_amount(d)))
        except Exception as e:
            print("  parse fail", e, a, b, c, d)
    print(" parsed winst,equity,bruto,omzet", parsed)
    if len(parsed) >= 2:
        y0, y1 = parsed[0], parsed[1]
        for name, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
            a, b = y0[i], y1[i]
            pct = (a - b) / abs(b) * 100 if b != 0 else None
            print(f"  {name}: {a:.0f} vs {b:.0f} -> {pct:.2f}%" if pct is not None else f"  {name}: {a} vs {b}")
    for lab in ["filed on", "neergelegd op", "déposés le", "Last balance sheet year"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 150]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:3])
    print()


urls = [
    ("faro_en", "https://www.companyweb.be/en/0893863017/faro-vlaams-steunpunt-voor-cultureel-erfgoed"),
    ("aiesh_en", "https://www.companyweb.be/en/0201712587"),
    ("rew_en", "https://www.companyweb.be/en/0644638937"),
    ("haute_en", "https://www.companyweb.be/en/0256981407/centre-hospitalier-regional-de-la-haute-senne"),
    ("haute_nl", "https://www.companyweb.be/nl/0256981407/centre-hospitalier-regional-de-la-haute-senne"),
    ("haute_fr", "https://www.companyweb.be/fr/0256981407/centre-hospitalier-regional-de-la-haute-senne"),
    ("cndg_en", "https://www.companyweb.be/en/0401690559/clinique-notre-dame-de-grace"),
    ("cndg_nl", "https://www.companyweb.be/nl/0401690559/clinique-notre-dame-de-grace"),
    ("verviers_en", "https://www.companyweb.be/en/0250893369/centre-hospitalier-regional-de-verviers"),
    ("verviers_nl", "https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers"),
]

for name, url in urls:
    p = fetch(name, url)
    if p:
        parse(p)
