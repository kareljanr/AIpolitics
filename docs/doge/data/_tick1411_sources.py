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
    "src_mrch_jr2025_nbb,AGB Merchtem VKT-inb jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00317853.pdf,NBB / AGB Merchtem,2026-08-19,budget,tick1411; VKT-inb 26.0.15 m81-f PDF 22p / 264500 bytes deposit 2026-00317853; AV 29.06.2026; header 22.07.2026; KBO 0824.869.093; assets 4925278 brutomarge 313807 debt 3382104 recv 1328425; table assets 4925277 not used",
    "src_mrch_site,AGB Merchtem official portal page,https://www.merchtem.be/AGB,Gemeente Merchtem / AGB Merchtem,2026-08-19,official_register,tick1411; AGB vrijetijdsinfrastructuur; zetel Nieuwstraat 1 1785 Merchtem; contact financies@merchtem.be",
    "src_kbo_mrch_0824869093,KBO AGB Merchtem 0824.869.093,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0824869093,KBO Public Search FOD Economie,2026-08-19,official_register,tick1411; Actief since 26.10.2009; zetel Nieuwstraat 1 1785 Merchtem; 0 VE; NACE 93.110; aanbestedende overheid; tel 052/38.11.75",
    "src_mrch_foi_contact,AGB Merchtem FOI channel / official contact (financies@merchtem.be; Nieuwstraat 1 Merchtem),https://www.merchtem.be/AGB,AGB Merchtem,2026-08-19,official_register,tick1411; voorzitter David De Valck; vennoot Gemeente Merchtem 0207.511.110; commissaris Bedrijfsrevisoren SD B00240 fee 3705",
])
print("sources +4")
