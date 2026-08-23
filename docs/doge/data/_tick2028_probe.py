# ephemeral probe preferred stalls + De Foyer site
import re
import ssl
import urllib.request
from pathlib import Path

outdir = Path("docs/doge/data/raw/tick2028")
outdir.mkdir(parents=True, exist_ok=True)
ctx = ssl.create_default_context()


def get(url, name):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
            html = r.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        title = re.search(r"<title>([^<]+)</title>", html)
        print("==", name, (title.group(1)[:100] if title else None))
        return html
    except Exception as e:
        print("FAIL", name, type(e).__name__, e)
        return ""


for name, url in [
    ("bornem_jr", "https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"),
    ("faro_cw", "https://www.companyweb.be/nl/0893863017/faro"),
    ("faro_cw2", "https://www.companyweb.be/en/0893863017"),
    ("aiesh_cw", "https://www.companyweb.be/nl/0212694814"),
    ("rew_cw", "https://www.companyweb.be/nl/0200768403"),
    ("foyer_site", "https://www.wzcdefoyer.be/"),
    ("foyer_zilver", "https://www.wzcdefoyer.be/zilversterre"),
]:
    html = get(url, name)
    if not html:
        continue
    year = None
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                year = m.group(1)
    print(" year", year)
    if "Jaarrekening 2025" in html or "JR2025" in html:
        print("  mentions JR2025")
    if "Jaarrekening 2024" in html:
        print("  mentions JR2024")
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    if emails:
        print(" emails", emails[:10])
    blocks = re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )
    print(" blocks", len(blocks), "y0", blocks[0] if blocks else None)
