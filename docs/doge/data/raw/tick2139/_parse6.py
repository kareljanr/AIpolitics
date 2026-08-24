from pathlib import Path
import re, html
t=Path("docs/doge/data/raw/tick2139/denderrust_wie.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t):
    print("E", m.group(0))
# also deobfuscate &#64;
t2=html.unescape(t)
for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t2):
    print("U", m.group(0))
# contact page unescape
c=html.unescape(Path("docs/doge/data/raw/tick2139/denderrust_contact.html").read_text(encoding="utf-8", errors="replace"))
emails=sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@denderrust\.be", c, re.I)))
print("CONTACT EMAILS", emails)
# visible department emails near Afdeling
for m in re.finditer(r"Afdeling.{0,120}", c):
    print(re.sub(r"<[^>]+>"," ",m.group(0))[:150])
