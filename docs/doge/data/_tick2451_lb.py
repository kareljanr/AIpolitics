from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2451_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_ninove"
SRC_PDF="src_hartjes_ninove_jr2025_nbb_pdf_2451"
LB="lb_hartjes_ninove_bruto_484k_omzet73_empty_pnl_jump_31k_destin_empty_jr2025"
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
"Hartjes Ninove bruto JUMP 484k / omzet+73 empty VKT / pnl JUMP 31k / destin empty (YE2025 leftover city_ninove CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Ninove>HartjesNinove>JR2025",
"483796",
"483796",
"PDF 9900 483796 envelope; omzet empty VKT; 73 empty VKT; 76A empty; bruto JUMP 483796; bedrijfswinst FLIP PROFIT 21273; pnl JUMP 31142; equity JUMP 437479; assets JUMP 478634; debt DROP 41156; FTE 8.2 DROP; kapitaalsubsidies DROP 27420; destin691 empty FLAT; cash JUMP 391809; geldbeleggingen empty; 1 VE leftover city_ninove CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_ninove CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_ninove",
"484k bruto envelope; omzet+73 empty VKT; 9901 FLIP PROFIT 21k; pnl JUMP 31k; destin empty; leftover city_ninove CIK",
"5.05",
"4.50",
"4.90",
"4.98",
"FOI Opgroeien matrix behind bruto 484k + why omzet+73 empty VKT + why pnl JUMP 31k destin empty while cash JUMP 392k and FTE DROP 8.2",
"active",
"",
"tick2451 leftover mined city_ninove CIK after Groepsopvang De Hartjes Tienen different-KBO skip; 1 VE; NOT De Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
