import re
from pathlib import Path
RAW = Path("docs/doge/data/raw/tick2094")

def plain(path):
    t = path.read_text(encoding="utf-8", errors="replace")
    p = re.sub(r"<script[\s\S]*?</script>", " ", t, flags=re.I)
    p = re.sub(r"<[^>]+>", " ", p)
    p = re.sub(r"\s+", " ", p)
    p = p.replace("&#x27;", "'").replace("&amp;", "&").replace("&#xEB;", "ë").replace("&#xE9;", "é")
    return t, p

# Lucia NL extract
t, p = plain(RAW / "lucia_nl.html")
print("=== LUCIA ===")
print("balansjaar", re.search(r"Laatste balansjaar\s+(\d{4})", p).group(1))
print("filed FAQ", re.search(r"neergelegd op ([0-9\-]+)", p).group(1))
objs = re.findall(r"\{\s*winst:\s*\"([^\"]+)\",\s*eigen_vermogen:\s*\"([^\"]+)\",\s*bruto_marge:\s*\"([^\"]+)\",\s*omzet:\s*\"([^\"]+)\"", t)
print("years objs", objs[:4])
m = re.search(r"Personeel\s+([\d,\.]+)\s+([\d,\.]+)", p)
print("pers", m.groups() if m else None)
# FTE from FAQ
m = re.search(r"([\d,\.]+)\s*FTE", p)
print("fte ctx", m.group(0) if m else None)

# EN for english labels / assets?
t2, p2 = plain(RAW / "lucia_en.html")
for key in ["Total assets", "Equity", "Turnover", "Profit", "Employees", "Latest", "Balance"]:
    i = p2.lower().find(key.lower())
    if i>=0: print("EN", key, p2[i:i+120])

# KBO
tk, pk = plain(RAW / "kbo_lucia.html")
print("=== KBO ===")
for key in ["Status", "Naam", "Adres", "Rechtsvorm", "Aantal", "Nace", "E-mail", "Email", "Web", "BTW", "Entiteit", "Hoedanigheid", "Actief", "Clarissen", "Turnhout", "87."]:
    i = pk.lower().find(key.lower())
    if i>=0: print(key, ":", pk[max(0,i-10):i+160])

# site
ts, ps = plain(RAW / "lucia_site.html")
print("=== SITE ===")
emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", ts))
print("emails", emails)
print(ps[:500])

# FARO / AGB years
for name in ["faro_nl.html", "agb_bornem_nl.html"]:
    tt, pp = plain(RAW / name)
    m = re.search(r"Laatste balansjaar\s+(\d{4})", pp)
    print(name, "YE", m.group(1) if m else None)

# recover AIESH/REW from prior tick
for old in [Path("docs/doge/data/raw/tick2093/aiesh_nl.html"), Path("docs/doge/data/raw/tick2093/rew_nl.html")]:
    tt, pp = plain(old)
    m = re.search(r"Laatste balansjaar\s+(\d{4})", pp)
    print(old.name, "YE", m.group(1) if m else None, "canon", re.search(r'rel=\"canonical\" href=\"([^\"]+)\"', tt).group(1) if re.search(r'rel=\"canonical\"', tt) else None)
