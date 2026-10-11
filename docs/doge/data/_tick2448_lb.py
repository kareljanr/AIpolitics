from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2448_stamp.txt").read_text().strip().splitlines()
EID="vzw_peutertuinen_go_mariakerke"
SRC_PDF="src_peutertuinen_jr2025_nbb_pdf_2448"
LB="lb_peutertuinen_bruto_872k_omzet73_empty_pnl_jump_115k_destin_empty_jr2025"
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
"Peutertuinen GO Mariakerke bruto DROP 872k / omzet+73 empty VKT / pnl JUMP 115k / destin empty (YE2025 leftover city_gent CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>OostVlaanderen>Gent>PeutertuinenGOMariakerke>JR2025",
"872268",
"872268",
"PDF 9900 872268 envelope; omzet empty VKT; 73 empty VKT; 76A DROP 0; bedrijfswinst JUMP 126095; pnl JUMP 115219; equity JUMP 1316171; assets JUMP 1658146; debt JUMP 341975; FTE 13.7 DROP; kapitaalsubsidies JUMP 491875; destin691 empty FLAT; cash DROP 550474; geldbeleggingen empty; aanbouw JUMP 627877; 2 VE leftover city_gent CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_gent CIK",
"Kind en Gezin-vergunde groepsopvang GO! + leftover city_gent",
"872k bruto envelope; omzet+73 empty VKT; 9901 JUMP 126k; pnl JUMP 115k; destin empty; leftover city_gent CIK",
"5.20",
"4.70",
"4.90",
"5.03",
"FOI Opgroeien matrix behind bruto 872k + why omzet+73 empty VKT + why pnl JUMP 115k while destin empty and aanbouw JUMP 628k",
"active",
"",
"tick2448 leftover mined city_gent CIK after Avida; 2 VE; NOT Mini-creches GO Next remine; NOT Stad Gent peutertuinen; NOT Villa Boempatat YE2024; NOT COB Annuntiaten remine; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
