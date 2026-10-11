from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2452_stamp.txt").read_text().strip().splitlines()
EID="vzw_harlekijntjes_tielt"
SRC_PDF="src_harlekijntjes_jr2025_nbb_pdf_2452"
LB="lb_harlekijntjes_bruto_1_90m_omzet73_empty_pnl_drop_144k_destin_jump_662k_jr2025"
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
"Harlekijntjes bruto JUMP 1.90m / omzet+73 empty VKT / pnl DROP 144k / destin JUMP 662k (YE2025 leftover city_tielt CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Tielt>Harlekijntjes>JR2025",
"1896924",
"1896924",
"PDF 9900 1896924 envelope; omzet empty VKT; 73 empty VKT; 76A JUMP 1700; bruto JUMP 1896924; bedrijfswinst DROP 136158; pnl DROP 144205; equity JUMP 1405811; assets JUMP 1693592; debt DROP 287780; FTE 27 DROP; kapitaalsubsidies DROP 203433; destin691 JUMP 661844; cash DROP 141324; geldbeleggingen JUMP 847580; 1 VE leftover city_tielt CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_tielt CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_tielt",
"1.90m bruto envelope; omzet+73 empty VKT; pnl DROP 144k; destin JUMP 662k; cash DROP 141k vs investments JUMP 848k; leftover city_tielt CIK",
"5.15",
"5.22",
"4.90",
"5.17",
"FOI Opgroeien matrix behind bruto 1.90m + why omzet+73 empty VKT + why destin JUMP 662k while cash DROP 141k and geldbeleggingen JUMP 848k and FTE DROP 27",
"active",
"",
"tick2452 leftover mined city_tielt CIK after Kinderdagverblijf De Hartjes Ninove different-KBO skip; 1 VE; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
