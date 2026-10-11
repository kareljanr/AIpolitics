#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2422_stamp.txt").read_text().strip().splitlines()
EID = "vzw_wintershove"
SRC_PDF = "src_wintershove_jr2025_nbb_pdf_2422"
COMM = "comm_wintershove_jr2025_statutory_omzet_6_65m_73_1_04m_pnl_loss_flip_23k"
LB = "lb_wintershove_omzet_6_65m_73_1_04m_opbr_7_79m_pnl_loss_flip_23k_destin_0_jr2025"
GAP = "gap_wintershove_zorg_matrix_omzet_6_65m_73_1_04m_opbr_7_79m_pnl_loss_flip_23k_destin_0_l5"
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
    '"{""2025_omzet"":6653784,""2025_73"":1039037,""2025_76A"":0,'
    '""2025_opbr"":7794859,""2025_74"":102038,'
    '""2025_pnl"":-22737,""2025_bedrijfswinst"":41192,'
    '""2025_equity"":2728813,""2025_assets"":5998955,""2025_debt"":2808568,'
    '""2025_fte"":95.7,""2025_kapitaalsubsidies"":383488,""2025_destin691"":0,'
    '""2025_cash"":516794,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":6188219,""2025_gebouwen22"":3736734,'
    '""2025_aanbouw27"":0,""2025_capex"":157112,'
    '""2025_fondsen10"":1298884,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":1046441,""2025_66A"":0,'
    '""2025_66B"":0,""2025_voorzieningen16"":461574,""2025_76B"":0,'
    '""2025_overlopend492"":7109,""2025_deelneming280"":25000,'
    '""2024_omzet"":6602468,""2024_73"":1162972,'
    '""2024_opbr"":7849363,""2024_pnl"":28270,""2024_bedrijfswinst"":92449,'
    '""2024_equity"":2831860,""2024_assets"":6249930,'
    '""2024_debt"":2939779,""2024_cash"":1104762,""2024_fte"":97,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":463798,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Wintershove vzw YE2025 (omzet JUMP 6.65m / 73 1.04m / opbr DROP 7.79m / pnl LOSS FLIP 23k / destin 0 / Strong PDF),{EID},Departement Zorg + leftover city_ieper Quattro-lid WZC,VZW WINTERSHOVE (KBO 0459.245.312; Actief; 1 VE Poperingseweg 288 Vlamertinge; RSZ2025 87.301; WZC 108 woongelegenheden),2026-06-17,2025,2025,6653784,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00178085.pdf,Public WZC dual of mined city_ieper,Publish Zorg/RIZIV/dagprijs matrix behind omzet 6.65m + why 73 DROP 1.04m + why 9904 LOSS FLIP 23k + destin 0 + cash DROP 517k,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Ieper>Wintershove>JR2025_statutory_L5,tick2422; Strong official native PDF; leftover city_ieper after Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; NOT WZC De Linde Lievegem 0467.355.403; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Wintershove omzet JUMP 6.65m / 73 1.04m / opbr DROP 7.79m / pnl LOSS FLIP 23k / destin 0 (YE2025 Ieper Quattro-lid WZC),L5,wzc_vzw_statutory,Vlaanderen>West-Vlaanderen>Ieper>Wintershove>JR2025,6653784,6653784,PDF omzet70 JUMP 6653784 envelope not commercial-only; 73 DROP 1039037; 76A empty; opbr 70/76A DROP 7794859; bedrijfswinst DROP 41192; pnl LOSS FLIP -22737; equity DROP 2728813; assets DROP 5998955; debt DROP 2808568; FTE 95.7; kapitaalsubsidies DROP 383488; destin691 empty; cash DROP 516794; geldbeleggingen 0; gebouwen DROP 3736734; 1 VE Poperingseweg 288 Vlamertinge,strong,{SRC_PDF},Departement Zorg + leftover city_ieper,Departement Zorg WZC + leftover city_ieper,6.65m omzet; 73 1.04m; opbr 7.79m; 9901 41k; pnl LOSS FLIP 23k; destin 0; leftover city_ieper,5.22,2.50,5.12,5.36,FOI Zorg/RIZIV/dagprijs matrix behind omzet 6.65m + why 73 DROP 1.04m + why 9904 LOSS FLIP 23k + destin 0 + cash DROP 517k,active,,tick2422; Strong official NBB native PDF + Strong KBO; leftover city_ieper after Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Quattro@2421; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Ieper>Wintershove>WZC,{EID},Zorg/RIZIV/dagprijs split behind omzet 6653784 (not commercial-only vs 73 1039037 all subsidies 733); why 73 DROP 1039037 (was 1162972); why 9904 LOSS FLIP -22737 (was PROFIT 28270) and 9901 DROP 41192 (was 92449); why destin 691 empty and 9905 -22737 fully to overgedragen 14 1046441; why cash DROP 516794 (was 1104762); FTE 95.7; 1 VE Poperingseweg 288 Vlamertinge; Quattro-lid,Strong official PDF leftover public WZC of city_ieper; 6.65m omzet; public WZC Quattro-lid not private clinic; not Kloosterstraat 6 Drongen; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479; not WZC De Linde Lievegem 0467.355.403,8,VZW WINTERSHOVE / Raad van Bestuur,info@wintershove.be,"Poperingseweg 288, 8908 Vlamertinge",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2422; ready NOT sent; Strong official native NBB PDF; leftover city_ieper Quattro-lid WZC after Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef / Quattro@2421; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
