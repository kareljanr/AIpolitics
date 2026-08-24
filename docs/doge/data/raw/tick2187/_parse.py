import re

html = open("docs/doge/data/raw/tick2187/en.html", encoding="utf-8").read()
nl = open("docs/doge/data/raw/tick2187/nl.html", encoding="utf-8").read()


def num(s):
    s = (s or "").strip().replace(" ", "").replace("\xa0", "")
    if s in ("", "-", "n/a", "N/A"):
        return None
    if re.search(r",\d{2}$", s) and "." in s:
        s = s.replace(".", "").replace(",", ".")
    elif s.count(",") > 1:
        s = s.replace(",", "")
    elif s.count(".") > 1:
        s = s.replace(".", "")
    elif "," in s and "." not in s:
        parts = s.split(",")
        if len(parts) == 2 and len(parts[1]) == 2:
            s = parts[0] + "." + parts[1]
        else:
            s = s.replace(",", "")
    return float(s)


for y in ("2025", "2024", "2023"):
    m = re.search(
        rf'{y}\s*:\s*\{{\s*winst:\s*"([^"]+)"\s*,\s*eigen_vermogen:\s*"([^"]+)"\s*,\s*bruto_marge:\s*"([^"]+)"\s*,\s*omzet:\s*"([^"]+)"',
        html,
        re.S,
    )
    if m:
        print(
            y,
            "pnl",
            num(m.group(1)),
            "eq",
            num(m.group(2)),
            "bruto",
            num(m.group(3)),
            "omzet",
            num(m.group(4)),
        )

# FTE history if present
for label in ("amountOfEmployees", "numberOfEmployees"):
    m = re.search(rf'{label}\s*=\s*"([^"]+)"', html)
    print(label, m.group(1) if m else None)

# Try table rows for employees prior year
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)
for pat in [
    r"Employees.{0,40}",
    r"Last balance sheet year 20\d\d",
    r"filed on [0-9-]{10}",
    r"Company size.{0,60}",
    r"Legal form.{0,80}",
    r"Address.{0,120}",
]:
    m = re.search(pat, text, re.I)
    print(pat[:30], "->", (m.group(0)[:140] if m else None))

# NL neerlegging
tn = re.sub(r"<[^>]+>", " ", nl)
tn = re.sub(r"\s+", " ", tn)
for pat in [
    r"neergelegd op [0-9-]{10}",
    r"Laatste balansjaar 20\d\d",
    r"Omzet.{0,80}",
    r"Eigen vermogen.{0,80}",
    r"Bruto.{0,80}",
    r"Winst.{0,80}",
]:
    m = re.search(pat, tn, re.I)
    print("NL", pat[:30], "->", (m.group(0)[:140] if m else None))

# look for FTE prior in js
for m in re.finditer(r"werknemers|employees|FTE|personeel", html, re.I):
    pass
# social balance often has window vars
for m in re.finditer(r"[A-Za-z]*[Ee]mployee[A-Za-z]*\s*=\s*\"[^\"]+\"", html):
    print("VAR", m.group(0)[:100])
for m in re.finditer(r"fte[^\"]{0,20}=\s*\"[^\"]+\"", html, re.I):
    print("FTEVAR", m.group(0)[:100])

# percent changes sometimes shown
for m in re.finditer(r"([\-+]?\d+[.,]\d+)\s*%", text):
    if m.start() < 5000:
        continue
print("sample pct near omzet:")
idx = text.lower().find("turnover")
print(text[idx : idx + 300] if idx >= 0 else "no turnover")
idx = text.lower().find("omzet")
print("omzet context", text[idx : idx + 200] if idx >= 0 else None)

# Parse HTML table if present for 2024 FTE
m = re.search(r"Employees</[^>]+></[^>]+><[^>]+>([0-9.,]+)", html)
print("emp cell", m.group(1) if m else None)
# prior year employees in kernCijfers? 
m = re.search(r"kernCijfers\s*=\s*(\{.*?\});", html, re.S)
if m:
    print("kernCijfers snippet", m.group(1)[:500])
