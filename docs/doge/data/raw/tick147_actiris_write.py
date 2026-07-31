# -*- coding: utf-8 -*-
"""Tick 147: rq_134 Actiris L5 named programmes beyond total."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T22:30:00Z"
TICK = 147
UNIT = "rq_134"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n".join(lines) + "\n", enc)


append_lines(DATA / "sources.csv", [
    'src_actiris_ra_2024,Actiris Rapport annuel 2024 Budget recettes depenses L5,https://www.actiris.brussels/media/torboyqi/ra_2024-fr_ok-24-h-1065F033.pdf,Actiris,2026-07-27,annual_report,"Budget final 767506000; realized exp 729735605 (95pct); recettes realized 753574458; ACS 200.9m; 6th reform 225.0m; functioning 167.9m; partnerships 57.7m; social economy 34.5m; staff 1518/1291 ETP"',
])

# Budgets — totals + major L5 realized
append_lines(DATA / "budgets.csv", [
    "bud_actiris_budget_final_2024,actiris,2024,767506000,,,budgeted,src_actiris_ra_2024,strong,Budget final total 2024 RA",
    "bud_actiris_exp_realized_2024,actiris,2024,729735605.38,,,outturn,src_actiris_ra_2024,strong,Total depenses realisees 2024 (95.08pct execution)",
    "bud_actiris_receipts_realized_2024,actiris,2024,753574458.43,,,outturn,src_actiris_ra_2024,strong,Recettes realisees 2024 (98pct of 767.5m budget)",
    "bud_actiris_functioning_2024,actiris,2024,167894145.47,,,outturn,src_actiris_ra_2024,strong,Frais de fonctionnement realize 167.9m (budget 178.6m 23pct)",
    "bud_actiris_cheques_2024,actiris,2024,6751615.70,,,outturn,src_actiris_ra_2024,strong,Cheques chercheurs d emploi realize",
    "bud_actiris_partnerships_2024,actiris,2024,57709078.40,,,outturn,src_actiris_ra_2024,strong,Partenariats marche emploi realize 57.7m",
    "bud_actiris_secteurs_ref_2024,actiris,2024,4863102.86,,,outturn,src_actiris_ra_2024,strong,Conventions secteurs professionnels centres reference",
    "bud_actiris_acs_2024,actiris,2024,200852843.82,,,outturn,src_actiris_ra_2024,strong,Postes travail subventionnes ACS realize 200.9m (largest L5 27.5pct)",
    "bud_actiris_ptp_2024,actiris,2024,1794097.19,,,outturn,src_actiris_ra_2024,strong,Placement infrascolarisés PTP",
    "bud_actiris_jeunes_2024,actiris,2024,8808945.20,,,outturn,src_actiris_ra_2024,strong,Emploi des jeunes initiatives transversales",
    "bud_actiris_discrim_2024,actiris,2024,566665.86,,,outturn,src_actiris_ra_2024,strong,Lutte discrimination embauche",
    "bud_actiris_6th_reform_2024,actiris,2024,225018303.81,,,outturn,src_actiris_ra_2024,strong,6ieme Reforme de l Etat realize 225.0m (30.8pct largest block)",
    "bud_actiris_garantie_jeunes_2024,actiris,2024,7144229.36,,,outturn,src_actiris_ra_2024,strong,Garantie Jeunes",
    "bud_actiris_contrats_insertion_2024,actiris,2024,7330236.45,,,outturn,src_actiris_ra_2024,strong,Contrats d insertion",
    "bud_actiris_reforme_aide_2024,actiris,2024,4669212.31,,,outturn,src_actiris_ra_2024,strong,Reforme aide a l emploi (low execution 61.9pct)",
    "bud_actiris_eco_sociale_2024,actiris,2024,34481645.16,,,outturn,src_actiris_ra_2024,strong,Economie sociale realize 34.5m",
    "bud_actiris_relance_2024,actiris,2024,464000,,,outturn,src_actiris_ra_2024,strong,Plan de relance",
    "bud_actiris_ukraine_2024,actiris,2024,377853.99,,,outturn,src_actiris_ra_2024,strong,Crise Ukraine",
    "bud_actiris_nonmarchand_2024,actiris,2024,1000000,,,outturn,src_actiris_ra_2024,strong,Accord non-marchand 2021-2024",
    "bud_actiris_bru_prog_2026,actiris,2026,648113000,,,budgeted,src_ccrek_bru_budget_2026_full,strong,BCR SGRBC programme line Actiris 648.1m 2026 (regional transfer perimeter not full institutional)",
])

append_lines(DATA / "commitments.csv", [
    'cmt_actiris_l5_2024,Actiris full institutional budget L5 programme split 2024,actiris,Actiris jobseekers employers partners,Contrat de gestion Actiris 2023-2027 + RA 2024,2023-01-01,2024,2024,767506000,"{""budget_final"":767506000,""exp_realized"":729735605.38,""receipts_realized"":753574458.43,""execution_pct"":95.08,""functioning"":167894145.47,""cheques"":6751615.70,""partnerships"":57709078.40,""secteurs_ref"":4863102.86,""acs_jobs"":200852843.82,""ptp"":1794097.19,""jeunes"":8808945.20,""discrimination"":566665.86,""6th_state_reform"":225018303.81,""garantie_jeunes"":7144229.36,""contrats_insertion"":7330236.45,""reforme_aide"":4669212.31,""economie_sociale"":34481645.16,""relance"":464000,""ukraine"":377853.99,""nonmarchand"":1000000,""staff_persons"":1518,""fte"":1291,""dei_avg_2024"":91628,""note_perimeter"":""institutional 730m realized vs BCR programme transfer 648m 2026 CoA; 6th reform 225m is large federalized employment aid passthrough""}",0,active,https://www.actiris.brussels/media/torboyqi/ra_2024-fr_ok-24-h-1065F033.pdf,Brussels PES dual VDAB/FOREM,Publish 2025-26 same L5 matrix; separate ACS and 6th-reform passthrough from ops,src_actiris_ra_2024,strong,Bruxelles>Emploi>Actiris,tick147; dual PES: Actiris 730m realized vs VDAB VL 0.75bn vs FOREM 2.66bn different perimeters',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_actiris_acs_jobs,Actiris ACS subsidized jobs ~200.9m 2024,brussels,subsidy,Bruxelles>Actiris>ACS,200852844,200852844,RA2024 strong: ACS postes subventionnes 200.9m of 729.7m exp (27.5pct); budget 205.9m,strong,src_actiris_ra_2024,Subsidized job holders employers Brussels,Wage subsidies ACS employment,Deadweight risk classic wage subsidy; dual PES measure stack,7,7.5,5,7.0,Evaluate net job creation; publish unit cost per ACS; reform path ongoing,seed,,tick147",
    "lb_actiris_6th_reform,Actiris 6th State Reform employment package ~225m 2024,brussels,programme,Bruxelles>Actiris>6e_reforme,225018304,225018304,RA2024 strong: largest single block 30.8pct of exp; federalized employment competences passthrough,strong,src_actiris_ra_2024,Brussels jobseekers via transferred competences,Employment aid post-6th-reform,Passthrough opacity vs pure Actiris ops 168m,5,7.5,6,6.2,Open L5 within 6th reform envelope; compare VDAB/FOREM,seed,,tick147",
])

# research_queue
rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_134,Actiris L5 named programmes beyond total,continuous,6,open,L5,actiris,'
    '"Named Actiris programme lines with EUR.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_134,Actiris L5 named programmes beyond total,continuous,6,done,L5,actiris,'
    '"Named Actiris programme lines with EUR.",'
    "gap_actiris_2025_26_l5,2026-07-27T14:00:00Z,2026-07-27T22:30:00Z,"
    '"tick147: RA2024 full L5 ACS 200.9m 6th-reform 225m ops 167.9m total exp 729.7m; FOI 2025-26"'
)
if old not in rtext:
    raise SystemExit("rq_134 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_134" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_actiris_2025_26_l5.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_actiris_2025_26_l5`  
**Status:** ready (human send only)  
**Linked:** rq_134 · cmt_actiris_l5_2024 · lb_actiris_acs_jobs

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Actiris — publicite de l administration / transparantie
     Avenue de l Astronomie 14
     1210 Bruxelles
     et/ou SPRB Bruxelles Emploi transparence@sprb.brussels

Betreft: Verzoek om openbaarmaking — Actiris budget L5 2025-2026

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Budget final et depenses realisees 2025 (et 2026 si disponible) avec la meme
   ventilation L5 que le Rapport annuel 2024 (fonctionnement, cheques, partenariats,
   ACS, 6e reforme de l Etat, economie sociale, Garantie Jeunes, contrats d insertion,
   etc.).
2. Reconciliation entre le budget institutionnel Actiris (~767m budget final 2024)
   et la ligne programme SGRBC/Cour des comptes (~648m 2026).
3. Detail L5 a l interieur de la ligne 6e reforme de l Etat (225m realise 2024).
4. Effectifs FTE et cout personnel 2025-2026.

Periode: 2024-01-01 a la date la plus recente.

### 2. Context

Le RA 2024 fournit une matrice L5 complete pour 2024. Manquent 2025-26 et le
detail interne de la 6e reforme.

Hierarchie: Bruxelles > Emploi > Actiris.

### 3. Vorm

Kopie digitale (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_actiris_2025_26_l5

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""",
    encoding="utf-8",
    newline="\n",
)

