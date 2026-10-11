from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2502_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_sjwetteren_jr2025_nbb_pdf_2502"
SRC_KBO="src_sjwetteren_kbo_2502"
SRC_SBM="src_sjwetteren_sbm_2502"
SRC_SITE="src_sjwetteren_site_2502"
EID="vzw_kdv_sint_jozef_wetteren"
GAP="gap_kdv_sint_jozef_wetteren_opgroeien_matrix_bruto_2_13m_omzet_drop_541k_pnl_jump_231k_destin_150k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT AGB Wetteren remine; NOT Woonpijler remine; NOT Trianval 0419.052.074 remine parent sec_flanders; NOT Zorg-Saam WZC Sint-Jozef Wetteren leftover-via-VE Gent remine; NOT Gesticht 0410.918.031 leftover city_ieper; NOT SAMEN 0728.627.079 remine leftover city_tielt WZC; NOT leftover city_buggenhout; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Sint-Jozef Wetteren deposit 2026-00174836,http://cdn.staatsbladmonitor.be/2026pdf/2026-00174836.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2502; official native statutory PDF 51686 bytes 13p VKT-VZW 26.0.15 m04-f; header 16.06.2026; AV 04.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-19 07:37:53 UTC OpenPDF 1.3.26; CDN Last-Modified 22.06.2026; statutory pages native; CDN 2026-00174836 GET 200 51686 MD5 029aa52ae54632d56fc4a78285ec1d6f; official NBB UUID 4245a5a9-698a-11f1-ba33-775c4b6fd5ad; VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; NBB broker HTML stub discarded; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Sint-Jozef 0408.475.314,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408475314,KBO Public Search FOD Economie,{DAY},official_register,tick2502; Actief; 2 VE leftover city_wetteren (official zetel Wegvoeringstraat 61 9230 Wetteren since 01.10.1990; VE 2.150.800.695 Kinderdagverblijven Sint Jozef Wegvoeringstraat 61 since 03.01.2006; VE 2.300.011.738 t Trudeken Florimond Leirensstraat 31 9230 Wetteren since 01.01.2020); VZW since 08.06.1971; RSZ2025 88.911 Kinderdagverblijven; FOI karen.meirlaen@kinderdagverblijfsintjozef.be; leftover mined city_wetteren CIK after leftover-type hunt; NOT AGB Wetteren remine; NOT Trianval remine; NOT Zorg-Saam leftover-via-VE",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf Sint-Jozef 0408475314 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0408475314,NBB Consult / SBM,{DAY},official_register,tick2502; deposit-id 2026-00174836 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID 4245a5a9-698a-11f1-ba33-775c4b6fd5ad; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Kinderdagverblijf Sint-Jozef FOI contact leftover city_wetteren CIK,https://www.kinderdagverblijfsintjozef.be/,Kinderdagverblijf Sint-Jozef VZW leftover city_wetteren CIK 2 VE,{DAY},foi_contact,tick2502; FOI karen.meirlaen@kinderdagverblijfsintjozef.be from official NBB PDF; official KBO zetel Wegvoeringstraat 61 9230 Wetteren; RSZ2025 88.911; leftover mined city_wetteren CIK; NOT AGB Wetteren remine; NOT Trianval remine; NOT Zorg-Saam leftover-via-VE; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Sint-Jozef,ASBL Kinderdagverblijf Sint-Jozef,Kinderdagverblijf Sint-Jozef VZW (leftover city_wetteren CIK),parastatal,city_wetteren,nl,https://www.kinderdagverblijfsintjozef.be/,karen.meirlaen@kinderdagverblijfsintjozef.be,Wegvoeringstraat 61 9230 Wetteren,tick2502 YE2025 Strong official native NBB PDF deposit 2026-00174836 + Strong KBO 0408.475.314 Actief 2 VE; omzet70 DROP 540560 ouder-fee slice; 73 empty VKT; 76A JUMP 447; envelope bruto9900 JUMP 2133695; pnl JUMP 230508; 9901 JUMP 249335; equity JUMP 2847914; assets JUMP 3855305; debt JUMP 912391; FTE JUMP 29.6; kapitaalsubsidies DROP 1776246; destin691 JUMP 150000; cash DROP 205430; geldbeleggingen JUMP 813476; leftover city_wetteren CIK 2 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_sjwetteren_omzet_jr2025_statutory,{EID},2025,540560,540560,540560,NBB VKT-VZW code 70 omzet YE2025 DROP -5.56% (ouder-fee slice; 73 empty VKT),{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 572365; 73 empty VKT; 76A 447 JUMP; FOI Opgroeien/Kind en Gezin/gemeente/ouder matrix behind bruto 2133695",
f"bud_sjwetteren_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 also empty VKT; FOI Opgroeien/VL/gemeente Wetteren matrix behind bruto because 73 empty",
f"bud_sjwetteren_opbr_jr2025_statutory,{EID},2025,2133695,2133695,2133695,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +2.53% (VKT envelope because 73 empty and bruto much larger than omzet),{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 2081000; omzet70 540560 DROP; 70/76A 541007; 76A 447 JUMP",
f"bud_sjwetteren_76A_jr2025_statutory,{EID},2025,447,447,447,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP from empty,{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 empty",
f"bud_sjwetteren_pnl_jr2025_statutory,{EID},2025,230508,230508,230508,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +59.86%,{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 144192; bedrijfswinst 9901 249335 JUMP; destin691 150000 JUMP",
f"bud_sjwetteren_bedrijfswinst_jr2025_statutory,{EID},2025,249335,249335,249335,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +58.00%,{SRC_PDF},strong,tick2502; PDF p5 native; YE2024 157809; 62 1696590 JUMP; 630 163491; 66A empty; 640/8 4279; 635/9 20000 DROP; 60/61 269394 JUMP",
f"bud_sjwetteren_equity_jr2025_statutory,{EID},2025,2847914,2847914,2847914,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.31%,{SRC_PDF},strong,tick2502; PDF p4 native; YE2024 2704254; kapitaalsubsidies 15 1776246 DROP; overgedragen 14 805865 JUMP; fondsen 10 115803 FLAT; bestemde 13 150000 JUMP",
f"bud_sjwetteren_assets_jr2025_statutory,{EID},2025,3855305,3855305,3855305,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +5.76%,{SRC_PDF},strong,tick2502; PDF p3 native; YE2024 3645241; MVA 22/27 2674703 DROP; cash 205430 DROP; geldbeleggingen 813476 JUMP from empty; aanbouw 27 empty",
f"bud_sjwetteren_debt_jr2025_statutory,{EID},2025,912391,912391,912391,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +5.36%,{SRC_PDF},strong,tick2502; PDF p4 native; YE2024 865987; 17 514919 DROP; voorzieningen 16 95000 JUMP",
f"bud_sjwetteren_cash_jr2025_statutory,{EID},2025,205430,205430,205430,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -69.70% (reallocated to geldbeleggingen 813476),{SRC_PDF},strong,tick2502; PDF p3 native; YE2024 678059; geldbeleggingen 50/53 813476 JUMP from empty; combined liquidity 1018906 JUMP; capex 8169 31803",
f"bud_sjwetteren_destin_jr2025_statutory,{EID},2025,150000,150000,150000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP from empty (investeringen),{SRC_PDF},strong,tick2502; PDF p6 native; YE2024 destin empty; 791 empty; overgedragen 14 805865 JUMP; bestemde 13 150000 JUMP",
])
print("entities+budgets ok")
print("CORE1 DONE")
