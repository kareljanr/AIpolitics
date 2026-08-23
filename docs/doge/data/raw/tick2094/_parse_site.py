import re
from pathlib import Path
RAW = Path("docs/doge/data/raw/tick2094")
t = (RAW/"site_lucia2.html").read_text(encoding="utf-8", errors="replace")
emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t)))
print("emails", emails)
phones = sorted(set(re.findall(r"0\d{1,2}[\s./\-]*\d{2,3}[\s./\-]*\d{2,3}[\s./\-]*\d{2,3}", t)))
print("phones", [p for p in phones if not p.startswith("0410")][:20])
plain = re.sub(r"<script[\s\S]*?</script>"," ",t,flags=re.I)
plain = re.sub(r"<[^>]+>"," ",plain)
plain = re.sub(r"\s+"," ",plain)
print(plain[:1500])
print("---")
for key in ["post@", "info@", "contact", "014", "Clarissen", "Turnhout", "mailto"]:
    i = plain.lower().find(key.lower())
    if i>=0: print(key, plain[max(0,i-40):i+120])
# also mailto in raw
print("mailto", re.findall(r"mailto:([^\"'\s>]+)", t, re.I))
print("href contacts", re.findall(r'href=\"([^\"]+)\"', t)[:40])
