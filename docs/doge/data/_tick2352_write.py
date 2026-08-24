# tick 2352 rq_2352 De Branding WAAK YE2025
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

EID = "vzw_de_branding_waak_kuurne"
GAP = "gap_de_branding_waak_nbb_pdf_assets_debt_bruto_gt_omzet_6_58x_pnl_drop_fte_jump_vaph_matrix_l5"
LB = "lb_de_branding_waak_bruto_23_07m_omzet_3_51m_6_58x_pnl_drop_fte_jump_jr2025"
COMM = "comm_de_branding_waak_jr2025_statutory_bruto_gt_omzet_6_58x_pnl_drop_vaph"
TS = "2026-08-24T20:10:00Z"
TICK = 2352
RQ = "rq_2352"
NEXT = "rq_2353"

OMZET = 3507384
BRUTO = 23068203
PNL = 717178
EQUITY = 13121232
FTE = 277.5
RATIO = 6.58

assert DATA.is_dir(), DATA

def append_unique(path: Path, lines: list[str], key: str):
    text = path.read_text(encoding="utf-8")
    if key in text:
        print(f"skip existing {key} in {path.name}")
        return False
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"appended {len(lines)} -> {path.name}")
    return True

srcs = [
    f"src_de_branding_waak_jr2025_cw_nl,Companyweb NL De Branding WAAK YE2025,https://www.companyweb.be/nl/0441399092/de-branding-waak-vzw,Companyweb,2026-08-24,commercial_registry_mirror,tick{TICK}; Medium CW NL; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE} filed 14.05.2026",
    f"src_de_branding_waak_jr2025_cw_en,Companyweb EN De Branding WAAK YE2025,https://www.companyweb.be/en/0441399092/de-branding-waak-vzw,Companyweb,2026-08-24,commercial_registry_mirror,tick{TICK}; Medium CW EN; bruto~{RATIO}x; pnl DROP; FTE JUMP",
    f"src_de_branding_waak_jr2025_cw_fr,Companyweb FR De Branding WAAK YE2025,https://www.companyweb.be/fr/0441399092/de-branding-waak-vzw,Companyweb,2026-08-24,commercial_registry_mirror,tick{TICK}; Medium CW FR; confirm YE2025",
    f"src_de_branding_waak_kbo,KBO De Branding WAAK 0441.399.092,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0441399092,KBO FOD Economie,2026-08-24,official_register,tick{TICK}; Strong KBO Actief Aanbestedende 7 VE RSZ 87.202 BTW 87.202+88.106",
    f"src_de_branding_waak_site_contact,De Branding FOI info@debranding.be,https://www.debranding.be/contact,de branding WAAK VZW,2026-08-24,foi_contact,tick{TICK}; info@debranding.be; Ringlaan 30 8500 Kortrijk; zetel Heirweg 125 Kuurne",
    f"src_de_branding_waak_nbb_consult,NBB CBSO consult De Branding WAAK,https://consult.cbso.nbb.be/consult-enterprise/0441399092,NBB,2026-08-24,official_register,tick{TICK}; PDF pending FOI",
]
append_unique(DATA / "sources.csv", srcs, "src_de_branding_waak_jr2025_cw_nl")

buds = [
    f"bud_de_branding_waak_omzet_jr2025_statutory,{EID},2025,{OMZET},{OMZET},{OMZET},CW statutory omzet YE2025 JUMP +6.06%,src_de_branding_waak_jr2025_cw_en,medium,tick{TICK}; vs 3307036",
    f"bud_de_branding_waak_bruto_jr2025_statutory,{EID},2025,{BRUTO},{BRUTO},{BRUTO},CW statutory bruto YE2025 ~{RATIO}x omzet,src_de_branding_waak_jr2025_cw_en,medium,tick{TICK}; primary L5",
    f"bud_de_branding_waak_pnl_jr2025_statutory,{EID},2025,{PNL},{PNL},{PNL},CW statutory pnl YE2025 DROP -20.88%,src_de_branding_waak_jr2025_cw_en,medium,tick{TICK}",
    f"bud_de_branding_waak_equity_jr2025_statutory,{EID},2025,{EQUITY},{EQUITY},{EQUITY},CW statutory equity YE2025 JUMP +4.29%,src_de_branding_waak_jr2025_cw_en,medium,tick{TICK}",
    f"bud_de_branding_waak_fte_jr2025_statutory,{EID},2025,{FTE},{FTE},{FTE},CW FTE JUMP {FTE},src_de_branding_waak_jr2025_cw_en,medium,tick{TICK}; vs 263",
]
append_unique(DATA / "budgets.csv", buds, "bud_de_branding_waak_omzet_jr2025_statutory")

