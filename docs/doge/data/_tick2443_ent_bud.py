from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
EID="vzw_jeugdhulp_don_bosco"
SRC_PDF="src_jdbv_jr2025_nbb_pdf_2443"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},Jeugdhulp Don Bosco Vlaanderen vzw,ASBL Jeugdhulp Don Bosco Vlaanderen,Jeugdhulp Don Bosco Vlaanderen VZW (leftover city_eeklo jeugdhulp),parastatal,city_eeklo,nl,https://jeugdhulpdonbosco.be/,info@jeugdhulpdonbosco.be,Waaistraat 6 9900 Eeklo,tick2443 YE2025 Strong official native NBB PDF deposit 2026-00259885 + Strong KBO 0408.666.344 Actief 17 VE zetel Waaistraat 6 9900 Eeklo RSZ2025 87.991; omzet70 JUMP 207924 commercial-only; 73 JUMP 27785881; 76A JUMP 671098 Mortsel sale; 70/76A JUMP 29159144 envelope; bruto9900 empty VOL; pnl DROP 830135; 9901 DROP 821772; equity JUMP 24731057; assets JUMP 33372760; debt JUMP 8641703; FTE 342 JUMP; kapitaalsubsidies DROP 7796340; destin691 DROP 830135 destin=pnl; cash JUMP 3303716; geldbeleggingen JUMP 12671844; gebouwen DROP 7430623; commissaris voorbehoud 2017-inbreng MVA; leftover mined city_eeklo after m-accent / Ascendere; 17 VE 2/17 Eeklo; Opgroeien jeugdhulp; NOT VIA Don Bosco vzw_via; NOT Kinderlach 0450.275.186; NOT m-accent 0465.841.411; NOT Ascendere 0409.470.553; NOT t Anemoontje 0413.354.612; NOT De Hummeltjes; NOT Helan; NOT Kloosterstraat 6 Drongen (VE Beekstraat 46c); AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_jdbv_opbr_jr2025_statutory,{EID},2025,29159144,29159144,29159144,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +6.94% (VZW envelope; omzet 70 207924 commercial-only vs large 73 27785881),{SRC_PDF},strong,tick2443; PDF p7 native; YE2024 identical 27265839; 73 27785881 JUMP; 76A 671098 JUMP Mortsel sale",
f"bud_jdbv_omzet_jr2025_statutory,{EID},2025,207924,207924,207924,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.41% (commercial-only vs large 73),{SRC_PDF},strong,tick2443; PDF p7 native; YE2024 identical 193581",
f"bud_jdbv_73_jr2025_statutory,{EID},2025,27785881,27785881,27785881,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.48%,{SRC_PDF},strong,tick2443; PDF p7 native; YE2024 identical 26595033; 731 218010 JUMP; 733 27567872 JUMP",
f"bud_jdbv_pnl_jr2025_statutory,{EID},2025,830135,830135,830135,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -36.65%,{SRC_PDF},strong,tick2443; PDF p8 native; YE2024 identical 1310352; bedrijfswinst 9901 821772 DROP; destin691 830135 DROP destin=pnl",
f"bud_jdbv_bedrijfswinst_jr2025_statutory,{EID},2025,821772,821772,821772,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -14.49%,{SRC_PDF},strong,tick2443; PDF p7 native; YE2024 identical 961016; 62 24343059 JUMP; 630 696488 DROP; 66A 306436 JUMP Veilige Trajecten",
f"bud_jdbv_equity_jr2025_statutory,{EID},2025,24731057,24731057,24731057,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +3.82%,{SRC_PDF},strong,tick2443; PDF p6 native; YE2024 identical 23820622; kapitaalsubsidies 7796340 DROP; overgedragen 14 empty; fondsen 10 4283735 JUMP; bestemde fondsen 13 12650983 JUMP",
f"bud_jdbv_assets_jr2025_statutory,{EID},2025,33372760,33372760,33372760,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +3.40%,{SRC_PDF},strong,tick2443; PDF p5 native; YE2024 identical 32273917; gebouwen 22 7430623 DROP; cash 3303716 JUMP; geldbeleggingen 12671844 JUMP",
f"bud_jdbv_debt_jr2025_statutory,{EID},2025,8641703,8641703,8641703,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +2.23%,{SRC_PDF},strong,tick2443; PDF p6 native; YE2024 identical 8453295; 17 2456810 DROP; 42/48 5879003 JUMP",
f"bud_jdbv_cash_jr2025_statutory,{EID},2025,3303716,3303716,3303716,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +10.35%,{SRC_PDF},strong,tick2443; PDF p5 native; YE2024 identical 2993936; geldbeleggingen 50/53 12671844 JUMP",
f"bud_jdbv_destin_jr2025_statutory,{EID},2025,830135,830135,830135,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -87.34% (destin=pnl 830135; was 6557130),{SRC_PDF},strong,tick2443; PDF p9 native; YE2024 destin 6557130 from overgedragen 14P 4321778 + onttrekking 925000; bestemde fondsen 13 12650983 JUMP FOI",
f"bud_jdbv_62_jr2025_statutory,{EID},2025,24343059,24343059,24343059,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +6.76%,{SRC_PDF},strong,tick2443; PDF p7 native; YE2024 identical 22802409; FTE 342 JUMP",
])
print("entities+budgets ok")
