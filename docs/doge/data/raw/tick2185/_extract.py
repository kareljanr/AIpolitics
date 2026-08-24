import re
import html as H
from pathlib import Path

p = Path("docs/doge/data/raw/tick2185")


def load(name):
    t = (p / name).read_text(encoding="utf-8")
    t = re.sub(r"<script[^>]*>.*?</script>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<style[^>]*>.*?</style>", " ", t, flags=re.S | re.I)
    text = H.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", text)


def nums_near(text, label, window=200):
    out = []
    for m in re.finditer(re.escape(label), text, re.I):
        chunk = text[m.start() : m.start() + window]
        vals = re.findall(r"-?\d[\d\s.,]*\d|\d", chunk)
        out.append((chunk[:160], vals[:12]))
    return out


for lang, fname in [
    ("en", "weerwerk_en.html"),
    ("nl", "weerwerk_nl.html"),
    ("fr", "weerwerk_fr.html"),
]:
    text = load(fname)
    print("=" * 20, lang, "len", len(text))
    labels = [
        "Turnover of the financial year",
        "Omzet van het boekjaar",
        "chiffre d'affaires",
        "Gross operating margin",
        "Brutomarge",
        "Bruto-bedrijfsmarge",
        "Marge brute d'exploitation",
        "Profit/Loss of the financial year",
        "Winst (Verlies) van het boekjaar",
        "Bénéfice (Perte) de l'exercice",
        "Equity",
        "Eigen vermogen",
        "Capitaux propres",
        "Number of employees",
        "Werknemers",
        "Effectif moyen",
        "Filing date",
        "Datum van neerlegging",
        "Date de dépôt",
        "Last available year",
        "Laatste beschikbare jaar",
    ]
    for lab in labels:
        hits = nums_near(text, lab, 220)
        if hits:
            print("--", lab)
            for chunk, vals in hits[:3]:
                print("  ", chunk)
                print("   vals:", vals)

# KBO
kbo = load("weerwerk_kbo.html")
print("=" * 20, "KBO")
for lab in [
    "Status van de entiteit",
    "Rechtstoestand",
    "Adres van de zetel",
    "E-mailadres",
    "Benaming",
    "Juridische vorm",
    "Aard van de gegevens",
    "Start",
    "BTW",
    "RSZ",
    "NACE",
    "0465.104.904",
]:
    i = kbo.lower().find(lab.lower())
    if i >= 0:
        print(lab, ":", kbo[i : i + 180])
