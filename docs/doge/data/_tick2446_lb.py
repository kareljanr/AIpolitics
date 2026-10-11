from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2446_stamp.txt").read_text().strip().splitlines()
EID="vzw_kinderkuren"
SRC_PDF="src_kinderkuren_jr2025_nbb_pdf_2446"
LB="lb_kinderkuren_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k_destin_drop_680k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},Kinderkuren bruto DROP 4.67m / omzet+73 empty VKT / pnl FLIP LOSS 618k / destin DROP 680k (YE2025 leftover city_leuven EVA),L5,eva_vzw_statutory,Vlaanderen>VlaamsBrabant>Leuven>Kinderkuren>JR2025,4674661,4674661,PDF 9900 4674661 envelope; omzet empty VKT; 73 empty VKT; 76A DROP 2432; bedrijfswinst FLIP -615411; pnl FLIP -617961; equity DROP 857351; assets DROP 1762362; debt DROP 905011; FTE 81.6 JUMP; kapitaalsubsidies empty; destin691 0 DROP (was 680000); cash JUMP 1417387; geldbeleggingen empty; 37 VE leftover city_leuven EVA,strong,{SRC_PDF},Opgroeien + leftover city_leuven EVA,EVA BKO + leftover city_leuven,4.67m bruto envelope; omzet+73 empty VKT; 9901 FLIP LOSS 615k; pnl FLIP LOSS 618k; destin DROP 680k; leftover city_leuven EVA,5.40,5.25,5.00,5.22,FOI Opgroeien/Stad Leuven matrix behind bruto 4.67m + why omzet+73 empty VKT + why pnl FLIP LOSS 618k while destin DROP 680k and FTE JUMP 12.7pct,active,,tick2446; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes / t Zonnetje; 37 VE EVA; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF IZW OFF Avida OFF Monte Rosa OFF De Wissel OFF De Slabbertjes OFF De Ukkies OFF De Hummeltjes OFF t Anemoontje OFF Jeugdhulp Don Bosco OFF Wigwam OFF t Zonnetje OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer OFF Konekt OFF Ter Engelen OFF Annuntiaten OFF MFC Combo OFF Grauwzusters convent OFF Jessa hospital special schema OFF Klein Hemelrijk remine OFF Pinnochio remine OFF Duinhuisjes VE t Anemoontje OFF VIA Don Bosco OFF De Speelboom Brussels",
])
print("leaderboard ok")
