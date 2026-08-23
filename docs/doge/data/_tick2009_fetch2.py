import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2009")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}

urls = [
    ("yperman_en", "https://www.companyweb.be/en/0462915078"),
    ("yperman_nl", "https://www.companyweb.be/nl/0462915078"),
    ("yperman_fr", "https://www.companyweb.be/fr/0462915078"),
    ("zorgkas_en", "https://www.companyweb.be/en/0475581694/vlaamse-zorgkas"),
    ("zorgkas_nl", "https://www.companyweb.be/nl/0475581694/vlaamse-zorgkas"),
    ("blasius_olv", "https://www.companyweb.be/en/0411975133"),
    ("blasius_olv_nl", "https://www.companyweb.be/nl/0411975133"),
    ("blasius_site", "https://www.azsintblasius.be/over-ons/beleid/kerncijfers"),
]
for name, url in urls:
    try:
        req = urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            data = resp.read()
        (dst / f"{name}.html").write_bytes(data)
        print("FETCH", name, len(data))
    except Exception as e:
        print("FAIL", name, e)


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


for name, _ in urls:
    path = dst / f"{name}.html"
    if not path.exists():
        continue
    t = path.read_text(encoding="utf-8", errors="replace")
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==", (title.group(1)[:100] if title else None))
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "Laatste balansjaar"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 130]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2], "blocks", blocks[:2])
    if blocks:
        y0 = tuple(parse_amount(x) for x in blocks[0])
        print(" y0", y0)
        if len(blocks) > 1:
            y1 = tuple(parse_amount(x) for x in blocks[1])
            print(" y1", y1)
            for n, i in [("winst", 0), ("equity", 1), ("bruto", 2), ("omzet", 3)]:
                a, b = y0[i], y1[i]
                pct = (a - b) / abs(b) * 100 if b else None
                print(
                    f"  {n} {a:.0f} vs {b:.0f} {pct:.2f}%"
                    if pct is not None
                    else f"  {n} {a} vs {b}"
                )
    # site table sniff
    if "blasius" in name and "Bedrijfsopbrengsten" in t:
        m = re.search(r"Bedrijfsopbrengsten.*?(\d[\d\.\s]{8,})", t)
        print(" site sniff", m.group(0)[:120] if m else None)
    print()
