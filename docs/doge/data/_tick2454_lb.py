from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2454_stamp.txt").read_text().strip().splitlines()
EID="vzw_medemens_kdv_antwerpen"
SRC_PDF="src_medemens_kdv_jr2025_nbb_pdf_2454"
LB="lb_medemens_kdv_opbr_9_55m_omzet_1_76m_73_7_57m_pnl_drop_500k_destin_jump_5_67m_jr2025"
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
"De Medemens Kinderdagverblijven opbr JUMP 9.55m / omzet JUMP 1.76m commercial-only / 73 JUMP 7.57m / pnl DROP 500k / destin JUMP 5.67m (YE2025 leftover city_antwerpen CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Antwerpen>MedemensKDV>JR2025",
"9548863",
"9548863",
"PDF 70/76A 9548863 envelope; omzet 1762950 commercial-only; 73 7571818; 76A 100810; bruto empty VOL; bedrijfswinst DROP 501545; pnl DROP 500404; equity JUMP 14533752; assets JUMP 16808555; debt JUMP 2186496; FTE 123.7 JUMP; kapitaalsubsidies DROP 3503975; destin691 JUMP 5672853; cash JUMP 3019243; geldbeleggingen FLAT 500000; 9 VE leftover city_antwerpen CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_antwerpen CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_antwerpen",
"9.55m opbr envelope; omzet 1.76m commercial-only vs 73 7.57m; pnl DROP 500k; destin JUMP 5.67m; leftover city_antwerpen CIK",
"5.25",
"5.45",
"5.00",
"5.28",
"FOI Opgroeien matrix behind opbr 9.55m + why omzet 1.76m commercial-only vs 73 7.57m + why pnl DROP 500k while destin JUMP 5.67m and cash JUMP 3.02m and FTE JUMP 123.7",
"active",
"",
"tick2454 leftover mined city_antwerpen CIK after OKO & ZO different-KBO skip; 9 VE; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")
