from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
EID="vzw_witje_wiebel"
COMM="comm_witje_wiebel_jr2025_statutory_bruto_1_88m_omzet73_empty_pnl_jump_301k"
LB="lb_witje_wiebel_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_jr2025"
GAP="gap_witje_wiebel_opgroeien_matrix_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_l5"
DRAFT=f"docs/doge/foi/drafts/{GAP}.md"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"foi_queue.csv", [
f"{GAP},Vlaanderen>Oost-Vlaanderen>Gent>WitjeWiebel>CIK,{EID},Opgroeien/ouderbijdragen split behind bruto 1878999 (omzet 70 empty + 73 empty VKT); why 70+73 empty while site lists 2 Gent campussen and Kinderopvangpunt Stad Gent; why 9904 JUMP 301158 (was 299585) and 9901 DROP 304658 (was 308105); why destin 691 300000 to bestemde fondsen 13 599585 while fondsen 10 stays 88712 and overgedragen 14 1059090; why cash JUMP 804896 (was 517039) at geldbeleggingen FLAT 650000 and gebouwen DROP 1134601 and capex 28703 and kapitaalsubsidies DROP 560470; FTE 25.3 FLAT (year-end 27); social balance 27 men / 0 women vs opleiding 30 women; 2 VE Gent Maria Middelares + Sint-Pieters; erfpacht Smidsestraat,Strong official PDF leftover public CIK of mined city_gent; 1.88m bruto; public Opgroeien CIK not private clinic; 2 VE both Gent not city_aalter leftover; not Kloosterstraat 6 Drongen; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Elfenbankje 0417.638.151; not Vormingscentrum 0413.342.338; not Helan 0464.151.037; not Duinhuisjes 0413.323.037; not t Bremhuisje 0445.265.533 stopgezet 1993; not Kinderlach 0450.275.186; not KISME 0894.549.440; not Kindercentrum 0408.226.775; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW KINDERDAGVERBLIJF WITJE WIEBEL / Raad van Bestuur,witje.wiebel@mijnziekenhuis.be,\"Kortrijksesteenweg 1020, 9000 Gent\",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2431; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_gent CIK after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
