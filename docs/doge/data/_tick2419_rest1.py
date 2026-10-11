#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2419_stamp.txt").read_text().strip().splitlines()
EID = "vzw_pagadder"
SRC_PDF = "src_pagadder_jr2025_nbb_pdf_2419"
COMM = "comm_pagadder_jr2025_statutory_opbr_1_61m_73_1_31m_pnl_drop_83k"
LB = "lb_pagadder_opbr_1_61m_73_1_31m_omzet_298k_pnl_drop_83k_destin_0_jr2025"
GAP = "gap_pagadder_opgroeien_matrix_opbr_1_61m_73_1_31m_omzet_298k_pnl_drop_83k_destin_0_l5"
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
    '"{""2025_omzet"":297790,""2025_bruto9900"":1330335,""2025_73"":1307284,'
    '""2025_76A"":2650,""2025_opbr"":1607724,'
    '""2025_pnl"":82665,""2025_bedrijfswinst"":72984,'
    '""2025_equity"":947907,""2025_assets"":1193085,""2025_debt"":245179,'
    '""2025_fte"":21.3,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":167197,""2025_geldbeleggingen"":786842,'
    '""2025_personnel62"":1247312,""2025_gebouwen22"":16904,'
    '""2025_aanbouw27"":0,""2025_capex"":8326,'
    '""2025_fondsen10"":0,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":947907,""2025_66A"":0,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2024_omzet"":283210,""2024_bruto9900"":1412537,""2024_73"":1302994,'
    '""2024_opbr"":1586776,""2024_pnl"":235343,""2024_bedrijfswinst"":220104,'
    '""2024_equity"":865241,""2024_assets"":1045203,'
    '""2024_debt"":179961,""2024_cash"":161792,""2024_fte"":20.3,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":550391}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},De Pagadder vzw YE2025 (opbr FLAT 1.61m / 73 1.31m / omzet 298k / pnl DROP 83k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK + leftover city_kortrijk,VZW Kinderopvang De Pagadder (KBO 0888.028.268; Actief; 2 VE Kloosterstraat + Marktstraat Marke; RSZ2025 88.911; Kind en Gezin CIK 2 groepsopvang),2026-06-01,2025,2025,1607724,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00133513.pdf,Public CIK dual of mined city_kortrijk,Publish Opgroeien/stad/ouder matrix behind opbr 1.61m + why 73 1.31m + why 9901 DROP 73k + pnl DROP 83k + destin 0 + 60/61 empty vs jaarverslag 279k+38k + debt JUMP 245k,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>De Pagadder>JR2025_statutory_L5,tick2419; Strong official native PDF; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; NOT Kloosterstraat 6 Drongen; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},De Pagadder opbr FLAT 1.61m / 73 1.31m / omzet 298k / pnl DROP 83k / destin 0 (YE2025 Kortrijk CIK),L5,cik_vzw_statutory,Vlaanderen>West-Vlaanderen>Kortrijk>De Pagadder>JR2025,1607724,1607724,PDF opbr 70+73+76A JUMP 1607724 VZW envelope; omzet70 JUMP 297790 commercial-only; 73 JUMP 1307284; 76A JUMP 2650; bruto9900 DROP 1330335; bedrijfswinst DROP 72984; pnl DROP 82665; equity JUMP 947907; assets JUMP 1193085; debt JUMP 245179; FTE JUMP 21.3; kapitaalsubsidies empty; destin691 empty; cash JUMP 167197; geldbeleggingen JUMP 786842; gebouwen DROP 16904; 2 VE Kloosterstraat + Marktstraat,strong,{SRC_PDF},Opgroeien + CIK leftover city_kortrijk,Opgroeien Kind en Gezin + leftover city_kortrijk,1.61m opbr; 73 1.31m; omzet 298k; 9901 DROP 73k; pnl DROP 83k; destin 0; leftover city_kortrijk,5.34,5.24,5.16,5.25,FOI Opgroeien/stad/ouder matrix behind opbr 1.61m + why 73 1.31m + why 9901 DROP 73k + pnl DROP 83k + destin 0 + 60/61 empty vs jaarverslag 279k+38k + debt JUMP 245k,active,,tick2419; Strong official NBB native PDF + Strong KBO; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Kortrijk>De Pagadder>CIK,{EID},Opgroeien/stad/ouder split behind opbr 1607724 (70 297790 commercial-only vs 73 1307284); why 9901 DROP 72984 (was 220104) and pnl DROP 82665 (was 235343); why destin 691 empty and 9905 82665 fully to overgedragen 14 947907; why 60/61 current empty (YE2024 212575) vs jaarverslag 279117 diensten + 37731 aankopen; why debt JUMP 245179 via 42/48 237529 and 44 JUMP 77077 (was 21092); FTE 21.3 JUMP; 2 VE Kloosterstraat + Marktstraat,Strong official PDF leftover public CIK of city_kortrijk; 1.61m opbr; public CIK not private clinic; not Kloosterstraat 6 Drongen; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang De Pagadder / Raad van Bestuur,boekhouding@de-ruyschaert.be,"Kloosterstraat 18, 8510 Marke",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2419; ready NOT sent; Strong official native NBB PDF; leftover city_kortrijk CIK after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
