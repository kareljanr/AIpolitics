from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2437_stamp.txt").read_text().strip().splitlines()
EID="vzw_monte_rosa"
COMM="comm_monte_rosa_jr2025_statutory_opbr_5_42m_73_5_32m_pnl_jump_349k"
LB="lb_monte_rosa_opbr_5_42m_73_5_32m_pnl_jump_349k_destin_2_05m_jr2025"
GAP="gap_monte_rosa_opgroeien_matrix_opbr_5_42m_omzet_empty_73_5_32m_pnl_jump_349k_destin_2_05m_l5"
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
f"{GAP},Vlaanderen>Vlaams-Brabant>Leuven>MonteRosa>OVBJ,{EID},Opgroeien split behind 73 5323280 (733 5283236) and why omzet 70 empty while 70/76A 5424143; why destin 691 JUMP 2050000 (was 176176) >> pnl 348642 while overgedragen 14 DROP 223125 and bestemde fondsen 13 JUMP 3128000 (investeringsfonds 2428000); why 9904 JUMP 348642 and 9901 JUMP 369456 while 70/76A FLAT; why aanbouw 27 JUMP 2333389 + cash JUMP 823541 + geldbeleggingen JUMP 1662593 while kapitaalsubsidies DROP 1749682; FTE 63.0 DROP; 4 VE Leuven+Herent+Deurne; OVBJ HCO 27693 modules,Strong official PDF leftover public OVBJ of mined city_leuven; 5.42m opbr envelope; public jeugdhulp not private clinic; 4 VE Leuven+Herent+Deurne not city_aalter leftover; not Kloosterstraat 6 Drongen; not Don Bosco 0408.666.344; not Ferm Kinderopvang 0416.117.627; not IZW 0430.278.439; not Avida 0438.814.241; not Konekt 0524.936.680; not Witje Wiebel 0443.654.937; not Beregoed 0447.515.042; not Windekind 0431.806.386; not Helan 0464.151.037; not CAR Noorderkempen 0408.078.010 scan; not Antenne 3000 0433.184.479,8,VZW Monte Rosa / Raad van Bestuur,info@monterosa.be,Heidebergstraat 249 3010 Leuven,{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2437; ready NOT sent; NOT every-10; Strong official native NBB PDF; leftover mined city_leuven OVBJ after IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; also leftover mined city_herent + leftover mined city_antwerpen same KBO; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Horizon off Accent off Waas off Halle Asse off Heuvelheem off ARC off VERBINT off CFR Zelzate off De Kade off Ter Eecken off De Hoeksteen off De Mereltjes off 3Wplus off t Eekhoorntje off Elfenbankje off Zonnestraal Junior off KINDEROPVANG ZONNESTRAAL off Kinderopvang Turnhout off Bengelhof off Buitenschoolse Opvang Ieper off Kinderopvang Mariawende off Denderkind off BKO GENK-OOST off KOS off De Pagadder off WZC De Ruyschaert off Quattro off Wintershove off Huize Zonnelied off OLV Gasthuis Poperinge off WZC De Linde Wortegem-Petegem off Kindercentrum off KISME off Duinhuisjes off Windekind off Beregoed off Witje Wiebel off Home Emmaus off WZC Sint-Coleta Gent off Ferm Kinderopvang off IZW off Avida off Ten Anker off Leieborg off m-accent Eeklo off Vriendenkring off Antenne 3000 off Noorderkempen scan off Zilverbos off Grimbergen VAPH Zonnestraal off Helan off Vormingscentrum off WZC De Linde Lievegem off Zonnelied Roosdaal off Curando off De Linde Ronse YE2024 off Kinderlach YE2024 off t Bremhuisje stopgezet 1993 off Knuffelboom no NBB off De Zeppelin no JR; AGB/FARO/Gandae still YE2024",
])
print("foi_queue ok")
