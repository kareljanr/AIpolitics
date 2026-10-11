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
    "src_ebk_jr2025_nbb,Erfgoed Brabantse Kouters MIC-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00321349.pdf,NBB / Erfgoed Brabantse Kouters,2026-08-19,budget,tick1428; MIC-VZW 25.0.13 m08-f PDF 7p / 34843 bytes deposit 2026-00321349; AV 25.03.2026; created 23.07.2026; neerlegging 2026-07-23; KBO 0741.478.094; assets 200838 cash 172470 debt 200838 leveranciers 153718 pnl 0; no commissaris",
    "src_ebk_site,Erfgoed Brabantse Kouters official site,https://www.brabantsekouters.be/projecten/erfgoed-brabantse-kouters,Erfgoed Brabantse Kouters / RLBK,2026-08-19,official_register,tick1428; leftover IGS projectvereniging / IOED of 12 Brabantse Kouters cities; zetel Houtemsesteenweg 23 1800 Vilvoorde; contact info@brabantsekouters.be; coordinator sebastiaan.goovaerts@brabantsekouters.be",
    "src_kbo_ebk_0741478094,KBO Projectvereniging Erfgoed Brabantse Kouters 0741.478.094,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0741478094,KBO Public Search FOD Economie,2026-08-19,official_register,tick1428; Actief since 06.01.2020; naam since 14.12.2022; zetel Houtemsesteenweg 23 1800 Vilvoorde; 0 VE; Projectvereniging; e-mail info@brabantsekouters.be since 06.01.2020",
    "src_ebk_foi_contact,Erfgoed Brabantse Kouters FOI channel (info@brabantsekouters.be; Houtemsesteenweg 23 Vilvoorde),https://www.brabantsekouters.be/projecten/erfgoed-brabantse-kouters,Erfgoed Brabantse Kouters,2026-08-19,official_register,tick1428; 12 member cities Asse/Grimbergen/Kraainem/Machelen/Meise/Merchtem/Steenokkerzeel/Vilvoorde/Wemmel/Wezembeek-Oppem/Zaventem/Zemst + RLBK; no commissaris named",
])
print("sources +4")
