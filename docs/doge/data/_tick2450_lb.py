from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2450_stamp.txt").read_text().strip().splitlines()
EID="vzw_hartjes_tienen"
SRC_PDF="src_hartjes_jr2025_nbb_pdf_2450"
LB="lb_hartjes_opbr_1_59m_omzet_252k_73_1_34m_pnl_jump_154k_destin_jump_154k_jr2025"
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
"Hartjes Tienen opbr JUMP 1.59m / omzet DROP 252k commercial-only / 73 JUMP 1.34m / pnl JUMP 154k / destin JUMP 154k (YE2025 leftover city_tienen CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Tienen>Hartjes>JR2025",
"1593834",
"1593834",
"PDF 70/76A 1593834 envelope; omzet 251750 commercial-only; 73 1342084 subsidies; 76A empty DROP; bruto JUMP 1447874; bedrijfswinst JUMP 147753; pnl JUMP 154432; equity JUMP 511958; assets JUMP 695457; debt DROP 183499; FTE 20.6 FLAT; kapitaalsubsidies empty DROP; destin691 JUMP 154432 destin=pnl; cash JUMP 174846; geldbeleggingen FLAT 250000; 1 VE leftover city_tienen CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_tienen CIK",
"Kind en Gezin-vergunde groepsopvang 74 plaatsen leftover city_tienen",
"1.59m opbr envelope; omzet 252k commercial-only; 73 1.34m; 9901 JUMP 148k; pnl JUMP 154k; destin JUMP 154k destin=pnl; leftover city_tienen CIK",
"5.10",
"5.20",
"4.90",
"5.16",
"FOI Opgroeien matrix behind opbr 1.59m + why omzet 252k commercial-only vs 73 1.34m + why pnl JUMP 154k destin=pnl while cash JUMP 175k and debt DROP 183k",
"active",
"",
"tick2450 leftover mined city_tienen CIK after De Wissel Tienen-site same-KBO skip; 1 VE; NOT De Hartjes Ninove remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
