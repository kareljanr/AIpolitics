#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2424_stamp.txt").read_text().strip().splitlines()
EID = "vzw_olv_gasthuis_poperinge"
SRC_PDF = "src_olv_gasthuis_jr2025_nbb_pdf_2424"
COMM = "comm_olv_gasthuis_jr2025_statutory_omzet_14_15m_73_2_64m_pnl_loss_improve_95k"
LB = "lb_olv_gasthuis_omzet_14_15m_73_2_64m_opbr_17_01m_pnl_loss_improve_95k_destin_0_jr2025"
GAP = "gap_olv_gasthuis_poperinge_zorg_matrix_omzet_14_15m_73_2_64m_opbr_17_01m_pnl_loss_improve_95k_destin_0_l5"
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
    '"{""2025_omzet"":14151870,""2025_73"":2641315,""2025_76A"":12831,'
    '""2025_opbr"":17008889,""2025_74"":202872,'
    '""2025_pnl"":-95063,""2025_bedrijfswinst"":-69796,'
    '""2025_equity"":9772731,""2025_assets"":15603053,""2025_debt"":5830322,'
    '""2025_fte"":191.8,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":1426890,""2025_geldbeleggingen"":2516447,'
    '""2025_personnel62"":13300785,""2025_gebouwen22"":8807680,'
    '""2025_aanbouw27"":466721,""2025_capex"":864635,'
    '""2025_fondsen10"":922191,""2025_bestemde13"":7923868,'
    '""2025_overgedragen14"":926671,""2025_66A"":6024,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2025_overlopend492"":86078,""2025_deelneming280"":0,'
    '""2024_omzet"":13565417,""2024_73"":2554343,'
    '""2024_opbr"":16336359,""2024_pnl"":-244629,""2024_bedrijfswinst"":-263284,'
    '""2024_equity"":9868117,""2024_assets"":16011350,'
    '""2024_debt"":6143233,""2024_cash"":1183307,""2024_fte"":188.2,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":323,'
    '""2024_geldbeleggingen"":3004307}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},OLV Gasthuis Poperinge vzw YE2025 (omzet JUMP 14.15m / 73 2.64m / opbr JUMP 17.01m / pnl LOSS IMPROVE 95k / destin 0 / Strong PDF),{EID},Departement Zorg + leftover city_poperinge Quattro-lid WZC,VZW Onze-Lieve-Vrouw Gasthuis (KBO 0445.066.385; Actief; 2 VE Ieperstraat 130 + WZC Emmaus Oostlaan 15 Poperinge; RSZ2025 87.101; WZC OLV + WZC Emmaus),2026-06-17,2025,2025,14151870,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00306712.pdf,Public WZC dual of mined city_poperinge,Publish Zorg/RIZIV/dagprijs matrix behind omzet 14.15m + why 73 JUMP 2.64m + why 9904 LOSS IMPROVE 95k + destin 0 + cash JUMP 1.43m + geldbeleggingen DROP 2.52m,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Poperinge>OLV Gasthuis>JR2025_statutory_L5,tick2424; Strong official native PDF; leftover city_poperinge after AGB De Kouter / De Lovie; Quattro-lid after Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC OLV Roosdaal 0421.031.171; NOT Emmaus AZ 0411.515.075; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; NOT WZC De Linde Lievegem 0467.355.403; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},OLV Gasthuis Poperinge omzet JUMP 14.15m / 73 2.64m / opbr JUMP 17.01m / pnl LOSS IMPROVE 95k / destin 0 (YE2025 Poperinge Quattro-lid WZC),L5,wzc_vzw_statutory,Vlaanderen>West-Vlaanderen>Poperinge>OLV Gasthuis>JR2025,14151870,14151870,PDF omzet70 JUMP 14151870 envelope not commercial-only; 73 JUMP 2641315; 76A DROP 12831; opbr 70/76A JUMP 17008889; bedrijfswinst LOSS IMPROVE -69796; pnl LOSS IMPROVE -95063; equity DROP 9772731; assets DROP 15603053; debt DROP 5830322; FTE 191.8; kapitaalsubsidies DROP 0; destin691 empty; cash JUMP 1426890; geldbeleggingen DROP 2516447; gebouwen DROP 8807680; aanbouw DROP 466721; 2 VE Ieperstraat 130 + Emmaus Oostlaan 15 Poperinge,strong,{SRC_PDF},Departement Zorg + leftover city_poperinge,Departement Zorg WZC + leftover city_poperinge,14.15m omzet; 73 2.64m; opbr 17.01m; 9901 -70k; pnl LOSS IMPROVE 95k; destin 0; leftover city_poperinge,5.25,2.75,5.12,5.47,FOI Zorg/RIZIV/dagprijs matrix behind omzet 14.15m + why 73 JUMP 2.64m + why 9904 LOSS IMPROVE 95k + destin 0 + cash JUMP 1.43m + geldbeleggingen DROP 2.52m,active,,tick2424; Strong official NBB native PDF + Strong KBO; leftover city_poperinge after AGB De Kouter / De Lovie; Quattro-lid after Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Poperinge>OLV Gasthuis>WZC,{EID},Zorg/RIZIV/dagprijs split behind omzet 14151870 (not commercial-only vs 73 2641315 subsidies 733 2637182 + 731 4133); why 73 JUMP 2641315 (was 2554343); why 9904 LOSS IMPROVE -95063 (was -244629) and 9901 LOSS IMPROVE -69796 (was -263284); why destin 691 empty (9905 -95063) and overgedragen 14 926671; why cash JUMP 1426890 (was 1183307) at geldbeleggingen DROP 2516447 and capex 864635; FTE 191.8; 2 VE Ieperstraat 130 + Emmaus Oostlaan 15 Poperinge; Quattro-lid,Strong official PDF leftover public WZC of city_poperinge; 14.15m omzet; public WZC Quattro-lid not private clinic; not Kloosterstraat 6 Drongen; not WZC OLV Roosdaal 0421.031.171; not Emmaus AZ 0411.515.075; not Huize Zonnelied 0415.082.497; not Wintershove 0459.245.312; not Quattro 0555.667.072; not WZC De Ruyschaert 0434.996.993; not De Pagadder 0888.028.268; not KOS 0891.472.362; not BKO GENK-OOST 0475.432.830; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479; not WZC De Linde Lievegem 0467.355.403,8,VZW Onze-Lieve-Vrouw Gasthuis / Raad van Bestuur,info@gasthuis.be,"Ieperstraat 130, 8970 Poperinge",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2424; ready NOT sent; Strong official native NBB PDF; leftover city_poperinge Quattro-lid WZC after AGB De Kouter / De Lovie / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
