#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2415_stamp.txt").read_text().strip().splitlines()
EID = "vzw_mariawende"
SRC_PDF = "src_mariawende_jr2025_nbb_pdf_2415"
COMM = "comm_mariawende_jr2025_statutory_bruto_3_35m_omzet73_empty_pnl_jump_736k"
LB = "lb_mariawende_bruto_3_35m_omzet73_empty_pnl_jump_736k_destin_736k_jr2025"
GAP = "gap_mariawende_opgroeien_matrix_bruto_3_35m_omzet73_empty_pnl_jump_736k_destin_736k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":3345554,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":3345554,'
    '""2025_pnl"":735612,""2025_bedrijfswinst"":588557,'
    '""2025_equity"":6465476,""2025_assets"":6896666,""2025_debt"":431190,'
    '""2025_fte"":45.2,""2025_kapitaalsubsidies"":1287136,""2025_destin691"":735612,'
    '""2025_cash"":331722,""2025_geldbeleggingen"":2537774,'
    '""2025_personnel62"":2600896,""2025_gebouwen22"":2697443,'
    '""2025_aanbouw27"":771235,""2025_capex"":190399,'
    '""2025_fondsen10"":20507,""2025_bestemde13"":3043990,'
    '""2025_overgedragen14"":2113842,""2025_66A"":2188,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_75"":167259,'
    '""2024_omzet"":0,""2024_bruto9900"":3057583,""2024_73"":0,'
    '""2024_opbr"":3057583,""2024_pnl"":406134,""2024_bedrijfswinst"":339908,'
    '""2024_equity"":5788504,""2024_assets"":6225112,'
    '""2024_debt"":436608,""2024_cash"":42769,""2024_fte"":43,'
    '""2024_destin691"":407576,""2024_kapitaalsubsidies"":1345777,'
    '""2024_geldbeleggingen"":2465192}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Kinderopvang Mariawende vzw YE2025 (bruto JUMP 3.35m / omzet+73 empty / pnl JUMP 736k / destin 736k / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK+BKO + leftover city_brugge,VZW Kinderopvang Mariawende (KBO 0411.611.184; Actief; 2 VE 2.153.783.446 Ons Tuintje / 2.212.055.306 t speelhuis; RSZ2025 88.911; CIK 140 + BKO),2026-06-24,2025,2025,3345554,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00302442.pdf,Public CIK+BKO dual of mined city_brugge,Publish Opgroeien/stad/ouder matrix behind bruto 3.35m + why 70+73 empty + why pnl JUMP 736k + destin 736k 100pct of 9905 + cash JUMP 7.7x + FTE JUMP 45.2,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Brugge>Mariawende>JR2025_statutory_L5,tick2415; Strong official native PDF; leftover city_brugge after Mintus@1269; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Kinderopvang Mariawende bruto JUMP 3.35m / omzet+73 empty / pnl JUMP 736k / destin 736k (YE2025 Brugge CIK+BKO),L5,cik_vzw_statutory,Vlaanderen>West-Vlaanderen>Brugge>Mariawende>JR2025,3345554,3345554,PDF bruto9900 JUMP 3345554 CIK envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst JUMP 588557; pnl JUMP 735612; equity JUMP 6465476; assets JUMP 6896666; debt DROP 431190; FTE JUMP 45.2; kapitaalsubsidies DROP 1287136; destin691 JUMP 735612; cash JUMP 331722; geldbeleggingen JUMP 2537774; gebouwen DROP 2697443; 2 VE Ons Tuintje 140 + BKO t Speelhuis,strong,{SRC_PDF},Opgroeien + CIK+BKO leftover city_brugge,Opgroeien Kind en Gezin + leftover city_brugge,3.35m bruto JUMP; omzet+73 empty; pnl JUMP 736k; destin 736k 100pct; leftover city_brugge,5.42,5.30,5.24,5.32,FOI Opgroeien/stad/ouder matrix behind bruto 3.35m + why 70+73 empty + why pnl JUMP 736k + destin 736k + cash JUMP 7.7x + FTE JUMP 45.2,active,,tick2415; Strong official NBB native PDF + Strong KBO; leftover city_brugge after Mintus@1269; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Brugge>Mariawende>CIK+BKO,{EID},Opgroeien/stad/ouder split behind bruto 3345554 and why 70+73 empty on VKT; why pnl JUMP 735612 (was 406134) and destin 691 735612 (100% of 9905) with overgedragen 14 FLAT 2113842; why cash JUMP 331722 (was 42769) and kapitaalsubsidies DROP 1287136; FTE 45.2 JUMP; 2 VE; Ons Tuintje 140 + BKO t Speelhuis,Strong official PDF leftover public CIK+BKO of city_brugge; 3.35m bruto; public CIK not private clinic; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderopvang Mariawende / Raad van Bestuur,directeur@ko-mariawende.be,"Keizerstraat 14 A, 8310 Brugge",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2415; ready NOT sent; Strong official native NBB PDF; leftover city_brugge CIK+BKO after Mintus@1269; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
