from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2446_stamp.txt").read_text().strip().splitlines()
EID="vzw_kinderkuren"
COMM="comm_kinderkuren_jr2025_statutory_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k"
LB="lb_kinderkuren_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k_destin_drop_680k_jr2025"
GAP="gap_kinderkuren_leuven_matrix_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k_destin_drop_680k_l5"
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
f"{GAP},Vlaanderen>VlaamsBrabant>Leuven>Kinderkuren>EVA,{EID},Opgroeien/Stad Leuven split behind bruto 4674661 (omzet+73 empty VKT) and why destin 691 DROP 0 (was 680000) while 791 onttrekking 680000 empties bestemde fondsen 13 and pnl FLIP LOSS -617961; why 9904 FLIP LOSS -617961 and 9901 FLIP LOSS -615411 while FTE JUMP 81.6 and 62 JUMP 5127146; why 76A DROP 2432; why cash JUMP 1417387 while assets DROP 1762362 and equity DROP 857351 and vorderingen 40/41 DROP 258224; FTE 81.6 JUMP while 62 JUMP; 37 VE leftover city_leuven EVA,Strong official PDF leftover public EVA of mined city_leuven; 4.67m bruto envelope; public EVA not private clinic; 37 VE; not Kloosterstraat 6 Drongen; not Wigwam 0435.015.207; not t Anemoontje 0413.354.612; not IZW 0430.278.439; not Monte Rosa 0413.350.751; not De Wissel 0421.913.376; not De Slabbertjes 0411.972.064; not t Zonnetje 0443.648.306; not Kinderdagverblijven Leuven 0413.321.255 absorbed; not Kinderlach 0450.275.186; not Helan 0464.151.037; not De Speelboom 0443.631.280 Brussels; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Kinderkuren / Raad van Bestuur,kinderkuren@leuven.be,Professor Van Overstraetenplein 1 3000 Leuven,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2446; ready NOT sent; Strong official native NBB PDF; leftover mined city_leuven EVA after Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes / t Zonnetje; 37 VE; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Monte Rosa off De Wissel off De Slabbertjes off De Ukkies off De Hummeltjes off t Anemoontje off Jeugdhulp Don Bosco off Wigwam off t Zonnetje off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR off Grauwzusters convent off Jessa hospital special schema off Klein Hemelrijk remine off Pinnochio remine off Duinhuisjes VE t Anemoontje off VIA Don Bosco off De Speelboom Brussels; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
