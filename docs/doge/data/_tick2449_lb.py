from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2449_stamp.txt").read_text().strip().splitlines()
EID="vzw_familia_genk"
SRC_PDF="src_familia_jr2025_nbb_pdf_2449"
LB="lb_familia_opbr_7_57m_omzet_1_25m_73_6_23m_pnl_jump_645k_destin_jump_462k_jr2025"
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
"Familia Genk opbr JUMP 7.57m / omzet JUMP 1.25m commercial-only / 73 JUMP 6.23m / pnl JUMP 645k / destin JUMP 462k (YE2025 leftover city_genk CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Limburg>Genk>Familia>JR2025",
"7571995",
"7571995",
"PDF 70/76A 7571995 envelope; omzet 1249649 commercial-only; 73 6232638 subsidies; 76A DROP 26485; bedrijfswinst JUMP 642132; pnl JUMP 645105; equity JUMP 4554709; assets JUMP 5674553; debt DROP 1065188; FTE 103.5 JUMP; kapitaalsubsidies DROP 1169221; destin691 JUMP 462255; cash DROP 256788; geldbeleggingen JUMP 1334280; 1 VE leftover city_genk CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_genk CIK",
"Kind en Gezin-vergunde groepsopvang + BKO + CIK inclusief + leftover city_genk",
"7.57m opbr envelope; omzet 1.25m commercial-only; 73 6.23m; 9901 JUMP 642k; pnl JUMP 645k; destin JUMP 462k; leftover city_genk CIK",
"5.45",
"5.25",
"4.90",
"5.22",
"FOI Opgroeien matrix behind opbr 7.57m + why omzet 1.25m commercial-only vs 73 6.23m + why pnl JUMP 645k while destin JUMP 462k and geldbeleggingen JUMP 1.33m",
"active",
"",
"tick2449 leftover mined city_genk CIK after BKO GENK-OOST; 1 VE; NOT BKO GENK-OOST remine; NOT Peutertuinen GO Mariakerke remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
