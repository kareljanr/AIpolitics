from pathlib import Path
import re

def decode_cf(cfemail: str) -> str:
    r = int(cfemail[:2], 16)
    email = "".join(chr(int(cfemail[i:i+2], 16) ^ r) for i in range(2, len(cfemail), 2))
    return email

t = Path("docs/doge/data/raw/tick2139/denderrust_contact.html").read_text(encoding="utf-8", errors="replace")
emails = []
for m in re.finditer(r'data-cfemail="([0-9a-fA-F]+)"', t):
    emails.append(decode_cf(m.group(1)))
print("DECODED", sorted(set(emails)))
# with context
for m in re.finditer(r'(.{0,80})data-cfemail="([0-9a-fA-F]+)"', t):
    ctx = re.sub(r"<[^>]+>", " ", m.group(1))
    ctx = re.sub(r"\s+", " ", ctx)[-60:]
    print(ctx, "->", decode_cf(m.group(2)))
