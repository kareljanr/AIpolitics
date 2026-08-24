from pathlib import Path
import re
t=Path("docs/doge/data/raw/tick2139/denderrust_contact.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t):
    print("EMAIL", m.group(0))
for m in re.finditer(r"(Alfons|De Cock|9310|Aalst|053[^<]{0,40}|mailto:[^\"'<>]+)", t, re.I):
    print("HIT", re.sub(r"\s+"," ", m.group(0))[:120])
# visible text around contact
text=re.sub(r"<script[\s\S]*?</script>"," ",t,flags=re.I)
text=re.sub(r"<style[\s\S]*?</style>"," ",text,flags=re.I)
text=re.sub(r"<[^>]+>"," ",text)
text=re.sub(r"\s+"," ",text)
i=text.lower().find("contact")
print(text[i:i+800] if i>=0 else text[:800])
