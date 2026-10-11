from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2503_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_avalon_jr2025_nbb_pdf_2503"
SRC_KBO="src_avalon_kbo_2503"
SRC_SBM="src_avalon_sbm_2503"
SRC_SITE="src_avalon_site_2503"
EID="vzw_avalon_buggenhout"
GAP="gap_avalon_buggenhout_vaph_matrix_70_76A_3_56m_omzet_commercial_73_jump_3_10m_pnl_improved_loss_33k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Heymeulen 0420.669.303 leftover city_buggenhout WZC YE2024; NOT Hunnegem 0808.756.504 leftover city_herzele WZC YE2024; NOT Kinderdagverblijf Sint-Jozef 0408.475.314 remine leftover city_wetteren CIK; NOT Schoonderhage 0419.635.460 remine parent sec_flanders; NOT leftover city_niel unused; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Avalon Buggenhout deposit 2026-00195078,http://cdn.staatsbladmonitor.be/2026pdf/2026-00195078.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2503; official native statutory PDF 48966 bytes 13p VKT-VZW 25.0.13 m04-f; header 23.06.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-25 03:31:17 UTC OpenPDF 1.3.26; CDN Last-Modified 09.07.2026; statutory pages native; CDN 2026-00195078 GET 200 48966 MD5 a0913cbc85054886940a4d104374fbd9; official NBB UUID 4a2a023d-52ae-11f1-9044-a36a566879c5; VKT-VZW 6.1.1 6.2 6.5 6.6 6.8 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Avalon 0464.778.666,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464778666,KBO Public Search FOD Economie,{DAY},official_register,tick2503; Actief; 1 VE leftover city_buggenhout (official zetel Broekstraat 27 9255 Buggenhout since 16.06.2009; VE 2.164.139.185 Avalon Broekstraat 27 since 02.08.2007); VZW since 13.09.1998; aanbestedende overheid since 13.09.1998; RSZ2025 87.304 Instellingen met huisvesting voor volwassenen met een lichamelijke handicap; FOI info@avalon-vzw.be; leftover mined city_buggenhout VAPH after leftover-type hunt; NOT De Heymeulen YE2024; NOT Hunnegem YE2024; NOT leftover-via-VE",
f"{SRC_SBM},NBB Consult / SBM fiche Avalon 0464778666 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0464778666,NBB Consult / SBM,{DAY},official_register,tick2503; deposit-id 2026-00195078 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID 4a2a023d-52ae-11f1-9044-a36a566879c5; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Avalon FOI contact leftover city_buggenhout VAPH,https://www.avalon-vzw.be/,Avalon VZW leftover city_buggenhout VAPH 1 VE,{DAY},foi_contact,tick2503; FOI info@avalon-vzw.be from official NBB PDF; official KBO zetel Broekstraat 27 9255 Buggenhout; RSZ2025 87.304; leftover mined city_buggenhout VAPH; NOT De Heymeulen YE2024; NOT Hunnegem YE2024; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Avalon,ASBL Avalon,Avalon VZW (leftover city_buggenhout VAPH),parastatal,city_buggenhout,nl,https://www.avalon-vzw.be/,info@avalon-vzw.be,Broekstraat 27 9255 Buggenhout,tick2503 YE2025 Strong official native NBB PDF deposit 2026-00195078 + Strong KBO 0464.778.666 Actief 1 VE; omzet70 JUMP 451254 commercial-only vs large 73; 73 JUMP 3100234; 76A JUMP 6579; envelope 70/76A JUMP 3558067; bruto9900 JUMP 3392631; pnl IMPROVED LOSS -32618; 9901 IMPROVED LOSS -36635; equity DROP 4344137; assets DROP 6039963; debt DROP 1573776; FTE JUMP 37.7; kapitaalsubsidies DROP 1831111; destin691 empty; cash JUMP 1086798; leftover city_buggenhout VAPH 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_avalon_omzet_jr2025_statutory,{EID},2025,451254,451254,451254,NBB VKT-VZW code 70 omzet YE2025 JUMP +13.88% (commercial-only vs large 73),{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 396248; 73 3100234 JUMP; 76A 6579 JUMP; FOI VAPH/gemeente/eigen-bijdrage matrix behind 70/76A 3558067",
f"bud_avalon_73_jr2025_statutory,{EID},2025,3100234,3100234,3100234,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.73%,{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 2960163; FOI VAPH PVB/RTH/woon+dag matrix behind large 73",
f"bud_avalon_opbr_jr2025_statutory,{EID},2025,3558067,3558067,3558067,NBB VKT-VZW envelope 70/76A YE2025 JUMP +6.01% (VZW because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 3356411; omzet70 451254 JUMP; 73 3100234 JUMP; 76A 6579 JUMP; bruto9900 3392631 JUMP",
f"bud_avalon_76A_jr2025_statutory,{EID},2025,6579,6579,6579,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP from empty,{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 empty",
f"bud_avalon_pnl_jr2025_statutory,{EID},2025,-32618,-32618,-32618,NBB VKT-VZW code 9904 verlies van het boekjaar YE2025 IMPROVED LOSS -64.09% narrower,{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 -90830; bedrijfswinst 9901 -36635 IMPROVED LOSS; destin691 empty",
f"bud_avalon_bedrijfswinst_jr2025_statutory,{EID},2025,-36635,-36635,-36635,NBB VKT-VZW code 9901 bedrijfsverlies YE2025 IMPROVED LOSS -59.27% narrower,{SRC_PDF},strong,tick2503; PDF p6 native; YE2024 -89948; 62 3165200 JUMP; 630 254913 DROP; 66A empty; 640/8 40453 JUMP; 635/9 -31300 DROP; 60/61 569637 JUMP",
f"bud_avalon_equity_jr2025_statutory,{EID},2025,4344137,4344137,4344137,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -2.40%,{SRC_PDF},strong,tick2503; PDF p5 native; YE2024 4451022; kapitaalsubsidies 15 1831111 DROP; overgedragen 14 373416 DROP; fondsen 10 1283861 FLAT; bestemde 13 855749 FLAT",
f"bud_avalon_assets_jr2025_statutory,{EID},2025,6039963,6039963,6039963,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -3.14%,{SRC_PDF},strong,tick2503; PDF p4 native; YE2024 6235881; MVA 22/27 4056609 DROP; cash 1086798 JUMP; geldbeleggingen 250000 FLAT; aanbouw 27 317040 FLAT",
f"bud_avalon_debt_jr2025_statutory,{EID},2025,1573776,1573776,1573776,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.54%,{SRC_PDF},strong,tick2503; PDF p5 native; YE2024 1631509; 17 866058 DROP; voorzieningen 16 122050 DROP",
f"bud_avalon_cash_jr2025_statutory,{EID},2025,1086798,1086798,1086798,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +10.00%,{SRC_PDF},strong,tick2503; PDF p4 native; YE2024 987971; geldbeleggingen 50/53 250000 FLAT; combined liquidity 1336798 JUMP; capex 8169 119601",
f"bud_avalon_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty,{SRC_PDF},strong,tick2503; PDF p7 native; YE2024 destin empty; 791 empty; overgedragen 14 373416 DROP; bestemde 13 855749 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")
