from pathlib import Path
import re
raw = Path("docs/doge/data/raw/tick2134")
for name in ["faro_en.html","aiesh_en.html","rew_en.html"]:
    html=(raw/name).read_text(encoding="utf-8", errors="replace")
    m=re.search(r"Last balance sheet year.*?font-medium[^>]*>\s*(\d{4})", html, re.S)
    title=re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    t = re.sub(r"<[^>]+>","",title.group(1)).strip()[:70] if title else "?"
    print(name, "year", m.group(1) if m else "?", "|", t)

html=(raw/"egmont_cw_en.html").read_text(encoding="utf-8", errors="replace")
print("---EGMONT---")
for label in ["Principal activity","Commercial name","Company size","Last balance sheet year","Status"]:
    i=html.find(label)
    if i>=0:
        print(label, "->", re.sub(r"\s+"," ",html[i:i+240])[:200])
yrs=re.findall(r"(202[0-9])\s*:\s*\{([^}]+)\}", html)
for y, body in yrs[:4]:
    print(y, body[:280].replace("\n"," "))
m=re.search(r"filed on ([0-9-]+)", html); print("filed", m.group(1) if m else None)
m=re.search(r"gross margin of €([0-9,\.]+)", html); print("bruto FAQ", m.group(1) if m else None)
m=re.search(r'total turnover of €([0-9,\.]+)', html); print("omzet FAQ", m.group(1) if m else None)
m=re.search(r'Employees = "([^"]+)"', html); print("emp", m.group(1) if m else None)
kbo=(raw/"egmont_kbo.html").read_text(encoding="utf-8", errors="replace")
for label in ["Status","Rechtsvorm","Adres","E-mail","Webadres","Aantal vestigingseenheden","Ondernemingsnummer"]:
    i=kbo.find(label)
    if i>=0:
        print("KBO", label, "->", re.sub(r"\s+"," ",kbo[i:i+280])[:260])
i=kbo.find("Activiteiten")
print("ACT", re.sub(r"\s+"," ",kbo[i:i+500])[:450] if i>=0 else "none")
# email from site search later
