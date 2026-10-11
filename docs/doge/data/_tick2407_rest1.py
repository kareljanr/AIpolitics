#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2407_stamp.txt").read_text().strip().splitlines()
EID = "vzw_3wplus_kinderopvang"
SRC_PDF = "src_3wplus_jr2025_nbb_pdf_2407"
COMM = "comm_3wplus_jr2025_statutory_bruto_7_16m_omzet73_empty_pnl_jump_destin_75k"
LB = "lb_3wplus_bruto_7_16m_omzet73_empty_pnl_jump_551k_destin_75k_jr2025"
GAP = "gap_3wplus_opgroeien_matrix_bruto_7_16m_omzet73_empty_pnl_jump_551k_destin_75k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":7160626,""2025_73"":0,'
    '""2025_pnl"":551218,""2025_bedrijfswinst"":544758,'
    '""2025_equity"":1682311,""2025_assets"":4301389,""2025_debt"":2619078,'
    '""2025_fte"":125.2,""2025_kapitaalsubsidies"":85875,""2025_destin691"":75000,'
    '""2025_cash"":871472,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":6491189,""2025_gebouwen22"":602648,'
    '""2025_aanbouw27"":338536,""2025_capex"":1242169,""2025_bestemde13"":250000,'
    '""2025_overgedragen14"":1346436,""2025_76A"":0,""2025_630"":88591,'
    '""2025_fondsen10"":0,""2025_8029"":41999,""2025_lt17"":668719,'
    '""2025_zakelijk9062"":508855,""2025_6408"":26456,'
    '""2024_bruto9900"":6952580,""2024_pnl"":75056,""2024_bedrijfswinst"":67511,'
    '""2024_equity"":1073649,""2024_assets"":2567712,""2024_debt"":1453396,'
    '""2024_kapitaalsubsidies"":28431,""2024_cash"":707639,""2024_fte"":106.2,'
    '""2024_destin691"":0,""2024_gebouwen22"":0,""2024_6408"":947596}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},3Wplus Kinderopvang vzw YE2025 (bruto JUMP 7.16m / omzet+73 empty / pnl JUMP 551k / destin 75k / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_asse,VZW 3Wplus Kinderopvang (KBO 0893.870.539; Actief; 54 VE; RSZ2025 88.919; Kinderopvang Vlaamse Gemeenschap since 01.04.2014),2026-07-09,2025,2025,7160626,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00273048.pdf,Public CIK dual of mined city_asse,Publish Opgroeien T1/T2/gemeente/ouder matrix behind bruto 7.16m + why 70/73 empty + pnl JUMP 551k + destin 75k + new buildings 603k + LT debt 669k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Asse>3WplusKinderopvang>JR2025_statutory_L5,tick2407; Strong official native PDF; leftover city_asse after De Mereltjes@2406; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},3Wplus Kinderopvang bruto JUMP 7.16m / omzet+73 empty / pnl JUMP 551k / destin 75k (YE2025 Asse CIK),L5,cik_vzw_statutory,Vlaanderen>Vlaams-Brabant>Asse>3WplusKinderopvang>JR2025,7160626,7160626,PDF bruto9900 JUMP 7160626 CIK envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst JUMP 544758; pnl JUMP 551218; equity JUMP 1682311; assets JUMP 4301389; debt JUMP 2619078; FTE JUMP 125.2; kapitaalsubsidies JUMP 85875; destin691 JUMP 75000; cash JUMP 871472; geldbeleggingen empty; gebouwen JUMP 602648; aanbouw JUMP 338536; capex 1242169; personeel 62 6491189; 54 VE,strong,{SRC_PDF},Opgroeien + CIK leftover city_asse,Opgroeien Kind en Gezin + leftover city_asse,7.16m bruto JUMP; omzet+73 empty; pnl JUMP 551k; destin 75k; leftover city_asse,5.55,5.58,5.25,5.46,FOI Opgroeien T1/T2/gemeente/ouder matrix behind bruto 7.16m + why 70/73 empty + pnl JUMP 551k + destin 75k + new buildings 603k + LT debt 669k,active,,tick2407; Strong official NBB native PDF + Strong KBO; leftover city_asse after De Mereltjes@2406; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Vlaams-Brabant>Asse>3WplusKinderopvang>CIK,{EID},Opgroeien T1/T2/gemeente/ouder split behind bruto 7160626 and why omzet 70 + 73 empty; why pnl JUMP 551218 (was 75056) and 9901 JUMP 544758; why destin 691 75000 sociaal passief; why debt JUMP 2619078 (LT 668719 new) and gebouwen JUMP 602648 + capex 1242169; 54 VE + FTE 125.2,Strong official PDF leftover public CIK of city_asse; 7.16m bruto; public intergemeentelijke kinderopvang not private clinic; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,3Wplus Kinderopvang VZW / Raad van Bestuur,kinderopvang@3wplus.be,"Z. 5 Mollem 250, 1730 Asse",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2407; ready NOT sent; Strong official native NBB PDF; leftover city_asse CIK after De Mereltjes@2406; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
