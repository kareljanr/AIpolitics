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
    "src_kstf_jr2025_nbb,Kusterfgoed MIC-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00241009.pdf,NBB / Kusterfgoed,2026-08-19,budget,tick1429; MIC-VZW 26.0.15 m08-f PDF 11p / 45818 bytes deposit 2026-00241009; AV 25.03.2026; created 02.07.2026; neerlegging 2026-07-02; KBO 0552.559.411; assets 162729 cash 153074 debt 62082 brutomarge 248766 pers 263807 pnl -16180; externe accountant MV Accounting no commissaris",
    "src_kstf_site,Kusterfgoed official site,https://www.kusterfgoed.be/,Kusterfgoed / Erfgoedcel,2026-08-19,official_register,tick1429; leftover IGS projectvereniging / IOED / erfgoedcel of 5 Middenkust cities + Knokke-Heist 2026; kantoor InnovOcean Campus Jacobsenstraat 1 8400 Oostende; contact info@kusterfgoed.be; tel 0471 27 07 70",
    "src_kbo_kstf_0552559411,KBO Projectvereniging Kusterfgoed 0552.559.411,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0552559411,KBO Public Search FOD Economie,2026-08-19,official_register,tick1429; Actief since 09.05.2012; naam since 09.05.2012; zetel Vindictivelaan 1 8400 Oostende; 2 VE; Projectvereniging; RSZ 94.999; aanbestedende overheid since 09.05.2012",
    "src_kstf_foi_contact,Kusterfgoed FOI channel (info@kusterfgoed.be; InnovOcean Campus Jacobsenstraat 1 Oostende),https://www.kusterfgoed.be/nl/contact,Kusterfgoed,2026-08-19,official_register,tick1429; 5 member cities Middelkerke/Oostende/De Haan/Blankenberge/Bredene + Knokke-Heist 2026; voorzitter Kamoen Kathleen; externe accountant MV Accounting 0540.535.963",
])
print("sources +4")
