# -*- coding: utf-8 -*-
"""Deep extract Arcor YE2025 + YoY + KBO + contact."""
import re
import html as H
from pathlib import Path

RAW = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\tick2208")


def to_text(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    text = H.unescape(re.sub(r"<[^>]+>", "\n", t))
    return re.sub(r"[ \t]+", " ", re.sub(r"\n+", "\n", text))


def parse_money_list(chunk):
    """Return list of ints/floats/None from € amounts or dashes in chunk."""
    out = []
    # match euro amounts or lone dash placeholders
    for m in re.finditer(r"(?:€\s*([\d.,]+)|(?<![€\d])-\s*(?=\n|$|€|[A-Za-z]))", chunk):
        if m.group(1) is None:
            out.append(None)
            continue
        raw = m.group(1).strip()
        if "," in raw and "." in raw:
            if raw.rfind(",") > raw.rfind("."):
                val = raw.replace(".", "").replace(",", ".")
            else:
                val = raw.replace(",", "")
        elif "," in raw:
            val = raw.replace(",", "")
        else:
            parts = raw.split(".")
            if len(parts) > 2 or (len(parts) == 2 and len(parts[-1]) == 3):
                val = raw.replace(".", "")
            else:
                val = raw
        try:
            if "." in val and len(val.split(".")[-1]) <= 2:
                out.append(float(val))
            else:
                out.append(int(float(val)))
        except Exception:
            out.append(raw)
    return out


def metric_block(text, key, n=800):
    idx = text.find(key)
    if idx < 0:
        print(f"MISSING {key}")
        return
    chunk = text[idx : idx + n]
    print(f"\n=== {key} ===")
    print(repr(chunk[:500]))
    nums = parse_money_list(chunk)
    print("nums:", nums[:8])


def main():
    for lang in ["en", "nl", "fr"]:
        p = RAW / f"arcor_{lang}.html"
        text = to_text(p)
        print("\n##########", lang, "##########")
        for pat in [
            r"Last balance sheet year\s*\n\s*(20\d{2})",
            r"Laatste balansjaar\s*\n\s*(20\d{2})",
            r"Dernier bilan\s*\n\s*(20\d{2})",
            r"filed on\s*([0-9.\-/]+)",
            r"neergelegd op\s*([0-9.\-/]+)",
            r"Company size\s*\n\s*([^\n]+)",
        ]:
            m = re.search(pat, text, re.I)
            if m:
                print(pat[:35], "->", m.group(1).strip())
        for key in [
            "Turnover",
            "Gross margin",
            "Profit/Loss",
            "Equity",
            "Employees",
            "Omzet",
            "Brutomarge",
            "Winst/Verlies",
            "Eigen vermogen",
            "Personeel",
            "Chiffre d'affaires",
            "Marge brute",
            "Bénéfice/Perte",
            "Capitaux propres",
            "Effectif",
        ]:
            if key in text:
                metric_block(text, key, 600)

    # KBO
    kbo = to_text(RAW / "kbo_arcor.html")
    print("\n########## KBO ##########")
    for pat in [
        r"Status van de entiteit\s*\n\s*([^\n]+)",
        r"Rechtsvorm\s*\n\s*([^\n]+)",
        r"Begindatum\s*\n\s*([^\n]+)",
        r"Adres van de zetel\s*\n\s*([^\n]+(?:\n[^\n]+){0,3})",
        r"E-mailadres\s*\n\s*([^\n]+)",
        r"Telefoonnummer\s*\n\s*([^\n]+)",
        r"Webadres\s*\n\s*([^\n]+)",
        r"Aantal vestigingseenheden\s*\n\s*([^\n]+)",
        r"RSZ\s*\n\s*([^\n]+)",
        r"BTW\s*\n\s*([^\n]+)",
        r"NACE[^\\n]*\n\s*([^\n]+)",
    ]:
        m = re.search(pat, kbo, re.I)
        if m:
            print(pat[:40], "->", re.sub(r"\s+", " ", m.group(1)).strip()[:160])

    # print interesting KBO lines
    for line in kbo.splitlines():
        if any(
            x in line.lower()
            for x in [
                "actief",
                "vzw",
                "nace",
                "rsz",
                "vestiging",
                "ronse",
                "mail",
                "www",
                "tel",
                "straat",
                "afkorting",
                "naam",
            ]
        ):
            if len(line.strip()) > 2:
                print("KBO:", line.strip()[:160])


if __name__ == "__main__":
    main()
