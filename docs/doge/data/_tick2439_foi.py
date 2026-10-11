from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
EID="vzw_slabbertjes"
COMM="comm_slabbertjes_jr2025_statutory_bruto_520k_pnl_drop_48k_destin_jump_375k"
LB="lb_slabbertjes_bruto_520k_omzet73_empty_pnl_drop_48k_destin_jump_375k_jr2025"
GAP="gap_slabbertjes_opgroeien_matrix_bruto_520k_omzet73_empty_pnl_drop_48k_destin_jump_375k_l5"
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
f"{GAP},Vlaanderen>Vlaams-Brabant>Leuven>DeSlabbertjes>CIK,{EID},Opgroeien split behind bruto 519885 (70+73 empty) and why destin 691 JUMP 375400 (was 61023) >> pnl 48280 while overgedragen 14 DROP empty (was 327120) and bestemde fondsen 13 JUMP 436423 and fondsen 10 FLAT 91491; why 9904 DROP 48280 and 9901 DROP 47360 while bruto DROP; why cash DROP 138351 while geldbeleggingen JUMP 257760 (was 0) and kapitaalsubsidies DROP 71963; FTE 10.6 JUMP while 62 DROP; 1 VE Leuven; CIK 30 plaatsen,Strong official PDF leftover public CIK of mined city_leuven; 520k bruto envelope; public kinderopvang not private clinic; 1 VE Leuven; not Kloosterstraat 6 Drongen; not Ferm Kinderopvang 0416.117.627; not t Eekhoorntje 0414.453.680; not De Wissel 0421.913.376; not Monte Rosa 0413.350.751; not IZW 0430.278.439; not Grauwzusters 0409.771.748 convent; not Kinderlach 0450.275.186; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderdagverblijf De Slabbertjes / Raad van Bestuur,info@deslabbertjes.be,Mechelsevest 4 3000 Leuven,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2439; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_leuven CIK after De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf; 1 VE Leuven; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
