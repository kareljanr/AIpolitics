#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "sources.csv", [
    "src_co7_jr2025_nbb,CultuurOverleg Zeven / CO7 MIC-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00080644.pdf,NBB / CultuurOverleg Zeven,2026-08-19,budget,tick1420; MIC-inb 25.0.11 m87-f PDF 11p / 43209 bytes deposit 2026-00080644; AV 26.03.2026; created 16.04.2026; KBO 0877.372.225; assets 691225 omzet 899440 diensten 900356 cash 552517 debt 297303; no commissaris",
    "src_co7_site,CO7 official portal,https://www.co7.be/,CultuurOverleg Zeven,2026-08-19,official_register,tick1420; leftover IGS 7 Zuidelijke Westhoek gemeenten; zetel Grote Markt 1 8970 Poperinge; contact info@co7.be; tel 057 34 66 94",
    "src_kbo_co7_0877372225,KBO CultuurOverleg Zeven 0877.372.225,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0877372225,KBO Public Search FOD Economie,2026-08-19,official_register,tick1420; Actief since 17.11.2005; zetel Grote Markt 1 8970 Poperinge; 0 VE; NACE 68.203/84.210; aanbestedende overheid; Projectvereniging",
    "src_co7_foi_contact,CO7 FOI channel / official contact (info@co7.be; Grote Markt 1 Poperinge),https://www.co7.be/contact,CultuurOverleg Zeven,2026-08-19,official_register,tick1420; 7 vennoten Heuvelland Ieper Langemark-Poelkapelle Mesen Poperinge Vleteren Zonnebeke; no commissaris; voorzitter Klaas Verbeke",
])
print("sources +4")
