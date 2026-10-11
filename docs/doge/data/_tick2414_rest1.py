#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2414_stamp.txt").read_text().strip().splitlines()
EID = "vzw_boi"
SRC_PDF = "src_boi_jr2025_nbb_pdf_2414"
COMM = "comm_boi_jr2025_statutory_bruto_484k_omzet73_empty_pnl_drop_3k"
LB = "lb_boi_bruto_484k_omzet73_empty_pnl_drop_3k_destin_0_jr2025"
GAP = "gap_boi_opgroeien_matrix_bruto_484k_omzet73_empty_pnl_drop_3k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":484201,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":484201,'
    '""2025_pnl"":3005,""2025_bedrijfswinst"":-61,'
    '""2025_equity"":307897,""2025_assets"":384848,""2025_debt"":76951,'
    '""2025_fte"":9.1,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":289668,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":482300,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":0,'
    '""2025_fondsen10"":66099,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":241798,""2025_66A"":0,'
    '""2025_66B"":690,""2025_voorzieningen16"":0,""2025_6061"":108364,'
    '""2024_omzet"":0,""2024_bruto9900"":476815,""2024_73"":0,'
    '""2024_opbr"":476815,""2024_pnl"":17211,""2024_bedrijfswinst"":17090,'
    '""2024_equity"":304892,""2024_assets"":413564,'
    '""2024_debt"":108672,""2024_cash"":318522,""2024_fte"":8.9,'
    '""2024_destin691"":0,""2024_voorzieningen16"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Buitenschoolse Opvang Ieper vzw YE2025 (bruto JUMP 484k / omzet+73 empty / pnl DROP 3k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin BKO + leftover city_ieper,VZW Buitenschoolse Opvang Ieper (KBO 0431.691.669; Actief; 3 VE 2.155.709.192 / 2.216.097.236 Holderdebolder / 2.216.097.533 Klavertje 4; RSZ2025 88.911; BKO 61+55/35),2026-06-03,2025,2025,484201,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00173514.pdf,Public BKO dual of mined city_ieper,Publish Opgroeien/stad/ouder matrix behind bruto 484k + why 70+73 empty + why 9901 LOSS FLIP -61 + pnl DROP 3k + destin 0 + cash DROP 9pct + FTE JUMP 9.1,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Ieper>BOI>JR2025_statutory_L5,tick2414; Strong official native PDF; leftover city_ieper after CAR De Klinker@2386; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; NOT Mariawende 0411.611.184; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Buitenschoolse Opvang Ieper bruto JUMP 484k / omzet+73 empty / pnl DROP 3k / destin 0 (YE2025 Ieper BKO),L5,cik_vzw_statutory,Vlaanderen>West-Vlaanderen>Ieper>BOI>JR2025,484201,484201,PDF bruto9900 JUMP 484201 BKO envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst LOSS FLIP -61; pnl DROP 3005; equity JUMP 307897; assets DROP 384848; debt DROP 76951; FTE JUMP 9.1; kapitaalsubsidies empty; destin691 empty; cash DROP 289668; geldbeleggingen empty; gebouwen empty; 3 VE Klavertje 4 61 + Holderdebolder 55/35,strong,{SRC_PDF},Opgroeien + BKO leftover city_ieper,Opgroeien Kind en Gezin + leftover city_ieper,484k bruto JUMP; omzet+73 empty; 9901 LOSS FLIP; pnl DROP 3k; destin 0; leftover city_ieper,5.08,4.86,5.04,4.99,FOI Opgroeien/stad/ouder matrix behind bruto 484k + why 70+73 empty + why 9901 LOSS FLIP -61 + pnl DROP 3k + destin 0 + cash DROP 9pct + FTE JUMP 9.1,active,,tick2414; Strong official NBB native PDF + Strong KBO; leftover city_ieper after CAR De Klinker@2386; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Ieper>BOI>BKO,{EID},Opgroeien/stad/ouder split behind bruto 484201 and why 70+73 empty on VKT; why 9901 LOSS FLIP -61 (was 17090) and pnl DROP 3005 (was 17211); why destin 691 empty and 9905 3005 fully to overgedragen 14 241798; why cash DROP 289668 and debt DROP 76951 via bezoldigingen 45 58716 (was 89649); FTE 9.1 JUMP; 3 VE; Klavertje 4 61 + Holderdebolder 55/35,Strong official PDF leftover public BKO of city_ieper; 484k bruto; public BKO not private clinic; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479; not Mariawende 0411.611.184,8,VZW Buitenschoolse Opvang Ieper / Raad van Bestuur,info@buitenschoolseopvangieper.be,"Appèlstraat 1, 8900 Ieper",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2414; ready NOT sent; Strong official native NBB PDF; leftover city_ieper BKO after CAR De Klinker@2386; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
