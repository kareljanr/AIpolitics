#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2405_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_hoeksteen"
SRC_PDF = "src_hoeksteen_jr2025_nbb_pdf_2405"
COMM = "comm_hoeksteen_jr2025_statutory_bruto_1_87m_omzet73_empty_pnl_loss_flip"
LB = "lb_hoeksteen_bruto_1_87m_omzet73_empty_pnl_loss_flip_7k_jr2025"
GAP = "gap_hoeksteen_opgroeien_t2_matrix_bruto_1_87m_omzet73_empty_pnl_loss_flip_7k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":1870177,""2025_73"":0,'
    '""2025_pnl"":-7060,""2025_bedrijfswinst"":-9026,'
    '""2025_equity"":8031,""2025_assets"":536744,""2025_debt"":528713,'
    '""2025_fte"":31,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":27702,""2025_geldbeleggingen"":142106,'
    '""2025_personnel62"":1855310,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":59167,""2025_bestemde13"":12073,'
    '""2025_overgedragen14"":-4041,""2025_76A"":0,""2025_630"":22310,'
    '""2025_66A"":151,""2025_41recv"":157607,""2025_fte_ye"":36.6,'
    '""2024_bruto9900"":1250221,""2024_pnl"":100566,""2024_bedrijfswinst"":102884,'
    '""2024_equity"":15091,""2024_assets"":383113,""2024_debt"":368022,'
    '""2024_kapitaalsubsidies"":0,""2024_cash"":9538,""2024_fte"":19.6,'
    '""2024_destin691"":12073,""2024_geldbeleggingen"":147538}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang De Hoeksteen vzw YE2025 (bruto JUMP 1.87m / omzet+73 empty / pnl LOSS FLIP 7k / destin empty / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_diksmuide,VZW Kinderopvang De Hoeksteen (KBO 0765.439.866; Actief; 9 VE; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 16.08.2022),2026-06-29,2025,2025,1870177,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00224895.pdf,Public CIK dual of mined city_diksmuide,Publish Opgroeien T1/T2/stad/ouder matrix behind bruto 1.87m + why 70/73 empty + pnl LOSS FLIP 7k + destin empty + T2 continuity 174 plaatsen,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Diksmuide>DeHoeksteen>JR2025_statutory_L5,tick2405; Strong official native PDF; leftover city_diksmuide after Ter Eecken@2404; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},De Hoeksteen bruto JUMP 1.87m / omzet+73 empty / pnl LOSS FLIP 7k / destin empty (YE2025 Diksmuide CIK),L5,cik_vzw_statutory,Vlaanderen>West-Vlaanderen>Diksmuide>DeHoeksteen>JR2025,1870177,1870177,PDF bruto9900 JUMP 1870177 CIK envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst LOSS FLIP -9026; pnl LOSS FLIP -7060; equity DROP 8031; assets JUMP 536744; debt JUMP 528713; FTE JUMP 31; kapitaalsubsidies empty; destin691 empty; cash JUMP 27702; geldbeleggingen DROP 142106; gebouwen empty; aanbouw empty; capex 59167; personeel 62 1855310; 41 recv 157607; T2 continuity 174 plaatsen 2026-2029,strong,{SRC_PDF},Opgroeien + CIK leftover city_diksmuide,Opgroeien Kind en Gezin + leftover city_diksmuide,1.87m bruto JUMP; omzet+73 empty; pnl LOSS FLIP 7k; destin empty; equity DROP 8k; leftover city_diksmuide,5.4,5.1,5.2,5.23,FOI Opgroeien T1/T2/stad/ouder matrix behind bruto 1.87m + why 70/73 empty + pnl LOSS FLIP 7k + destin empty + T2 continuity 174 plaatsen,active,,tick2405; Strong official NBB native PDF + Strong KBO; leftover city_diksmuide after Ter Eecken@2404; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Diksmuide>DeHoeksteen>CIK,{EID},Opgroeien T1/T2/stad/ouder split behind bruto 1870177 and why omzet 70 + 73 empty; why pnl LOSS FLIP -7060 (was +100566) and 9901 LOSS FLIP -9026 after personeel 1855310; why 691 empty (was 12073); why equity DROP 8031 on assets 536744 and debt 528713; T2 continuity 174 plaatsen 2026-2029 + bulletkrediet 2032,Strong official PDF leftover public CIK of city_diksmuide; 1.87m bruto; public kinderopvang not private clinic; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,Kinderopvang De Hoeksteen VZW / Raad van Bestuur,gerdy.desmedt@de-hoeksteen.be,"Beerststraat 36, 8600 Diksmuide",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2405; ready NOT sent; Strong official native NBB PDF; leftover city_diksmuide CIK after Ter Eecken@2404; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
