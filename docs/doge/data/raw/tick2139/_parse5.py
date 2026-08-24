from pathlib import Path
import re
t=Path("docs/doge/data/raw/tick2139/denderrust_contact.html").read_text(encoding="utf-8", errors="replace")
# all emails including obfuscated
for m in re.finditer(r"(?:mailto:|email|@[a-z]|denderrust\.be)[^<>\s\"']{0,60}", t, re.I):
    s=m.group(0)
    if "denderrust" in s.lower() or "@" in s:
        print(s[:100])
# also site footer from home
home=Path("docs/doge/data/raw/tick2139/denderrust_site.html").read_text(encoding="utf-8", errors="replace")
for m in re.finditer(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", home):
    print("HOME", m.group(0))
print("---")
# look for info@
print("info@", "info@denderrust.be" in t or "info@denderrust.be" in home)
# extract from data-email or similar
for m in re.finditer(r"data-[a-z-]*=\"[^\"]*@|[a-z0-9._+-]+&#64;|[a-z0-9._+-]+@denderrust", t, re.I):
    print("D", m.group(0)[:80])
