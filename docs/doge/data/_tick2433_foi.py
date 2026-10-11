from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2433_stamp.txt").read_text().strip().splitlines()
EID="vzw_wzc_sint_coleta_gent"
COMM="comm_sint_coleta_jr2025_statutory_omzet_5_61m_73_983k_pnl_drop_75k"
LB="lb_sint_coleta_omzet_5_61m_73_983k_pnl_drop_75k_destin_0_jr2025"
GAP="gap_sint_coleta_wzc_matrix_omzet_5_61m_73_983k_pnl_drop_75k_destin_0_l5"
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
f"{GAP},Vlaanderen>Oost-Vlaanderen>Gent>WZCSintColeta>WZC,{EID},RIZIV/Vlaams/stad Gent/VIPA split behind omzet 5614657 (70 envelope not commercial-only vs 73 982687); why 73 DROP 982687 (733 956206) while 70 JUMP 5614657; why 9904 DROP 75406 (was 194096) and 9901 DROP 69308 (was 192776); why destin 691 empty while overgedragen 14 1890348 absorbs all pnl and bestemde fondsen 13 stays 425746; why cash JUMP 478451 at geldbeleggingen JUMP 650876 and capex 136286 and gebouwen DROP 2042258; FTE 66.8 JUMP (year-end 88); 1 VE Gent; WZC-afrekening geraamd,Strong official PDF leftover public WZC of mined city_gent; 5.61m omzet; public RVT not private clinic; 1 VE Gent not city_aalter leftover; not Kloosterstraat 6 Drongen; not Home Emmaus 0451.749.190; not De Foyer 0413.796.456; not Emmaus AZ 0411.515.075; not Witje Wiebel 0443.654.937; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Elfenbankje 0417.638.151; not Vormingscentrum 0413.342.338; not Helan 0464.151.037; not Knuffelboom 0478.310.859; not De Zeppelin 0454.001.867; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Woon- en Zorgcentrum Sint-Coleta Gent / Raad van Bestuur,info@sintcoleta.be,\"Sint-Coletastraat 4, 9000 Gent\",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2433; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_gent WZC after Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
