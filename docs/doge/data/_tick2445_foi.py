from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
EID="vzw_t_zonnetje"
COMM="comm_zonnetje_jr2025_statutory_bruto_2_11m_omzet73_empty_pnl_drop_176k"
LB="lb_zonnetje_bruto_2_11m_omzet73_empty_pnl_drop_176k_destin_empty_jr2025"
GAP="gap_zonnetje_opgroeien_matrix_bruto_2_11m_omzet73_empty_pnl_drop_176k_destin_empty_l5"
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
f"{GAP},Vlaanderen>OostVlaanderen>Waregem>tZonnetje>CIK,{EID},Opgroeien split behind bruto 2113971 (omzet+73 empty VKT) and why destin 691 empty while pnl 175969 goes to overgedragen 14 JUMP 1391528 and bestemde fondsen 13 empty and fondsen 10 FLAT 47700; why 9904 DROP 175969 and 9901 DROP 158114 while FTE JUMP 30.5 and 62 JUMP 1848937; why 76A JUMP 10445; why cash DROP 279435 while geldbeleggingen JUMP 900000 and kapitaalsubsidies DROP 213065 and capex JUMP 251244; FTE 30.5 JUMP while 62 JUMP; 3 VE Waregem+Kruisem+Nazareth-De Pinte,Strong official PDF leftover public CIK of mined city_waregem + leftover city_kruisem; 2.11m bruto envelope; public CIK not private clinic; 3 VE; not Kloosterstraat 6 Drongen; not Kindercentrum 0408.226.775; not KINDEROPVANG ZONNESTRAAL 0413.351.642; not Zonnestraal Junior 0866.116.859; not KDV De Regenboog 0671.670.560 BV; not Wigwam 0435.015.207; not Jeugdhulp Don Bosco 0408.666.344; not t Anemoontje 0413.354.612; not Kinderlach 0450.275.186; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW t Zonnetje kinderdagverblijven / Raad van Bestuur,inge.moens@kdvzonnetje.be,Kasteellaan 1 9840 Nazareth-De Pinte,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2445; ready NOT sent; Strong official native NBB PDF; leftover mined city_waregem CIK after Kindercentrum + leftover mined city_kruisem after Wigwam / Jeugdhulp Don Bosco; 3 VE; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off De Ukkies off De Hummeltjes off t Anemoontje off Jeugdhulp Don Bosco off Wigwam off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema off Klein Hemelrijk remine off Pinnochio remine off Duinhuisjes VE t Anemoontje off VIA Don Bosco; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
