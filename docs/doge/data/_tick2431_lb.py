from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
EID="vzw_witje_wiebel"
SRC_PDF="src_witje_wiebel_jr2025_nbb_pdf_2431"
COMM="comm_witje_wiebel_jr2025_statutory_bruto_1_88m_omzet73_empty_pnl_jump_301k"
LB="lb_witje_wiebel_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_jr2025"
GAP="gap_witje_wiebel_opgroeien_matrix_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_l5"
DRAFT=f"docs/doge/foi/drafts/{GAP}.md"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Witje Wiebel bruto FLAT 1.88m / omzet+73 empty / pnl JUMP 301k / destin 300k (YE2025 leftover city_gent CIK),L5,cik_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>WitjeWiebel>JR2025,1878999,1878999,PDF omzet 70 empty VKT (73 empty; 76A empty); bruto 1878999 envelope; bedrijfswinst DROP 304658; pnl JUMP 301158; equity JUMP 2307857; assets JUMP 2843864; debt DROP 536007; FTE 25.3; kapitaalsubsidies DROP 560470; destin691 300000; cash JUMP 804896; geldbeleggingen FLAT 650000; gebouwen DROP 1134601; aanbouw empty; 2 VE Gent Maria Middelares + Sint-Pieters,strong,{SRC_PDF},Opgroeien + leftover city_gent,Opgroeien CIK + leftover city_gent,1.88m bruto; 70+73 empty; 9901 305k DROP; pnl JUMP 301k; destin 300k; leftover city_gent,5.18,3.55,5.05,5.17,FOI Opgroeien/ouderbijdragen matrix behind bruto 1.88m + why 70+73 empty vs 2 Gent campussen + why destin 300k of 301k pnl + FTE 25.3,active,,tick2431; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993",
])
print("leaderboard ok")
