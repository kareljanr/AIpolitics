from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
EID="vzw_avida"
SRC_PDF="src_avida_jr2025_nbb_pdf_2436"
COMM="comm_avida_jr2025_statutory_omzet_42_86m_73_11_55m_pnl_drop_784k"
LB="lb_avida_omzet_42_86m_73_11_55m_pnl_drop_784k_destin_0_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Avida omzet JUMP 42.86m / 73 JUMP 11.55m / pnl DROP 784k / destin 0 (YE2025 leftover city_gent WZC),L5,wzc_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Gent>Avida>JR2025,42857494,42857494,PDF omzet 70 42857494 envelope not commercial-only vs 73 11552982; 76A 37803; 70/76A 55138086; bruto empty VOL; bedrijfswinst DROP -484969; pnl DROP -784162; equity JUMP 32531263; assets JUMP 67049389; debt JUMP 34448367; FTE 624.2 JUMP; kapitaalsubsidies JUMP 10271770; destin691 empty; cash JUMP 6847926; geldbeleggingen DROP 0; gebouwen JUMP 43981165; 7 VE Gent+Lochristi+Damme+Beveren; Conecto merger 01.01.2025,strong,{SRC_PDF},Departement Zorg + leftover city_gent,RVT/ROB + leftover city_gent,42.86m omzet envelope; 73 11.55m; 9901 -485k DROP; pnl DROP 784k consecutive losses; destin empty; leftover city_gent,5.42,4.28,5.00,5.47,FOI Zorg/RIZIV/steden matrix behind omzet 42.86m + 73 11.55m + why consecutive losses 784k + why destin empty + Conecto merger opening,active,,tick2436; Strong official NBB native PDF + Strong KBO; leftover mined city_gent after IZW / Ferm Kinderopvang / WZC Sint-Coleta Gent / Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer",
])
print("leaderboard ok")
