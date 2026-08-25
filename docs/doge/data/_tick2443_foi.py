from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
EID="vzw_jeugdhulp_don_bosco"
COMM="comm_jdbv_jr2025_statutory_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k"
LB="lb_jdbv_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k_destin_drop_6_56m_jr2025"
GAP="gap_jdbv_jeugdhulp_matrix_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k_l5"
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
f"{GAP},Vlaanderen>OostVlaanderen>Eeklo>JeugdhulpDonBosco>jeugdhulp,{EID},Opgroeien split behind opbr 29159144 (omzet 207924 commercial-only vs 73 27785881) and why destin 691 DROP 830135 = pnl while prior destin 6557130 and bestemde fondsen 13 JUMP 12650983 and fondsen 10 JUMP 4283735; why 9904 DROP 830135 and 9901 DROP 821772 while FTE JUMP 342; why 76A JUMP 671098 Mortsel sale and 66A JUMP 306436 Veilige Trajecten; why cash JUMP 3303716 while geldbeleggingen JUMP 12671844 and kapitaalsubsidies DROP 7796340; commissaris voorbehoud 2017-inbreng MVA NBV 474416; FTE 342 JUMP while 62 JUMP; 17 VE 2/17 Eeklo,Strong official PDF leftover public jeugdhulp of mined city_eeklo; 29.16m opbr envelope; public jeugdhulp not private clinic; 17 VE 2/17 Eeklo; not Kloosterstraat 6 Drongen; not VIA Don Bosco vzw_via; not Kinderlach 0450.275.186; not m-accent 0465.841.411; not Ascendere 0409.470.553; not t Anemoontje 0413.354.612; not De Hummeltjes 0409.987.425; not De Ukkies 0412.729.654; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Jeugdhulp Don Bosco Vlaanderen / Raad van Bestuur,info@jeugdhulpdonbosco.be,Waaistraat 6 9900 Eeklo,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2443; ready NOT sent; Strong official native NBB PDF; leftover mined city_eeklo jeugdhulp after m-accent / Ascendere; 17 VE 2/17 Eeklo; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off De Ukkies off De Hummeltjes off t Anemoontje off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema off Klein Hemelrijk remine off Pinnochio remine off Duinhuisjes VE t Anemoontje off VIA Don Bosco; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
