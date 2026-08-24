from pathlib import Path
import re

kbo = Path("docs/doge/data/raw/tick2203/kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
text = re.sub(r"\n+", "\n", text)
lines = [l.strip() for l in text.splitlines() if l.strip()]
for i, l in enumerate(lines):
    if any(
        x in l.lower()
        for x in [
            "status",
            "rechtsvorm",
            "naam",
            "adres",
            "vestiging",
            "nace",
            "rsz",
            "btw",
            "actief",
            "overijse",
            "ijsedal",
            "ondernemingsnummer",
            "bestuur",
            "email",
            "website",
            "aanbested",
        ]
    ):
        ctx = " | ".join(lines[i : i + 3])
        print(ctx[:220])

# also print first 80 non-empty lines
print("---HEAD---")
for l in lines[:80]:
    print(l[:160])
