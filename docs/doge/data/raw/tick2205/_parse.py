from pathlib import Path
import re
import urllib.request

out = Path("docs/doge/data/raw/tick2205")
for n, u in [
    ("oesterbank_en.html", "https://www.companyweb.be/en/0407762165/de-oesterbank"),
    ("oesterbank_nl.html", "https://www.companyweb.be/nl/0407762165/de-oesterbank"),
    ("oesterbank_fr.html", "https://www.companyweb.be/fr/0407762165/de-oesterbank"),
    ("kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407762165&lang=nl"),
]:
    path = out / n
    if n.startswith("oesterbank_en") and (out / "oesterbank.html").exists() and not path.exists():
        (out / "oesterbank.html").replace(path) if False else None
    if not path.exists() or path.stat().st_size < 1000:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        d = urllib.request.urlopen(req, timeout=25).read()
        path.write_bytes(d)
        print("fetched", n, len(d))
    else:
        print("have", n, path.stat().st_size)

# prefer en from oesterbank.html copy if needed
en = out / "oesterbank_en.html"
if not en.exists() and (out / "oesterbank.html").exists():
    en.write_bytes((out / "oesterbank.html").read_bytes())

text = en.read_text(encoding="utf-8", errors="replace")
print("filed", re.search(r"filed on ([0-9-]+)", text).group(1))
m = re.search(r"total turnover of .([0-9.,]+)", text)
print("faq", m.group(1) if m else None)
print("empty", bool(re.search(r"did not publish any turnover", text, re.I)))
parts = re.split(r'title="Section [^"]+"', text)
for part in parts[1:8]:
    lab = re.search(r">\s*([A-Za-z /]+)<", part[:500])
    euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
    plain = re.findall(r"<span>([-0-9]+(?:[.,][0-9]+)?)</span>", part)
    pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
    print(lab.group(1).strip() if lab else "?", euros[:4], plain[:4], pct[:3])
