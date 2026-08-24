# -*- coding: utf-8 -*-
import re
from pathlib import Path

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2259")


def nums(s):
    return re.findall(r'[\d\u00a0.]+', s.replace(",", ""))


def parse_cw(lang):
    t = (RAW / f"erables_{lang}.html").read_text(encoding="utf-8", errors="replace")
    print("====", lang)
    # JSON-ish fields often in script
    for key in [
        "omzet",
        "brutomarge",
        "winst",
        "eigenVermogen",
        "fte",
        "balanstotaal",
        "schulden",
        "cash",
        "omzetGroei",
        "winstGroei",
        "brutomargeGroei",
        "eigenVermogenGroei",
        "fteGroei",
    ]:
        ms = re.findall(rf'{key}:\s*"([^"]+)"', t)
        if ms:
            print(key, ms[:6])
    # FAQ answers
    for pat in [
        r"turnover of \u20ac([0-9,.]+)",
        r"Gross margin of \u20ac([0-9,.]+)",
        r"profit of \u20ac([0-9,.]+)",
        r"loss of \u20ac([0-9,.]+)",
        r"equity of \u20ac([0-9,.]+)",
        r"filed on ([0-9-]+)",
        r"neergelegd op ([0-9.-]+)",
        r"Employees = \"([^\"]+)\"",
        r"([0-9]+[,.]?[0-9]*) FTE",
        r"Rue[^<]{5,80}",
        r"@[\w.-]+\.[a-z]{2,}",
        r"Last balance sheet year.{0,80}",
        r"Laatste balansjaar.{0,80}",
        r"NACE[^<]{0,80}",
        r"Principal activity.{0,120}",
        r"Hoofdactiviteit.{0,120}",
        r"establishment unit",
        r"vestigingseenhe",
        r"Unit[eé]s? d.établissement",
        r"C\.A\.V\.A|Les Erables|CAVA",
    ]:
        ms = re.findall(pat, t, re.I)
        if ms:
            print(pat[:50], [re.sub(r"\s+", " ", str(m))[:100] for m in ms[:8]])
    # table years headers
    years = re.findall(r">(202[0-9])<", t)
    print("years", sorted(set(years)))


def parse_kbo():
    t = (RAW / "erables_kbo.html").read_text(encoding="utf-8", errors="replace")
    print("==== KBO")
    # strip tags lightly
    text = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    for key in [
        "Ondernemingsnummer",
        "Status",
        "Maatschappelijke naam",
        "Afgekorte naam",
        "Adres van de zetel",
        "Rechtsvorm",
        "Aantal vestigingseenheden",
        "NACE",
        "RSZ",
        "E-mail",
        "Telefoon",
        "Website",
    ]:
        m = re.search(rf"{key}\s+([^\n]{{0,200}})", text, re.I)
        if m:
            print(key, m.group(1)[:180])
    # VE count
    m = re.search(r"Aantal vestigingseenheden \(VE\):\s*(\d+)", text)
    if m:
        print("VE", m.group(1))
    m = re.search(r"(\d+)\s+Gegevens en Activiteiten per VE", text)
    if m:
        print("VE alt", m.group(1))
    # emails / phones
    print("emails", re.findall(r"[\w.-]+@[\w.-]+", text)[:10])
    print("phones", re.findall(r"0\d{1,2}[\s./-]?\d{2,3}[\s./-]?\d{2}[\s./-]?\d{2}", text)[:10])
    print("addrs", re.findall(r"Rue[^,]{5,60},\s*\d{4}", text)[:5])
    # NACE lines
    for m in re.finditer(r"88\.993[^.]{0,80}", text):
        print("nace", m.group(0)[:100])


for lang in ("en", "nl", "fr"):
    parse_cw(lang)
parse_kbo()
