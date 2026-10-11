#!/usr/bin/env python3
"""Surgical patch rq_2415=done + spawn rq_2416; do not rewrite whole 63MB file."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2415_stamp.txt").read_text().strip().splitlines()
GAP = "gap_mariawende_opgroeien_matrix_bruto_3_35m_omzet73_empty_pnl_jump_736k_destin_736k_l5"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
n2415 = rq_raw.count(b"rq_2415,")
if n2415 != 1:
    raise SystemExit(f"expected 1 rq_2415 marker, found {n2415}")
if b"rq_2416," in rq_raw:
    raise SystemExit("rq_2416 already exists")

new_2415 = (
    "rq_2415,leftover dual — Kinderopvang Mariawende YE2025 Strong (bruto JUMP 3.35m / omzet+73 empty / pnl JUMP 736k / destin 736k),"
    "hole_fill,8,done,L5,vzw_mariawende,"
    "Tick 2415 leftover after Buitenschoolse Opvang Ieper. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens; NOT CAR Roeselare; NOT Ascendere; NOT CAR De Klinker; NOT CAR De Hert; NOT REVA Kohesi; NOT CGG Kohesi; NOT Beschut Wonen Kohesi; NOT LDSST; NOT De Schans; NOT CAR Houtland; NOT Zonnebloem; NOT ZWZ; NOT CAR Horizon; NOT CAR Accent; NOT Waas; NOT CAR Halle Asse; NOT Heuvelheem; NOT ARC; NOT VERBINT; NOT CFR Zelzate; NOT De Kade; NOT Ter Eecken; NOT De Hoeksteen; NOT De Mereltjes; NOT 3Wplus; NOT t Eekhoorntje; NOT Elfenbankje; NOT Zonnestraal Junior; NOT KINDEROPVANG ZONNESTRAAL; NOT Kinderopvang Turnhout; NOT Bengelhof; NOT Buitenschoolse Opvang Ieper). "
    "Took Kinderopvang Mariawende 0411.611.184 deposit 2026-00302442 leftover city_brugge. Distinct from Buitenschoolse Opvang Ieper 0431.691.669 and from Vormingscentrum 0413.342.338 training. Distinct from Bengelhof already mined. "
    "Do NOT redo Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg/Zonnestraal parent stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie 0454.250.505 YE2024 skip. Ben Woonzorgnetwerk already in entities skip. Vriendenkring 0436.787.139 stopgezet 16.11.1995 skip. CAR Antenne 3000 0433.184.479 CDN 403 skip. AZ Sint-Maria 0467.967.491 CDN 403 skip. CAR Noorderkempen 0408.078.010 YE2025 2026-00145984 SCAN skip. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-25T03:55:33Z,{STAMP},"
    "tick2415 Kinderopvang Mariawende 0411.611.184 YE2025 Strong official native PDF 2026-00302442; bruto9900 JUMP 3345554 CIK envelope; omzet70 empty; 73 empty; 76A empty; pnl JUMP 735612; 9901 JUMP 588557; equity JUMP 6465476; assets JUMP 6896666; debt DROP 431190; FTE JUMP 45.2; kapitaalsubsidies DROP 1287136; destin691 JUMP 735612; cash JUMP 331722; geldbeleggingen JUMP 2537774; gebouwen DROP 2697443; 2 VE Ons Tuintje 140 + BKO t Speelhuis leftover city_brugge after Mintus@1269; FOI ready NOT sent; leftover city_brugge; NOT every-10 (next 2420); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum\n"
)
new_2416 = (
    "rq_2416,leftover dual after Kinderopvang Mariawende — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After Kinderopvang Mariawende YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054; NOT Ascendere 0409.470.553; NOT CAR De Klinker 0430.535.290; NOT CAR De Hert 0409.371.672; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT Beschut Wonen Kohesi 0451.932.995; NOT LDSST 0410.121.344; NOT De Schans 0430.473.231; NOT CAR Houtland 0408.436.019; NOT Zonnebloem 0421.039.386; NOT ZWZ 0832.024.923; NOT CAR Horizon 0418.529.759; NOT CAR Accent 0413.208.122; NOT Waas 0415.472.279; NOT CAR Halle Asse 0425.788.230; NOT Heuvelheem 0413.210.201; NOT ARC 0408.434.930; NOT VERBINT 0408.032.379; NOT CFR Zelzate 0419.645.952; NOT De Kade 0413.650.659; NOT Ter Eecken 0432.465.392; NOT De Hoeksteen 0765.439.866; NOT De Mereltjes 0412.778.352; NOT 3Wplus 0893.870.539; NOT t Eekhoorntje 0414.453.680; NOT Elfenbankje 0417.638.151; NOT Zonnestraal Junior 0866.116.859; NOT KINDEROPVANG ZONNESTRAAL 0413.351.642; NOT Kinderopvang Turnhout 0465.284.947; NOT Bengelhof 0455.442.813; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Kinderopvang Mariawende 0411.611.184). "
    "Do NOT redo Kinderopvang Mariawende/Buitenschoolse Opvang Ieper/Bengelhof/Kinderopvang Turnhout/KINDEROPVANG ZONNESTRAAL/Zonnestraal Junior/Elfenbankje/t Eekhoorntje/3Wplus/De Mereltjes/De Hoeksteen/Ter Eecken/De Kade/CFR Zelzate/VERBINT/Carrewiel/ARC/Heuvelheem/CAR Halle Asse/Waas/CAR Accent/CAR Horizon/ZWZ/Zonnebloem/CAR Houtland/De Schans/LDSST/Beschut Wonen Kohesi/REVA Kohesi/CGG Kohesi/CAR De Hert/CAR De Klinker/Ascendere/CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. CAR Overleie YE2024 skip. Ben already in entities skip. Vriendenkring 0436.787.139 stopgezet skip. CAR Antenne 3000 leftover city_leuven CDN 403 re-HEAD only. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB 2026-00299006 CDN 403 skip unless official PDF downloads. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 2026-00145984 SCAN 1.09MB Ricoh no native euros — skip unless OCR. Zeepreventorium still YE2024. De Bolster still YE2024. Vormingscentrum 0413.342.338 leftover city_gent 2026-00134360 53k training not CIK — only if leftover training of mined parent is in LOOP.md priority. Helan Kinderopvang 0464.151.037 leftover city_antwerpen 2026-00206337 909k Helan-HH-adjacent skip (Helan HH family already skipped). Hunt unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital of another mined Flanders city with live official YE2025 PDF euros; do NOT invent from Companyweb/Belscope.,"
    f",{STAMP},{STAMP},"
    "spawned after tick2415; Kinderopvang Mariawende taken leftover city_brugge after Mintus; Noorderkempen scan skip; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; AGB/FARO/Gandae still YE2024; next every-10 is 2420\n"
)

idx = rq_raw.rfind(b"rq_2415,")
if idx < 0:
    raise SystemExit("rq_2415 line not found")
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2415.encode("utf-8"))
    f.write(new_2416.encode("utf-8"))
print("patched research_queue rq_2415 + rq_2416; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2415,2415,no,"
    "tick2415 leftover dual Kinderopvang Mariawende 0411.611.184 Strong native PDF (bruto9900 JUMP 3345554 CIK envelope; omzet70 empty; 73 empty; 76A empty; pnl JUMP 735612; 9901 JUMP 588557; equity JUMP 6465476; assets JUMP 6896666; debt DROP 431190; FTE JUMP 45.2; kapitaalsubsidies DROP 1287136; destin691 JUMP 735612; cash JUMP 331722; geldbeleggingen JUMP 2537774; gebouwen DROP 2697443; 2 VE Ons Tuintje 140 + BKO t Speelhuis); leftover city_brugge after Mintus@1269; NOT every-10 (next 2420); OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Horizon OFF Accent OFF Waas OFF Halle Asse OFF Heuvelheem OFF ARC OFF VERBINT OFF CFR Zelzate OFF De Kade OFF Ter Eecken OFF De Hoeksteen OFF De Mereltjes OFF 3Wplus OFF t Eekhoorntje OFF Elfenbankje OFF Zonnestraal Junior OFF KINDEROPVANG ZONNESTRAAL OFF Kinderopvang Turnhout OFF Bengelhof OFF Buitenschoolse Opvang Ieper OFF Ten Anker OFF Leieborg OFF m-accent Eeklo OFF Vriendenkring OFF Antenne 3000 OFF Noorderkempen scan OFF Zilverbos OFF Grimbergen VAPH Zonnestraal OFF Helan OFF Vormingscentrum; AGB/FARO/Gandae YE2024; next rq_2416; next every-10 2420\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
if ",rq_2414,2414," not in cur:
    raise SystemExit("loop_state not at 2414; abort")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")
print("rq+state ok")
