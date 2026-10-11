#!/usr/bin/env python3
"""Surgical patch rq_2423=done + spawn rq_2424; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2423_stamp.txt").read_text().strip().splitlines()
GAP = "gap_zonnelied_ieper_zorg_matrix_omzet_10_95m_73_2_43m_opbr_13_61m_pnl_jump_280k_destin_240k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
n2423 = rq_raw.count(b"rq_2423,")
if n2423 != 1:
    raise SystemExit(f"expected 1 rq_2423 marker, found {n2423}")
if b"rq_2424," in rq_raw:
    raise SystemExit("rq_2424 already exists")

new_2423 = (
    "rq_2423,leftover dual — Huize Zonnelied YE2025 Strong (omzet JUMP 10.95m / 73 2.43m / opbr JUMP 13.61m / pnl JUMP 280k / destin 240k),"
    "hole_fill,8,done,L5,vzw_huize_zonnelied,"
    "Tick 2423 leftover after Wintershove. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem; NOT ARC; NOT VERBINT; NOT CFR Zelzate; NOT De Kade; NOT Ter Eecken; NOT De Hoeksteen; NOT De Mereltjes; NOT 3Wplus; NOT t Eekhoorntje; NOT Elfenbankje; NOT Zonnestraal Junior; NOT KINDEROPVANG ZONNESTRAAL; NOT Kinderopvang Turnhout; NOT Bengelhof; NOT Buitenschoolse Opvang Ieper; NOT Kinderopvang Mariawende; NOT Denderkind; NOT BKO GENK-OOST; NOT KOS; NOT De Pagadder; NOT WZC De Ruyschaert; NOT Quattro; NOT Wintershove). "
    "Took Huize Zonnelied VZW 0415.082.497 deposit 2026-00185108 leftover city_ieper / Quattro-lid. Distinct from Wintershove 0459.245.312 and Quattro 0555.667.072 and WZC De Ruyschaert 0434.996.993 and De Pagadder 0888.028.268 and from Kloosterstraat 6 Drongen. Distinct from Zonnelied Roosdaal 0420.607.638 already in entities. Distinct from WZC De Linde Lievegem 0467.355.403 already in entities. Distinct from Vormingscentrum 0413.342.338 training. "
    "Do NOT redo Wintershove/Quattro/WZC De Ruyschaert/De Pagadder/KOS/BKO GENK-OOST/Denderkind/Kinderopvang Mariawende/Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg/Zonnestraal parent stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. AZ Sint-Maria 0467.967.491 CDN 403 skip. CAR Noorderkempen 0408.078.010 YE2025 2026-00145984 SCAN skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T04:51:48Z,{STAMP},"
    "tick2423 Huize Zonnelied 0415.082.497 YE2025 Strong official native PDF 2026-00185108; omzet70 JUMP 10947653 envelope not commercial-only; 73 DROP 2431251; 76A empty; opbr 70/76A JUMP 13607953; pnl JUMP 280337; 9901 DROP 411779; equity JUMP 9780553; assets DROP 20080302; debt DROP 10217646; FTE 147.6; kapitaalsubsidies DROP 4944671; destin691 JUMP 240169; cash DROP 190094; geldbeleggingen JUMP 2390338; gebouwen DROP 10636541; aanbouw JUMP 1686141; 1 VE Stationsstraat 24 Ieper leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; FOI ready NOT sent; leftover city_ieper; NOT every-10; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal\n"
)
new_2424 = (
    "rq_2424,leftover dual after Huize Zonnelied — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Huize Zonnelied YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930; NOT VERBINT 0408.032.379; NOT CFR Zelzate 0419.645.952; NOT De Kade 0413.650.659; NOT Ter Eecken 0432.465.392; NOT De Hoeksteen 0765.439.866; NOT De Mereltjes 0412.778.352; NOT 3Wplus 0893.870.539; NOT t Eekhoorntje 0414.453.680; NOT Elfenbankje 0417.638.151; NOT Zonnestraal Junior 0866.116.859; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Kinderopvang Turnhout 0465.284.947; NOT Bengelhof 0455.442.813; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Kinderopvang Mariawende 0411.611.184; NOT Denderkind 0479.127.045; NOT BKO GENK-OOST 0475.432.830; NOT KOS 0891.472.362; NOT De Pagadder 0888.028.268; NOT WZC De Ruyschaert 0434.996.993; NOT Quattro 0555.667.072; NOT Wintershove 0459.245.312; NOT Huize Zonnelied 0415.082.497). "
    "Do NOT redo Huize Zonnelied/Wintershove/Quattro/WZC De Ruyschaert/De Pagadder/KOS/BKO GENK-OOST/Denderkind/Kinderopvang Mariawende/Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 2026-00145984 SCAN 1.09MB Ricoh no native euros — skip unless OCR. Zeepreventorium still YE2024. De Bolster still YE2024. Vormingscentrum 0413.342.338 leftover city_gent 2026-00134360 53k training not CIK — only if leftover training of mined parent is in LOOP.md priority. Helan Kinderopvang 0464.151.037 leftover city_antwerpen 2026-00206337 909k Helan-HH-adjacent skip (Helan HH family already skipped). NEXT leftover candidates: unused Quattro-member WZC OLV Gasthuis Poperinge 0445.066.385 leftover city_poperinge 2026-00306712 CDN live YE2025 HEAD 200 Last-Modified 02.08.2026 1571427 B — take ONLY if unused + official YE2025 PDF euros; WZC De Linde Wortegem-Petegem 0425.773.085 (Quattro-lid; NOT WZC De Linde Lievegem 0467.355.403 already in entities) — take ONLY if unused + official YE2025 PDF euros; St Jozef Zonnebeke and Sint-Vincentius Avelgem already in entities skip; Zonnelied Roosdaal already in entities skip; do NOT invent from Companyweb/Belscope. Else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital of a mined Flanders city with TRUE YE2025 statutory PDF. Next every-10 is 2430.,"
    f",{STAMP},{STAMP},"
    "spawned after tick2423; Huize Zonnelied taken leftover city_ieper / Quattro-lid after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef / Quattro@2421; Noorderkempen scan skip; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; AGB/FARO/Gandae still YE2024; next every-10 is 2430\n"
)

idx = rq_raw.rfind(b"rq_2423,")
if idx < 0:
    raise SystemExit("rq_2423 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2423.encode("utf-8"))
    f.write(new_2424.encode("utf-8"))
print("patched research_queue rq_2423 + rq_2424; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2423,2423,no,"
    "tick2423 leftover dual Huize Zonnelied 0415.082.497 Strong native PDF (omzet70 JUMP 10947653 envelope not commercial-only; 73 DROP 2431251; 76A empty; opbr 70/76A JUMP 13607953; pnl JUMP 280337; 9901 DROP 411779; equity JUMP 9780553; assets DROP 20080302; debt DROP 10217646; FTE 147.6; kapitaalsubsidies DROP 4944671; destin691 JUMP 240169; cash DROP 190094; geldbeleggingen JUMP 2390338; gebouwen DROP 10636541; aanbouw JUMP 1686141; 1 VE Stationsstraat 24 Ieper); leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; NOT every-10; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Kinderopvang Mariawende OFF Denderkind OFF BKO GENK-OOST OFF KOS OFF De Pagadder OFF WZC De Ruyschaert OFF Quattro OFF Wintershove OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum OFF WZC De Linde Lievegem OFF Zonnelied Roosdaal; AGB/FARO/Gandae YE2024; next rq_2424; next every-10 2430\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2422,2422," not in cur:
    raise SystemExit("loop_state not at 2422; abort")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")
