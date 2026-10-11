from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2440_stamp.txt").read_text().strip().splitlines()
EID="vzw_ukkies"
COMM="comm_ukkies_jr2025_statutory_bruto_5_13m_pnl_flat_309k_destin_flat_309k"
LB="lb_ukkies_bruto_5_13m_omzet73_empty_pnl_flat_309k_destin_flat_309k_jr2025"
GAP="gap_ukkies_opgroeien_matrix_bruto_5_13m_omzet73_empty_pnl_flat_309k_destin_flat_309k_l5"
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
f"{GAP},Vlaanderen>Limburg>Hasselt>DeUkkies>CIK,{EID},Opgroeien split behind bruto 5126812 (70+73 empty) and why destin 691 FLAT 308628 = pnl 308628 while overgedragen 14 FLAT 1484169 and bestemde fondsen 13 JUMP 618560 and fondsen 10 FLAT 1187923; why 9904 FLAT 308628 and 9901 JUMP 300046 while bruto JUMP; why cash JUMP 1065696 while geldbeleggingen JUMP 1287959 and kapitaalsubsidies DROP 705041; FTE 79.3 FLAT while 62 JUMP; 3 VE Hasselt; CIK 212 plaatsen + 5 BOA; site 462 plaatsen,Strong official PDF leftover public CIK+BOA of mined city_hasselt; 5.13m bruto envelope; public kinderopvang not private clinic; 3 VE Hasselt; not Kloosterstraat 6 Drongen; not De Slabbertjes 0411.972.064; not Ferm Kinderopvang 0416.117.627; not t Eekhoorntje 0414.453.680; not Grauwzusters 0409.771.748 convent; not Jessa 0821.142.117; not Kinderlach 0450.275.186; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW De Ukkies / Raad van Bestuur,secretariaat@ukkies.be,Erasmuslaan 14 3500 Hasselt,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2440; ready NOT sent; EVERY-10; Strong official native NBB PDF; leftover mined city_hasselt CIK after Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 3 VE Hasselt; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
