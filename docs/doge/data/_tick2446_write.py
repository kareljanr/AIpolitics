from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2446_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_kinderkuren_jr2025_nbb_pdf_2446"
SRC_KBO="src_kinderkuren_kbo_2446"
SRC_SBM="src_kinderkuren_sbm_2446"
SRC_SITE="src_kinderkuren_site_2446"
GAP="gap_kinderkuren_leuven_matrix_bruto_4_67m_omzet73_empty_pnl_flip_loss_618k_destin_drop_680k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderkuren (Kinderopvang Leuven) deposit 2026-00321398,http://cdn.staatsbladmonitor.be/2026pdf/2026-00321398.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2446; official native PDF 1096996 bytes 53p VKT-VZW 26.0.15 m04-f; header 23.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-03; CreationDate 2026-07-23 13:52:34 UTC OpenPDF 1.3.26; all 53p native; VKT-VZW 6.3 7 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderkuren 0478.167.834,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0478167834,KBO Public Search FOD Economie,{DAY},official_register,tick2446; Actief; 37 VE; naam Kinderkuren since 18.12.2025 (PDF header still Kinderopvang Leuven); VZW since 18.12.2001; begindatum 18.12.2001; zetel Professor Van Overstraetenplein 1 3000 Leuven since 05.10.2010; aanbestedende overheid since 18.12.2001; EVA Stad Leuven; RSZ2025 88.919; VE 2.157.823.396 Stadskantoor vzw; FOI kinderkuren@leuven.be; leftover mined city_leuven; NOT Wigwam 0435.015.207; NOT t Anemoontje 0413.354.612; NOT IZW 0430.278.439; NOT Monte Rosa 0413.350.751; NOT De Wissel 0421.913.376; NOT De Slabbertjes 0411.972.064; NOT t Zonnetje 0443.648.306; NOT Kinderdagverblijven Leuven 0413.321.255 absorbed; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderkuren 0478167834 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0478167834,NBB Consult,{DAY},official_register,tick2446; deposit-id 2026-00321398 YE 30/12/2025 filing 23/07/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Kinderkuren FOI contact leftover city_leuven EVA,https://www.leuven.be/kinderopvang-kinderkuren,VZW Kinderkuren Stad Leuven EVA BKO,{DAY},foi_contact,tick2446; FOI kinderkuren@leuven.be; zetel Professor Van Overstraetenplein 1 3000 Leuven; kantoor Tiensevest 132 3000 Leuven; leftover mined city_leuven after Wigwam / t Anemoontje / IZW / Monte Rosa / De Wissel / De Slabbertjes; 37 VE; NOT Kloosterstraat 6 Drongen; NOT t Zonnetje; NOT Wigwam; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
