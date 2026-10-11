from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2499_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_ten_dries_jr2025_nbb_pdf_2499"
SRC_KBO="src_ten_dries_kbo_2499"
SRC_SBM="src_ten_dries_sbm_2499"
SRC_SITE="src_ten_dries_site_2499"
EID="vzw_ten_dries_deinze"
GAP="gap_ten_dries_deinze_vaph_matrix_70_76A_9_39m_omzet_commercial_73_jump_8_65m_pnl_drop_106k_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Vierklaver 0436.015.889 remine leftover city_deinze VAPH; NOT leftover city_eeklo via Vierklaver VE; NOT Leieborg 0418.832.835 remine; NOT Demival 0407.409.007 remine; NOT Ascendere remine leftover city_eeklo; NOT Kinderlach YE2024 leftover city_eeklo; NOT Villa Boempatat leftover city_gent; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Ten Dries deposit 2026-00212085,http://cdn.staatsbladmonitor.be/2026pdf/2026-00212085.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2499; official native statutory PDF 600892 bytes 47p VOL-VZW 23.0.10 m05-f; header 29.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-29 13:05:48 UTC OpenPDF 1.3.26; CDN Last-Modified 11.07.2026; statutory pages native; CDN 2026-00212085 GET 200 600892 MD5 eee8b7632f1b92e53134733b1ffa9da6; official NBB UUID 9ab36d1a-73b9-11f1-9ea1-d77d620372b0; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.16 niet dienstig; prior-year identical not restated; commissaris Baker Tilly Bedrijfsrevisoren BV B00190 / De Blander Christel A00258; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Ten Dries 0410.571.207,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410571207,KBO Public Search FOD Economie,{DAY},official_register,tick2499; Actief; 1 VE leftover city_deinze (official zetel Poeldendries 32 9850 Deinze since 01.01.2019; VE 2.153.606.470 M.P.I. Ten Dries since 19.05.2006); VZW since 15.01.1955; RSZ2025 88.103; FOI tendries@tendries.be; leftover mined city_deinze VAPH/MFC after leftover-type hunt; NOT Vierklaver remine; NOT leftover city_eeklo via Vierklaver VE",
f"{SRC_SBM},NBB Consult / SBM fiche Ten Dries 0410571207 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0410571207,NBB Consult / SBM,{DAY},official_register,tick2499; deposit-id 2026-00212085 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial UUID 9ab36d1a-73b9-11f1-9ea1-d77d620372b0; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},Ten Dries FOI contact leftover city_deinze VAPH/MFC,https://tendries.be/,Ten Dries VZW leftover city_deinze VAPH/MFC 1 VE,{DAY},foi_contact,tick2499; FOI tendries@tendries.be; official KBO zetel Poeldendries 32 9850 Deinze; MFC VAPH woon+dag minderjarigen motorische/meervoudige handicap; RSZ2025 88.103; leftover mined city_deinze VAPH/MFC; NOT Vierklaver remine; NOT leftover city_eeklo via Vierklaver VE; NOT Leieborg remine; NOT Demival remine; NOT leftover-via-VE",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Multifunctioneel Centrum Ten Dries,ASBL MFC Ten Dries,MFC Ten Dries VZW (leftover city_deinze VAPH/MFC),parastatal,city_deinze,nl,https://tendries.be/,tendries@tendries.be,Poeldendries 32 9850 Deinze,tick2499 YE2025 Strong official native NBB PDF deposit 2026-00212085 + Strong KBO 0410.571.207 Actief 1 VE; omzet70 JUMP 357127 commercial-only vs large 73; 73 JUMP 8648576; 76A DROP 1666; envelope 70/76A JUMP 9392001; pnl DROP 106116; 9901 DROP 129620; equity JUMP 8249399; assets JUMP 12364030; debt JUMP 4114631; FTE DROP 104; kapitaalsubsidies JUMP 3272755; destin691 empty; cash DROP 386799; geldbeleggingen DROP 2773494; leftover city_deinze VAPH/MFC 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_ten_dries_omzet_jr2025_statutory,{EID},2025,357127,357127,357127,NBB VOL-VZW code 70 omzet YE2025 JUMP +5.76% (commercial-only vs large 73),{SRC_PDF},strong,tick2499; PDF p7 native; YE2024 337685; 6.9 MFC Ten Dries / België",
f"bud_ten_dries_73_jr2025_statutory,{EID},2025,8648576,8648576,8648576,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +2.44%,{SRC_PDF},strong,tick2499; PDF p7 native; YE2024 8442241; 733 8586829; 731 61747; 730 empty; 732 empty; FOI VAPH/VL/PVB/RTH/MFC/gemeente matrix behind omzet+73",
f"bud_ten_dries_opbr_jr2025_statutory,{EID},2025,9392001,9392001,9392001,NBB VOL-VZW envelope 70/76A YE2025 JUMP +1.69% (VZW because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2499; PDF p7 native; YE2024 9235672; omzet70 357127 JUMP; 76A 1666 DROP",
f"bud_ten_dries_76A_jr2025_statutory,{EID},2025,1666,1666,1666,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -98.84%,{SRC_PDF},strong,tick2499; PDF p7 native; YE2024 143409",
f"bud_ten_dries_pnl_jr2025_statutory,{EID},2025,106116,106116,106116,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -75.12%,{SRC_PDF},strong,tick2499; PDF p8 native; YE2024 426430; bedrijfswinst 9901 129620 DROP; destin691 empty",
f"bud_ten_dries_bedrijfswinst_jr2025_statutory,{EID},2025,129620,129620,129620,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -55.38%,{SRC_PDF},strong,tick2499; PDF p7 native; YE2024 290502; 62 7904740 JUMP; 630 417814 JUMP; 66A 110674 DROP; 640/8 34038 JUMP; 635/9 empty; 631/4 empty",
f"bud_ten_dries_equity_jr2025_statutory,{EID},2025,8249399,8249399,8249399,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +34.14%,{SRC_PDF},strong,tick2499; PDF p6 native; YE2024 6149819; kapitaalsubsidies 15 3272755 JUMP; overgedragen 14 2293920 JUMP; fondsen 10 852623 FLAT; bestemde fondsen 13 1830101 FLAT",
f"bud_ten_dries_assets_jr2025_statutory,{EID},2025,12364030,12364030,12364030,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +32.73%,{SRC_PDF},strong,tick2499; PDF p5 native; YE2024 9314476; MVA 22/27 8815314 JUMP; cash 386799 DROP; geldbeleggingen 2773494 DROP; aanbouw 27 empty FLIP",
f"bud_ten_dries_debt_jr2025_statutory,{EID},2025,4114631,4114631,4114631,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +30.02%,{SRC_PDF},strong,tick2499; PDF p6 native; YE2024 3164657; 17 2308316 JUMP; 42/48 1802077 DROP",
f"bud_ten_dries_cash_jr2025_statutory,{EID},2025,386799,386799,386799,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -31.80%,{SRC_PDF},strong,tick2499; PDF p5 native; YE2024 567131; geldbeleggingen 50/53 2773494 DROP; capex 5258768",
f"bud_ten_dries_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 FLAT 1830101),{SRC_PDF},strong,tick2499; PDF p9 native; YE2024 destin empty; 791 empty; fondsen 10 852623 FLAT",
])
print("entities+budgets ok")
print("CORE1 DONE")
