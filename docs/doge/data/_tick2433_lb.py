from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2433_stamp.txt").read_text().strip().splitlines()
EID="vzw_wzc_sint_coleta_gent"
SRC_PDF="src_sint_coleta_jr2025_nbb_pdf_2433"
COMM="comm_sint_coleta_jr2025_statutory_omzet_5_61m_73_983k_pnl_drop_75k"
LB="lb_sint_coleta_omzet_5_61m_73_983k_pnl_drop_75k_destin_0_jr2025"
GAP="gap_sint_coleta_wzc_matrix_omzet_5_61m_73_983k_pnl_drop_75k_destin_0_l5"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},WZC Sint-Coleta Gent omzet JUMP 5.61m / 73 DROP 983k / pnl DROP 75k / destin 0 (YE2025 leftover city_gent WZC),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>WZCSintColeta>JR2025,5614657,5614657,PDF omzet 70 5614657 envelope not commercial-only vs 73 982687; 76A 70552; 70/76A 6796611; bruto empty VOL; bedrijfswinst DROP 69308; pnl DROP 75406; equity JUMP 2789036; assets DROP 4673967; debt DROP 1884932; FTE 66.8 JUMP; kapitaalsubsidies DROP 173334; destin691 empty; cash JUMP 478451; geldbeleggingen JUMP 650876; gebouwen DROP 2042258; aanbouw 0; 1 VE Gent,strong,{SRC_PDF},Departement Zorg + leftover city_gent,WZC RVT + leftover city_gent,5.61m omzet; 73 DROP 983k; 9901 69k DROP; pnl DROP 75k; destin 0; leftover city_gent,5.24,3.90,5.00,5.28,FOI RIZIV/Vlaams/stad Gent/VIPA matrix behind omzet 5.61m + why 73 DROP + why destin 0 of 75k pnl + FTE 66.8 JUMP,active,,tick2433; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer",
])
print("leaderboard ok")