ent = (
    f"{EID},de branding WAAK VZW (Kuurne / VAPH woon+dag mentale handicap),"
    f"de branding WAAK ASBL (Kuurne / hebergement + jour handicap mental),"
    f"de branding WAAK VZW (Kuurne / VAPH residential+day care mental disability),"
    f"parastatal,sec_flanders,nl,https://www.debranding.be,info@debranding.be,"
    f"\"Heirweg 125, 8520 Kuurne\","
    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0441.399.092 Actief Aanbestedende 7 VE RSZ 87.202 BTW 87.202+88.106; "
    f"omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; filed 14.05.2026; "
    f"FOI {GAP}; WAAK maatwerk dual same zetel; AGB/FARO YE2024; not TE-additive"
)
append_unique(DATA / "entities.csv", [ent], EID + ",")

cash = (
    '{"2025_omzet":3507384,"2025_bruto":23068203,"2025_pnl":717178,"2025_equity":13121232,"2025_fte":277.5,'
    '"2024_omzet":3307036,"2024_bruto":20746940,"2024_pnl":906403,"2024_equity":12581946,"2024_fte":263.0}'
)
comm = (
    f"{COMM},De Branding WAAK YE2025 leftover dual (omzet 3.51m / bruto 23.07m ~{RATIO}x / pnl DROP / FTE JUMP / Medium),"
    f"{EID},personen mentale handicap Zuid-West-Vlaanderen / VAPH + WAAK groep,"
    f"VZW de branding WAAK (KBO 0441.399.092; Actief; Aanbestedende; 7 VE; RSZ 87.202),"
    f"2026-05-14,2025,2025,{BRUTO},\"{cash}\",0,active,"
    f"https://www.companyweb.be/en/0441399092/de-branding-waak-vzw,"
    f"VAPH residential+day care adults mental disability,"
    f"Publish NBB PDF; reconcile bruto>>omzet ~{RATIO}x + VAPH matrix,"
    f"src_de_branding_waak_jr2025_cw_en,medium,"
    f"Vlaanderen>WestVlaanderen>Kuurne>DeBrandingWAAK>JR2025_statutory_L5,"
    f"tick{TICK}; Medium CW; after Korenbloem@2351; not TE-additive"
)
append_unique(DATA / "commitments.csv", [comm], COMM)

lb = (
    f"{LB},De Branding WAAK bruto 23.07m / omzet 3.51m ~{RATIO}x / pnl DROP / FTE JUMP (YE2025),"
    f"L5,vaph_vzw_statutory,Vlaanderen>WestVlaanderen>Kuurne>DeBrandingWAAK>JR2025,"
    f"{BRUTO},{BRUTO},"
    f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} / equity {EQUITY} / FTE {FTE} / filed 14.05.2026,"
    f"medium,src_de_branding_waak_jr2025_cw_en,"
    f"VAPH adults mental disability Kuurne-Kortrijk / WAAK groep dual,"
    f"Residential+day care adults with mental disability,"
    f"bruto JUMP +11.19%; bruto>>omzet ~{RATIO}x (23.07m vs 3.51m); pnl DROP -20.88%; equity JUMP +4.29%; FTE JUMP {FTE}; 7 VE Aanbestedende; filed 14.05.2026,"
    f"7.5,5.5,3.0,6.35,"
    f"Publish NBB PDF assets/debt/cash FOI; disclose bruto>>omzet ~{RATIO}x composition (VAPH PVB/RTH vs commercial omzet); reconcile pnl DROP while bruto JUMP; 7-VE cost allocation as aanbestedende overheid; WAAK maatwerk dual opacity,"
    f"open,,tick{TICK}; Medium CW; FOI {GAP}; stall AGB Bornem JR2024 / FARO/AIESH/Gandae/Aralea/Manupal/Vlotter YE2024; after Korenbloem@2351; not TE-additive of 348bn"
)
append_unique(DATA / "leaderboard.csv", [lb], LB)

foi = (
    f"{GAP},Vlaanderen>WestVlaanderen>Kuurne>DeBrandingWAAK>NBB_PDF,{EID},"
    f"NBB PDF YE2025 assets/debt; bruto {BRUTO} ~{RATIO}x omzet {OMZET}; pnl DROP {PNL}; VAPH/PVB matrix + WAAK dual,"
    f"Medium CW Aanbestedende VAPH Kuurne bruto 23.07m ~{RATIO}x omzet; assets/debt Unknown; pnl DROP with bruto JUMP,"
    f"8,de branding WAAK VZW,info@debranding.be,\"Ringlaan 30 / Heirweg 125, 8520 Kuurne\","
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-24,,,,,,"
    f"{COMM},{LB},{TS},{TS},"
    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO"
)
append_unique(DATA / "foi_queue.csv", [foi], GAP)

