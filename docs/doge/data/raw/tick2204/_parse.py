from pathlib import Path
import re
import urllib.request

out = Path("docs/doge/data/raw/tick2204")
for n, u in [
    ("trianval_en.html", "https://www.companyweb.be/en/0419052074/trianval"),
    ("trianval_nl.html", "https://www.companyweb.be/nl/0419052074/trianval"),
    ("trianval_fr.html", "https://www.companyweb.be/fr/0419052074/trianval"),
    ("kbo.html", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419052074&lang=nl"),
]:
    if not (out / n).exists() or (out / n).stat().st_size < 1000:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        d = urllib.request.urlopen(req, timeout=25).read()
        (out / n).write_bytes(d)
        print("fetched", n, len(d))
    else:
        print("have", n, (out / n).stat().st_size)

text = (out / "trianval_en.html").read_text(encoding="utf-8", errors="replace")
print("filed", re.search(r"filed on ([0-9-]+)", text).group(1))
m = re.search(r"total turnover of .([0-9.,]+)", text)
print("faq", m.group(1) if m else None)
parts = re.split(r'title="Section [^"]+"', text)
for part in parts[1:8]:
    lab = re.search(r">\s*([A-Za-z /]+)<", part[:500])
    euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
    plain = re.findall(r"<span>([-0-9]+(?:[.,][0-9]+)?)</span>", part)
    pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
    print(lab.group(1).strip() if lab else "?", euros[:4], plain[:4], pct[:3])
