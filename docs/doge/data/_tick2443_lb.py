from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
EID="vzw_jeugdhulp_don_bosco"
SRC_PDF="src_jdbv_jr2025_nbb_pdf_2443"
LB="lb_jdbv_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k_destin_drop_6_56m_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Jeugdhulp Don Bosco Vlaanderen opbr JUMP 29.16m / omzet JUMP 208k commercial-only / 73 JUMP 27.79m / pnl DROP 830k / destin DROP 6.56m (YE2025 leftover city_eeklo jeugdhulp),L5,jeugdhulp_vzw_statutory,Vlaanderen>OostVlaanderen>Eeklo>JeugdhulpDonBosco>JR2025,29159144,29159144,PDF 70/76A 29159144 envelope; omzet 207924 commercial-only; 73 27785881 JUMP; 76A 671098 JUMP Mortsel sale; bruto empty VOL; bedrijfswinst DROP 821772; pnl DROP 830135; equity JUMP 24731057; assets JUMP 33372760; debt JUMP 8641703; FTE 342 JUMP; kapitaalsubsidies DROP 7796340; destin691 DROP 830135 destin=pnl; cash JUMP 3303716; geldbeleggingen JUMP 12671844; gebouwen DROP 7430623; commissaris voorbehoud 2017-inbreng MVA; 17 VE 2/17 Eeklo,strong,{SRC_PDF},Opgroeien + leftover city_eeklo,Jeugdhulp + leftover city_eeklo,29.16m opbr envelope; omzet 208k commercial-only vs 73 27.79m; 9901 822k DROP; pnl DROP 830k; destin DROP 6.56m to 830k = pnl; leftover city_eeklo,5.60,6.10,5.00,5.56,FOI Opgroeien matrix behind opbr 29.16m + why omzet 208k commercial-only vs 73 27.79m + why destin DROP 6.56m to 830k = pnl + commissaris voorbehoud 2017-inbreng MVA 474k,active,,tick2443; Strong official NBB native PDF + Strong KBO; leftover mined city_eeklo after m-accent / Ascendere; 17 VE 2/17 Eeklo; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco",
])
print("leaderboard ok")
