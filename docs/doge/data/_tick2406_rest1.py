#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2406_stamp.txt").read_text().strip().splitlines()
EID = "vzw_kinderopvang_mereltjes"
SRC_PDF = "src_mereltjes_jr2025_nbb_pdf_2406"
COMM = "comm_mereltjes_jr2025_statutory_bruto_3_03m_omzet73_empty_pnl_jump"
LB = "lb_mereltjes_bruto_3_03m_omzet73_empty_pnl_jump_105k_jr2025"
GAP = "gap_mereltjes_opgroeien_matrix_bruto_3_03m_omzet73_empty_pnl_jump_105k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":3028501,""2025_73"":0,'
    '""2025_pnl"":105317,""2025_bedrijfswinst"":74712,'
    '""2025_equity"":3341795,""2025_assets"":3681651,""2025_debt"":339856,'
    '""2025_fte"":46.4,""2025_kapitaalsubsidies"":452828,""2025_destin691"":0,'
    '""2025_cash"":425878,""2025_geldbeleggingen"":1010540,'
    '""2025_personnel62"":2794513,""2025_gebouwen22"":1983174,'
    '""2025_aanbouw27"":60854,""2025_capex"":31291,""2025_bestemde13"":955533,'
    '""2025_overgedragen14"":1353438,""2025_76A"":117472,""2025_630"":154020,'
    '""2025_fondsen10"":579996,""2025_8179"":262147,""2025_fte_ye"":39.1,'
    '""2024_bruto9900"":3092998,""2024_pnl"":32463,""2024_bedrijfswinst"":-22080,'
    '""2024_equity"":3271088,""2024_assets"":3900196,""2024_debt"":629109,'
    '""2024_kapitaalsubsidies"":487438,""2024_cash"":230795,""2024_fte"":47.2,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":1000000,""2024_76A"":1765}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang De Mereltjes vzw YE2025 (bruto DROP 3.03m / omzet+73 empty / pnl JUMP 105k / destin empty / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_tongeren_borgloon,VZW Kinderopvang De Mereltjes (KBO 0412.778.352; Actief; 1 VE; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; Aanbestedende overheid since 18.01.2003),2026-06-29,2025,2025,3028501,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00216076.pdf,Public CIK dual of mined city_tongeren_borgloon,Publish Opgroeien T1/T2/stad/ouder matrix behind bruto 3.03m + why 70/73 empty + pnl JUMP 105k + 76A 117k + destin empty,{SRC_PDF},strong,Vlaanderen>Limburg>Tongeren-Borgloon>DeMereltjes>JR2025_statutory_L5,tick2406; Strong official native PDF; leftover city_tongeren_borgloon after De Hoeksteen@2405; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},De Mereltjes bruto DROP 3.03m / omzet+73 empty / pnl JUMP 105k / destin empty (YE2025 Tongeren-Borgloon CIK),L5,cik_vzw_statutory,Vlaanderen>Limburg>Tongeren-Borgloon>DeMereltjes>JR2025,3028501,3028501,PDF bruto9900 DROP 3028501 CIK envelope; omzet70 empty; 73 empty; 76A JUMP 117472; bedrijfswinst PROFIT FLIP 74712; pnl JUMP 105317; equity JUMP 3341795; assets DROP 3681651; debt DROP 339856; FTE DROP 46.4; kapitaalsubsidies DROP 452828; destin691 empty; cash JUMP 425878; geldbeleggingen JUMP 1010540; gebouwen 1983174; aanbouw 60854; capex 31291; overdrachten 262147; personeel 62 2794513; 135 plaatsen,strong,{SRC_PDF},Opgroeien + CIK leftover city_tongeren_borgloon,Opgroeien Kind en Gezin + leftover city_tongeren_borgloon,3.03m bruto DROP; omzet+73 empty; pnl JUMP 105k; 76A JUMP 117k; destin empty; leftover city_tongeren_borgloon,5.4,5.25,5.2,5.28,FOI Opgroeien T1/T2/stad/ouder matrix behind bruto 3.03m + why 70/73 empty + pnl JUMP 105k + 76A 117k + destin empty,active,,tick2406; Strong official NBB native PDF + Strong KBO; leftover city_tongeren_borgloon after De Hoeksteen@2405; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Tongeren-Borgloon>DeMereltjes>CIK,{EID},Opgroeien T1/T2/stad/ouder split behind bruto 3028501 and why omzet 70 + 73 empty; why pnl JUMP 105317 (was 32463) and 9901 PROFIT FLIP 74712 after 76A JUMP 117472; why 691 empty; why debt DROP 339856 (was 629109) and cash JUMP 425878; 135 plaatsen + FTE 46.4 vs year-end 39.1,Strong official PDF leftover public CIK of city_tongeren_borgloon; 3.03m bruto; public kinderopvang not private clinic; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,Kinderopvang De Mereltjes VZW / Raad van Bestuur,kinderdagverblijf@mereltjes.be,"Hasseltsesteenweg 16, 3700 Tongeren-Borgloon",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2406; ready NOT sent; Strong official native NBB PDF; leftover city_tongeren_borgloon CIK after De Hoeksteen@2405; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
