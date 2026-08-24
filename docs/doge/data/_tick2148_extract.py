# -*- coding: utf-8 -*-
import re
from pathlib import Path

base = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2148")
for name in [
    "hemeco_en.html",
    "hemeco_nl.html",
    "hemeco_fr.html",
    "hemeco_kbo.html",
]:
    t = (base / name).read_text(encoding="utf-8", errors="replace")
    print("====", name, "====")
    for key in [
        "Employees",
        "Establishments",
        "Nace",
        "Status",
        "Address",
        "Phone",
        "Email",
        "Website",
        "StartDate",
        "LegalForm",
        "CompanyName",
        "Vat",
    ]:
        m = re.search(rf'{key}\s*=\s*"([^"]+)"', t)
        if m:
            print(key, m.group(1)[:160])
    # strip tags for KBO-ish text hits
    plain = re.sub(r"<[^>]+>", " ", t)
    plain = re.sub(r"\s+", " ", plain)
    for lab in [
        "Status van de entiteit",
        "Adres van de zetel",
        "Rechtsvorm",
        "Aantal vestigingen",
        "Ondernemingsnummer",
        "Hulpverleningszone",
        "brandweer",
        "84.250",
        "aanbestedende",
        "Actief",
        "Since",
        "Founded",
        "Establishments",
    ]:
        if lab.lower() in plain.lower():
            i = plain.lower().find(lab.lower())
            print("hit", lab, "->", plain[i : i + 180])
    emails = set(
        re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)
    )
    emails = {
        e
        for e in emails
        if not any(
            x in e.lower()
            for x in ["companyweb", "example", "sentry", "google", "wix", "schema"]
        )
    }
    if emails:
        print("emails", emails)
