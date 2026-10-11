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
    "src_eddl_jr2025_nbb,Erfgoed Denderland MIC-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00110901.pdf,NBB / Erfgoed Denderland,2026-08-19,budget,tick1427; MIC-VZW 25.0.12 m08-f PDF 10p / 40314 bytes deposit 2026-00110901; AV 20.03.2026; created 11.05.2026; neerlegging 2026-05-14; KBO 0544.953.225; assets 454221 lidgeld 498745 diensten 573634 cash 320049 debt 381012; no commissaris",
    "src_eddl_site,Erfgoed Denderland official site,https://www.erfgoedceldenderland.be/,Erfgoed Denderland,2026-08-19,official_register,tick1427; leftover IGS projectvereniging / IOED of 6 Denderland cities; zetel Onderwijsstraat 1 9300 Aalst; contact erfgoedcel@aalst.be; tel 053 72 36 36",
    "src_kbo_eddl_0544953225,KBO Intergemeentelijke Projectvereniging Erfgoed Denderland 0544.953.225,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0544953225,KBO Public Search FOD Economie,2026-08-19,official_register,tick1427; Actief since 27.11.2013; zetel Onderwijsstraat 1 9300 Aalst; 0 VE; Projectvereniging; aanbestedende overheid; tel/e-mail/web since 15.06.2021",
    "src_eddl_foi_contact,Erfgoed Denderland FOI channel (erfgoedcel@aalst.be; Onderwijsstraat 1 Aalst),https://www.erfgoedceldenderland.be/,Erfgoed Denderland,2026-08-19,official_register,tick1427; 6 member cities Aalst/Denderleeuw/Erpe-Mere/Haaltert/Lede/Ninove; voorzitter Caroline De Meerleer; no commissaris named",
])
print("sources +4")
