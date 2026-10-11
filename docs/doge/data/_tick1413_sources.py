#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
def append_lf(path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
rows = [
    "src_pmbs_jr2025_nbb,PATRIMONIUM MBS VOL-kap jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00136170.pdf,NBB / PATRIMONIUM MBS NV,2026-08-19,budget,tick1413; VOL-kap 25.0.12 m02-f PDF 41p / 1814120 bytes deposit 2026-00136170; AV 08.05.2026; header 01.06.2026; KBO 0886.391.839; assets 1600122 omzet 107101 diensten 112337; table euros match PDF not used as source",
    "src_pmbs_site,PATRIMONIUM MBS parent official site (IOK),https://www.iok.be,IOK Afvalbeheer / PATRIMONIUM MBS,2026-08-19,official_register,tick1413; leftover daughter NV same zetel Antwerpseweg 1 2440 Geel; KBO no own web/email; jaarverslag T 014 53 53 00; contact info@iok.be",
    "src_kbo_pmbs_0886391839,KBO PATRIMONIUM MBS 0886.391.839,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0886391839,KBO Public Search FOD Economie,2026-08-19,official_register,tick1413; Actief since 15.01.2007; zetel Antwerpseweg 1 2440 Geel; 0 VE; NACE 81.100; aanbestedende overheid; NV since 01.11.2018; kapitaal 1000000",
    "src_pmbs_foi_contact,PATRIMONIUM MBS FOI channel / official contact (info@iok.be; Antwerpseweg 1 Geel),https://www.iok.be,PATRIMONIUM MBS / IOK Afvalbeheer,2026-08-19,official_register,tick1413; voorzitters Ward Kennes + Ivan Blauwhoff; commissaris EY B160 Christoph Oris A02341 fee 4356; vennoten IOK 60pct + IVAREM 40pct",
]
append_lf(DATA / "sources.csv", rows)
print("sources +4")
