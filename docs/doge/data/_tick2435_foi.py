from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2435_stamp.txt").read_text().strip().splitlines()
EID="vzw_izw_leuven"
COMM="comm_izw_jr2025_statutory_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k"
LB="lb_izw_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k_destin_35k_jr2025"
GAP="gap_izw_vaph_matrix_opbr_1_33m_omzet_530k_73_803k_pnl_drop_10k_destin_35k_l5"
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
f"{GAP},Vlaanderen>Vlaams-Brabant>Leuven>IZW>VAPH,{EID},VAPH/Vlaams/Leuven/Grimbergen split behind opbr 1333228 (70 530078 commercial-only vs 73 802987); why 73 DROP 802987 while 70 JUMP 530078; why 9904 DROP 10323 (was 188046) and 9901 DROP 5047 (was 184611); why destin 691 JUMP 35000 (was empty; destin > pnl) while overgedragen 14 DROP 561991 and bestemde fondsen 13 JUMP 185000; why 66A 62904 vakantiegeld vordering Vlaamse overheid 2025 afgeboekt; why cash DROP 1444638 is almost all of assets 1468447 (gebouwen empty; geldbeleggingen empty); FTE 17.3 JUMP; 3 VE Leuven+Grimbergen; VAPH-afrekening geraamd,Strong official PDF leftover public VAPH of mined city_leuven; 1.33m opbr; public VAPH not private clinic; 3 VE Leuven+Grimbergen not city_aalter leftover; not Kloosterstraat 6 Drongen; not Ferm Kinderopvang 0416.117.627; not Alvinnenberg 0434.390.150; not Hejmen 0426.383.987; not Staf 0431.333.660; not Grimbergen VAPH Zonnestraal; not WZC Sint-Coleta Gent 0448.294.507; not Home Emmaus 0451.749.190; not Witje Wiebel 0443.654.937; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Helan 0464.151.037; not Knuffelboom 0478.310.859; not De Zeppelin 0454.001.867; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW IZW / Raad van Bestuur,info@izw.be,Riddersstraat 60 bus 02 3000 Leuven,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2435; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_leuven VAPH after Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf / MFC Combo; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
