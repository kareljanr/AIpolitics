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
    "src_evpk_jr2025_nbb,Erfgoed Voorkempen MIC-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00151989.pdf,NBB / Erfgoed Voorkempen,2026-08-19,budget,tick1425; MIC-inb 26.0.12 m87-f PDF 12p / 44523 bytes deposit 2026-00151989; AV 27.03.2026; header 09.06.2026; created 11.06.2026; KBO 0650.649.076; assets 623422 brutomarge 49498 cash 499042 debt 497984; no commissaris",
    "src_evpk_site,Erfgoed Voorkempen official page (Regionaal Landschap de Voorkempen),https://www.rldv.be/erfgoed-voorkempen/,Regionaal Landschap de Voorkempen,2026-08-19,official_register,tick1425; leftover IGS projectvereniging of 14 Voorkempen cities; zetel Schildesteenweg 99 2520 Ranst; contact info@rldevoorkempen.be; redirect from erfgoedvoorkempen.be",
    "src_kbo_evpk_0650649076,KBO Projectvereniging erfgoed Voorkempen 0650.649.076,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0650649076,KBO Public Search FOD Economie,2026-08-19,official_register,tick1425; Actief since 01.01.2016; zetel Schildesteenweg 99 2520 Ranst; 0 VE; Projectvereniging; tel 03 312 87 11; e-mail info@rldevoorkempen.be",
    "src_evpk_foi_contact,Erfgoed Voorkempen FOI channel (info@rldevoorkempen.be; Schildesteenweg 99 Ranst),https://www.rldv.be/erfgoed-voorkempen/,Erfgoed Voorkempen,2026-08-19,official_register,tick1425; 14 member cities Brasschaat/Brecht/Essen/Kalmthout/Kapellen/Malle/Ranst/Schilde/Schoten/Wijnegem/Wommelgem/Wuustwezel/Zandhoven/Zoersel; no commissaris named",
])
print("sources +4")
