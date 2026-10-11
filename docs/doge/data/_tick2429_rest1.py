#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2429_stamp.txt").read_text().strip().splitlines()
EID = "vzw_windekind"
SRC_PDF = "src_windekind_jr2025_nbb_pdf_2429"
COMM = "comm_windekind_jr2025_statutory_bruto_1_18m_omzet73_empty_pnl_drop_61k"
LB = "lb_windekind_bruto_1_18m_omzet73_empty_pnl_drop_61k_destin_61k_jr2025"
GAP = "gap_windekind_opgroeien_matrix_bruto_1_18m_omzet73_empty_pnl_drop_61k_destin_61k_l5"
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
    '"{""2025_omzet"":0,""2025_73"":0,""2025_76A"":0,'
    '""2025_bruto"":1184568,'
    '""2025_pnl"":61273,""2025_bedrijfswinst"":62541,'
    '""2025_equity"":500665,""2025_assets"":631200,""2025_debt"":130534,'
    '""2025_fte"":16.5,""2025_kapitaalsubsidies"":0,""2025_destin691"":61273,'
    '""2025_cash"":520891,""2025_geldbeleggingen"":20000,'
    '""2025_personnel62"":1094857,""2025_gebouwen22"":29869,'
    '""2025_aanbouw27"":0,""2025_capex"":6951,'
    '""2025_fondsen10"":500665,""2025_overgedragen14"":0,'
    '""2025_66A"":0,""2025_66B"":0,""2025_voorzieningen16"":0,'
    '""2025_76B"":0,""2025_630"":23239,'
    '""2024_omzet"":0,""2024_73"":0,'
    '""2024_bruto"":1084985,""2024_pnl"":67127,""2024_bedrijfswinst"":69317,'
    '""2024_equity"":439392,""2024_assets"":555952,'
    '""2024_debt"":116560,""2024_cash"":462496,""2024_fte"":17.1,'
    '""2024_destin691"":67127,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Windekind vzw YE2025 (bruto JUMP 1.18m / omzet+73 empty / pnl DROP 61k / destin 61k / Strong PDF),{EID},Opgroeien + leftover city_gent CIK,VZW KINDERDAGVERBLIJF WINDEKIND (KBO 0431.806.386; Actief; 1 VE Roggestraat 17 9000 Gent; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap),2026-06-30,2025,2025,1184568,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00320133.pdf,Public CIK dual of mined city_gent,Publish Opgroeien/ouderbijdragen matrix behind bruto 1.18m + why 70+73 empty vs 69 Opgroeien plaatsen + why 9904 DROP 61k + destin 61k + FTE DROP 16.5,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Gent>Windekind>JR2025_statutory_L5,tick2429; Strong official native PDF; leftover mined city_gent after Elfenbankje / AGB Kunsten / AGB Erfgoed; NOT Kloosterstraat 6 Drongen; NOT Elfenbankje 0417.638.151; NOT Beregoed 0447.515.042; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Windekind bruto JUMP 1.18m / omzet+73 empty / pnl DROP 61k / destin 61k (YE2025 leftover city_gent CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>Windekind>JR2025,1184568,1184568,PDF bruto 9900 JUMP 1184568 envelope (omzet70 empty VKT; 73 empty VKT; 76A empty); bedrijfswinst DROP 62541; pnl DROP 61273; equity JUMP 500665; assets JUMP 631200; debt JUMP 130534; FTE 16.5; kapitaalsubsidies empty; destin691 61273; cash JUMP 520891; geldbeleggingen JUMP 20000; gebouwen DROP 29869; aanbouw empty; 1 VE Gent 69 plaatsen,strong,{SRC_PDF},Opgroeien + leftover city_gent,Opgroeien CIK + leftover city_gent,1.18m bruto; omzet+73 empty; 9901 63k DROP; pnl DROP 61k; destin 61k; leftover city_gent,5.20,2.00,5.10,5.19,FOI Opgroeien/ouderbijdragen matrix behind bruto 1.18m + why 70+73 empty vs 69 Opgroeien plaatsen + why 9904 DROP 61k + destin 61k + FTE DROP 16.5,active,,tick2429; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Gent>Windekind>CIK,{EID},Opgroeien/ouderbijdragen split behind bruto 1184568 (omzet 70 empty + 73 empty VKT); why 70+73 empty while site lists 69 Opgroeien-gesubsidieerde plaatsen; why 9904 DROP 61273 (was 67127) and 9901 DROP 62541 (was 69317); why destin 691 61273 to fondsen 10 500665 while code 13 empty; why cash JUMP 520891 (was 462496) at geldbeleggingen JUMP 20000 and gebouwen DROP 29869 and capex 6951; FTE 16.5 DROP (was 17.1); 1 VE Gent 69 plaatsen,Strong official PDF leftover public CIK of mined city_gent; 1.18m bruto; public Opgroeien CIK not private clinic; not Kloosterstraat 6 Drongen; not Elfenbankje 0417.638.151; not Beregoed 0447.515.042; not Vormingscentrum 0413.342.338; not Helan 0464.151.037; not Duinhuisjes 0413.323.037; not t Bremhuisje 0445.265.533 stopgezet 1993; not Kinderlach 0450.275.186; not KISME 0894.549.440; not Kindercentrum 0408.226.775; not KOS 0891.472.362; not WZC De Linde Wortegem-Petegem 0425.773.085; not OLV Gasthuis Poperinge 0445.066.385; not Huize Zonnelied 0415.082.497; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW KINDERDAGVERBLIJF WINDEKIND / Raad van Bestuur,info@windekind.gent,"Roggestraat 17, 9000 Gent",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2429; ready NOT sent; Strong official native NBB PDF; leftover mined city_gent CIK after Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
