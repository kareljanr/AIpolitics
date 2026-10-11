from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2435_stamp.txt").read_text().strip().splitlines()
EID="vzw_izw_leuven"
SRC_PDF="src_izw_jr2025_nbb_pdf_2435"
COMM="comm_izw_jr2025_statutory_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k"
LB="lb_izw_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k_destin_35k_jr2025"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"leaderboard.csv", [
f"{LB},IZW opbr DROP 1.33m / omzet JUMP 530k commercial-only / 73 DROP 803k / pnl DROP 10k / destin 35k (YE2025 leftover city_leuven VAPH),L5,vaph_vzw_statutory,Vlaanderen>Vlaams-Brabant>Leuven>IZW>JR2025,1333228,1333228,PDF omzet 70 530078 commercial-only vs large 73 802987; 76A 163; 70+73+76A 1333228 envelope; bruto DROP 815478 VKT; bedrijfswinst DROP 5047; pnl DROP 10323; equity JUMP 867134; assets DROP 1468447; debt DROP 601313; FTE 17.3 JUMP; kapitaalsubsidies empty; destin691 JUMP 35000; cash DROP 1444638; geldbeleggingen empty; gebouwen empty; 66A 62904; 3 VE Leuven+Grimbergen,strong,{SRC_PDF},VAPH + leftover city_leuven,VAPH ADL + leftover city_leuven,1.33m opbr; 70 commercial-only vs 73 803k; 9901 5k DROP; pnl DROP 10k; destin 35k > pnl; leftover city_leuven,5.38,3.12,5.00,5.20,FOI VAPH/Vlaams/Leuven/Grimbergen matrix behind opbr 1.33m + why 70 commercial-only vs large 73 + why destin 35k of 10k pnl + why 66A 63k vakantiegeld,active,,tick2435; Strong official NBB native PDF + Strong KBO; leftover mined city_leuven after Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf / MFC Combo; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Huize Zonnelied OFF OLV Gasthuis Poperinge OFF WZC De Linde Wortegem-Petegem OFF Kindercentrum OFF KISME OFF Duinhuisjes OFF Windekind OFF Beregoed OFF Witje Wiebel OFF Home Emmaus OFF WZC Sint-Coleta Gent OFF Ferm Kinderopvang OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal OFF Curando OFF De Linde Ronse YE2024 OFF Kinderlach YE2024 OFF t Bremhuisje stopgezet 1993 OFF Knuffelboom no NBB OFF De Zeppelin no JR OFF Emmaus AZ OFF De Foyer",
])
print("leaderboard ok")
