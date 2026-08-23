# ephemeral extract filing date + KBO VE for Samen Ouder
import re
from pathlib import Path

for lang in ["en", "nl", "fr"]:
    html = Path(f"docs/doge/data/raw/tick2040/samen_ouder_{lang}.html").read_text(encoding="utf-8")
    print("===", lang, "len", len(html))
    for lab in [
        "Accounts filed",
        "Neergelegd",
        "Déposés",
        "Filing date",
        "Datum neerlegging",
        "Date de dépôt",
        "Laatste neerlegging",
    ]:
        for m in re.finditer(re.escape(lab), html, re.I):
            print(lab, "->", repr(html[m.start() : m.start() + 280].replace("\n", " "))[:220])
    # generic: look for dd-mm-2026 near jaarrekening wording
    for m in re.finditer(r"\d{2}[-/.]\d{2}[-/.]2026", html):
        ctx = html[max(0, m.start() - 60) : m.start() + 30].replace("\n", " ")
        if "1994" not in ctx:
            print("2026date", m.group(), ctx)
    emp = re.search(r'Employees\s*=\s*"([^"]+)"', html)
    print("emp_var", emp.group(1) if emp else None)
    # FTE display
    i = html.find("Employees")
    if i < 0:
        i = html.find("Werknemers")
    if i >= 0:
        print("emp_ctx", repr(html[i : i + 200].replace("\n", " "))[:180])

html = Path("docs/doge/data/raw/tick2040/samen_ouder_kbo.html").read_text(encoding="utf-8")
text = re.sub(r"<script[\s\S]*?</script>", "", html, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", "", text, flags=re.I)
text = re.sub(r"<[^>]+>", "\n", text)
text = text.replace("&nbsp;", " ")
lines = [l.strip() for l in text.splitlines() if l.strip()]
for i, l in enumerate(lines):
    low = l.lower()
    if any(
        k in low
        for k in [
            "status",
            "actief",
            "vzw",
            "tereken",
            "sint-niklaas",
            "vestiging",
            "e-mail",
            "rechtsvorm",
            "aanbested",
            "ondernemingsnummer",
            "0453",
            "begindatum",
        ]
    ):
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        print(f"KBO[{i}] {l} || next={nxt[:80]}")
