from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2501_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_samen_jr2025_nbb_pdf_2501"
SRC_KBO="src_samen_kbo_2501"
SRC_SBM="src_samen_sbm_2501"
SRC_SITE="src_samen_site_2501"
EID="vzw_samen_tielt"
GAP="gap_samen_tielt_wzc_matrix_omzet_14_79m_73_jump_2_81m_pnl_loss_305k_cash_drop_1_22m_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Zonnewende 0735.627.214 remine leftover city_tielt WZC; NOT De Luifel 0434.011.652 remine leftover city_tielt VAPH; NOT Mivalti 0416.406.548 remine leftover city_tielt VAPH parent sec_flanders; NOT De Harlekijntjes remine leftover city_tielt CIK; NOT leftover city_dentergem (Dentergem VE only); NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 SAMEN deposit 2026-00229914,http://cdn.staatsbladmonitor.be/2026pdf/2026-00229914.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2501; official native statutory PDF 1867462 bytes 50p VOL-VZW 25.0.13 m05-f; header 25.06.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-01 02:28:34 UTC OpenPDF 1.3.26; CDN Last-Modified 23.07.2026; statutory pages native; CDN 2026-00229914 GET 200 1867462 MD5 15b2e69eb6c057a0ec18d52501a5faf3; official NBB UUID fb2c07a2-6951-11f1-b667-13b7f733fa50; VOL-VZW 6.1 6.2.1-4 6.3.4 6.3.5 6.4.1-2 6.5.1-3 6.16 niet dienstig; prior-year identical not restated; commissaris Moore Audit BV B00212 / Van Ryckeghem Geert A01269 / Vandeputte Jo A02119; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO SAMEN 0728.627.079,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0728627079,KBO Public Search FOD Economie,{DAY},official_register,tick2501; Actief; 3 VE leftover city_tielt (official zetel Krommewalstraat 9 8700 Tielt since 01.01.2025; VE 2.290.504.451 SAMEN Krommewalstraat 9 since 01.01.2025; VE 2.290.523.752 SAMEN Hekkenstraat 1 8720 Dentergem since 20.10.2023; VE 2.317.778.178 Residentie Kloosterhof Kloosterhof 49 8720 Dentergem since 01.07.2019); VZW since 17.06.2019; RSZ2025 87.301 ROB; FOI samentielt@gvo.be; leftover mined city_tielt WZC after leftover-type hunt; Dentergem VE only; NOT De Zonnewende remine; NOT De Luifel remine; NOT Mivalti remine",
f"{SRC_SBM},NBB Consult / SBM fiche SAMEN 0728627079 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0728627079,NBB Consult / SBM,{DAY},official_register,tick2501; deposit-id 2026-00229914 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID fb2c07a2-6951-11f1-b667-13b7f733fa50; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},SAMEN FOI contact leftover city_tielt WZC,https://www.samentielt.gvo.be/,SAMEN VZW leftover city_tielt WZC 3 VE,{DAY},foi_contact,tick2501; FOI samentielt@gvo.be; official KBO zetel Krommewalstraat 9 8700 Tielt; WZC + AW + DVC GVO; RSZ2025 87.301 ROB; leftover mined city_tielt WZC; Dentergem VE only; NOT De Zonnewende remine; NOT De Luifel remine; NOT Mivalti remine; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},SAMEN,ASBL SAMEN,SAMEN VZW (leftover city_tielt WZC),parastatal,city_tielt,nl,https://www.samentielt.gvo.be/,samentielt@gvo.be,Krommewalstraat 9 8700 Tielt,tick2501 YE2025 Strong official native NBB PDF deposit 2026-00229914 + Strong KBO 0728.627.079 Actief 3 VE; omzet70 JUMP 14791167 material not commercial-only; 73 JUMP 2813573; 76A DROP 72928; envelope omzet70 JUMP 14791167; 70/76A JUMP 18017846; pnl IMPROVED LOSS -305249; 9901 FLIP 247706; equity DROP 6321909; assets DROP 39656390; debt DROP 33334481; FTE JUMP 177.6; kapitaalsubsidies JUMP 527989; destin691 empty; cash DROP 2242270; geldbeleggingen empty; leftover city_tielt WZC 3 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_samen_omzet_jr2025_statutory,{EID},2025,14791167,14791167,14791167,NBB VOL-VZW code 70 omzet YE2025 JUMP +21.77% (material not commercial-only),{SRC_PDF},strong,tick2501; PDF p7 native; YE2024 12146758; 6.9 WZC 5475358 / AW 970790 / DVC 33872 / Mut-RIZIV 8012625 / Andere 298523",
f"bud_samen_73_jr2025_statutory,{EID},2025,2813573,2813573,2813573,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +3.66%,{SRC_PDF},strong,tick2501; PDF p7 native; YE2024 2714341; 733 2813573; 730 empty; 731 empty; 732 empty; FOI RIZIV/VL/zorgkas/gemeente matrix behind omzet+73",
f"bud_samen_opbr_jr2025_statutory,{EID},2025,14791167,14791167,14791167,NBB VOL-VZW envelope omzet 70 YE2025 JUMP +21.77% (VZW because omzet material not commercial-only),{SRC_PDF},strong,tick2501; PDF p7 native; YE2024 12146758; 70/76A 18017846 JUMP; 76A 72928 DROP",
f"bud_samen_76A_jr2025_statutory,{EID},2025,72928,72928,72928,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -64.58%,{SRC_PDF},strong,tick2501; PDF p7 native; YE2024 205923; 764/8 72928",
f"bud_samen_pnl_jr2025_statutory,{EID},2025,-305249,-305249,-305249,NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 IMPROVED LOSS (was -469342),{SRC_PDF},strong,tick2501; PDF p8 native; YE2024 -469342; bedrijfswinst 9901 247706 FLIP PROFIT; destin691 empty",
f"bud_samen_bedrijfswinst_jr2025_statutory,{EID},2025,247706,247706,247706,NBB VOL-VZW code 9901 bedrijfswinst YE2025 FLIP PROFIT (was -134997),{SRC_PDF},strong,tick2501; PDF p7 native; YE2024 -134997; 62 11898410 JUMP; 630 1840163 JUMP; 66A 218387 JUMP; 640/8 128921 JUMP; 635/9 -7932; 631/4 4539",
f"bud_samen_equity_jr2025_statutory,{EID},2025,6321909,6321909,6321909,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -3.36%,{SRC_PDF},strong,tick2501; PDF p6 native; YE2024 6541650; kapitaalsubsidies 15 527989 JUMP; overgedragen 14 423920 DROP; fondsen 10 5370001 FLAT",
f"bud_samen_assets_jr2025_statutory,{EID},2025,39656390,39656390,39656390,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -7.02%,{SRC_PDF},strong,tick2501; PDF p5 native; YE2024 42649653; MVA 22/27 35309292 JUMP; cash 2242270 DROP; geldbeleggingen empty; aanbouw 27 empty FLIP (was 14149626)",
f"bud_samen_debt_jr2025_statutory,{EID},2025,33334481,33334481,33334481,NBB VOL-VZW code 17/49 schulden YE2025 DROP -7.66%,{SRC_PDF},strong,tick2501; PDF p6 native; YE2024 36100071; 17 29263911 DROP; 42/48 4053845 DROP",
f"bud_samen_cash_jr2025_statutory,{EID},2025,2242270,2242270,2242270,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -35.11%,{SRC_PDF},strong,tick2501; PDF p5 native; YE2024 3455661; geldbeleggingen 50/53 empty; capex 8161 777795; 8181 14463659",
f"bud_samen_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty),{SRC_PDF},strong,tick2501; PDF p9 native; YE2024 destin empty; 791 empty; overgedragen 14 423920 DROP",
])
print("entities+budgets ok")
print("CORE1 DONE")
