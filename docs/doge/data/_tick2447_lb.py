from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2447_stamp.txt").read_text().strip().splitlines()
EID="vzw_cob_annuntiaten_heverlee"
SRC_PDF="src_cobah_jr2025_nbb_pdf_2447"
LB="lb_cobah_bruto_2_46m_omzet73_empty_pnl_drop_199k_destin_empty_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
print("lb helper ready", STAMP)

row = ",".join([
LB,
"COB Annuntiaten Heverlee bruto DROP 2.46m / omzet+73 empty VKT / pnl DROP 199k / destin empty (YE2025 leftover city_leuven CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>VlaamsBrabant>Leuven>COBAnnuntiatenHeverlee>JR2025",
"2462444",
"2462444",
"PDF 9900 2462444 envelope; omzet empty VKT; 73 empty VKT; 76A JUMP 3698; bedrijfswinst DROP 12020; pnl DROP 8845; equity DROP 2993102; assets JUMP 4525424; debt JUMP 1532322; FTE 43.5 JUMP; kapitaalsubsidies DROP 1792722; destin691 empty FLAT; cash JUMP 433864; geldbeleggingen empty; 4 VE leftover city_leuven CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_leuven CIK",
"Kind en Gezin-vergunde groepsopvang + leftover city_leuven",
"2.46m bruto envelope; omzet+73 empty VKT; 9901 DROP 12k; pnl DROP 199k; destin empty; leftover city_leuven CIK",
"5.25",
"4.90",
"4.90",
"5.02",
"FOI Opgroeien matrix behind bruto 2.46m + why omzet+73 empty VKT + why pnl DROP 199k while destin empty and FTE JUMP 10.1pct",
"active",
"",
"tick2447 leftover mined city_leuven CIK after Kinderkuren; 4 VE; NOT WZC Annuntiaten remine; NOT Kinderkuren; NOT Kinderdagverblijven Leuven absorbed; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
