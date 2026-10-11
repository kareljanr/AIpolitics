#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2425_stamp.txt").read_text().strip().splitlines()
EID = "vzw_wzc_de_linde_wortegem"
SRC_PDF = "src_de_linde_wortegem_jr2025_nbb_pdf_2425"
COMM = "comm_de_linde_wortegem_jr2025_statutory_omzet_5_52m_73_1_05m_pnl_flip_62k"
LB = "lb_de_linde_wortegem_omzet_5_52m_73_1_05m_opbr_6_68m_pnl_flip_62k_destin_62k_jr2025"
GAP = "gap_de_linde_wortegem_zorg_matrix_omzet_5_52m_73_1_05m_opbr_6_68m_pnl_flip_62k_destin_62k_l5"
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
    '"{""2025_omzet"":5515186,""2025_73"":1049648,""2025_76A"":1500,'
    '""2025_opbr"":6683103,""2025_74"":116769,'
    '""2025_pnl"":62128,""2025_bedrijfswinst"":90793,'
    '""2025_equity"":3155455,""2025_assets"":6379220,""2025_debt"":3223765,'
    '""2025_fte"":71.4,""2025_kapitaalsubsidies"":36182,""2025_destin691"":62128,'
    '""2025_cash"":1196793,""2025_geldbeleggingen"":19621,'
    '""2025_personnel62"":4987141,""2025_gebouwen22"":4339615,'
    '""2025_aanbouw27"":0,""2025_capex"":84494,'
    '""2025_fondsen10"":1807689,""2025_bestemde13"":1311584,'
    '""2025_overgedragen14"":0,""2025_66A"":24,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2025_overlopend492"":142,""2025_deelneming280"":0,'
    '""2024_omzet"":5206034,""2024_73"":1050540,'
    '""2024_opbr"":6375889,""2024_pnl"":-151989,""2024_bedrijfswinst"":-126874,'
    '""2024_equity"":3104102,""2024_assets"":6413779,'
    '""2024_debt"":3309677,""2024_cash"":1104053,""2024_fte"":68.3,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":46957,'
    '""2024_geldbeleggingen"":20135}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},WZC De Linde Wortegem-Petegem vzw YE2025 (omzet JUMP 5.52m / 73 1.05m / opbr JUMP 6.68m / pnl FLIP 62k / destin 62k / Strong PDF),{EID},Departement Zorg + leftover city_oudenaarde Quattro-lid WZC,VZW De Linde (KBO 0425.773.085; Actief; 1 VE Lindestraat 16 9790 Wortegem-Petegem; RSZ2025 87.301; WZC 89 woongelegenheden),2026-06-08,2025,2025,5515186,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00162292.pdf,Public WZC dual of nearby mined city_oudenaarde,Publish Zorg/RIZIV/dagprijs matrix behind omzet 5.52m + why 73 DROP 1.05m + why 9904 PROFIT FLIP 62k + destin 62k + cash JUMP 1.20m,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Wortegem-Petegem>WZC De Linde>JR2025_statutory_L5,tick2425; Strong official native PDF; leftover nearby mined city_oudenaarde after SOLVA / HVVA; leftover unmined city_wortegem_petegem city GE; Quattro-lid after OLV Gasthuis Poperinge@2424 / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC De Linde Lievegem 0467.355.403; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},WZC De Linde Wortegem-Petegem omzet JUMP 5.52m / 73 1.05m / opbr JUMP 6.68m / pnl FLIP 62k / destin 62k (YE2025 Quattro-lid WZC),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Wortegem-Petegem>WZC De Linde>JR2025,5515186,5515186,PDF omzet70 JUMP 5515186 envelope not commercial-only; 73 DROP 1049648; 76A JUMP 1500; opbr 70/76A JUMP 6683103; bedrijfswinst PROFIT FLIP 90793; pnl PROFIT FLIP 62128; equity JUMP 3155455; assets DROP 6379220; debt DROP 3223765; FTE 71.4; kapitaalsubsidies DROP 36182; destin691 JUMP 62128; cash JUMP 1196793; geldbeleggingen DROP 19621; gebouwen DROP 4339615; aanbouw empty; 1 VE Lindestraat 16 9790,strong,{SRC_PDF},Departement Zorg + leftover city_oudenaarde,Departement Zorg WZC + leftover city_oudenaarde,5.52m omzet; 73 1.05m; opbr 6.68m; 9901 91k FLIP; pnl FLIP 62k; destin 62k; leftover city_oudenaarde,5.18,2.48,5.12,5.33,FOI Zorg/RIZIV/dagprijs matrix behind omzet 5.52m + why 73 DROP 1.05m + why 9904 PROFIT FLIP 62k + destin 62k + cash JUMP 1.20m,active,,tick2425; Strong official NBB native PDF + Strong KBO; leftover nearby mined city_oudenaarde after SOLVA / HVVA; leftover unmined city_wortegem_petegem city GE; Quattro-lid after OLV Gasthuis Poperinge@2424 / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Wortegem-Petegem>WZC De Linde>WZC,{EID},Zorg/RIZIV/dagprijs split behind omzet 5515186 (not commercial-only vs 73 1049648); why 73 DROP 1049648 (was 1050540); why 9904 PROFIT FLIP 62128 (was -151989) and 9901 PROFIT FLIP 90793 (was -126874); why destin 691 62128 (100% of 9905) and overgedragen 14 empty; why cash JUMP 1196793 (was 1104053) at geldbeleggingen 19621 and capex 84494; FTE 71.4; 1 VE Lindestraat 16 9790 Wortegem-Petegem; Quattro-lid,Strong official PDF leftover public WZC of nearby mined city_oudenaarde; 5.52m omzet; public WZC Quattro-lid not private clinic; not Kloosterstraat 6 Drongen; not WZC De Linde Lievegem 0467.355.403; not OLV Gasthuis Poperinge 0445.066.385; not Huize Zonnelied 0415.082.497; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW De Linde / Raad van Bestuur,nadine@wzcdelinde.be,"Lindestraat 16, 9790 Wortegem-Petegem",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2425; ready NOT sent; Strong official native NBB PDF; leftover nearby mined city_oudenaarde Quattro-lid WZC after SOLVA / HVVA / OLV Gasthuis Poperinge@2424 / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; leftover unmined city_wortegem_petegem city GE; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
