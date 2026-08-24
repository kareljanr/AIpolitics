import re

html = open("docs/doge/raw/tick2221/manus_en.html", encoding="utf-8").read()
m = re.search(r"window\.cw\.kernCijfers\s*=\s*\{(.*?)\};", html, re.S)
print("CW kern", m.group(1)[:1200] if m else None)
m = re.search(r'amountOfEmployees\s*=\s*"([^"]+)"', html)
print("emp", m.group(1) if m else None)
for pat in [r"filed on ([0-9-]+)", r"Last financial year.{0,40}(\d{4})"]:
    ms = re.findall(pat, html)
    print(pat, ms[:3])
