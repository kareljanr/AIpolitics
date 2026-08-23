import re
from pathlib import Path

t = Path("docs/doge/data/raw/tick2014/kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<script[^>]*>.*?</script>", " ", t, flags=re.S | re.I)
text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.S | re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)
for pat in [
    "Status van de entiteit",
    "Adres van de zetel",
    "Rechtsvorm",
    "E-mailadres",
    "e-mail",
    "Naam",
    "Ondernemingsnummer",
    "Begindatum",
    "Aantal",
    "Actief",
    "VZW",
]:
    i = text.find(pat)
    if i >= 0:
        print(pat, "=>", text[i : i + 220])
        print("---")

t2 = Path("docs/doge/data/raw/tick2014/hhleuven_en.html").read_text(
    encoding="utf-8", errors="replace"
)
for pat in [
    r"Naamsestraat.{0,60}",
    r"streetAddress.{0,80}",
    r"postalLine1.{0,80}",
    r"companyweb\.be/en/0412939886/[^\"']+",
]:
    ms = re.findall(pat, t2)
    if ms:
        print("CW", pat, ms[:5])

# establishment count / email
for lab in ["Establishments", "Email", "phone", "Start date", "Legal form"]:
    i = t2.lower().find(lab.lower())
    if i >= 0:
        chunk = re.sub(r"\s+", " ", t2[i : i + 250])
        print(lab, chunk[:200])
