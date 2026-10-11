from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
EID="vzw_t_zonnetje"
SRC_PDF="src_zonnetje_jr2025_nbb_pdf_2445"
LB="lb_zonnetje_bruto_2_11m_omzet73_empty_pnl_drop_176k_destin_empty_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},t Zonnetje bruto JUMP 2.11m / omzet+73 empty VKT / pnl DROP 176k / destin empty (YE2025 leftover city_waregem + city_kruisem CIK),L5,cik_vzw_statutory,Vlaanderen>OostVlaanderen>Waregem>tZonnetje>JR2025,2113971,2113971,PDF 9900 2113971 envelope; omzet empty VKT; 73 empty VKT; 76A JUMP 10445; bedrijfswinst DROP 158114; pnl DROP 175969; equity JUMP 1652293; assets JUMP 2101178; debt JUMP 448885; FTE 30.5 JUMP; kapitaalsubsidies DROP 213065; destin691 empty; cash DROP 279435; geldbeleggingen JUMP 900000; 3 VE Waregem+Kruisem+Nazareth-De Pinte,strong,{SRC_PDF},Opgroeien + leftover city_waregem + leftover city_kruisem,CIK + leftover city_waregem + leftover city_kruisem,2.11m bruto envelope; omzet+73 empty VKT; 9901 158k DROP; pnl DROP 176k; destin empty; leftover city_waregem + city_kruisem,5.35,5.20,5.00,5.18,FOI Opgroeien matrix behind bruto 2.11m + why omzet+73 empty VKT + why pnl DROP 176k while destin empty and cash DROP 54pct while beleggingen JUMP 900k,active,,tick2445; Strong official NBB native PDF + Strong KBO; leftover mined city_waregem after Kindercentrum + leftover mined city_kruisem after Wigwam / Jeugdhulp Don Bosco; 3 VE; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Jeugdhulp Don Bosco OFF Wigwam OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco",
])
print("leaderboard ok")
