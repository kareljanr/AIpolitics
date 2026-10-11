from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2440_stamp.txt").read_text().strip().splitlines()
EID="vzw_ukkies"
SRC_PDF="src_ukkies_jr2025_nbb_pdf_2440"
LB="lb_ukkies_bruto_5_13m_omzet73_empty_pnl_flat_309k_destin_flat_309k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},De Ukkies bruto JUMP 5.13m / omzet+73 empty / pnl FLAT 309k / destin FLAT 309k (YE2025 leftover city_hasselt CIK),L5,cik_vzw_statutory,Vlaanderen>Limburg>Hasselt>DeUkkies>JR2025,5126812,5126812,PDF 9900 5126812 envelope omzet empty; 73 empty; 76A 42695 JUMP; bedrijfswinst JUMP 300046; pnl FLAT 308628; equity JUMP 3995693; assets FLAT 4695584; debt DROP 699892; FTE 79.3 FLAT; kapitaalsubsidies DROP 705041; destin691 FLAT 308628 destin=pnl; cash JUMP 1065696; geldbeleggingen JUMP 1287959; gebouwen DROP 1766727; 3 VE Hasselt,strong,{SRC_PDF},Opgroeien + leftover city_hasselt,CIK+BOA kinderopvang + leftover city_hasselt,5.13m bruto envelope; 70+73 empty; 9901 300k JUMP; pnl FLAT 309k; destin FLAT 309k = pnl; leftover city_hasselt,5.35,3.85,5.00,5.20,FOI Opgroeien matrix behind bruto 5.13m + why 70+73 empty at 462 plaatsen + why destin 309k = pnl while cash JUMP 1.07m,active,,tick2440; Strong official NBB native PDF + Strong KBO; leftover mined city_hasselt after Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 3 VE Hasselt; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema",
])
print("leaderboard ok")
