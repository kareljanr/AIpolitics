from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2438_stamp.txt").read_text().strip().splitlines()
EID="vzw_de_wissel"
SRC_PDF="src_de_wissel_jr2025_nbb_pdf_2438"
COMM="comm_de_wissel_jr2025_statutory_opbr_8_58m_73_8_10m_pnl_jump_102k"
LB="lb_de_wissel_opbr_8_58m_73_8_10m_pnl_jump_102k_destin_200k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},De Wissel opbr JUMP 8.58m / 73 JUMP 8.10m / pnl JUMP 102k / destin JUMP 200k (YE2025 leftover city_leuven OVBJ),L5,ovbj_vzw_statutory,Vlaanderen>Vlaams-Brabant>Leuven>DeWissel>JR2025,8576450,8576450,PDF 70/76A 8576450 envelope omzet empty; 73 8101474; 76A 200; bruto empty VOL; bedrijfswinst JUMP 109342; pnl JUMP 101865; equity JUMP 3645083; assets JUMP 6189923; debt JUMP 2466620; FTE 82.7 JUMP; kapitaalsubsidies JUMP 1651366; destin691 JUMP 200000 destin>pnl; cash JUMP 656811; geldbeleggingen DROP empty; gebouwen JUMP 3467123; 1 VE Leuven,strong,{SRC_PDF},Opgroeien + leftover city_leuven,OVBJ jeugdhulp + leftover city_leuven,8.58m opbr envelope; 73 8.10m; 9901 109k JUMP; pnl JUMP 102k; destin JUMP 200k > pnl; leftover city_leuven,5.42,4.60,5.10,5.37,FOI Opgroeien matrix behind 73 8.10m + why destin 200k > pnl 102k + bouwprojecten gebouwen JUMP 3.47m,active,,tick2438; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after Monte Rosa / IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; 1 VE Leuven; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo",
])
print("leaderboard ok")
