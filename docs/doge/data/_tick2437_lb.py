from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2437_stamp.txt").read_text().strip().splitlines()
EID="vzw_monte_rosa"
SRC_PDF="src_monte_rosa_jr2025_nbb_pdf_2437"
COMM="comm_monte_rosa_jr2025_statutory_opbr_5_42m_73_5_32m_pnl_jump_349k"
LB="lb_monte_rosa_opbr_5_42m_73_5_32m_pnl_jump_349k_destin_2_05m_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Monte Rosa opbr FLAT 5.42m / 73 JUMP 5.32m / pnl JUMP 349k / destin JUMP 2.05m (YE2025 leftover city_leuven OVBJ),L5,ovbj_vzw_statutory,Vlaanderen>Vlaams-Brabant>Leuven>MonteRosa>JR2025,5424143,5424143,PDF 70/76A 5424143 envelope omzet empty; 73 5323280; 76A empty; bruto empty VOL; bedrijfswinst JUMP 369456; pnl JUMP 348642; equity JUMP 5395536; assets JUMP 7358796; debt JUMP 1963260; FTE 63.0 DROP; kapitaalsubsidies DROP 1749682; destin691 JUMP 2050000 destin>>pnl; cash JUMP 823541; geldbeleggingen JUMP 1662593; gebouwen DROP 1478450; 4 VE Leuven+Herent+Deurne,strong,{SRC_PDF},Opgroeien + leftover city_leuven,OVBJ jeugdhulp + leftover city_leuven,5.42m opbr envelope; 73 5.32m; 9901 369k JUMP; pnl JUMP 349k; destin JUMP 2.05m >> pnl; leftover city_leuven,5.35,4.42,5.10,5.29,FOI Opgroeien matrix behind 73 5.32m + why destin 2.05m >> pnl 349k + bouwprojecten aanbouw 2.33m,active,,tick2437; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; also leftover mined city_herent + leftover mined city_antwerpen same KBO; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten",
])
print("leaderboard ok")
