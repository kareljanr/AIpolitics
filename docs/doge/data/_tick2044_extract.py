# ephemeral extract YE figures
import re

RAW = "docs/doge/data/raw/tick2044"


def extract_js_years(path):
    html = open(path, encoding="utf-8").read()
    # CW embeds like: 2025 :{ winst: "...", eigen_vermogen: "...", bruto_marge: "...", omzet: "..."
    blocks = re.findall(
        r"(202[0-9])\s*:\s*\{\s*winst:\s*\"([^\"]*)\",\s*eigen_vermogen:\s*\"([^\"]*)\",\s*bruto_marge:\s*\"([^\"]*)\",\s*omzet:\s*\"([^\"]*)\"",
        html,
    )
    print("===", path, "js blocks", len(blocks))
    for b in blocks:
        print(" ", b)
    # FTE
    fte = re.findall(r"Personeel|Employees|personnel|FTE", html, re.I)
    # table rows near 2025
    m = re.search(r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*([0-9]{4})", html, re.I | re.S)
    if m:
        print(" EN last year", m.group(1))
    m = re.search(r"Laatste balansjaar\s*</div>\s*<div[^>]*>\s*([0-9]{4})", html, re.I | re.S)
    if m:
        print(" NL last year", m.group(1))
    # filed date
    for pat in [r"[Nn]eergelegd[^\d]{0,40}(\d{2}[./-]\d{2}[./-]\d{4})", r"[Ff]iled[^\d]{0,40}(\d{2}[./-]\d{2}[./-]\d{4})", r"d[eé]pos[eé]s?[^\d]{0,40}(\d{2}[./-]\d{2}[./-]\d{4})"]:
        mm = re.search(pat, html)
        if mm:
            print(" filed", mm.group(1), "via", pat[:20])
    # personnel numbers in JS
    pers = re.findall(r"(202[0-9])\s*:\s*\{[^}]*?(?:personeel|employees|fte)[^0-9\"]{0,20}\"([0-9.,]+)\"", html, re.I)
    print(" pers hints", pers[:6])
    # simpler: look for FTE near table
    for snip in re.finditer(r".{0,40}(31(?:[.,]0)?|29[.,]6).{0,40}", html):
        s = re.sub(r"\s+", " ", snip.group(0))
        if "FTE" in s or "ersoneel" in s or "Employee" in s or "personeel" in s.lower():
            print(" fte snip", s[:100])
            break


for f in ["faro_en.html", "agb_bornem_nl.html", "verlosser_en.html", "verlosser_nl.html", "verlosser_fr.html"]:
    extract_js_years(f"{RAW}/{f}")

# site email
site = open(f"{RAW}/verlosser_site.html", encoding="utf-8").read()
emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", site))
print("emails", emails)
print("site title", re.search(r"<title>([^<]+)", site, re.I).group(1)[:80] if re.search(r"<title>", site, re.I) else "?")

kbo = open(f"{RAW}/verlosser_kbo.html", encoding="utf-8").read()
print("kbo status", "Actief" in kbo or "Active" in kbo)
print("kbo name hit", "Verlosser" in kbo)
