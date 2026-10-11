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
    "src_whdv_jr2025_nbb,DVV Westhoek VKT-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00300232.pdf,NBB / DVV Westhoek,2026-08-19,budget,tick1415; VKT-inb 25.0.13 m81-f PDF 27p / 786056 bytes deposit 2026-00300232; AV 23.06.2026; header 16.07.2026; created 16.07.2026; KBO 0695.496.928; assets 3145801 brutomarge 2859900 pers 2648974 cash 1859774 debt 1158449; commissaris assets 3145800.75 not used",
    "src_whdv_site,DVV Westhoek official portal,https://dvvwesthoek.be/,DVV Westhoek,2026-08-19,official_register,tick1415; leftover IGS 17 Westhoek gemeenten + WVI; zetel Grote Markt 6 8600 Diksmuide; contact info@dvvwesthoek.be",
    "src_kbo_whdv_0695496928,KBO DVV Westhoek 0695.496.928,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0695496928,KBO Public Search FOD Economie,2026-08-19,official_register,tick1415; Actief since 22.12.2017; zetel Grote Markt 6 8600 Diksmuide; 2 VE; NACE 84.130; aanbestedende overheid; tel 051/970400; e-mail info@dvvwesthoek.be",
    "src_whdv_foi_contact,DVV Westhoek FOI channel / official contact (info@dvvwesthoek.be; Grote Markt 6 Diksmuide),https://dvvwesthoek.be/nl/contactgegevens/,DVV Westhoek,2026-08-19,official_register,tick1415; 18 vennoten 17 gemeenten + WVI; commissaris Walter Hosten Bedrijfsrevisor BV B196 fee 7277",
])
print("sources +4")
