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
    "src_vtrt_jr2025_nbb,Viertoren MIC-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00070101.pdf,NBB / Viertoren,2026-08-19,budget,tick1421; MIC-inb 23.0.6 m87-f PDF 10p / 41364 bytes deposit 2026-00070101; AV 31.03.2026; created 02.04.2026; KBO 0744.514.689; assets 211378 brutomarge 110397 pers 79534 cash 189139 debt 8791; no commissaris",
    "src_vtrt_site,Viertoren official portal,https://viertoren.be/,Viertoren,2026-08-19,official_register,tick1421; leftover IGS 4 Westhoek kust gemeenten De Panne Koksijde Nieuwpoort Veurne; zetel Zeelaan 303 8670 Koksijde; contact info@viertoren.be; coordinator Mathieu Karreman tel 0494 56 74 94",
    "src_kbo_vtrt_0744514689,KBO Viertoren 0744.514.689,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0744514689,KBO Public Search FOD Economie,2026-08-19,official_register,tick1421; Actief since 01.10.2019; zetel Zeelaan(Kok) 303 8670 Koksijde; 0 VE; Projectvereniging; tel 058/53 30 93",
    "src_vtrt_foi_contact,Viertoren FOI channel / official contact (info@viertoren.be; Zeelaan 303 Koksijde),https://viertoren.be/nl/over-ons,Viertoren,2026-08-19,official_register,tick1421; 4 vennoten De Panne Koksijde Nieuwpoort Veurne; no commissaris; voorzitter Frederic Devos",
])
print("sources +4")
