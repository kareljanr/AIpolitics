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
    "src_bnlg_jr2025_nbb,BIONERGA LOGISTICS VOL-kap jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00119950.pdf,NBB / BIONERGA LOGISTICS,2026-08-19,budget,tick1423; VOL-kap 25.0.12 m02-f PDF 90p / 2003913 bytes deposit 2026-00119950; AV 20.04.2026; header 13.05.2026; created 26.05.2026; KBO 0553.855.647; assets 3510439 omzet 1717525 diensten 1289949 cash 956680 debt 1845683; commissaris BDO 3740",
    "src_bnlg_site,Bionerga official portal (parent + Logistics same zetel),https://bionerga.be/,Bionerga,2026-08-19,official_register,tick1423; leftover 100pct daughter of Bionerga NV 0882.280.227; zetel Herkenrodesingel 14 3500 Hasselt; contact info@bionerga.be; Optimo truck fleet Limburg.net",
    "src_kbo_bnlg_0553855647,KBO BIONERGA LOGISTICS 0553.855.647,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0553855647,KBO Public Search FOD Economie,2026-08-19,official_register,tick1423; Actief since 13.06.2014; zetel Herkenrodesingel 14 3500 Hasselt; 1 VE; NV; NACE 77.120; aanbestedende overheid; kapitaal 1000000",
    "src_bnlg_foi_contact,BIONERGA LOGISTICS FOI channel / parent contact (info@bionerga.be; Herkenrodesingel 14 Hasselt),https://bionerga.be/,Bionerga,2026-08-19,official_register,tick1423; 100pct aandeelhouder Bionerga NV; bestuurders Bionerga NV (Peeters Philip) + Nuhma CV (Kelchtermans Ludo); commissaris BDO",
])
print("sources +4")
