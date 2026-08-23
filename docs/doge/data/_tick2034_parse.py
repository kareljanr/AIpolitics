import re
from pathlib import Path
from html import unescape

raw = Path("docs/doge/data/raw/tick2034")


def text(html: str) -> str:
    html = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", " ", html, flags=re.I)
    t = re.sub(r"<[^>]+>", "\n", html)
    t = unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n+", "\n", t)
    return t


def money_near(blob: str, labels):
    out = {}
    for lab in labels:
        # look for label then euro amount nearby
        pats = [
            rf"{lab}[^\n]{{0,80}}€\s*([0-9][0-9\.\s,]*)",
            rf"{lab}[^\n]{{0,80}}EUR\s*([0-9][0-9\.\s,]*)",
            rf"{lab}[^\n]{{0,120}}([0-9]{{1,3}}(?:[\.\s][0-9]{{3}})+(?:,[0-9]+)?)",
        ]
        for p in pats:
            m = re.search(p, blob, flags=re.I)
            if m:
                out[lab] = m.group(1).strip()
                break
    return out


for name in [
    "bernardus_nl",
    "bernardus_en",
    "bernardus_fr",
    "bernardus_kbo",
    "olv_roosdaal_nl",
    "olva_nl",
    "triest_nl",
    "faro_cw",
    "aiesh",
    "bornem",
]:
    p = raw / f"{name}.html"
    if not p.exists():
        print(name, "MISSING")
        continue
    t = text(p.read_text(encoding="utf-8", errors="replace"))
    print("=" * 60, name)
    # key snippets
    keys = [
        "Laatste balansjaar",
        "Last balance sheet year",
        "Dernier exercice",
        "Omzet",
        "Turnover",
        "Chiffre d",
        "Winst",
        "Profit",
        "Bénéfice",
        "Verlies",
        "Loss",
        "Eigen vermogen",
        "Equity",
        "Capitaux propres",
        "Brutomarge",
        "Gross margin",
        "Marge brute",
        "FTE",
        "VTE",
        "neergelegd",
        "filed",
        "déposé",
        "Actief",
        "Active",
        "Actif",
        "Assenede",
        "Roosdaal",
        "Antwerpen",
        "Merelbeke",
        "2025",
        "2024",
        "Jaarrekening 2025",
        "Jaarrekening 2024",
    ]
    lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
    # print interesting lines
    interesting = []
    for i, ln in enumerate(lines):
        if any(k.lower() in ln.lower() for k in keys) or re.search(r"€\s*[0-9]", ln):
            interesting.append((i, ln[:180]))
    for i, ln in interesting[:80]:
        print(f"{i}: {ln}")
    # also dump financial table-ish neighborhood
    for lab in ["Omzet", "Turnover", "Winst/Verlies", "Profit/Loss", "Eigen vermogen", "Equity", "Brutomarge", "Gross margin"]:
        for i, ln in enumerate(lines):
            if lab.lower() in ln.lower():
                for j in range(max(0, i - 1), min(len(lines), i + 6)):
                    print(f"CTX {lab} {j}: {lines[j][:160]}")
                break
