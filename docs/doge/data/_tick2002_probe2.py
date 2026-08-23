# ephemeral tick2002 probe2 — parse prior + fetch AZ Turnhout/Klina/Monica/Sint-Maarten/Vesalius + UZB
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2002")
dst.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}


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


def summarize_text(name, t):
    title = re.search(r"<title>([^<]+)</title>", t)
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        t,
    )
    print("==", name, "==")
    print(" title", (title.group(1)[:130] if title else None))
    print(" blocks", blocks[:3])
    for lab in ["Last balance sheet year", "filed on", "neergelegd op", "déposés le"]:
        i = t.find(lab)
        if i >= 0:
            print(" ", lab, repr(t[i : i + 160]))
    em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
    print(" FTE", em[:2])
    if "No financial data available" in t:
        print(" OPAQUE")
    if blocks:
        try:
            y0 = tuple(parse_amount(x) for x in blocks[0])
            print(" y0 winst,equity,bruto,omzet", y0)
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
        except Exception as e:
            print(" parse err", e)
    print()


# copy+summarize prior tick2001 candidates
prior = Path("docs/doge/data/raw/tick2001")
for name in [
    "az_turnhout_en.html",
    "turnhout_en.html",
    "turnhout_nl.html",
    "az_klina_en.html",
    "az_monica_en.html",
    "az_sint_maarten_en.html",
    "az_vesalius_en.html",
    "az_sintjan_en.html",
    "erasme_en.html",
]:
    s = prior / name
    if s.exists():
        data = s.read_bytes()
        (dst / name).write_bytes(data)
        print("copied", name, len(data))
        summarize_text(name, data.decode("utf-8", errors="replace"))

# also tick1998 uzb
for name in ["uzb_en.html", "uzb_acad_en.html", "azklina.html", "azmonica.html"]:
    s = Path("docs/doge/data/raw/tick1998") / name
    if s.exists():
        data = s.read_bytes()
        (dst / f"from1998_{name}").write_bytes(data)
        print("copied1998", name, len(data))
        summarize_text(f"from1998_{name}", data.decode("utf-8", errors="replace"))


def fetch(name, url):
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))
    summarize_text(name, data.decode("utf-8", errors="replace"))


urls = [
    ("turnhout_en", "https://www.companyweb.be/en/0897191602/az-turnhout"),
    ("turnhout_nl", "https://www.companyweb.be/nl/0897191602/az-turnhout"),
    ("turnhout_fr", "https://www.companyweb.be/fr/0897191602/az-turnhout"),
    ("klina_en", "https://www.companyweb.be/en/0434302850/algemeen-ziekenhuis-klina"),
    ("sintmaarten_en", "https://www.companyweb.be/en/0411515075"),
    ("monica_search", "https://www.companyweb.be/en/search?q=AZ+Monica"),
]

for name, url in urls:
    try:
        fetch(name, url)
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
