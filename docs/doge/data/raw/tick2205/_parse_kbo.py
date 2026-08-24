from pathlib import Path
import re

raw = Path("docs/doge/data/raw/tick2205/kbo.html").read_text(encoding="utf-8")
text = re.sub(r"<script[\s\S]*?</script>", "", raw, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
text = text.replace("&nbsp;", " ")
lines = [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()]
lines = [l for l in lines if l]
for i, l in enumerate(lines):
    print(f"{i:03d}|{l[:160]}")
