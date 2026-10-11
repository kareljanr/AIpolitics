from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2444_stamp.txt").read_text().strip().splitlines()
EID="vzw_wigwam"
SRC_PDF="src_wigwam_jr2025_nbb_pdf_2444"
LB="lb_wigwam_bruto_1_07m_omzet73_empty_pnl_drop_36_destin_jump_150k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Wigwam bruto JUMP 1.07m / omzet+73 empty VKT / pnl DROP 36 / destin JUMP 150k (YE2025 leftover city_leuven CIK),L5,cik_vzw_statutory,Vlaanderen>VlaamsBrabant>Leuven>Wigwam>JR2025,1068827,1068827,PDF 9900 1068827 envelope; omzet empty VKT; 73 empty VKT; 76A JUMP 22522; bedrijfswinst DROP 26727; pnl DROP 36; equity DROP 896597; assets DROP 2053811; debt DROP 1157214; FTE 18.6 JUMP; kapitaalsubsidies DROP 644459; destin691 JUMP 149849 destin>>pnl; cash JUMP 207008; geldbeleggingen empty; gebouwen DROP 1739199; 1 VE Leuven 45 plaatsen,strong,{SRC_PDF},Opgroeien + leftover city_leuven,CIK + leftover city_leuven,1.07m bruto envelope; omzet+73 empty VKT; 9901 27k DROP; pnl DROP 36; destin JUMP 150k >> pnl; leftover city_leuven,5.40,5.10,5.00,5.17,FOI Opgroeien matrix behind bruto 1.07m + why omzet+73 empty VKT + why pnl DROP to 36 while destin JUMP 150k and FTE JUMP 18.6,active,,tick2444; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after Jeugdhulp Don Bosco / t Anemoontje / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE Leuven; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Jeugdhulp Don Bosco OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco",
])
print("leaderboard ok")
