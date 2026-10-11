from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
EID="vzw_slabbertjes"
SRC_PDF="src_slabbertjes_jr2025_nbb_pdf_2439"
COMM="comm_slabbertjes_jr2025_statutory_bruto_520k_pnl_drop_48k_destin_jump_375k"
LB="lb_slabbertjes_bruto_520k_omzet73_empty_pnl_drop_48k_destin_jump_375k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},De Slabbertjes bruto DROP 520k / omzet+73 empty / pnl DROP 48k / destin JUMP 375k (YE2025 leftover city_leuven CIK),L5,cik_vzw_statutory,Vlaanderen>Vlaams-Brabant>Leuven>DeSlabbertjes>JR2025,519885,519885,PDF 9900 519885 envelope omzet empty; 73 empty; 76A 2808 DROP; bedrijfswinst DROP 47360; pnl DROP 48280; equity JUMP 599876; assets JUMP 662430; debt DROP 62554; FTE 10.6 JUMP; kapitaalsubsidies DROP 71963; destin691 JUMP 375400 destin>>pnl; cash DROP 138351; geldbeleggingen JUMP 257760; gebouwen DROP 208808; 1 VE Leuven,strong,{SRC_PDF},Opgroeien + leftover city_leuven,CIK kinderopvang + leftover city_leuven,520k bruto envelope; 70+73 empty; 9901 47k DROP; pnl DROP 48k; destin JUMP 375k >> pnl; leftover city_leuven,5.30,3.80,5.00,5.18,FOI Opgroeien matrix behind bruto 520k + why destin 375k >> pnl 48k + cash DROP while geldbeleggingen JUMP 258k,active,,tick2439; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf; 1 VE Leuven; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent",
])
print("leaderboard ok")
