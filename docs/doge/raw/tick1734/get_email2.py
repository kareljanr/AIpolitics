import urllib.request, ssl, re
from pathlib import Path

ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
u = "https://www.sint-jozef-rumst.be/contact"
req = urllib.request.Request(u, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as r:
    html = r.read().decode("utf-8", "replace")
Path("docs/doge/raw/tick1734/contact.html").write_text(html, encoding="utf-8")

# find emailcloak / addy / obfuscation blocks
for pat in [
    r"email-cloak[^<]{0,500}",
    r"cloak[^<]{0,300}",
    r"jQuery\(function\([^)]*\)\{[^}]{0,800}\}",
    r"function\s+\w*mail\w*\([^)]*\)\{[^}]{0,500}\}",
    r"String\.fromCharCode\([^)]{0,200}\)",
    r"&#\d+;",
]:
    ms = re.findall(pat, html, re.I | re.S)
    print("PAT", pat[:40], "n", len(ms))
    for m in ms[:3]:
        print(m[:250])
        print("---")

# decode all numeric entities in body
body = re.sub(r"&#(\d+);?", lambda m: chr(int(m.group(1))), html)
emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", body))
print("decoded emails", emails)

# also look near "Administratie" / "Boekhouding"
idx = body.lower().find("administratie")
print("admin ctx", body[idx : idx + 400] if idx >= 0 else "none")
idx = body.lower().find("@")
print("at idx", idx)
if idx >= 0:
    print(body[max(0, idx - 80) : idx + 80])
