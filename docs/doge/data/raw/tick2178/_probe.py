import re
from pathlib import Path

OUT = Path(__file__).resolve().parent


def year_blocks(text):
    for m in re.finditer(r"(20\d\d)\s*:\s*\{([^}]{20,500})\}", text):
        body = m.group(2)
        if "omzet" in body or "winst" in body or "bruto" in body:
            yield m.group(1), body


def main():
    for name in ["waak_en", "waak_nl", "waak_fr", "faro_en", "aiesh_en", "rew_en", "stijn_en"]:
        p = OUT / f"{name}.html"
        if not p.exists():
            print("MISSING", name)
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        print("===", name)
        for year, body in year_blocks(text):
            print(" YEAR", year)
            print(" ", body[:450])
        for pat in [
            r'Employees\s*=\s*"([^"]+)"',
            r"window\.cw\.employees[^\n]{0,100}",
            r"deposited on[^<]{0,100}",
            r"filed on[^<]{0,120}",
            r"déposés le[^<]{0,80}",
            r"neergelegd[^.]{0,100}",
            r'startDate\s*=\s*"([^"]+)"',
            r"Last balance sheet year[\s\S]{0,120}?>(20\d\d)<",
            r"balansjaar[\s\S]{0,120}?>(20\d\d)<",
            r"Laatste jaarrekening[\s\S]{0,200}?>(20\d\d)<",
        ]:
            m = re.search(pat, text, re.I)
            if m:
                print(" HIT", pat[:40], "=>", re.sub(r"\s+", " ", m.group(0))[:140])

    kbo = (OUT / "kbo_waak.html").read_text(encoding="utf-8", errors="replace")
    print("=== kbo_waak")
    for pat in [
        r"Actief|Active",
        r"Vereniging zonder winstoogmerk",
        r"Adres van de zetel[\s\S]{0,250}",
        r"E-mailadres[\s\S]{0,150}",
        r"Webadres[\s\S]{0,150}",
        r"NACE[\s\S]{0,250}",
        r"Aantal exter[\s\S]{0,100}",
        r"Vestigingseenhe[\s\S]{0,120}",
        r"RSZ[\s\S]{0,80}",
        r"aanbestedende[\s\S]{0,80}",
    ]:
        m = re.search(pat, kbo, re.I)
        if m:
            print(" KBO", pat[:28], "=>", re.sub(r"\s+", " ", m.group(0))[:180])


if __name__ == "__main__":
    main()