draft = f"""# FOI draft — de branding WAAK Kuurne (NBB PDF / bruto>>omzet ~{RATIO}x / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** de branding WAAK VZW — KBO **0441.399.092** (Actief; Aanbestedende; Heirweg 125, 8520 Kuurne; FTE {FTE}; 7 VE; RSZ **87.202**)  
**recipient:** info@debranding.be · Ringlaan 30 8500 Kortrijk / zetel Heirweg 125 Kuurne  
**tick:** {TICK} · **confidence:** Medium

## Context
CW YE2025: omzet **EUR{OMZET}** (+6.06%); bruto **EUR{BRUTO}** (~**{RATIO}x**); pnl **EUR{PNL}** DROP -20.88%; equity **EUR{EQUITY}**; FTE **{FTE}**; filed **14.05.2026**. WAAK maatwerk dual same zetel.

## Brief
```text
Aan: de branding WAAK VZW via info@debranding.be
Betreft: Openbaarmaking jaarrekening 2025 de branding WAAK (KBO 0441.399.092)
1. NBB/CBSO PDF YE2025 (activa/schulden/cash)
2. Toelichting bruto EUR{BRUTO} >> omzet EUR{OMZET} (~{RATIO}x) — VAPH/PVB/RTH vs commercieel
3. Toelichting pnl DROP EUR{PNL} terwijl bruto JUMP +11.19%
4. Overzicht publieke toelagen YE2025 + relatie WAAK maatwerk (zelfde zetel)
5. Schulden LT/KT en liquide middelen; kostentoerekening 7 VE
Ref: {GAP}
```
- [x] ready NOT sent
"""
draft_path = FOI / f"{GAP}.md"
if not draft_path.exists():
    draft_path.write_text(draft, encoding="utf-8")
    print(f"wrote {draft_path.name}")
else:
    print(f"skip draft {draft_path.name}")

rq_path = DATA / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = None
for line in rq.splitlines():
    if line.startswith(f"{RQ},"):
        old = line
        break
if not old:
    raise SystemExit(f"{RQ} not found")
new = (
    f"{RQ},leftover dual — De Branding WAAK YE2025 Medium (bruto JUMP 23.07m / ~{RATIO}x omzet / pnl DROP / FTE JUMP {FTE}),"
    f"hole_fill,8,done,L5,{EID},"
    f"After Korenbloem@2351. Prefer AGB/FARO YE2025 else FREE. Do NOT redo Korenbloem/Leieborg/Helan HH/Oostrem/Staf stack.,"
    f"{GAP},2026-08-24T20:00:00Z,{TS},"
    f"tick{TICK}; De Branding WAAK 0441.399.092 YE2025 Medium (omzet {OMZET}; bruto {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 7 VE Aanbestedende); FOI {GAP} ready not sent; next EVERY-10 2360"
)
rq = rq.replace(old, new)
if f"{NEXT}," not in rq:
    spawn = (
        f"{NEXT},leftover dual after De Branding WAAK — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk,"
        f"hole_fill,8,open,L5,,"
        f"After De Branding WAAK@2352. Prefer AGB/FARO YE2025 else FREE (Gandae/Aralea/Manupal/Vlotter if YE2025). Do NOT redo De Branding WAAK/Korenbloem/Leieborg/Helan HH stack.,,"
        f"{TS},{TS},spawned after tick{TICK} De Branding WAAK; next EVERY-10 2360"
    )
    if not rq.endswith("\n"):
        rq += "\n"
    rq += spawn + "\n"
    print(f"spawned {NEXT}")
rq_path.write_text(rq, encoding="utf-8")
print("updated research_queue")

state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{RQ},{TICK},no,"
    f"tick{TICK} leftover dual De Branding WAAK 0441.399.092 Medium (omzet JUMP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 7 VE Aanbestedende); after Korenbloem@2351; AGB/FARO YE2024; next {NEXT}; next EVERY-10 2360\n"
)
(DATA / "loop_state.csv").write_text(state, encoding="utf-8")
print("updated loop_state")

log_block = f"""
### {TS} - tick {TICK} - {RQ} De Branding WAAK Kuurne (bruto JUMP 23.07m / ~{RATIO}x omzet / pnl DROP / FTE JUMP {FTE} / Medium)

- Unit: **{RQ}** leftover dual after **Korenbloem@2351**. Prefer NON-stall: AGB Bornem still **JR2024**; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Took FREE Flemish VAPH **de branding WAAK VZW** YE2025 (KBO **0441.399.092**; Heirweg 125, 8520 Kuurne; **Actief** **7 VE**; Aanbestedende; RSZ **87.202**; info@debranding.be) — WAAK maatwerk dual same zetel. Do not redo Korenbloem/Leieborg/Helan HH/Oostrem stack.
- Found: CW NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +6.06%; bruto **EUR{BRUTO}** JUMP +11.19% (~**{RATIO}x**); pnl **EUR{PNL}** DROP -20.88%; equity **EUR{EQUITY}** JUMP +4.29%; FTE **{FTE}** JUMP; neerlegging **14.05.2026**. Strong KBO. Assets/debt Unknown. Medium.
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi 6.35); entities (+1); foi + draft `{GAP}`; {RQ}=done + {NEXT} open; loop_state ticks={TICK}.
- FOI: **ready not sent**. NOT every-10 (next **2360**). Next: {NEXT}.
"""
log_text = LOG.read_text(encoding="utf-8")
if f"tick {TICK} - {RQ}" not in log_text:
    LOG.write_text(log_text.rstrip() + "\n" + log_block, encoding="utf-8")
    print("appended loop_log")
else:
    print("skip log")

print(f"DONE tick {TICK}")
