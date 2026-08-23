# ephemeral fetch tick2071 — MSW NZVL YE2025
import re
import ssl
import urllib.request
from pathlib import Path

ctx = ssl.create_default_context()
outdir = Path("docs/doge/data/raw/tick2071")
outdir.mkdir(parents=True, exist_ok=True)

urls = [
    ("msw_nl", "https://www.companyweb.be/nl/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen"),
    ("msw_en", "https://www.companyweb.be/en/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen"),
    ("msw_fr", "https://www.companyweb.be/fr/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen"),
    ("msw_kbo", "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419384646"),
    ("msw_short", "https://www.companyweb.be/en/0419384646"),
]


def year_of(html):
    for lab in ["Last balance sheet year", "Laatste balansjaar", "Dernier bilan"]:
        i = html.find(lab)
        if i >= 0:
            m = re.search(r"font-medium[^>]*>\s*(\d{4}|N/A)", html[i : i + 220])
            if m:
                return m.group(1)
    return None


def parse_blocks(html):
    return re.findall(
        r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
        html,
    )


for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
            html = resp.read().decode("utf-8", "replace")
        (outdir / f"{name}.html").write_text(html, encoding="utf-8")
        print("OK", name, len(html), "Y", year_of(html), "blocks", parse_blocks(html)[:3])
        # extract useful strings
        for pat in [
            r"filed on ([0-9\-]+)",
            r"neergelegd op ([0-9\.]+)",
            r'Employees\s*=\s*"([^"]+)"',
            r"Werknemers[^<]*</[^>]+>\s*<[^>]+>([^<]+)",
            r"NACE[^0-9]*([0-9\.]+)",
            r"mailto:([^\"'\s>]+)",
            r"@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
        ]:
            m = re.search(pat, html, re.I)
            if m:
                print("  ", pat[:40], "->", m.group(0)[:80] if m.lastindex is None else m.group(1)[:80])
        # KBO specifics
        if "kbo" in name:
            for lab in ["Status", "Rechtsvorm", "Adres", "E-mail", "Telefoon", "Aanbestedende", "Naam"]:
                i = html.find(lab)
                if i >= 0:
                    snippet = re.sub(r"\s+", " ", html[i : i + 200])[:160]
                    print("  KBO", snippet)
    except Exception as e:
        print("FAIL", name, type(e).__name__, str(e)[:200])
