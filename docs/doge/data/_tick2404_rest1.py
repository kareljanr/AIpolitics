#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2404_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_ter_eecken"
SRC_PDF = "src_tereecken_jr2025_nbb_pdf_2404"
COMM = "comm_tereecken_jr2025_statutory_bruto_3_72m_omzet73_empty_pnl_loss_widen"
LB = "lb_tereecken_bruto_3_72m_omzet73_empty_pnl_loss_widen_208k_jr2025"
GAP = "gap_tereecken_riziv_vl_matrix_bruto_3_72m_omzet73_empty_pnl_loss_widen_208k_l5"
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
    '"{""2025_omzet"":0,""2025_bruto9900"":3717716,""2025_73"":0,'
    '""2025_pnl"":-207524,""2025_bedrijfswinst"":-105938,'
    '""2025_equity"":3873571,""2025_assets"":6549101,""2025_debt"":2675530,'
    '""2025_fte"":42.3,""2025_kapitaalsubsidies"":3177969,""2025_destin691"":0,'
    '""2025_cash"":177912,""2025_geldbeleggingen"":180306,'
    '""2025_personnel62"":3515328,""2025_gebouwen22"":5824359,'
    '""2025_aanbouw27"":0,""2025_capex"":125324,""2025_bestemde13"":300000,'
    '""2025_overgedragen14"":395602,""2025_76A"":2800,""2025_630"":192110,'
    '""2025_66A"":102348,""2025_hyp91621"":400000,""2025_41recv"":696,'
    '""2024_bruto9900"":3443276,""2024_pnl"":-12939,""2024_bedrijfswinst"":-70103,'
    '""2024_equity"":4181780,""2024_assets"":7552374,""2024_debt"":3370594,'
    '""2024_kapitaalsubsidies"":3278654,""2024_cash"":151641,""2024_fte"":42.3,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":102153}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Ter Eecken vzw YE2025 (bruto JUMP 3.72m / omzet+73 empty / pnl LOSS WIDEN 208k / destin empty / Strong PDF),{EID},RIZIV + Departement Zorg CAR + leftover city_oudenaarde,VZW Ter Eecken (KBO 0432.465.392; Actief; 1 VE; RSZ2025 86.101; VAZG HCO 29586; RIZIV 96560332),2026-05-07,2025,2025,3717716,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00107832.pdf,Public CAR dual of mined city_oudenaarde,Publish RIZIV/VAZG/stad matrix behind bruto 3.72m + why 70/73 empty + pnl LOSS WIDEN 208k + destin empty + 41 recv collapse,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Oudenaarde>TerEecken>JR2025_statutory_L5,tick2404; Strong official native PDF; leftover city_oudenaarde after De Kade@2403; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952; NOT VERBINT 0408.032.379; NOT ARC 0408.434.930; NOT Heuvelheem 0413.210.201; NOT CAR Halle Asse 0425.788.230; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR Noorderkempen 0408.078.010 scan; NOT Antenne 3000 0433.184.479; NOT H.Hart Oudenaarde 0407.644.082; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},Ter Eecken bruto JUMP 3.72m / omzet+73 empty / pnl LOSS WIDEN 208k / destin empty (YE2025 Oudenaarde CAR),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Oudenaarde>TerEecken>JR2025,3717716,3717716,PDF bruto9900 JUMP 3717716 CAR envelope; omzet70 empty; 73 empty; 76A 2800; bedrijfswinst LOSS WIDEN -105938; pnl LOSS WIDEN -207524; equity DROP 3873571; assets DROP 6549101; debt DROP 2675530; FTE 42.3 FLAT; kapitaalsubsidies DROP 3177969; destin691 empty; cash JUMP 177912; geldbeleggingen JUMP 180306; gebouwen 5824359; aanbouw empty; capex 125324; personeel 62 3515328; 41 recv 696 was 1067374,strong,{SRC_PDF},RIZIV + CAR leftover city_oudenaarde,Departement Zorg + leftover city_oudenaarde,3.72m bruto JUMP; omzet+73 empty; pnl LOSS WIDEN 208k; destin empty; 41 recv collapse; leftover city_oudenaarde,5.4,5.3,5.2,5.30,FOI RIZIV/VAZG/stad matrix behind bruto 3.72m + why 70/73 empty + pnl LOSS WIDEN 208k + destin empty + 41 recv collapse,active,,tick2404; Strong official NBB native PDF + Strong KBO; leftover city_oudenaarde after De Kade@2403; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Oudenaarde>TerEecken>CAR,{EID},RIZIV/VAZG/stad split behind bruto 3717716 and why omzet 70 + 73 empty; why pnl LOSS WIDEN -207524 (was -12939) and 9901 LOSS WIDEN -105938 after personeel 3515328; why 691 empty; why 41 recv collapse 696 (was 1067374); why kapitaalsubsidies DROP 3177969 with capex 125324 and hypotheek 400000+manda at 1445000,Strong official PDF leftover public CAR of city_oudenaarde; 3.72m bruto; public CAR not private clinic; not De Kade 0413.650.659; not CFR Zelzate 0419.645.952; not VERBINT 0408.032.379; not ARC 0408.434.930; not Heuvelheem 0413.210.201; not CAR Halle Asse 0425.788.230; not Waas 0415.472.279; not CAR Accent 0413.208.122; not CAR Horizon 0418.529.759; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479; not H.Hart Oudenaarde 0407.644.082,8,Ter Eecken VZW / Raad van Bestuur,onthaal@cartereecken.be,"Vlaanderenstraat 2, 9700 Oudenaarde",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2404; ready NOT sent; Strong official native NBB PDF; leftover city_oudenaarde CAR after De Kade@2403; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
