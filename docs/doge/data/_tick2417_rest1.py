#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2417_stamp.txt").read_text().strip().splitlines()
EID = "vzw_bko_genk_oost"
SRC_PDF = "src_bkogenkoost_jr2025_nbb_pdf_2417"
COMM = "comm_bkogenkoost_jr2025_statutory_bruto_1_28m_omzet73_empty_pnl_jump_217k"
LB = "lb_bkogenkoost_bruto_1_28m_omzet73_empty_pnl_jump_217k_destin_0_jr2025"
GAP = "gap_bkogenkoost_opgroeien_matrix_bruto_1_28m_omzet73_empty_pnl_jump_217k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":1280713,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":1280713,'
    '""2025_pnl"":217320,""2025_bedrijfswinst"":205436,'
    '""2025_equity"":1085679,""2025_assets"":1237904,""2025_debt"":152226,'
    '""2025_fte"":18.8,""2025_kapitaalsubsidies"":21116,""2025_destin691"":0,'
    '""2025_cash"":912920,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":1065918,""2025_gebouwen22"":0,'
    '""2025_aanbouw27"":0,""2025_capex"":21456,'
    '""2025_fondsen10"":0,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":1064563,""2025_66A"":0,'
    '""2025_66B"":0,""2025_voorzieningen16"":0,""2025_76B"":0,'
    '""2024_omzet"":0,""2024_bruto9900"":1172805,""2024_73"":0,'
    '""2024_opbr"":1172805,""2024_pnl"":128777,""2024_bedrijfswinst"":116626,'
    '""2024_equity"":865241,""2024_assets"":1056395,'
    '""2024_debt"":191154,""2024_cash"":755507,""2024_fte"":20.9,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":17997,'
    '""2024_geldbeleggingen"":0}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},BKO GENK-OOST vzw YE2025 (bruto JUMP 1.28m / omzet+73 empty / pnl JUMP 217k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin BKO + leftover city_genk,VZW BKO GENK-OOST (KBO 0475.432.830; Actief; 2 VE zetel Reinpadstraat 169 + De Bonobo 2.160.424.877; RSZ2025 88.919; Kind en Gezin IBO De Apenstaart + De Bonobo),2026-05-11,2025,2025,1280713,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00112540.pdf,Public BKO dual of mined city_genk,Publish Opgroeien/stad/ouder matrix behind bruto 1.28m + why 70+73 empty + why 9901 JUMP 205k + pnl JUMP 217k + destin 0 + FTE DROP 18.8,{SRC_PDF},strong,Vlaanderen>Limburg>Genk>BKO_GENK_OOST>JR2025_statutory_L5,tick2417; Strong official native PDF; leftover city_genk after CAW Limburg / BWOL; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},BKO GENK-OOST bruto JUMP 1.28m / omzet+73 empty / pnl JUMP 217k / destin 0 (YE2025 Genk BKO),L5,cik_vzw_statutory,Vlaanderen>Limburg>Genk>BKO_GENK_OOST>JR2025,1280713,1280713,PDF bruto9900 JUMP 1280713 BKO envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst JUMP 205436; pnl JUMP 217320; equity JUMP 1085679; assets JUMP 1237904; debt DROP 152226; FTE DROP 18.8; kapitaalsubsidies JUMP 21116; destin691 empty; cash JUMP 912920; geldbeleggingen empty; gebouwen empty; 2 VE De Apenstaart + De Bonobo,strong,{SRC_PDF},Opgroeien + BKO leftover city_genk,Opgroeien Kind en Gezin + leftover city_genk,1.28m bruto JUMP; omzet+73 empty; 9901 JUMP 205k; pnl JUMP 217k; destin 0; leftover city_genk,5.32,5.24,5.16,5.22,FOI Opgroeien/stad/ouder matrix behind bruto 1.28m + why 70+73 empty + why 9901 JUMP 205k + pnl JUMP 217k + destin 0 + FTE DROP 18.8,active,,tick2417; Strong official NBB native PDF + Strong KBO; leftover city_genk after CAW Limburg / BWOL; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Limburg>Genk>BKO_GENK_OOST>BKO,{EID},Opgroeien/stad/ouder split behind bruto 1280713 and why 70+73 empty on VKT; why 9901 JUMP 205436 (was 116626) and pnl JUMP 217320 (was 128777); why destin 691 empty and 9905 217320 fully to overgedragen 14 1064563; why cash JUMP 912920 and debt DROP 152226 via 42/48 152226 and 45 133026; FTE 18.8 DROP; 2 VE; De Apenstaart + De Bonobo,Strong official PDF leftover public BKO of city_genk; 1.28m bruto; public BKO not private clinic; not Denderkind 0479.127.045; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW BKO GENK-OOST / Raad van Bestuur,info@deapenstaart.be,"Reinpadstraat 169, 3600 Genk",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2417; ready NOT sent; Strong official native NBB PDF; leftover city_genk BKO after CAW Limburg / BWOL; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
