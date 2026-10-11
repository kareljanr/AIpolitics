from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2496_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_vierklaver_jr2025_nbb_pdf_2496"
SRC_KBO="src_vierklaver_kbo_2496"
SRC_SBM="src_vierklaver_sbm_2496"
SRC_SITE="src_vierklaver_site_2496"
EID="vzw_vierklaver_deinze"
GAP="gap_vierklaver_deinze_vaph_matrix_70_76A_13_91m_omzet_commercial_73_jump_11_51m_destin_jump_3_50m_pnl_flip_213k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT leftover city_eeklo (Eeklo is VE only; zetel Deinze); NOT Leieborg 0418.832.835 remine; NOT Demival 0407.409.007 remine; NOT Ascendere remine leftover city_eeklo; NOT KISME remine; NOT Jeugdhulp Don Bosco remine; NOT Trento remine; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Vierklaver deposit 2026-00178582,http://cdn.staatsbladmonitor.be/2026pdf/2026-00178582.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2496; official native statutory PDF 771087 bytes 49p VOL-VZW 25.0.13 m05-f; header 16.06.2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-20 05:30:55 UTC OpenPDF 1.3.26; CDN Last-Modified 22.06.2026; statutory pages native; CDN 2026-00178582 GET 200 771087 MD5 d063ba72784ed69e01739b9b06430d0d; official NBB UUID fea3c017-33d9-11f1-84fe-b5d060e5ffd7; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.5.1-3 6.14 6.16 niet dienstig; prior-year identical not restated; commissaris EY Bedrijfsrevisoren BV / Vyvey Line; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Vierklaver 0436.015.889,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0436015889,KBO Public Search FOD Economie,{DAY},official_register,tick2496; Actief; 6 VE leftover city_deinze (zetel Haarkenstraat 32 bus A000 9850 Deinze since 01.01.2019; VE 2.138.447.548 Haarkenstraat 32 Deinze + 2.274.588.335 Ten Bosse 151 Deinze + 2.138.447.647 Lenen 7 Maldegem + 2.138.447.746 Krommewege 44 Maldegem + 2.289.058.359 Garenstraat 46 Eeklo + 2.325.972.403 Adegem-Dorp 23B Maldegem); VZW since 01.12.1988; RSZ2025 87.202; FOI secretariaat@de-vierklaver.be; leftover mined city_deinze VAPH after leftover-type hunt; NOT leftover city_eeklo; NOT Leieborg remine; NOT Demival remine",
f"{SRC_SBM},NBB Consult / SBM fiche Vierklaver 0436015889 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0436015889,NBB Consult / SBM,{DAY},official_register,tick2496; deposit-id 2026-00178582 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID fea3c017-33d9-11f1-84fe-b5d060e5ffd7; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},De Vierklaver FOI contact leftover city_deinze VAPH,https://www.de-vierklaver.be/,De Vierklaver VZW leftover city_deinze VAPH 6 VE,{DAY},foi_contact,tick2496; FOI secretariaat@de-vierklaver.be; zetel Haarkenstraat 32 bus A000 9850 Deinze; campus hanNAH Garenstraat 46 9900 Eeklo; RSZ2025 87.202 VAPH; leftover mined city_deinze VAPH; NOT leftover city_eeklo; NOT Leieborg remine; NOT Demival remine; NOT Ascendere remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},De Vierklaver,ASBL De Vierklaver,De Vierklaver VZW (leftover city_deinze VAPH),parastatal,city_deinze,nl,https://www.de-vierklaver.be/,secretariaat@de-vierklaver.be,Haarkenstraat 32 bus A000 9850 Deinze,tick2496 YE2025 Strong official native NBB PDF deposit 2026-00178582 + Strong KBO 0436.015.889 Actief 6 VE; omzet70 JUMP 1746754 commercial-only vs large 73; 73 JUMP 11513087; 76A empty; envelope 70/76A JUMP 13914807; pnl FLIP LOSS 213049; 9901 DEEPER LOSS 234486; equity DROP 6745980; assets JUMP 9723578; debt JUMP 2977598; FTE JUMP 138; kapitaalsubsidies DROP 1894593; destin691 JUMP 3500000; 791 empty; cash JUMP 3450957; geldbeleggingen empty; leftover city_deinze VAPH 6 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_vierklaver_omzet_jr2025_statutory,{EID},2025,1746754,1746754,1746754,NBB VOL-VZW code 70 omzet YE2025 JUMP +6.11% (commercial-only vs large 73),{SRC_PDF},strong,tick2496; PDF p7 native; YE2024 1646162; 6.9 no category split",
f"bud_vierklaver_73_jr2025_statutory,{EID},2025,11513087,11513087,11513087,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +3.58%,{SRC_PDF},strong,tick2496; PDF p7 native; YE2024 11114718; 733 11485019; 731 28068; 730 empty; 732 empty; FOI VAPH/VL/PVB/RTH matrix behind omzet+73",
f"bud_vierklaver_opbr_jr2025_statutory,{EID},2025,13914807,13914807,13914807,NBB VOL-VZW envelope 70/76A bedrijfsopbrengsten YE2025 JUMP +3.51% (VZW because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2496; PDF p7 native; YE2024 13443065; omzet 1746754 commercial-only; 76A empty",
f"bud_vierklaver_76A_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty (was 9275),{SRC_PDF},strong,tick2496; PDF p7 native; YE2024 9275",
f"bud_vierklaver_pnl_jr2025_statutory,{EID},2025,-213049,-213049,-213049,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was +32058),{SRC_PDF},strong,tick2496; PDF p8 native; YE2024 32058; bedrijfswinst 9901 -234486 DEEPER LOSS; destin691 JUMP 3500000",
f"bud_vierklaver_bedrijfswinst_jr2025_statutory,{EID},2025,-234486,-234486,-234486,NBB VOL-VZW code 9901 bedrijfsverlies YE2025 DEEPER LOSS (was -2120),{SRC_PDF},strong,tick2496; PDF p7 native; YE2024 -2120; 62 11379257 JUMP; 630 688570 JUMP; 66A 4072 JUMP; 640/8 451333 DROP; 635/9 empty; 631/4 empty",
f"bud_vierklaver_equity_jr2025_statutory,{EID},2025,6745980,6745980,6745980,NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -6.15%,{SRC_PDF},strong,tick2496; PDF p6 native; YE2024 7187755; kapitaalsubsidies 15 1894593 DROP; overgedragen 14 574862 DROP; fondsen 10 126525 FLAT; bestemde fondsen 13 4150000 JUMP",
f"bud_vierklaver_assets_jr2025_statutory,{EID},2025,9723578,9723578,9723578,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +1.55%,{SRC_PDF},strong,tick2496; PDF p5 native; YE2024 9574696; MVA 22/27 5294299 DROP; cash 3450957 JUMP; geldbeleggingen empty; aanbouw 27 256647 JUMP",
f"bud_vierklaver_debt_jr2025_statutory,{EID},2025,2977598,2977598,2977598,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +24.74%,{SRC_PDF},strong,tick2496; PDF p6 native; YE2024 2386941; 17 150931 DROP; 42/48 2803509 JUMP",
f"bud_vierklaver_cash_jr2025_statutory,{EID},2025,3450957,3450957,3450957,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +43.56%,{SRC_PDF},strong,tick2496; PDF p5 native; YE2024 2403820; geldbeleggingen 50/53 empty; capex 213405",
f"bud_vierklaver_destin_jr2025_statutory,{EID},2025,3500000,3500000,3500000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty; 791 empty; 13 JUMP 4150000),{SRC_PDF},strong,tick2496; PDF p9 native; YE2024 destin empty; 791 empty; 14 DROP 574862; fondsen 10 126525 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")
