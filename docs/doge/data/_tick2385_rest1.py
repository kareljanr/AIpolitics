#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP = "2026-08-25T00:04:21Z"
DAY = "2026-08-25"
EID = "vzw_ascendere"
SRC_PDF = "src_ascendere_jr2025_nbb_pdf_2385"
COMM = "comm_ascendere_jr2025_statutory_omzet_4_34m_73_866k_pnl_drop"
LB = "lb_ascendere_omzet_4_34m_73_866k_pnl_drop_jr2025"
GAP = "gap_ascendere_riziv_vl_vaph_matrix_omzet_4_34m_73_866k_pnl_drop_destin_empty_l5"
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
    '"{""2025_omzet"":4338634,""2025_bruto"":4821515,""2025_73"":865623,'
    '""2025_pnl"":27286,""2025_bedrijfswinst"":43210,""2025_equity"":3529703,'
    '""2025_assets"":5657078,""2025_debt"":2127375,""2025_fte"":52.5,'
    '""2025_kapitaalsubsidies"":1098275,""2025_destin691"":0,""2025_cash"":1688162,'
    '""2025_geldbeleggingen"":0,""2025_personnel62"":4483299,'
    '""2025_gebouwen22"":3144561,""2025_aanbouw27"":0,'
    '""2025_capex8169"":107227,""2025_fondsen10"":1005224,'
    '""2025_bestemde13"":0,""2025_overgedragen14"":1426204,'
    '""2025_fin_opbr75"":5425,""2025_diensten6061"":409175,'
    '""2024_omzet"":4318609,""2024_bruto"":4822639,'
    '""2024_73"":905659,""2024_pnl"":145593,""2024_bedrijfswinst"":165869,'
    '""2024_equity"":3551681,""2024_assets"":5719819,""2024_debt"":2168138,'
    '""2024_kapitaalsubsidies"":1147539,""2024_cash"":1462037,""2024_fte"":54.4,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":250000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Ascendere vzw YE2025 (omzet 4.34m / 73 866k / pnl DROP 27k / destin empty / Strong PDF),{EID},RIZIV + Departement Zorg + VAPH + leftover city_eeklo,VZW Ascendere (KBO 0409.470.553; Actief; 4 VE; RSZ2025 86.959),2026-06-29,2025,2025,4338634,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00209823.pdf,Public CAR dual of mined city_eeklo,Publish RIZIV/VL/VAPH matrix inside omzet 4.34m + explain 73 866k DROP + pnl DROP 81% + cash 1.69m + emptied 250k belegging + destin empty + 1.10m kapitaalsubsidies,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Eeklo>Ascendere>JR2025_statutory_L5,tick2385; Strong official native PDF; leftover city_eeklo after CAR Roeselare@2384; NOT Kloosterstraat 6; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Ascendere omzet 4.34m / 73 866k / pnl DROP 81% / destin empty (YE2025 Eeklo),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Eeklo>Ascendere>JR2025,4338634,4338634,PDF omzet JUMP 4338634 CAR envelope; bruto DROP 4821515 ~1.11x; 73 DROP 865623; bedrijfswinst DROP 43210; pnl DROP 27286; equity DROP 3529703; assets DROP 5657078; debt DROP 2127375; FTE 52.5 DROP; kapitaalsubsidies DROP 1098275; destin691 empty; cash JUMP 1688162; geldbeleggingen emptied; gebouwen 3144561; capex 107227; personnel 4483299,strong,{SRC_PDF},children with developmental difficulties / CP / NAH Eeklo Lede Ninove Wetteren,RIZIV + Departement Zorg + VAPH + leftover city_eeklo,4.34m CAR omzet; 866k 73 subsidies DROP; pnl DROP 81%; cash 1.69m + emptied 250k belegging; destin empty; 1.10m kapitaalsubsidies; leftover city_eeklo,5.6,5.4,5.3,5.48,FOI RIZIV/VL/VAPH matrix + 73 866k DROP + pnl DROP 81% + cash 1.69m + emptied 250k belegging + destin empty + 1.10m kapitaalsubsidies,active,,tick2385; Strong official NBB native PDF + Strong KBO; leftover city_eeklo after CAR Roeselare@2384; OFF Drongen OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Eeklo>Ascendere>RIZIV_VL_VAPH_CAR,{EID},RIZIV/Departement Zorg/VAPH split inside omzet 4338634; why 73 865623 DROP; why pnl DROP 27286 (-81%); why cash 1688162 JUMP + emptied 250000 belegging; nature of destin 691 empty and kapitaalsubsidies 15 1098275; FTE DROP 52.5; 90pct forfaits,Strong official PDF leftover public CAR of city_eeklo; 4.34m omzet; public not private clinic,8,Ascendere VZW / Guido Schelfaut voorzitter / Bart Volders algemeen directeur,info@ascendere.be,"Melkerij 25, 9900 Eeklo",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2385; ready NOT sent; Strong official native NBB PDF; leftover city_eeklo CAR after CAR Roeselare@2384; off Drongen off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
