from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2453_stamp.txt").read_text().strip().splitlines()
EID="vzw_oko_zo_zele"
SRC_PDF="src_oko_zo_jr2025_nbb_pdf_2453"
LB="lb_oko_zo_bruto_914k_omzet73_empty_pnl_flip_15k_destin_empty_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
row = ",".join([
LB,
"OKO & ZO bruto DROP 914k / omzet+73 empty VKT / pnl FLIP LOSS 15k / destin empty (YE2025 leftover city_zele CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Zele>OKOZO>JR2025",
"914033",
"914033",
"PDF 9900 914033 envelope; omzet empty VKT; 73 empty VKT; 76A empty; bruto DROP 914033; bedrijfswinst FLIP LOSS -20522; pnl FLIP LOSS -15184; equity DROP 668157; assets DROP 858840; debt DROP 190683; FTE 14.2 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 419271; geldbeleggingen DROP 0; 2 VE leftover city_zele CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_zele CIK",
"Kind en Gezin-vergunde BKO + dienst opvanggezinnen leftover city_zele",
"914k bruto envelope; omzet+73 empty VKT; pnl FLIP LOSS 15k; destin empty; cash JUMP 419k vs investments DROP 65k; leftover city_zele CIK",
"5.05",
"5.06",
"4.90",
"5.04",
"FOI Opgroeien matrix behind bruto 914k + why omzet+73 empty VKT + why pnl FLIP LOSS 15k while destin empty and cash JUMP 419k and geldbeleggingen DROP 65k and FTE DROP 14.2",
"active",
"",
"tick2453 leftover mined city_zele CIK after KINDEROPVANG De Harlekijntjes different-KBO skip; 2 VE; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
