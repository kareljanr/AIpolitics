#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2390_stamp.txt").read_text().strip().splitlines()
EID = "vzw_ldsst"
SRC_PDF = "src_ldsst_jr2025_nbb_pdf_2390"
COMM = "comm_ldsst_jr2025_statutory_bruto_591k_73_179k_pnl_flip_destin_59k"
LB = "lb_ldsst_bruto_591k_73_179k_pnl_flip_destin_59k_jr2025"
GAP = "gap_ldsst_riziv_vl_logopedie_matrix_bruto_591k_73_179k_pnl_flip_destin_59k_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

cash_json = (
    '"{""2025_omzet"":35784,""2025_bruto9900"":591161,""2025_73"":179055,'
    '""2025_pnl"":98656,""2025_bedrijfswinst"":98983,""2025_equity"":162403,'
    '""2025_assets"":437505,""2025_debt"":275102,""2025_fte"":6.9,'
    '""2025_kapitaalsubsidies"":0,""2025_destin691"":59104,""2025_cash"":35597,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":491403,'
    '""2025_gebouwen22"":0,""2025_aanbouw27"":0,'
    '""2025_capex"":0,""2025_fondsen10"":0,'
    '""2025_bestemde13"":122851,""2025_overgedragen14"":39552,'
    '""2025_76A"":0,""2025_791"":0,""2025_vorderingen41"":400657,'
    '""2025_overige_schulden48"":205439,'
    '""2024_omzet"":37007,""2024_bruto9900"":453044,'
    '""2024_73"":187301,""2024_pnl"":-7767,""2024_bedrijfswinst"":-7440,'
    '""2024_equity"":63747,""2024_assets"":225201,""2024_debt"":161454,'
    '""2024_kapitaalsubsidies"":0,""2024_cash"":39831,""2024_fte"":6.7,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},LDSST vzw YE2025 (bruto JUMP 591k / 73 179k / pnl PROFIT FLIP 99k / destin 59k / Strong PDF),{EID},Departement Zorg + leftover city_hasselt,VZW LDSST (KBO 0410.121.344; Actief; 1 VE; RSZ2025 86.996),2026-06-29,2025,2025,591161,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243690.pdf,Public Kohesi-family logopedie dual of mined city_hasselt,Publish RIZIV/VL/logopedie matrix inside bruto 591k + 73 179k + omzet 36k commercial-only + pnl PROFIT FLIP 99k + destin 59k + assets 2x,{SRC_PDF},strong,Vlaanderen>Limburg>Hasselt>LDSST>JR2025_statutory_L5,tick2390 EVERY-10; Strong official native PDF; leftover city_hasselt after BW Kohesi@2389; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT De Schans 0430.473.231; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},LDSST bruto JUMP 591k / 73 179k / pnl PROFIT FLIP 99k / destin 59k (YE2025 Hasselt),L5,logopedie_vzw_statutory,Vlaanderen>Limburg>Hasselt>LDSST>JR2025,591161,591161,PDF bruto JUMP 591161 MIC envelope; omzet DROP 35784 commercial-only; 73 DROP 179055; bedrijfswinst PROFIT FLIP 98983; pnl PROFIT FLIP 98656; equity JUMP 162403; assets JUMP 437505; debt JUMP 275102; FTE 6.9 JUMP; kapitaalsubsidies empty; destin691 JUMP 59104; cash DROP 35597; geldbeleggingen empty; gebouwen empty; capex empty; personnel 491403; overige vorderingen 400657; overige schulden 205439,strong,{SRC_PDF},clients speech-voice therapy Limburg,Departement Zorg + leftover city_hasselt,591k MIC bruto JUMP 30pct; 73 179k; omzet 36k commercial-only; pnl PROFIT FLIP 99k; destin 59k; assets almost 2x; leftover city_hasselt,6.2,4.2,4.8,5.00,FOI RIZIV/VL/logopedie matrix + bruto 591k + 73 179k + pnl PROFIT FLIP 99k + destin 59k + assets 2x + BTW-eenheid,active,,tick2390 EVERY-10; Strong official NBB native PDF + Strong KBO; leftover city_hasselt after BW Kohesi@2389; OFF Drongen OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Hasselt>LDSST>RIZIV_VL_logopedie,{EID},RIZIV/Departement Zorg/VAPH split inside bruto 591161; why omzet 35784 commercial-only vs 73 179055 DROP; why pnl PROFIT FLIP 98656 (was -7767) and destin 691 59104 JUMP; why assets 437505 almost 2x and overige vorderingen 400657 / overige schulden 205439 JUMP; FTE 6.9; BTW-eenheid REVA/CGG/BW/De Schans,Strong official PDF leftover public Kohesi-family logopedie of city_hasselt; 591k bruto; public not private clinic; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995,8,LDSST VZW / Erik Ottenbourgs voorzitter / Johan Gommers dagelijks bestuur,info@kohesi.be,"Ilgatlaan 11 bus 7, 3500 Hasselt",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2390 EVERY-10; ready NOT sent; Strong official native NBB PDF; leftover city_hasselt logopedie after BW Kohesi@2389; off Drongen off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
