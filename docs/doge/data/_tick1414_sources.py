#!/usr/bin/env python3
from pathlib import Path
DATA = Path("/workspace/AIpolitics/docs/doge/data")
def append_lf(path: Path, rows: list[str]) -> None:
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))
append_lf(DATA / "sources.csv", [
    "src_kluz_jr2025_nbb,AGB De Kluize VKT-kap jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00286795.pdf,NBB / AGB De Kluize,2026-08-19,budget,tick1414; VKT-kap 23.0.10 m01-f PDF 17p / 260838 bytes deposit 2026-00286795; AV 11.05.2026; header 09.07.2026; created 14.07.2026; KBO 0844.272.162; assets 5831290 brutomarge 342519 debt 5761761 lease 4483958; table assets 5831291 not used",
    "src_kluz_site,AGB De Kluize official portal page,https://oosterzele.be/bestuur/agb-de-kluize,Gemeente Oosterzele / AGB De Kluize,2026-08-19,official_register,tick1414; AGB sport/GC/erfgoed/jeugd; zetel Sportstraat 3 9860 Oosterzele; contact david.delandsheere@oosterzele.be",
    "src_kbo_kluz_0844272162,KBO AGB De Kluize 0844.272.162,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0844272162,KBO Public Search FOD Economie,2026-08-19,official_register,tick1414; Actief since 28.09.2011; zetel Sportstraat 3 9860 Oosterzele; 0 VE; NACE 93.110/90.312/84.119; aanbestedende overheid; tel 09/363.83.31; e-mail david.delandsheere@oosterzele.be",
    "src_kluz_foi_contact,AGB De Kluize FOI channel / official contact (david.delandsheere@oosterzele.be; Sportstraat 3 Oosterzele),https://oosterzele.be/bestuur/agb-de-kluize,AGB De Kluize,2026-08-19,official_register,tick1414; voorzitter Mia Waterloos; vennoot Gemeente Oosterzele 0207.454.294; commissaris Blommaert & Co B 513 Johnny Blommaert N 1541 fee unpublished",
])
print("sources +4")
