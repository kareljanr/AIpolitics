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
    "src_enpk_jr2025_nbb,Erfgoed Noorderkempen VKT-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00061596.pdf,NBB / Erfgoed Noorderkempen,2026-08-19,budget,tick1426; VKT-inb 26.0.8 m81-f PDF 17p / 56875 bytes deposit 2026-00061596; AV 24.03.2026; created 25.03.2026; neerlegging 2026-03-25; KBO 0863.327.714; assets 480193 brutomarge 831915 pers 767960 cash 376948 debt 78901; no commissaris",
    "src_enpk_site,Erfgoed Noorderkempen official site,https://erfgoednoorderkempen.be/,Erfgoed Noorderkempen,2026-08-19,official_register,tick1426; leftover IGS projectvereniging of 11 Noorderkempen cities; zetel Grote Markt 1 2300 Turnhout; kantoor Druivenstraat 18; contact info@erfgoednoorderkempen.be; tel 014 44 33 62",
    "src_kbo_enpk_0863327714,KBO ERFGOED NOORDERKEMPEN 0863.327.714,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0863327714,KBO Public Search FOD Economie,2026-08-19,official_register,tick1426; Actief since 10.02.2004; zetel Grote Markt 1 2300 Turnhout; 1 VE; Projectvereniging; NACE 91.220; Werkgever RSZ; aanbestedende overheid",
    "src_enpk_foi_contact,Erfgoed Noorderkempen FOI channel (info@erfgoednoorderkempen.be; Grote Markt 1 Turnhout),https://erfgoednoorderkempen.be/contact/,Erfgoed Noorderkempen,2026-08-19,official_register,tick1426; 11 member cities Arendonk/Baarle-Hertog/Beerse/Hoogstraten/Kasterlee/Merksplas/Oud-Turnhout/Ravels/Rijkevorsel/Turnhout/Vosselaar; voorzitter Arnold Wittenberg; no commissaris named",
])
print("sources +4")
