from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2441_stamp.txt").read_text().strip().splitlines()
EID="vzw_hummeltjes"
SRC_PDF="src_hummeltjes_jr2025_nbb_pdf_2441"
LB="lb_hummeltjes_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},De Hummeltjes opbr JUMP 13.11m / omzet JUMP 1.40m commercial-only / 73 JUMP 11.28m / pnl DROP 259k / destin DROP 70k (YE2025 leftover city_hasselt CIK),L5,cik_vzw_statutory,Vlaanderen>Limburg>Hasselt>DeHummeltjes>JR2025,13105742,13105742,PDF 70/76A 13105742 envelope; omzet 1401475 commercial-only; 73 11277795 JUMP; 76A 57881 DROP; bedrijfswinst DROP 247462; pnl DROP 259329; equity JUMP 5708548; assets JUMP 9784745; debt JUMP 3968488; FTE 152.9 JUMP; kapitaalsubsidies DROP 2662209; destin691 DROP 70000 destin<pnl; cash JUMP 2100999; geldbeleggingen JUMP 500000; gebouwen DROP 5417866; 13 VE zetel Hasselt,strong,{SRC_PDF},Opgroeien + leftover city_hasselt,CIK+BOA+CKG kinderopvang + leftover city_hasselt,13.11m opbr envelope; omzet 1.40m commercial-only vs 73 11.28m; 9901 247k DROP; pnl DROP 259k; destin DROP 70k < pnl; leftover city_hasselt,5.42,4.15,5.00,5.36,FOI Opgroeien matrix behind opbr 13.11m + why omzet 1.40m commercial-only vs 73 11.28m + why pnl DROP 259k and destin DROP 70k while cash JUMP 2.10m,active,,tick2441; Strong official NBB native PDF + Strong KBO; leftover mined city_hasselt after De Ukkies / Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 13 VE zetel Hasselt; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine",
])
print("leaderboard ok")
