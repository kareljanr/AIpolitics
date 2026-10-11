from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
EID="vzw_home_emmaus"
SRC_PDF="src_home_emmaus_jr2025_nbb_pdf_2432"
COMM="comm_home_emmaus_jr2025_statutory_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k"
LB="lb_home_emmaus_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k_destin_0_jr2025"
GAP="gap_home_emmaus_vaph_matrix_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k_destin_0_l5"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Home Emmaus opbr JUMP 2.23m / omzet 279k commercial-only / 73 JUMP 1.95m / pnl JUMP 271k / destin 0 (YE2025 leftover city_gent VAPH),L5,vaph_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>HomeEmmaus>JR2025,2230552,2230552,PDF omzet 70 279413 commercial-only vs large 73 1951139; 76A 0; opbr 2230552 envelope; bruto 2086695; bedrijfswinst JUMP 193689; pnl JUMP 270624; equity JUMP 2562446; assets JUMP 2911569; debt JUMP 349123; FTE 26.6 DROP; kapitaalsubsidies JUMP 27614; destin691 empty; cash DROP 736197; geldbeleggingen JUMP 1841875; gebouwen empty; aanbouw empty; 1 VE Gent-Ledeberg,strong,{SRC_PDF},VAPH + leftover city_gent,VAPH dagcentrum + leftover city_gent,2.23m opbr; 70 commercial-only vs 73 1.95m; 9901 194k JUMP; pnl JUMP 271k; destin 0; leftover city_gent,5.20,3.68,5.05,5.21,FOI VAPH/PVF/RTH matrix behind opbr 2.23m + why 70 commercial-only vs large 73 + why destin 0 of 271k pnl + FTE 26.6 DROP,active,,tick2432; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ",
])
print("leaderboard ok")
