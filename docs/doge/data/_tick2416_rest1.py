#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2416_stamp.txt").read_text().strip().splitlines()
EID = "vzw_denderkind"
SRC_PDF = "src_denderkind_jr2025_nbb_pdf_2416"
COMM = "comm_denderkind_jr2025_statutory_bruto_3_96m_omzet73_empty_pnl_drop_25k"
LB = "lb_denderkind_bruto_3_96m_omzet73_empty_pnl_drop_25k_destin_0_jr2025"
GAP = "gap_denderkind_opgroeien_matrix_bruto_3_96m_omzet73_empty_pnl_drop_25k_destin_0_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":3957120,""2025_73"":0,'
    '""2025_76A"":0,""2025_opbr"":3957120,'
    '""2025_pnl"":25088,""2025_bedrijfswinst"":-17514,'
    '""2025_equity"":1896227,""2025_assets"":3918204,""2025_debt"":2021977,'
    '""2025_fte"":59.9,""2025_kapitaalsubsidies"":0,""2025_destin691"":0,'
    '""2025_cash"":1338704,""2025_geldbeleggingen"":0,'
    '""2025_personnel62"":3788253,""2025_gebouwen22"":2420068,'
    '""2025_aanbouw27"":0,""2025_capex"":805612,'
    '""2025_fondsen10"":0,""2025_bestemde13"":0,'
    '""2025_overgedragen14"":1896227,""2025_66A"":3034,'
    '""2025_66B"":13032,""2025_voorzieningen16"":0,""2025_76B"":63569,'
    '""2024_omzet"":0,""2024_bruto9900"":3824624,""2024_73"":0,'
    '""2024_opbr"":3824624,""2024_pnl"":244823,""2024_bedrijfswinst"":246160,'
    '""2024_equity"":1871139,""2024_assets"":3078743,'
    '""2024_debt"":1207604,""2024_cash"":783860,""2024_fte"":56.3,'
    '""2024_destin691"":0,""2024_kapitaalsubsidies"":0,'
    '""2024_geldbeleggingen"":300000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Denderkind vzw YE2025 (bruto JUMP 3.96m / omzet+73 empty / pnl DROP 25k / destin 0 / Strong PDF),{EID},Opgroeien + Kind en Gezin CIK+BKO + leftover city_aalst,VZW Denderkind (KBO 0479.127.045; Actief; 16 VE HQ 2.157.744.016 + 15 KDV-sites incl. Ede-kind 2.388.220.073; RSZ2025 88.911; 12 KDV + BKO),2026-03-19,2025,2025,3957120,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00065367.pdf,Public CIK+BKO dual of mined city_aalst,Publish Opgroeien/stad/ouder matrix behind bruto 3.96m + why 70+73 empty + why 9901 LOSS FLIP -18k + pnl DROP 25k + destin 0 + debt JUMP 67pct + FTE JUMP 59.9,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Aalst>Denderkind>JR2025_statutory_L5,tick2416; Strong official native PDF; leftover city_aalst after CAR De Hert; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Junior 0866.116.859; NOT Helan 0464.151.037; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Denderkind bruto JUMP 3.96m / omzet+73 empty / pnl DROP 25k / destin 0 (YE2025 Aalst CIK+BKO),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Aalst>Denderkind>JR2025,3957120,3957120,PDF bruto9900 JUMP 3957120 CIK envelope; omzet70 empty; 73 empty; 76A empty; bedrijfswinst LOSS FLIP -17514; pnl DROP 25088; equity JUMP 1896227; assets JUMP 3918204; debt JUMP 2021977; FTE JUMP 59.9; kapitaalsubsidies empty; destin691 empty; cash JUMP 1338704; geldbeleggingen DROP 0; gebouwen JUMP 2420068; 16 VE 12 KDV + BKO,strong,{SRC_PDF},Opgroeien + CIK+BKO leftover city_aalst,Opgroeien Kind en Gezin + leftover city_aalst,3.96m bruto JUMP; omzet+73 empty; 9901 LOSS FLIP; pnl DROP 25k; destin 0; leftover city_aalst,5.45,5.36,5.24,5.35,FOI Opgroeien/stad/ouder matrix behind bruto 3.96m + why 70+73 empty + why 9901 LOSS FLIP -18k + pnl DROP 25k + destin 0 + debt JUMP 67pct + FTE JUMP 59.9,active,,tick2416; Strong official NBB native PDF + Strong KBO; leftover city_aalst after CAR De Hert; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Aalst>Denderkind>CIK+BKO,{EID},Opgroeien/stad/ouder split behind bruto 3957120 and why 70+73 empty on VKT; why 9901 LOSS FLIP -17514 (was 246160) and pnl DROP 25088 (was 244823); why destin 691 empty and 9905 25088 fully to overgedragen 14 1896227; why cash JUMP 1338704 and debt JUMP 2021977 via 42/48 802710 and 45 511888; FTE 59.9 JUMP; 16 VE; 12 KDV + BKO,Strong official PDF leftover public CIK+BKO of city_aalst; 3.96m bruto; public CIK not private clinic; not Kinderopvang Mariawende 0411.611.184; not Buitenschoolse Opvang Ieper 0431.691.669; not Bengelhof 0455.442.813; not Kinderopvang Turnhout 0465.284.947; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Junior 0866.116.859; not Helan 0464.151.037; not Elfenbankje 0417.638.151; not t Eekhoorntje 0414.453.680; not 3Wplus 0893.870.539; not De Mereltjes 0412.778.352; not De Hoeksteen 0765.439.866; not Ter Eecken 0432.465.392; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not Vormingscentrum 0413.342.338; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Denderkind / Raad van Bestuur,info@denderkind.be,"Korte Zoutstraat 32 bus K, 9300 Aalst",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2416; ready NOT sent; Strong official native NBB PDF; leftover city_aalst CIK+BKO after CAR De Hert; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
