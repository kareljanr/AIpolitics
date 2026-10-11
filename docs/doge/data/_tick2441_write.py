from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2441_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hummeltjes_jr2025_nbb_pdf_2441"
SRC_KBO="src_hummeltjes_kbo_2441"
SRC_SBM="src_hummeltjes_sbm_2441"
SRC_SITE="src_hummeltjes_site_2441"
GAP="gap_hummeltjes_opgroeien_matrix_opbr_13_11m_omzet_1_40m_73_11_28m_pnl_drop_259k_destin_drop_70k_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Hummeltjes deposit 2026-00225380,http://cdn.staatsbladmonitor.be/2026pdf/2026-00225380.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2441; official native PDF 436041 bytes 45p VOL-VZW 23.0.10 m05-f; header 30.06.2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-23; CreationDate 2026-06-30 22:33:04 UTC OpenPDF 1.3.26; financials pp.1-38 native text euros; commissarisverslag pp.39-45 native Moore Audit BV oordeel zonder voorbehoud; VOL-VZW 6.1 6.2.1-6.2.4 6.4.1-6.4.3 6.5.1-6.5.3 6.13 6.14 6.16 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Hummeltjes 0409.987.425,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409987425,KBO Public Search FOD Economie,{DAY},official_register,tick2441; Actief; 13 VE zetel 2.145.112.933 Zuster Stanislaslaan 1 3500 Hasselt since 02.01.1998 + 6/13 VE Hasselt; naam De Hummeltjes vzw since 18.06.2018; VZW since 29.08.1958; begindatum 29.08.1958; zetel Zuster Stanislaslaan 1 3500 Hasselt since 01.01.2025; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; Pinnochio 0438.745.648 opgeslorpt since 20.12.2023; Klein Hemelrijk 0413.866.336 opgeslorpt since 31.03.2026 na YE2025; FOI info@hummeltjes.be; NOT De Ukkies 0412.729.654; NOT Grauwzusters 0409.771.748; NOT Jessa 0821.142.117; NOT Kinderlach 0450.275.186; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche De Hummeltjes 0409987425 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0409987425,NBB Consult,{DAY},official_register,tick2441; deposit-id 2026-00225380 YE 30/12/2025 filing 30/06/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Hummeltjes FOI contact leftover city_hasselt CIK,https://www.hummeltjes.be/,VZW De Hummeltjes Opgroeien CIK+BOA+CKG,{DAY},foi_contact,tick2441; FOI info@hummeltjes.be; tel 011 22 50 34; zetel Zuster Stanislaslaan 1 3500 Hasselt; leftover mined city_hasselt after De Ukkies / Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; Opgroeien CIK+BOA+CKG; site 450 plaatsen / 6 KDV + 2 BOA; 13 VE zetel Hasselt; NOT Kloosterstraat 6 Drongen; NOT De Ukkies; NOT Grauwzusters convent; NOT Jessa hospital; NOT Klein Hemelrijk remine; NOT Pinnochio remine; NOT Kinderlach; NOT Helan",
])
print("sources ok")
