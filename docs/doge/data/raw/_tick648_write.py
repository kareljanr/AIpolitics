# -*- coding: utf-8 -*-
"""Tick 648: Encours engagements + Section particuliere EU dual EFRO — rq_639."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T03:45:00Z"
TICK = 648
RQ = "rq_639"
NEXT_RQ = "rq_640"
GAP = "gap_encours_section_part_l5_2025"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str]) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and any(
            L.startswith(key + ",") or L.startswith("\ufeff" + key + ",")
            for L in existing.splitlines()
        ):
            print(f"SKIP exists {key}")
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += row + "\n"
        existing = text
        added += 1
        print(f"ADD {key}")
    path.write_bytes(text.encode("utf-8"))
    return added


def update_rq_done(path: Path, rq_id: str, notes: str) -> None:
    text = read_text(path)
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(rq_id + ",") or L.startswith("\ufeff" + rq_id + ","):
            parts = L.split(",")
            if len(parts) >= 5:
                parts[4] = "done"
            if len(parts) >= 11:
                parts[10] = NOW
            if len(parts) >= 12:
                parts[11] = notes.replace(",", ";")
            else:
                parts.append(notes.replace(",", ";"))
            L = ",".join(parts)
            print(f"RQ done {rq_id}")
        out.append(L)
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


def spawn_rq(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    if any(L.startswith(key + ",") for L in text.splitlines()):
        print(f"SKIP spawn {key}")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    path.write_bytes(text.encode("utf-8"))
    print(f"SPAWN {key}")


def set_loop_state(path: Path) -> None:
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes"
    notes = (
        f"tick{TICK} encours 7.57bn section part EU dual EFRO; "
        f"next {NEXT_RQ}; progress@650 in 2; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "encours_wal,Encours engagements Wallonie,Encours des engagements Region wallonne,Walloon commitment stock (unliquidated obligations) dual VL,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA s5.5 eoy2023 6839.6m hors section part; 12Nov2024 DO table 7565.42m; missing CRAC+Sowafinal 2000.5m + dechets promesses 77.2m; dual VL open commitments; tick648",
    "section_particuliere_wal,Section particuliere UE Wallonie,Section particuliere cofinancements europeens RW,Walloon EU cofinancing special section Feder FSE dual EFRO VL,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA ch.7 BI2025 section10 start -311.766m rec 389.143m dep 158.745m eoy -81.368m; Feder2127 rec 92 dep 39.291; FSE2127 rec 67.589 dep 65.579; dual EFRO VL; tick648",
]

src_rows = [
    "src_ccrek_encours_section_part_bi2025,CoA Budget RW encours engagements + section particuliere dual EFRO,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick648: encours eoy2023 6839.6m hors SP; BA2024 potential +107.1m; BI2025 potential -1013.0m (CL>CE); incomplete +CRAC/Sowafinal 2000.5m + dechets promesses 77.2m; DO table encours 12Nov2024 total 7565.42m (DO10 2488.4 DO18 1638.6 DO14 1524.9 DO16 708.2 DO17 615.3); DO36 CE 224.791 CL 57.987 path eng -207.725; section part BI2025 rec 389.143 dep 158.745 start -311.766 eoy -81.368; Feder2127 92/39.291 FSE2127 67.589/65.579 Feder1420 close 183.402; effort structurel dep 242.782m",
    "src_dual_encours_eu_wal_vl_tick648,Dual WAL encours + EU section vs VL EFRO commitments,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA encours + prior VL EFRO,2026-08-01,synthesis,Strong dual: WAL encours 7.57bn + incomplete +2.08bn class vs VL open commitment stacks; section part Feder/FSE dual EFRO Flanders; not TE-additive; tick648",
]

bud_rows = [
    # Encours core
    "bud_encours_eoy2023,encours_wal,2023,6839600000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,Encours engagements eoy2023 6839.6m hors section particuliere CoA s5.5; tick648",
    "bud_encours_12nov2024,encours_wal,2024,7565420000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,Encours DO table total 7565.42m at 12 Nov 2024; tick648",
    "bud_encours_potential_plus_ba2024,encours_wal,2024,107100000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,BA2024 CE-CL gap +107.1m potential encours increase; tick648",
    "bud_encours_potential_minus_bi2025,encours_wal,2025,1013000000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,BI2025 CL-CE surplus 1013.0m potential encours reduction; tick648",
    "bud_encours_missing_crac_sowafinal_2023,encours_wal,2023,2000500000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,CRAC+Sowafinal conventions not in encours stock eoy2023 2000.5m CoA; tick648",
    "bud_encours_missing_dechets_promesses_2023,encours_wal,2023,77200000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,Waste infra firm promises not in encours eoy2023 77.2m; tick648",
    "bud_encours_incomplete_add_2023,encours_wal,2023,2077700000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,Sum missing CRAC/Sowafinal+dechets 2000.5+77.2=2077.7m; true stock class ~8917m; tick648",
    # DO-level encours 12/11/2024
    "bud_encours_do10_12nov2024,do10_secretariat_wal,2024,2488401000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO10 encours 2488.401m 12Nov2024 (PRW-heavy); tick648",
    "bud_encours_do18_12nov2024,wallonie_gov,2024,1638625000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO18 encours 1638.625m 12Nov2024; tick648",
    "bud_encours_do14_12nov2024,wallonie_gov,2024,1524936000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO14 encours 1524.936m 12Nov2024; tick648",
    "bud_encours_do16_12nov2024,wallonie_gov,2024,708213000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO16 encours 708.213m 12Nov2024; tick648",
    "bud_encours_do17_12nov2024,wallonie_gov,2024,615290000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO17 encours 615.290m 12Nov2024; tick648",
    "bud_encours_do15_12nov2024,wallonie_gov,2024,381032000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO15 encours 381.032m 12Nov2024; tick648",
    "bud_encours_do11_12nov2024,wallonie_gov,2024,95234000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO11 encours 95.234m 12Nov2024; tick648",
    "bud_encours_do09_12nov2024,wallonie_gov,2024,44560000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO09 encours 44.560m 12Nov2024; tick648",
    "bud_encours_do12_12nov2024,wallonie_gov,2024,32010000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO12 Digital encours 32.010m 12Nov2024; tick648",
    "bud_encours_do19_12nov2024,wallonie_debt,2024,35933000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,DO19 Finances encours 35.933m 12Nov2024; tick648",
    # DO36 EU provisions
    "bud_do36_cofinanc_ce_bi2025,section_particuliere_wal,2025,224791000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,DO36 EU cofinanc 2021-27 CE BI2025 224.791m path eng -207.725m; tick648",
    "bud_do36_cofinanc_cl_bi2025,section_particuliere_wal,2025,57987000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,DO36 EU cofinanc 2021-27 CL BI2025 57.987m path +6.830m; tick648",
    "bud_do36_cofinanc_ce_ba2024,section_particuliere_wal,2024,432516000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,DO36 BA2024 CE 432.516m; tick648",
    "bud_do34_cofinanc_legacy_cl_ba2024,section_particuliere_wal,2024,56252000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,DO34 2014-20 cofinanc BA2024 CL 56.252m zeroed BI2025; tick648",
    # Section particuliere
    "bud_sp_start_2025,section_particuliere_wal,2025,-311766000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Section part solde 01/01/25 -311.766m (kEUR); tick648",
    "bud_sp_recettes_bi2025,section_particuliere_wal,2025,389143000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Section part recettes BI2025 389.143m; tick648",
    "bud_sp_depenses_bi2025,section_particuliere_wal,2025,158745000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Section part depenses BI2025 158.745m; tick648",
    "bud_sp_eoy2025,section_particuliere_wal,2025,-81368000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Section part solde eoy2025 est -81.368m; tick648",
    "bud_sp_feder2127_rec_bi2025,section_particuliere_wal,2025,92000000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Feder 2021-27 recettes BI2025 92.0m; tick648",
    "bud_sp_feder2127_dep_bi2025,section_particuliere_wal,2025,39291000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Feder 2021-27 depenses BI2025 39.291m; tick648",
    "bud_sp_feder2127_start_2025,section_particuliere_wal,2025,-100111000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Feder 2021-27 solde 01/01/25 -100.111m; tick648",
    "bud_sp_fse2127_rec_bi2025,section_particuliere_wal,2025,67589000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,FSE 2021-27 recettes BI2025 67.589m; tick648",
    "bud_sp_fse2127_dep_bi2025,section_particuliere_wal,2025,65579000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,FSE 2021-27 depenses BI2025 65.579m; tick648",
    "bud_sp_feder1420_rec_bi2025,section_particuliere_wal,2025,183402000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Feder 2014-20 recettes close BI2025 183.402m (zero eoy); tick648",
    "bud_sp_rtet_dep_bi2025,section_particuliere_wal,2025,51624000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,RTE-T depenses BI2025 51.624m; tick648",
    "bud_effort_structurel_dep_bi2025,wallonie_gov,2025,242782000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Effort structurel depenses BI2025 242.782m (economy 101.065m 42pct); tick648",
    "bud_total_cl_bi2025_wal,wallonie_gov,2025,22029416000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Total general CL BI2025 22029.416m CoA DO table; tick648",
    "bud_total_ce_bi2025_wal,wallonie_gov,2025,21016449000,,,budgeted,src_ccrek_encours_section_part_bi2025,strong,Total general CE BI2025 21016.449m CoA DO table; tick648",
    "bud_exec_cl_12nov2024_wal,wallonie_gov,2024,16428938000,,,outturn,src_ccrek_encours_section_part_bi2025,strong,Execution CL 12Nov2024 16428.938m (75.4pct of BA CL); tick648",
]

cmt_rows = [
    'cmt_encours_wal_coa_bi2025,Encours engagements Wallonie CoA s5.5 BI2025,encours_wal,Third-party contractors subsidy recipients,Decret budget RW + CoA s5.5,2023-12-31,2023,2025,7565420000,"{""eoy2023_m"":6839.6,""nov2024_m"":7565.42,""potential_plus_ba2024_m"":107.1,""potential_minus_bi2025_m"":1013.0,""missing_crac_sowafinal_m"":2000.5,""missing_dechets_m"":77.2,""incomplete_add_m"":2077.7,""true_stock_class_m"":8917,""note"":""Strong CoA; stock not annual TE; incomplete perimeter""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Unliquidated commitment stock,Publish full L5 DO/project encours; include CRAC/Sowafinal,src_ccrek_encours_section_part_bi2025,strong,Wallonie>Encours,tick648',
    'cmt_section_particuliere_eu_bi2025,Section particuliere EU cofinancing BI2025 dual EFRO,section_particuliere_wal,EU project promoters Feder FSE,EU structural funds + CoA ch.7,2021-01-01,2025,2027,389143000,"{""start_m"":-311.766,""rec_m"":389.143,""dep_m"":158.745,""eoy_m"":-81.368,""feder2127_rec_m"":92,""feder2127_dep_m"":39.291,""fse2127_rec_m"":67.589,""fse2127_dep_m"":65.579,""do36_ce_m"":224.791,""do36_cl_m"":57.987,""note"":""Strong CoA; dual VL EFRO not TE-additive""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,EU cofinancing special section,Absorb absorption risk; dual EFRO VL FOI,src_ccrek_encours_section_part_bi2025,strong,Wallonie>Section_particuliere,tick648',
    'cmt_effort_structurel_dep_bi2025,Effort structurel depenses 242.8m BI2025 by minister,wallonie_gov,SPW UAP subsidy recipients,Gouvernement wallon budget 2025,2024-11-15,2025,2025,242782000,"{""total_m"":242.782,""economy_m"":101.065,""economy_pct"":42,""mobility_m"":39.253,""mobility_pct"":16,""common_m"":61.766,""common_pct"":25,""health_m"":23.036,""note"":""Strong CoA Table26; not all structural if under-consumed lines""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Structural expenditure effort path,Track delivery vs underuse FOI,src_ccrek_encours_section_part_bi2025,strong,Wallonie>Effort_structurel,tick648',
    'cmt_dual_encours_eu_wal_vl_2025,Dual WAL encours 7.57bn + EU section vs VL EFRO,encours_wal,Regional commitment and EU stacks,CoA WAL + prior VL EFRO,2024-11-15,2024,2025,0,"{""wal_encours_nov2024_m"":7565.42,""wal_incomplete_m"":2077.7,""wal_sp_rec_m"":389.143,""note"":""Not TE-additive dual commitment/EU stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional commitment dual map,Cross-region encours transparency,src_dual_encours_eu_wal_vl_tick648,strong,Belgium>Encours_EU>dual,tick648',
    'cmt_do36_cofinanc_2127_bi2025,DO36 EU cofinancing provision 2021-27 BI2025,section_particuliere_wal,Regional match funding projects,Budget RW DO36,2024-11-15,2025,2027,224791000,"{""ce_m"":224.791,""cl_m"":57.987,""path_eng_m"":-207.725,""ba_ce_m"":432.516,""note"":""Eng collapse vs sticky CL residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Regional EU match provision,Map to section part liquidations FOI,src_ccrek_encours_section_part_bi2025,strong,Wallonie>DO36>Cofinanc,tick648',
]

lb_rows = [
    "lb_encours_7_57bn_2024,Encours engagements 7.57bn 12Nov2024,Wallonia,ops,Wallonie>Encours>7_57bn,7565420000,7565420000,Strong CoA: DO table encours 7565.42m; eoy2023 6839.6m; incomplete +2078m CRAC/Sowafinal/dechets,strong,src_ccrek_encours_section_part_bi2025,Contractors subsidy recipients,Unliquidated commitment stock,Mega stock opacity residual dual,7.5,9.0,4,7.65,FOI full L5 encours map + incomplete perimeter,seed,,tick648",
    "lb_encours_incomplete_2_08bn_2023,Encours incomplete CRAC/Sowafinal/dechets 2.08bn,Wallonia,ops,Wallonie>Encours>incomplete_2_08bn,2077700000,2077700000,Strong CoA: CRAC+Sowafinal 2000.5m + dechets promesses 77.2m excluded from official encours,strong,src_ccrek_encours_section_part_bi2025,Local infra waste operators,Off-book commitment perimeter,Governance understatement residual,7.5,8.5,4,7.40,Include in official encours FOI,seed,,tick648",
    "lb_encours_do10_2_49bn_2024,DO10 PRW encours 2.49bn 12Nov2024,Wallonia,ops,Wallonie>Encours>DO10_2_49bn,2488401000,2488401000,Strong CoA: DO10 encours 2488.401m largest DO share PRW-heavy,strong,src_ccrek_encours_section_part_bi2025,PRW operators,Unliquidated recovery commitments,Dual PRW opacity residual,6.5,8.5,4,6.95,FOI project L5 encours,seed,,tick648",
    "lb_sp_eu_rec_389m_2025,Section particuliere EU rec 389m BI2025,Wallonia,ops,Wallonie>Section_part>rec_389m,389143000,389143000,Strong CoA ch.7: SP rec 389.143m dep 158.745m start -311.8m eoy -81.4m; Feder+FSE dual EFRO,strong,src_ccrek_encours_section_part_bi2025,EU project promoters,EU cofinancing special section,Absorption risk residual,5.5,7.5,4,6.10,FOI project L5 dual EFRO,seed,,tick648",
    "lb_do36_cofinanc_path_208m_2025,DO36 cofinanc eng path -208m BI2025,Wallonia,ops,Wallonie>DO36>path_eng_208m,207725000,224791000,Strong CoA: DO36 CE path -207.725m (432.5 to 224.8); CL only 58.0m,strong,src_ccrek_encours_section_part_bi2025,EU match funding,Regional cofinancing provision taper,Eng collapse residual,6.0,7.5,4,6.30,Map liquidations FOI,seed,,tick648",
    "lb_dual_encours_eu_wal_vl_2025,Dual WAL encours 7.57bn vs VL EFRO stacks,Belgium,ops,Belgium>Encours_EU>dual,7565420000,0,Strong dual: WAL encours 7.57bn + incomplete 2.08bn + SP 389m vs VL open commitments/EFRO; not TE-additive,strong,src_dual_encours_eu_wal_vl_tick648,BE regional taxpayers,Parallel commitment/EU stacks,Dual opacity residual,6.5,8.5,4,6.95,Cross-region encours FOI,seed,,tick648",
]

foi_row = (
    f"{GAP},Wallonie>Encours_SectionPart>L5_2025,encours_wal,"
    "Full encours L5 by DO/programme/project 2023-2025; incomplete CRAC/Sowafinal 2.0bn + dechets 77m "
    "inclusion; section part Feder/FSE/RTE-T project list; DO36 match map; dual VL EFRO,"
    "CoA encours+SP totals strong tick648; L5 residual dual,"
    "5,SPW Budget / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_encours_wal_coa_bi2025|cmt_section_particuliere_eu_bi2025|cmt_dual_encours_eu_wal_vl_2025,"
    "lb_encours_7_57bn_2024|lb_encours_incomplete_2_08bn_2023|lb_dual_encours_eu_wal_vl_2025,"
    f"{NOW},{NOW},tick648 CoA encours section part primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW s5.5 encours + ch.7 section particulière; dual VL EFRO prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Encours engagements + section particulière UE L5

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Ventilation L5 de l'encours des engagements au 31/12/2023, 12/11/2024
   et 31/12/2024 (si disponible): par division organique, programme et
   projet (CoA: eoy2023 6.839,6 mEUR; 12/11/2024 7.565,4 mEUR).
2. Inclusion ou justification de l'exclusion des engagements CRAC et
   Sowafinal (2.000,5 mEUR eoy2023) et des promesses fermes déchets
   (77,2 mEUR) — mise à jour 2024-2025.
3. Section particulière BI2025: liste des projets Feder 2021-27, FSE
   2021-27, RTE-T avec montants recettes/dépenses et bénéficiaires
   (CoA: rec 389,1 / dep 158,7 mEUR).
4. Cartographie DO36 provisions cofinancement 2021-27 (CE 224,8 /
   CL 58,0 mEUR) vers liquidations section particulière.
5. Effort structurel dépenses 242,8 mEUR: lignes budgétaires exactes
   et état d'exécution à mi-2025.

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 §5.5 + DO table encours col + ch.7.
- Dual VL: EFRO Flanders / open commitment stacks (prior).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual encours/EU hole-fill -- **Encours engagements + Section particuliere** dual EFRO)
- Found: **Encours** (primary CoA s5.5): eoy2023 **EUR6.840bn** (hors SP); 12Nov2024 DO table **EUR7.565bn**; BI2025 potential reduction **EUR1.013bn** (CL>CE); incomplete **+EUR2.078bn** (CRAC/Sowafinal **EUR2.001bn** + dechets **EUR77.2m**). Top DO encours: DO10 **EUR2.488bn** / DO18 **EUR1.639bn** / DO14 **EUR1.525bn**. **Section particuliere:** rec **EUR389.1m** / dep **EUR158.7m** / start **-EUR311.8m** / eoy **-EUR81.4m**; Feder2127 rec **EUR92m** dep **EUR39.3m**; FSE2127 **EUR67.6/65.6m**. **DO36** CE **EUR224.8m** path eng **-EUR207.7m**. Effort structurel dep **EUR242.8m**. Dual **EFRO VL**. Strong confidence CoA; L5 residual FOI.
- Wrote: entities (+2); budgets (+36); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@650 in 2 ticks; rq_116 deferred
"""


def main() -> None:
    n_ent = append_rows(ROOT / "entities.csv", ent_rows)
    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_bud = append_rows(ROOT / "budgets.csv", bud_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    n_foi = append_rows(ROOT / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    if not draft_path.exists():
        draft_path.write_text(foi_draft, encoding="utf-8")
        print(f"WROTE draft {draft_path.name}")
    else:
        print(f"SKIP draft exists {draft_path.name}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} encours 7.57bn section part EU dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after encours dual; rq_116 deferred; progress@650 in 2",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log_text = read_text(LOG)
    if f"-- tick {TICK}" not in log_text[-3000:]:
        if not log_text.endswith("\n"):
            log_text += "\n"
        log_text += log_entry
        LOG.write_bytes(log_text.encode("utf-8"))
        print("LOG appended")
    else:
        print("SKIP log already has tick")

    print(
        f"DONE tick{TICK}: ent+{n_ent} src+{n_src} bud+{n_bud} cmt+{n_cmt} lb+{n_lb} foi+{n_foi}"
    )


if __name__ == "__main__":
    main()
