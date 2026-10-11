from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2445_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_zonnetje_jr2025_nbb_pdf_2445"
SRC_KBO="src_zonnetje_kbo_2445"
SRC_SBM="src_zonnetje_sbm_2445"
SRC_SITE="src_zonnetje_site_2445"
GAP="gap_zonnetje_opgroeien_matrix_bruto_2_11m_omzet73_empty_pnl_drop_176k_destin_empty_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 t Zonnetje kinderdagverblijven deposit 2026-00162372,http://cdn.staatsbladmonitor.be/2026pdf/2026-00162372.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2445; official native PDF 49901 bytes 12p VKT-VZW 26.0.12 m04-f; header 12.06.2026; AV 04.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-20; CreationDate 2026-06-16 01:33:12 UTC OpenPDF 1.3.26; all 12p native; VKT-VZW 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO t Zonnetje kinderdagverblijven 0443.648.306,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443648306,KBO Public Search FOD Economie,{DAY},official_register,tick2445; Actief; 3 VE 2.154.838.667 BKO Dol-fijn Kasteellaan 1 9840 Nazareth-De Pinte since 03.07.2006; 2.218.012.589 KDV t sprookjesparadijs Hedekensdriesstraat 18A 9770 Kruisem since 01.01.2010; 2.218.012.886 KDV t Regenboogje Nieuwhuizenstraat 7 8790 Waregem since 01.01.2010; naam t Zonnetje kinderdagverblijven since 20.06.2023; VZW since 10.12.1990; begindatum 10.12.1990; zetel Kasteellaan 1 9840 Nazareth-De Pinte since 01.01.2025; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI inge.moens@kdvzonnetje.be; leftover mined city_waregem + leftover mined city_kruisem; NOT Kindercentrum 0408.226.775; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Zonnestraal Junior 0866.116.859; NOT KDV De Regenboog 0671.670.560 BV; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche t Zonnetje 0443648306 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0443648306,NBB Consult,{DAY},official_register,tick2445; deposit-id 2026-00162372 YE 30/12/2025 filing 12/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},t Zonnetje FOI contact leftover city_waregem + city_kruisem CIK,https://www.kdvzonnetje.be/,VZW t Zonnetje Opgroeien CIK,{DAY},foi_contact,tick2445; FOI inge.moens@kdvzonnetje.be; zetel Kasteellaan 1 9840 Nazareth-De Pinte; leftover mined city_waregem after Kindercentrum + leftover mined city_kruisem; 3 VE Waregem + Kruisem + Nazareth-De Pinte; NOT Kloosterstraat 6 Drongen; NOT Kindercentrum; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT KDV De Regenboog BV; NOT Helan; NOT Kinderlach",
])
print("sources ok")
