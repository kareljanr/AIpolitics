from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2441_stamp.txt").read_text().strip().splitlines()
EID="vzw_hummeltjes"
COMM="comm_hummeltjes_jr2025_statutory_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k"
LB="lb_hummeltjes_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k_jr2025"
GAP="gap_hummeltjes_opgroeien_matrix_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k_l5"
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
f"{GAP},Vlaanderen>Limburg>Hasselt>DeHummeltjes>CIK,{EID},Opgroeien split behind opbr 13105742 (omzet 1401475 commercial-only vs 73 11277795) and why destin 691 DROP 70000 < pnl 259329 while overgedragen 14 JUMP 647265 and bestemde fondsen 13 JUMP 1570000 and fondsen 10 FLAT 829074; why 9904 DROP 259329 and 9901 DROP 247462 while opbr JUMP; why cash JUMP 2100999 while geldbeleggingen JUMP 500000 and kapitaalsubsidies DROP 2662209; FTE 152.9 JUMP while 62 JUMP; 13 VE zetel Hasselt; CIK+BOA+CKG 450 plaatsen,Strong official PDF leftover public CIK+BOA+CKG of mined city_hasselt; 13.11m opbr envelope; public kinderopvang not private clinic; 13 VE zetel Hasselt; not Kloosterstraat 6 Drongen; not De Ukkies 0412.729.654; not Ferm Kinderopvang 0416.117.627; not De Slabbertjes 0411.972.064; not Grauwzusters 0409.771.748 convent; not Jessa 0821.142.117; not Klein Hemelrijk 0413.866.336 remine; not Pinnochio 0438.745.648 remine; not Kinderlach 0450.275.186; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW De Hummeltjes / Raad van Bestuur,info@hummeltjes.be,Zuster Stanislaslaan 1 3500 Hasselt,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2441; ready NOT sent; Strong official native NBB PDF; leftover mined city_hasselt CIK after De Ukkies / Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 13 VE zetel Hasselt; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off De Ukkies off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
