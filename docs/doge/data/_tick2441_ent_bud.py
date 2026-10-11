from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2441_stamp.txt").read_text().strip().splitlines()
EID="vzw_hummeltjes"
SRC_PDF="src_hummeltjes_jr2025_nbb_pdf_2441"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},De Hummeltjes vzw,ASBL De Hummeltjes,De Hummeltjes VZW (leftover city_hasselt CIK+BOA+CKG),parastatal,city_hasselt,nl,https://www.hummeltjes.be/,info@hummeltjes.be,Zuster Stanislaslaan 1 3500 Hasselt,tick2441 YE2025 Strong official native NBB PDF deposit 2026-00225380 + Strong KBO 0409.987.425 Actief 13 VE zetel Zuster Stanislaslaan 1 3500 Hasselt RSZ2025 88.911; omzet70 JUMP 1401475 commercial-only; 73 JUMP 11277795; 76A DROP 57881; 70/76A JUMP 13105742 envelope; bruto9900 empty VOL; pnl DROP 259329; 9901 DROP 247462; equity JUMP 5708548; assets JUMP 9784745; debt JUMP 3968488; FTE 152.9 JUMP; kapitaalsubsidies DROP 2662209; destin691 DROP 70000 destin<pnl; cash JUMP 2100999; geldbeleggingen JUMP 500000; gebouwen DROP 5417866; aanbouw JUMP 136841; leftover mined city_hasselt after De Ukkies / Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; 13 VE zetel Hasselt + 6/13 VE Hasselt; Opgroeien CIK+BOA+CKG 450 plaatsen; Pinnochio 0438.745.648 opgeslorpt 20.12.2023; Klein Hemelrijk 0413.866.336 opgeslorpt 31.03.2026 na YE2025 do not remine; NOT Kloosterstraat 6 Drongen; NOT De Ukkies 0412.729.654; NOT Ferm Kinderopvang 0416.117.627; NOT De Slabbertjes 0411.972.064; NOT Grauwzusters 0409.771.748 convent; NOT Jessa 0821.142.117; NOT Kinderlach; NOT Helan; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Don Bosco YE2024 not taken; Villa Boempatat YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hummeltjes_opbr_jr2025_statutory,{EID},2025,13105742,13105742,13105742,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.65% (VZW envelope; omzet 70 1401475 commercial-only vs large 73 11277795),{SRC_PDF},strong,tick2441; PDF p7 native; YE2024 identical 12404911; 73 11277795 JUMP; 74 368591 JUMP; 76A 57881 DROP",
f"bud_hummeltjes_omzet_jr2025_statutory,{EID},2025,1401475,1401475,1401475,NBB VOL-VZW code 70 omzet YE2025 JUMP +8.97% (ouderbijdragen; commercial-only vs large 73),{SRC_PDF},strong,tick2441; PDF p7 native; YE2024 identical 1286093",
f"bud_hummeltjes_73_jr2025_statutory,{EID},2025,11277795,11277795,11277795,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.52%,{SRC_PDF},strong,tick2441; PDF p7+toel 6.9 native; YE2024 identical 10790315; 731 30900 DROP; 733 11246895 JUMP",
f"bud_hummeltjes_pnl_jr2025_statutory,{EID},2025,259329,259329,259329,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -53.07%,{SRC_PDF},strong,tick2441; PDF p8 native; YE2024 identical 552603; bedrijfswinst 9901 247462 DROP; destin691 70000 DROP destin<pnl",
f"bud_hummeltjes_bedrijfswinst_jr2025_statutory,{EID},2025,247462,247462,247462,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -54.59%,{SRC_PDF},strong,tick2441; PDF p7 native; YE2024 identical 544940; 62 10263962 JUMP; 630 406810 DROP; 66A 47860",
f"bud_hummeltjes_equity_jr2025_statutory,{EID},2025,5708548,5708548,5708548,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +2.20%,{SRC_PDF},strong,tick2441; PDF p6 native; YE2024 identical 5585606; kapitaalsubsidies 2662209 DROP; overgedragen 14 647265 JUMP; fondsen 10 829074 FLAT; bestemde fondsen 13 1570000 JUMP",
f"bud_hummeltjes_assets_jr2025_statutory,{EID},2025,9784745,9784745,9784745,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +2.00%,{SRC_PDF},strong,tick2441; PDF p5 native; YE2024 identical 9593084; gebouwen 22 5417866 DROP; cash 2100999 JUMP; geldbeleggingen 500000 JUMP",
f"bud_hummeltjes_debt_jr2025_statutory,{EID},2025,3968488,3968488,3968488,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +0.85%,{SRC_PDF},strong,tick2441; PDF p6 native; YE2024 identical 3934958; 17 1282108 FLAT; 42/48 2040483",
f"bud_hummeltjes_cash_jr2025_statutory,{EID},2025,2100999,2100999,2100999,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +18.08%,{SRC_PDF},strong,tick2441; PDF p5 native; YE2024 identical 1779290; geldbeleggingen 50/53 500000 JUMP",
f"bud_hummeltjes_destin_jr2025_statutory,{EID},2025,70000,70000,70000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -90.49% (destin < pnl 259329),{SRC_PDF},strong,tick2441; PDF p9 native; YE2024 identical 735647; bestemde fondsen 13 1570000 JUMP FOI",
f"bud_hummeltjes_62_jr2025_statutory,{EID},2025,10263962,10263962,10263962,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +5.85%,{SRC_PDF},strong,tick2441; PDF p7 native; YE2024 identical 9696705; FTE 152.9 JUMP",
])
print("entities+budgets ok")
