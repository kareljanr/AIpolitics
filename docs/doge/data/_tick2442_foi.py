from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
EID="vzw_anemoontje"
COMM="comm_anemoontje_jr2025_statutory_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k"
LB="lb_anemoontje_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k_jr2025"
GAP="gap_anemoontje_opgroeien_matrix_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k_l5"
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
f"{GAP},Vlaanderen>VlaamsBrabant>Leuven>Anemoontje>CIK,{EID},Opgroeien split behind opbr 834926 (omzet 136595 commercial-only vs 73 698331) and why destin 691 JUMP 598014 >> pnl 105278 while overgedragen 14 DROP 202982 and bestemde fondsen 13 JUMP 598014 and fondsen 10 FLAT 12702; why 9904 JUMP 105278 and 9901 JUMP 109330 while FTE DROP 8.1; why cash JUMP 332675 while geldbeleggingen FLAT 250000 and kapitaalsubsidies DROP 515543; FTE 8.1 DROP while 62 JUMP; 1 VE Leuven; CIK 40 plaatsen,Strong official PDF leftover public CIK of mined city_leuven; 835k opbr envelope; public kinderopvang not private clinic; 1 VE Leuven; not Kloosterstraat 6 Drongen; not Duinhuisjes VE t Anemoontje 2.375.207.425; not De Slabbertjes 0411.972.064; not Ferm Kinderopvang 0416.117.627; not t Eekhoorntje 0414.453.680; not De Wissel 0421.913.376; not Monte Rosa 0413.350.751; not IZW 0430.278.439; not De Hummeltjes 0409.987.425; not De Ukkies 0412.729.654; not Kinderlach 0450.275.186; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderdagverblijf t Anemoontje / Raad van Bestuur,info@kinderdagverblijfanemoontje.be,Bosstraat 30 3012 Leuven,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2442; ready NOT sent; Strong official native NBB PDF; leftover mined city_leuven CIK after De Hummeltjes / De Ukkies / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE Leuven; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off De Ukkies off De Hummeltjes off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema off Klein Hemelrijk remine off Pinnochio remine off Duinhuisjes VE t Anemoontje; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
