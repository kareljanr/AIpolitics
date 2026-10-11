from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2454_stamp.txt").read_text().strip().splitlines()
EID="vzw_medemens_kdv_antwerpen"
SRC_PDF="src_medemens_kdv_jr2025_nbb_pdf_2454"
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"entities.csv", [
f"{EID},De Medemens Kinderdagverblijven VZW,ASBL De Medemens Creches,De Medemens Kinderdagverblijven VZW (leftover city_antwerpen CIK),parastatal,city_antwerpen,nl,https://www.demedemens.be/aanbod/kinderopvang,yonca.albayrak@demedemens.be,Lokkaardstraat 10 2018 Antwerpen,tick2454 YE2025 Strong official native NBB PDF deposit 2026-00206605 + Strong KBO 0893.678.915 Actief 9 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap aanbestedende overheid; omzet70 JUMP 1762950 commercial-only; 73 JUMP 7571818; 76A JUMP 100810; envelope 70/76A JUMP 9548863; bruto9900 empty VOL; pnl DROP 500404; 9901 DROP 501545; equity JUMP 14533752; assets JUMP 16808555; debt JUMP 2186496; FTE 123.7 JUMP; kapitaalsubsidies DROP 3503975; destin691 JUMP 5672853; 791 empty; cash JUMP 3019243; geldbeleggingen FLAT 500000; leftover mined city_antwerpen after OKO & ZO different-KBO skip; 9 VE CIK not private; NOT Kloosterstraat 6 Drongen; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_medemens_kdv_opbr_jr2025_statutory,{EID},2025,9548863,9548863,9548863,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +9.67% (VZW envelope because omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2454; PDF p7 native; YE2024 identical 8706655; 76A 100810 JUMP",
f"bud_medemens_kdv_omzet_jr2025_statutory,{EID},2025,1762950,1762950,1762950,NBB VOL-VZW code 70 omzet YE2025 JUMP +19.81% (commercial-only kinderdagverblijven vs large 73 7571818),{SRC_PDF},strong,tick2454; PDF p7 native; YE2024 identical 1471486; 73 also JUMP",
f"bud_medemens_kdv_73_jr2025_statutory,{EID},2025,7571818,7571818,7571818,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +7.50%,{SRC_PDF},strong,tick2454; PDF p7 native; YE2024 identical 7043292; 730/731/732 empty; 733 current-year column empty in native extract prior 7043292; FOI Opgroeien split behind 73 7571818",
f"bud_medemens_kdv_pnl_jr2025_statutory,{EID},2025,500404,500404,500404,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -41.05% (was 848906),{SRC_PDF},strong,tick2454; PDF p8 native; YE2024 identical 848906; bedrijfswinst 9901 501545 DROP; destin691 JUMP 5672853",
f"bud_medemens_kdv_bedrijfswinst_jr2025_statutory,{EID},2025,501545,501545,501545,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -40.45% (was 842210),{SRC_PDF},strong,tick2454; PDF p7 native; YE2024 identical 842210; 62 6768393 JUMP; 630 454052 JUMP; 66A 49142 JUMP",
f"bud_medemens_kdv_equity_jr2025_statutory,{EID},2025,14533752,14533752,14533752,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +9.74%,{SRC_PDF},strong,tick2454; PDF p6 native; YE2024 identical 13244296; kapitaalsubsidies 3503975 DROP; overgedragen 14 empty DROP; fondsen 10 1475810 JUMP; bestemde fondsen 13 9553967 JUMP",
f"bud_medemens_kdv_assets_jr2025_statutory,{EID},2025,16808555,16808555,16808555,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +9.31%,{SRC_PDF},strong,tick2454; PDF p5 native; YE2024 identical 15376491; MVA 22/27 9307040 JUMP; cash 3019243 JUMP; geldbeleggingen 500000 FLAT; aanbouw 27 31224 JUMP",
f"bud_medemens_kdv_debt_jr2025_statutory,{EID},2025,2186496,2186496,2186496,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +2.55%,{SRC_PDF},strong,tick2454; PDF p6 native; YE2024 identical 2132195; 42/48 1242725 JUMP",
f"bud_medemens_kdv_cash_jr2025_statutory,{EID},2025,3019243,3019243,3019243,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +33.96%,{SRC_PDF},strong,tick2454; PDF p5 native; YE2024 identical 2253921; geldbeleggingen 50/53 500000 FLAT",
f"bud_medemens_kdv_destin_jr2025_statutory,{EID},2025,5672853,5672853,5672853,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +568.36% (791 empty; destin 5672853 vs pnl 500404 via 14P 5172450),{SRC_PDF},strong,tick2454; PDF p9 native; YE2024 destin 848906; overgedragen 14 empty DROP FOI",
f"bud_medemens_kdv_62_jr2025_statutory,{EID},2025,6768393,6768393,6768393,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +12.41%,{SRC_PDF},strong,tick2454; PDF p7 native; YE2024 identical 6020906; FTE 123.7 JUMP",
])
print("entities+budgets ok")
