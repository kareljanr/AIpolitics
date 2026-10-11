from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2498_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_meredal_jr2025_nbb_pdf_2498"
SRC_KBO="src_meredal_kbo_2498"
SRC_SBM="src_meredal_sbm_2498"
SRC_SITE="src_meredal_site_2498"
EID="vzw_meredal_erpe_mere"
GAP="gap_meredal_erpe_mere_wzc_matrix_omzet_8_22m_73_drop_1_09m_pnl_drop_185k_cash_drop_1_32m_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Avondzon 0419.044.057 remine leftover city_erpe_mere WZC; NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 YE2024; NOT Maria Boodschap 0415.653.116 absorbed into De Medemens 0428.692.191 leftover-via-VE; NOT leftover city_niel via Maria Boodschap; NOT Hope 0548.641.403 serviceflats; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Meredal deposit 2026-00108199,http://cdn.staatsbladmonitor.be/2026pdf/2026-00108199.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2498; official native statutory PDF 1675808 bytes 44p VOL-VZW 25.0.11 m05-f; header 07.05.2026; AV 29.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-12 01:14:54 UTC OpenPDF 1.3.26; CDN Last-Modified 05.06.2026; statutory pages native; CDN 2026-00108199 GET 200 1675808 MD5 a4a6206ebf62abf5ccc9d08d0683b0e2; official NBB UUID 15d657bd-4a25-11f1-aad4-9d0c78a15cab; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; prior-year identical not restated; commissaris VYVEY & C° BEDRIJFSREVISOREN B00523 / Koopman Vincent; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Meredal 0419.333.671,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419333671,KBO Public Search FOD Economie,{DAY},official_register,tick2498; Actief; 1 VE leftover city_erpe_mere (official zetel Vijverstraat 38 9420 Erpe-Mere since 17.06.2004; VE 2.154.994.362 since 10.07.2006); VZW since 20.02.1979; RSZ2025 87.301; aanbestedende overheid since 18.01.2003; FOI administratie@wzcmeredal.be; leftover mined city_erpe_mere WZC after leftover-type hunt; NOT Avondzon remine; NOT WZC Sint-Vincentius YE2024",
f"{SRC_SBM},NBB Consult / SBM fiche Meredal 0419333671 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0419333671,NBB Consult / SBM,{DAY},official_register,tick2498; deposit-id 2026-00108199 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID 15d657bd-4a25-11f1-aad4-9d0c78a15cab; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Meredal FOI contact leftover city_erpe_mere WZC,https://www.meredal.be/,Meredal VZW leftover city_erpe_mere WZC 1 VE,{DAY},foi_contact,tick2498; FOI administratie@wzcmeredal.be; official KBO zetel Vijverstraat 38 9420 Erpe-Mere; WZC + assistentiewoningen De Merelaar + De Valeriaan; RSZ2025 87.301 ROB; leftover mined city_erpe_mere WZC; NOT Avondzon remine; NOT WZC Sint-Vincentius YE2024; NOT Maria Boodschap absorbed; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Meredal,ASBL Meredal,Meredal VZW (leftover city_erpe_mere WZC),parastatal,city_erpe_mere,nl,https://www.meredal.be/,administratie@wzcmeredal.be,Vijverstraat 38 9420 Erpe-Mere,tick2498 YE2025 Strong official native NBB PDF deposit 2026-00108199 + Strong KBO 0419.333.671 Actief 1 VE; omzet70 JUMP 8224110 material not commercial-only; 73 DROP 1091421; 76A DROP 10; envelope omzet70 JUMP 8224110; 70/76A JUMP 9464409; pnl DROP 185241; 9901 DROP 374227; equity JUMP 10586696; assets DROP 20590835; debt DROP 9571459; FTE JUMP 92.4; kapitaalsubsidies DROP 0; destin691 DROP 185241; cash DROP 1316785; geldbeleggingen JUMP 4081030; leftover city_erpe_mere WZC 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_meredal_omzet_jr2025_statutory,{EID},2025,8224110,8224110,8224110,NBB VOL-VZW code 70 omzet YE2025 JUMP +3.19% (material not commercial-only),{SRC_PDF},strong,tick2498; PDF p7 native; YE2024 7969825; 6.9 no category split",
f"bud_meredal_73_jr2025_statutory,{EID},2025,1091421,1091421,1091421,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -7.93%,{SRC_PDF},strong,tick2498; PDF p7 native; YE2024 1185364; 733 1091371; 731 50; 730 empty; 732 empty; FOI RIZIV/VL/zorgkas/gemeente matrix behind omzet+73",
f"bud_meredal_opbr_jr2025_statutory,{EID},2025,8224110,8224110,8224110,NBB VOL-VZW envelope omzet 70 YE2025 JUMP +3.19% (VZW because omzet material not commercial-only),{SRC_PDF},strong,tick2498; PDF p7 native; YE2024 7969825; 70/76A 9464409 JUMP; 76A 10 DROP",
f"bud_meredal_76A_jr2025_statutory,{EID},2025,10,10,10,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -99.98%,{SRC_PDF},strong,tick2498; PDF p7 native; YE2024 54715",
f"bud_meredal_pnl_jr2025_statutory,{EID},2025,185241,185241,185241,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -75.84%,{SRC_PDF},strong,tick2498; PDF p8 native; YE2024 766756; bedrijfswinst 9901 374227 DROP; destin691 DROP 185241",
f"bud_meredal_bedrijfswinst_jr2025_statutory,{EID},2025,374227,374227,374227,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -60.48%,{SRC_PDF},strong,tick2498; PDF p7 native; YE2024 946927; 62 6737249 JUMP; 630 715291 DROP; 66A 867 DROP; 640/8 5815 JUMP; 635/9 0 FLIP; 631/4 empty",
f"bud_meredal_equity_jr2025_statutory,{EID},2025,10586696,10586696,10586696,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +1.77%,{SRC_PDF},strong,tick2498; PDF p6 native; YE2024 10402887; kapitaalsubsidies 15 0 DROP; overgedragen 14 empty; fondsen 10 2905934 FLAT; bestemde fondsen 13 7680762 JUMP",
f"bud_meredal_assets_jr2025_statutory,{EID},2025,20590835,20590835,20590835,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -3.18%,{SRC_PDF},strong,tick2498; PDF p5 native; YE2024 21266694; MVA 22/27 14680019 DROP; cash 1316785 DROP; geldbeleggingen 4081030 JUMP; aanbouw 27 empty",
f"bud_meredal_debt_jr2025_statutory,{EID},2025,9571459,9571459,9571459,NBB VOL-VZW code 17/49 schulden YE2025 DROP -8.24%,{SRC_PDF},strong,tick2498; PDF p6 native; YE2024 10431127; 17 7776295 DROP; 42/48 1754319 JUMP",
f"bud_meredal_cash_jr2025_statutory,{EID},2025,1316785,1316785,1316785,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -55.30%,{SRC_PDF},strong,tick2498; PDF p5 native; YE2024 2945791; geldbeleggingen 50/53 4081030 JUMP; capex 63438",
f"bud_meredal_destin_jr2025_statutory,{EID},2025,185241,185241,185241,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -75.84% (791 empty; 13 JUMP 7680762),{SRC_PDF},strong,tick2498; PDF p9 native; YE2024 destin 766756; 791 empty; fondsen 10 2905934 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")