append_lines(DATA / "foi_queue.csv", [
    "gap_actiris_2025_26_l5,Bruxelles>Emploi>Actiris>L5_2025_26,actiris,L5 budget matrix 2025-2026 same structure as RA2024; reconcile institutional ~730-767m vs BCR programme 648m; detail inside 6th reform 225m block,2024 L5 full strong; multi-year incomplete,5,Actiris / SPRB transparence,transparence@sprb.brussels,,docs/doge/foi/drafts/gap_actiris_2025_26_l5.md,ready,2026-07-27,,,,,cmt_actiris_l5_2024,lb_actiris_acs_jobs,2026-07-27T22:30:00Z,2026-07-27T22:30:00Z,tick147 partial 2024 filled; human send",
])

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 hospitals universities Myria; FOI ready human send. rq_134 Actiris L5 done."\n',
    "utf-8",
)

log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Actiris L5 named programmes beyond total)
- Found (strong Actiris Rapport annuel 2024 Budget table):
  - **Budget final 2024: EUR 767.506m** · **exp realized EUR 729.736m** (95.1%) · recettes **753.574m**.
  - **Top L5 realized:** 6e reforme **EUR 225.0m** (30.8%) · **ACS jobs EUR 200.9m** (27.5%) · functioning **EUR 167.9m** (23.0%) · partnerships **EUR 57.7m** · economie sociale **EUR 34.5m**.
  - Other named: jeunes 8.8 · contrats insertion 7.3 · Garantie Jeunes 7.1 · cheques 6.8 · reforme aide 4.7 · secteurs ref 4.9.
  - Staff end-2024: **1,518 persons / 1,291 ETP**; DEI avg **91,628**.
  - Perimeter note: institutional ~730m vs BCR SGRBC programme line **648.1m 2026** (CoA) — not same scope.
- Wrote: source 1; budgets 20; cmt_actiris_l5_2024; lb ACS + 6th reform; rq_134=done; FOI residual ready.
- FOI: gap_actiris_2025_26_l5 human send.
- Next: prio6 **rq_140 hospitals** / **rq_141 universities** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick147 write OK")
