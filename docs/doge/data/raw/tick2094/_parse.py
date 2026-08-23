# -*- coding: utf-8 -*-
"""Parse CW kerncijfers JSON + Bornem JR page for tick 2094."""
import re
import ssl
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent
CTX = ssl.create_default_context()
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
FTE_PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*[^}]*?personeelsbestand:\s*"([^"]+)"',
    re.I,
)
# alternate FTE embedding
FTE_PAT2 = re.compile(
    r'personeelsbestand[^}]{0,200}?(20\d\d)\s*:\s*"([^"]+)"',
    re.I,
)
FILED_PAT = re.compile(
    r'(?:Neergelegd|Filing date|Date de dépôt)[^0-9]{0,40}([0-9]{2}[-/.][0-9]{2}[-/.][0-9]{4})',
    re.I,
)
VE_PAT = re.compile(r'(\d+)\s*(?:vestiging|establishment|établissement)', re.I)
NACE_PAT = re.compile(r'(87\.\d{3}|88\.\d{3}|86\.\d{3}|35\.\d{3}|36\.\d{3})')


def parse_file(path: Path):
    html = path.read_text(encoding="utf-8", errors="replace")
    print(f"=== {path.name}")
    rows = list(PAT.finditer(html))
    if not rows:
        # try without spaces variants
        pat2 = re.compile(
            r"(20\d\d)\s*:\s*\{\s*winst:\s*'([^']+)',\s*eigen_vermogen:\s*'([^']+)',\s*bruto_marge:\s*'([^']+)',\s*omzet:\s*'([^']+)'"
        )
        rows = list(pat2.finditer(html))
    for m in rows:
        print(
            f" YR {m.group(1)} winst={m.group(2)} eq={m.group(3)} bruto={m.group(4)} omzet={m.group(5)}"
        )
    ftes = list(re.finditer(r'(20\d\d)\s*:\s*"([0-9]+(?:[.,][0-9]+)?)"\s*(?=,|\})', html))
    # better: look for chart series personeelsbestand
    for block_name in ["personeelsbestand", "workforce", "effectif"]:
        idx = html.lower().find(block_name)
        if idx >= 0:
            window = html[idx : idx + 800]
            yrs = re.findall(r'(20\d\d)\s*:\s*"([^"]+)"', window)
            if yrs:
                print(f" FTE block {block_name}:", yrs[:6])
                break
    filed = FILED_PAT.findall(html)
    if filed:
        print(" filed:", filed[:4])
    ve = VE_PAT.findall(html)
    if ve:
        print(" VE mentions:", ve[:5])
    nace = NACE_PAT.findall(html)
    if nace:
        print(" NACE:", sorted(set(nace))[:8])
    # address / email
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)))
    emails = [e for e in emails if not any(x in e.lower() for x in ["example", "sentry", "schema", "wix", "companyweb"])]
    if emails:
        print(" emails:", emails[:8])
    # trend arrows often encoded as class jump/drop near amounts — extract from JSON trend fields if any
    for m in re.finditer(r'(omzet|bruto_marge|winst|eigen_vermogen)_trend[\"\']?\s*:\s*[\"\']?([A-Za-z_+%-]+)', html, re.I):
        print(" trend", m.group(1), m.group(2))
    # percent changes
    for m in re.finditer(r'(omzet|bruto_marge|winst|eigen_vermogen)[^%]{0,40}([+-]?[0-9]+(?:[.,][0-9]+)?)\s*%', html, re.I):
        print(" pct", m.group(1), m.group(2))
        if m.start() > 500000:
            break


def fetch_bornem():
    urls = [
        ("bornem_jr", "https://www.bornem.be/jaarrekening"),
        ("bornem_bestuur", "https://www.bornem.be/bestuur"),
        ("bornem_search", "https://www.bornem.be/zoeken?search=jaarrekening+AGB"),
        ("bornem_agb", "https://www.bornem.be/agb"),
        # prior tick URL pattern from loop_log
        ("bornem_jr2", "https://www.bornem.be/bestuur/financien/jaarrekening"),
        ("bornem_copy", "https://www.bornem.be/bestuur-en-beleid/financieel-beleid/jaarrekening-gemeente-ocmw-en-agb"),
    ]
    # also copy from tick2086 if needed
    for name, url in urls:
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, context=CTX, timeout=40) as r:
                html = r.read().decode("utf-8", errors="replace")
            (OUT / f"{name}.html").write_text(html, encoding="utf-8")
            print(f"BORNEM OK {name} {len(html)}")
            for m in re.finditer(r'href="([^"]+)"[^>]*>([^<]{0,100})', html, re.I):
                href, txt = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
                blob = (href + " " + txt).lower()
                if any(k in blob for k in ["jaarrekening", "agb", "2025", "2024", "pdf", "bbc"]):
                    print(" ", txt[:70], "->", href[:140])
        except Exception as e:
            print(f"BORNEM FAIL {name}: {e}")


def main():
    for name in [
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "lucia_nl.html",
        "lucia_en.html",
        "lucia_fr.html",
    ]:
        p = OUT / name
        if p.exists():
            parse_file(p)
            print()
    # also parse tick2091 cand for comparison
    cand = Path(__file__).resolve().parents[1] / "tick2091" / "cand_0410151137_nl.html"
    if cand.exists():
        print("--- prior cand ---")
        parse_file(cand)
        print()
    fetch_bornem()


if __name__ == "__main__":
    main()
