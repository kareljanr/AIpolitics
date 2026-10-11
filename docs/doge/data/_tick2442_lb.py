from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
EID="vzw_anemoontje"
SRC_PDF="src_anemoontje_jr2025_nbb_pdf_2442"
LB="lb_anemoontje_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},t Anemoontje opbr JUMP 835k / omzet JUMP 137k commercial-only / 73 JUMP 698k / pnl JUMP 105k / destin JUMP 598k (YE2025 leftover city_leuven CIK),L5,cik_vzw_statutory,Vlaanderen>VlaamsBrabant>Leuven>Anemoontje>JR2025,834926,834926,PDF 70+73 834926 envelope; omzet 136595 commercial-only; 73 698331 JUMP; 76A empty; bruto JUMP 759661; bedrijfswinst JUMP 109330; pnl JUMP 105278; equity JUMP 1329241; assets JUMP 1575233; debt DROP 245992; FTE 8.1 DROP; kapitaalsubsidies DROP 515543; destin691 JUMP 598014 destin>>pnl; cash JUMP 332675; geldbeleggingen FLAT 250000; gebouwen DROP 898992; 1 VE Leuven,strong,{SRC_PDF},Opgroeien + leftover city_leuven,CIK kinderopvang + leftover city_leuven,835k opbr envelope; omzet 137k commercial-only vs 73 698k; 9901 109k JUMP; pnl JUMP 105k; destin JUMP 598k >> pnl; leftover city_leuven,5.35,3.90,5.00,5.19,FOI Opgroeien matrix behind opbr 835k + why omzet 137k commercial-only vs 73 698k + why destin JUMP 598k >> pnl 105k while overgedragen DROP 203k,active,,tick2442; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after De Hummeltjes / De Ukkies / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE Leuven; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje",
])
print("leaderboard ok")
