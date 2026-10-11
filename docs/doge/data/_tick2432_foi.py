from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
EID="vzw_home_emmaus"
COMM="comm_home_emmaus_jr2025_statutory_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k"
LB="lb_home_emmaus_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k_destin_0_jr2025"
GAP="gap_home_emmaus_vaph_matrix_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k_destin_0_l5"
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
f"{GAP},Vlaanderen>Oost-Vlaanderen>Gent>HomeEmmaus>VAPH,{EID},VAPH/PVF/RTH split behind opbr 2230552 (omzet 70 279413 commercial-only vs 73 1951139); why 70 commercial-only while site lists Home + dagcentrum + DIO and VAPH-erkenning; why 9904 JUMP 270624 (was 226461 restated) and 9901 JUMP 193689 (was 141307); why destin 691 empty while overgedragen 14 2399832 absorbs all pnl and bestemde fondsen 13 stays 135000; why cash DROP 736197 (was 1017801) at geldbeleggingen JUMP 1841875 and capex 86283 and kapitaalsubsidies JUMP 27614 from empty; FTE 26.6 DROP (year-end 25.9); 1 VE Gent-Ledeberg; VAPH-afrekening geraamd,Strong official PDF leftover public VAPH of mined city_gent; 2.23m opbr; public VAPH not private clinic; 1 VE Gent-Ledeberg not city_aalter leftover; not Kloosterstraat 6 Drongen; not Emmaus AZ 0411.515.075; not Witje Wiebel 0443.654.937; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Elfenbankje 0417.638.151; not Vormingscentrum 0413.342.338; not Helan 0464.151.037; not Knuffelboom 0478.310.859; not De Zeppelin 0454.001.867; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Home Emmaus / Raad van Bestuur,boekhouding@dovencentrum-emmaus.be,\"Van den Heckestraat 41-43, 9050 Gent\",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2432; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_gent VAPH after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
