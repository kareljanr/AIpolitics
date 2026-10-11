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
    "src_rpsk_jr2025_nbb,Erfgoed Rupelstreek MIC-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00079897.pdf,NBB / Erfgoed Rupelstreek,2026-08-19,budget,tick1431; MIC-inb 25.0.11 m87-f PDF 10p / 40153 bytes deposit 2026-00079897; AV 23.03.2026; created 15.04.2026; neerlegging 2026-04-15; KBO 0822.286.618; assets 58035 cash 31653 debt 0 brutomarge -10959 pnl -10998; externe accountant YvR Accountancy no commissaris",
    "src_rpsk_site,Erfgoed Rupelstreek official site,https://erfgoedrupelstreek.be/,Erfgoed Rupelstreek / IOED,2026-08-19,official_register,tick1431; leftover IGS projectvereniging / IOED of 5 Rupelstreek cities Boom/Hemiksem/Niel/Rumst/Schelle; kantoor Hoogstraat 27 2850 Boom; contact info@erfgoedrupelstreek.be; coordinator tom@erfgoedrupelstreek.be",
    "src_kbo_rpsk_0822286618,KBO Erfgoed Rupelstreek 0822.286.618,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0822286618,KBO Public Search FOD Economie,2026-08-19,official_register,tick1431; Actief since 13.11.2009; naam since 13.11.2009; zetel Schommelei 1 2850 Boom Provinciaal Domein De Schorre; 0 VE; Projectvereniging; aanbestedende overheid since 13.11.2009",
    "src_rpsk_foi_contact,Erfgoed Rupelstreek FOI channel (info@erfgoedrupelstreek.be; Hoogstraat 27 Boom),https://erfgoedrupelstreek.be/contact/,Erfgoed Rupelstreek,2026-08-19,official_register,tick1431; 5 member cities Boom/Hemiksem/Niel/Rumst/Schelle; voorzitter Goris Vera; externe accountant YvR Accountancy & Tax 0425.179.011",
])
print("sources +4")
