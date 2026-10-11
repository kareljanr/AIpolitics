#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2423_stamp.txt").read_text().strip().splitlines()
EID = "vzw_huize_zonnelied"
SRC_PDF = "src_huize_zonnelied_jr2025_nbb_pdf_2423"
COMM = "comm_huize_zonnelied_jr2025_statutory_omzet_10_95m_73_2_43m_pnl_jump_280k"
LB = "lb_huize_zonnelied_omzet_10_95m_73_2_43m_opbr_13_61m_pnl_jump_280k_destin_240k_jr2025"
GAP = "gap_zonnelied_ieper_zorg_matrix_omzet_10_95m_73_2_43m_opbr_13_61m_pnl_jump_280k_destin_240k_l5"
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
    '"{""2025_omzet"":10947653,""2025_73"":2431251,""2025_76A"":0,'
    '""2025_opbr"":13607953,""2025_74"":229049,'
    '""2025_pnl"":280337,""2025_bedrijfswinst"":411779,'
    '""2025_equity"":9780553,""2025_assets"":20080302,""2025_debt"":10217646,'
    '""2025_fte"":147.6,""2025_kapitaalsubsidies"":4944671,""2025_destin691"":240169,'
    '""2025_cash"":190094,""2025_geldbeleggingen"":2390338,'
    '""2025_personnel62"":10187453,""2025_gebouwen22"":10636541,'
    '""2025_aanbouw27"":1686141,""2025_capex"":1410927,'
    '""2025_fondsen10"":1590591,""2025_bestemde13"":2166561,'
    '""2025_overgedragen14"":1078730,""2025_66A"":56256,'
    '""2025_66B"":0,""2025_voorzieningen16"":82103,""2025_76B"":0,'
    '""2025_overlopend492"":545633,""2025_deelneming280"":25000,'
    '""2024_omzet"":10571109,""2024_73"":2442799,'
    '""2024_opbr"":13230939,""2024_pnl"":169750,""2024_bedrijfswinst"":559045,'
    '""2024_equity"":9752721,""2024_assets"":21052718,'
    '""2024_debt"":11210419,""2024_cash"":1432212,""2024_fte"":141.6,'
    '""2024_destin691"":200000,""2024_kapitaalsubsidies"":5197176,'
    '""2024_geldbeleggingen"":1990338}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Huize Zonnelied vzw YE2025 (omzet JUMP 10.95m / 73 2.43m / opbr JUMP 13.61m / pnl JUMP 280k / destin 240k / Strong PDF),{EID},Departement Zorg + leftover city_ieper Quattro-lid WZC,VZW Huize Zonnelied (KBO 0415.082.497; Actief; 1 VE Stationsstraat 24 Ieper; RSZ2025 87.301; WZC + DVC Zonnegloed / kortverblijf / zorgflats),2026-06-17,2025,2025,10947653,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00185108.pdf,Public WZC dual of mined city_ieper,Publish Zorg/RIZIV/dagprijs matrix behind omzet 10.95m + why 73 DROP 2.43m + why 9904 JUMP 280k + destin 240k + cash DROP 190k + aanbouw JUMP 1.69m,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Ieper>Huize Zonnelied>JR2025_statutory_L5,tick2423; Strong official native PDF; leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Zonnelied Roosdaal 0420.607.638; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; NOT WZC De Linde Lievegem 0467.355.403; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Huize Zonnelied omzet JUMP 10.95m / 73 2.43m / opbr JUMP 13.61m / pnl JUMP 280k / destin 240k (YE2025 Ieper Quattro-lid WZC),L5,wzc_vzw_statutory,Vlaanderen>West-Vlaanderen>Ieper>Huize Zonnelied>JR2025,10947653,10947653,PDF omzet70 JUMP 10947653 envelope not commercial-only; 73 DROP 2431251; 76A empty; opbr 70/76A JUMP 13607953; bedrijfswinst DROP 411779; pnl JUMP 280337; equity JUMP 9780553; assets DROP 20080302; debt DROP 10217646; FTE 147.6; kapitaalsubsidies DROP 4944671; destin691 JUMP 240169; cash DROP 190094; geldbeleggingen JUMP 2390338; gebouwen DROP 10636541; aanbouw JUMP 1686141; 1 VE Stationsstraat 24 Ieper,strong,{SRC_PDF},Departement Zorg + leftover city_ieper,Departement Zorg WZC + leftover city_ieper,10.95m omzet; 73 2.43m; opbr 13.61m; 9901 412k; pnl JUMP 280k; destin 240k; leftover city_ieper,5.25,2.65,5.12,5.43,FOI Zorg/RIZIV/dagprijs matrix behind omzet 10.95m + why 73 DROP 2.43m + why 9904 JUMP 280k + destin 240k + cash DROP 190k + aanbouw JUMP 1.69m,active,,tick2423; Strong official NBB native PDF + Strong KBO; leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Ieper>Huize Zonnelied>WZC,{EID},Zorg/RIZIV/dagprijs split behind omzet 10947653 (not commercial-only vs 73 2431251 all subsidies 733); why 73 DROP 2431251 (was 2442799); why 9904 JUMP 280337 (was 169750) and 9901 DROP 411779 (was 559045); why destin 691 JUMP 240169 (200000 VIPA-aflossing + 40169 half-of-rest; 9905 280337) and overgedragen 14 1078730; why cash DROP 190094 (was 1432212) at capex 1410927 and aanbouw JUMP 1686141; FTE 147.6; 1 VE Stationsstraat 24 Ieper; Quattro-lid,Strong official PDF leftover public WZC of city_ieper; 10.95m omzet; public WZC Quattro-lid not private clinic; not Kloosterstraat 6 Drongen; not Zonnelied Roosdaal 0420.607.638; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479; not WZC De Linde Lievegem 0467.355.403,8,VZW Huize Zonnelied / Raad van Bestuur,info@huizezonnelied.be,"Stationsstraat 24, 8900 Ieper",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2423; ready NOT sent; Strong official native NBB PDF; leftover city_ieper Quattro-lid WZC after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef / Quattro@2421; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
