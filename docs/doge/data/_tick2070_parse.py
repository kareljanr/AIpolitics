# ephemeral tick2070 parse CW HTML
from pathlib import Path
import re
import html as htmllib

raw = Path("docs/doge/data/raw/tick2070")


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def parse_file(name):
    t = (raw / name).read_text(encoding="utf-8", errors="replace")
    print("====", name, "len", len(t))
    for key in [
        "nationalId",
        "naamOfAfkorting",
        "amountOfEmployees",
        "adres",
        "ondernemingsnummer",
    ]:
        m = re.search(rf'window\.cw\.{key}\s*=\s*"([^"]*)"', t)
        if m:
            print(key, htmllib.unescape(m.group(1)))
    # last balance year near label
    m = re.search(
        r"Last balance sheet year\s*</div>\s*<div[^>]*>\s*(\d{4})",
        t,
        re.I | re.S,
    )
    if m:
        print("last_year", m.group(1))
    m = re.search(
        r"were filed on ([0-9]{2}-[0-9]{2}-[0-9]{4})",
        t,
    )
    if m:
        print("filed", m.group(1))
    # FAQ turnover
    m = re.search(
        r"recorded a total turnover of [€EUR ]*([0-9.,]+)",
        t,
    )
    if m:
        print("faq_turnover", m.group(1))
    # year financial dict blocks in JS (companyweb embeds kerncijfers)
    # Pattern often: 2025:{ winst:..., omzet:...}
    for ym in re.finditer(r"(20(?:2[0-9]))\s*:\s*\{([^{}]{0,1200})\}", t):
        body = ym.group(2)
        if any(
            k in body
            for k in (
                "winst",
                "omzet",
                "bruto",
                "eigen",
                "personeel",
                "9904",
                "Profit",
                "Turnover",
            )
        ):
            print("YEAR", ym.group(1), body[:700].replace("\n", " "))
    # also try extracting visible table numbers after Profit/Loss etc
    plain = strip_tags(t)
    plain = re.sub(r"\s+", " ", plain)
    for label in [
        "Profit/Loss",
        "Turnover",
        "Equity",
        "Gross margin",
        "Employees",
        "Last balance sheet year",
    ]:
        idx = plain.find(label)
        if idx >= 0:
            print("CTX", label, "=>", plain[idx : idx + 160])
    print()


for n in [
    "welvaart_en.html",
    "welvaart_nl.html",
    "welvaart_fr.html",
    "welvaart_kbo.html",
    "welvaart_site.html",
    "msw_nzvl_en.html",
    "rew_en.html",
    "faro_en.html",
    "aiesh_en.html",
    "agb_bornem_en.html",
]:
    if (raw / n).exists():
        parse_file(n)
