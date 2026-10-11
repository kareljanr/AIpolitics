from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
EID="vzw_avida"
COMM="comm_avida_jr2025_statutory_omzet_42_86m_73_11_55m_pnl_drop_784k"
LB="lb_avida_omzet_42_86m_73_11_55m_pnl_drop_784k_destin_0_jr2025"
GAP="gap_avida_wzc_matrix_omzet_42_86m_73_11_55m_pnl_drop_784k_destin_0_l5"
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
f"{GAP},Vlaanderen>Oost-Vlaanderen>Gent>Avida>WZC,{EID},Zorg/RIZIV/steden split behind omzet 42857494 (envelope not commercial-only vs 73 11552982) and 73 11552982 (733 11521960); why statutory omzet JUMP +119.55% while pro-forma combined +1.77%; why 9904 DROP -784162 (was -415792; consecutive losses) and 9901 DROP -484969 (was -253696) while 70/76A JUMP 55138086; why destin 691 empty while 791 onttrekking 1094294 and fondsen 10 JUMP 12928239; why geldbeleggingen 50/53 emptied 4000000 to 0 while cash JUMP 6847926; Conecto 0433.961.964 merger opening 01.01.2025 + Exalta rename 11.12.2024; FTE 624.2 JUMP; 7 VE Gent+Lochristi+Damme+Beveren; kapitaalsubsidies JUMP 10271770,Strong official PDF leftover public WZC of mined city_gent; 42.86m omzet envelope; public RVT/ROB not private clinic; 7 VE Gent+Lochristi+Damme+Beveren not city_aalter leftover; not Kloosterstraat 6 Drongen; not WZC Sint-Coleta Gent 0448.294.507; not Home Emmaus 0451.749.190; not De Foyer 0413.796.456; not Groep Zorg H. Familie; not IZW 0430.278.439; not Ferm Kinderopvang 0416.117.627; not Witje Wiebel 0443.654.937; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Avida / Raad van Bestuur,info@avida.be,Molenaarsstraat 34 9000 Gent,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2436; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_gent WZC after IZW / Ferm Kinderopvang / WZC Sint-Coleta Gent / Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
