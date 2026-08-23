from pathlib import Path
import re, html as H

def plain(path):
    t = Path(path).read_text(encoding="utf-8", errors="replace")
    t = H.unescape(t)
    t = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)

raw = Path("docs/doge/raw/tick2078/vander_en.html").read_text(encoding="utf-8", errors="replace")
print("emails", re.findall(r"mailto:([^\"'>\s]+)", raw, re.I)[:10])
print("sites", re.findall(r"https?://(?!www\.companyweb)([^\"'>\s]+)", raw, re.I)[:15])

en = plain("docs/doge/raw/tick2078/vander_en.html")
for pat in [
    r"Balance year.{0,90}",
    r"filed on .{0,50}",
    r"Turnover.{0,160}",
    r"Profit/Loss.{0,160}",
    r"Equity.{0,160}",
    r"Gross margin.{0,160}",
    r"Staff.{0,90}",
    r"Employees.{0,90}",
    r"Full name.{0,120}",
    r"Registered office.{0,160}",
    r"Principal activity.{0,120}",
]:
    m = re.search(pat, en, re.I)
    if m:
        print(m.group(0)[:170])

kp = plain("docs/doge/raw/tick2078/kbo.html")
for pat in [
    r"Status.{0,40}",
    r"Adres van de zetel.{0,160}",
    r"Rechtsvorm.{0,100}",
    r"E-mailadres.{0,100}",
    r"Webadres.{0,120}",
    r"Aantal.{0,80}",
    r"Telefoon.{0,80}",
    r"aanbestedende.{0,80}",
    r"Maatschappelijke naam.{0,120}",
    r"Afgekorte.{0,80}",
]:
    m = re.search(pat, kp, re.I)
    if m:
        print("KBO", m.group(0)[:170])

# dump around known markers
for key in ["Adres van de zetel", "E-mail", "Webadres", "vestigingseenheid", "Telefoonnummer"]:
    idx = kp.lower().find(key.lower())
    print(key, "=>", kp[idx:idx+220] if idx>=0 else "NONE")

nl = plain("docs/doge/raw/tick2078/vander_stokken_nl.html")
idx = nl.lower().find("maatschappelijke zetel")
print("NL zetel", nl[idx:idx+220] if idx>=0 else "NONE")
idx = nl.lower().find("huidige maatschappelijke")
print("NL huidige", nl[idx:idx+220] if idx>=0 else "NONE")
