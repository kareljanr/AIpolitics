# ephemeral — fetch AZ Oostende NL/FR/KBO
import re
import ssl
import urllib.request
from pathlib import Path

dst = Path("docs/doge/data/raw/tick2008")
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0)"}
urls = [
    ("azo_nl", "https://www.companyweb.be/nl/0800023336/algemeen-ziekenhuis-oostende"),
    ("azo_fr", "https://www.companyweb.be/fr/0800023336/algemeen-ziekenhuis-oostende"),
    (
        "azo_kbo",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0800023336",
    ),
]
for name, url in urls:
    req = urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=45) as resp:
        data = resp.read()
    (dst / f"{name}.html").write_bytes(data)
    print("FETCH", name, len(data))

t = (dst / "azo_nl.html").read_text(encoding="utf-8", errors="replace")
blocks = re.findall(
    r'\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)",\s*currency:\s*"euro"',
    t,
)
print("NL blocks", blocks[:2])
i = t.find("Laatste balansjaar")
print("Laatste slice", repr(t[i : i + 200]) if i >= 0 else None)
em = re.findall(r'Employees\s*=\s*"([^"]+)"', t)
print("FTE", em)
k = (dst / "azo_kbo.html").read_text(encoding="utf-8", errors="replace")
for lab in ["Status", "Actief", "vestigingseenheden", "E-mail", "Naam", "Oprichtingsdatum", "Juridische vorm"]:
    j = k.find(lab)
    if j >= 0:
        print(lab, repr(k[j : j + 200]))
