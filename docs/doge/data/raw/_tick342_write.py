# tick 342 — CCA FWB dual AV ~44m 2024 vs VAF Flanders
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
now = "2026-07-31T09:45:00Z"

with open(root / "sources.csv", "a", encoding="utf-8") as f:
    f.write(
        "src_cca_bilan_2024,FWB Centre du Cinema et de l Audiovisuel Bilan 2024 envelope and L5,"
        "https://audiovisuel.cfwb.be/actualite/news/bilan-2024-du-centre-du-cinema-et-de-laudiovisuel/,"
        "FWB CCA / culture.be,2026-07-31,official_press_bilan,"
        "Strong: global AV envelope >44m 2024 (43.15m 2023); FWB 26.6m + editeurs 17.4m (RTBF 5.8 private 11.6); "
        "Commission Cinema promises 13.24m; Series 1.635m; operators 4.198m; dual VAF Flanders; tick342\n"
    )

with open(root / "entities.csv", "a", encoding="utf-8") as f:
    f.write(
        "cca_fwb,Centre du Cinema et de l Audiovisuel CCA FWB,"
        "Centre du Cinema et de l Audiovisuel,"
        "FWB Wallonia-Brussels audiovisual support centre dual VAF Flanders,"
        "agency,fwb_gov,fr,https://audiovisuel.cfwb.be,,,,"
        "Envelope >44m 2024 FWB 26.6m+editeurs 17.4m; dual VAF ~30.7m VL; tick342\n"
    )
    # update vaf note
ent = (root / "entities.csv").read_text(encoding="utf-8")
ent = re.sub(
    r"vaf,Vlaams Audiovisueel Fonds VAF,[^\n]+",
    "vaf,Vlaams Audiovisueel Fonds VAF,Fonds audiovisuel flamand VAF,"
    "Flanders audiovisual support agency Film Media Game Screen Flanders,"
    "agency,vlaanderen_gov,nl,https://www.vaf.be,,,,"
    "VL dots ~30.7m 2024-25; dual CCA FWB envelope >44m 2024; tick341-342",
    ent,
    count=1,
)
(root / "entities.csv").write_text(ent, encoding="utf-8")

bud = [
    "bud_cca_envelope_total_2024,cca_fwb,2024,44000000,,,budgeted,src_cca_bilan_2024,strong,CCA global audiovisual envelope more than 44m EUR 2024 (press: plus de 44m; prior year 43.15m)",
    "bud_cca_envelope_total_2023,cca_fwb,2023,43150000,,,budgeted,src_cca_bilan_2024,strong,CCA global audiovisual envelope 43.15m EUR 2023 (bilan 2024 comparison)",
    "bud_cca_fwb_contrib_2024,cca_fwb,2024,26600000,,,budgeted,src_cca_bilan_2024,strong,FWB contribution to CCA AV envelope 26.6m 2024",
    "bud_cca_editeurs_contrib_2024,cca_fwb,2024,17400000,,,budgeted,src_cca_bilan_2024,strong,Editors distributors legal investment obligation 17.4m 2024 (RTBF 5.8 + private 11.6)",
    "bud_cca_rtbf_contrib_2024,cca_fwb,2024,5800000,,,budgeted,src_cca_bilan_2024,strong,RTBF contribution within editeurs block 5.8m 2024",
    "bud_cca_private_editeurs_2024,cca_fwb,2024,11600000,,,budgeted,src_cca_bilan_2024,strong,Private editors distributors 11.6m 2024 legal investment",
    "bud_cca_commission_cinema_2024,cca_fwb,2024,13240000,,,budgeted,src_cca_bilan_2024,strong,Commission du Cinema promises of aid 13.24m 2024 (near 13.26m 2023 record)",
    "bud_cca_series_commission_2024,cca_fwb,2024,1635000,,,budgeted,src_cca_bilan_2024,strong,Commission Series first year 12 aids total 1.635m 2024",
    "bud_cca_operateurs_2024,cca_fwb,2024,4198105,,,budgeted,src_cca_bilan_2024,strong,Aides aux operateurs audiovisuels 55 operators 4.198105m 2024",
    "bud_cca_promotion_2024,cca_fwb,2024,712262,,,budgeted,src_cca_bilan_2024,strong,Promotion aids total 712262 EUR 2024",
    "bud_cca_taxshelter_raised_2024,cca_fwb,2024,84730000,,,budgeted,src_cca_bilan_2024,strong,Tax shelter funds raised FWB investors 84.73m 2024 (+14pct vs 74.18m 2023) — not pure TE cash out",
    "bud_cca_europe_creative_media_be_2024,cca_fwb,2024,9400000,,,budgeted,src_cca_bilan_2024,strong,Europe Creative MEDIA grants to Belgian projects 9.4m 2024 (7.2m 2023)",
    "bud_av_dual_vaf_cca_class_2024,vaf,2024,75100000,,,budgeted,src_cca_bilan_2024,medium,Illustrative dual AV class VAF VL dots 30.7m + CCA envelope 44m ~74.7m 2024 not additive TE (different perimeters)",
]
with open(root / "budgets.csv", "a", encoding="utf-8") as f:
    f.write("\n".join(bud) + "\n")


def cmt(cid, title, eid, ben, legal, ddate, sy, ey, tot, cash, rem, url, goal, cut, src, conf, path, notes):
    cf = json.dumps(cash, separators=(",", ":")).replace('"', '""')
    rem_s = "" if rem is None else str(rem)
    return (
        f'{cid},{title},{eid},{ben},{legal},{ddate},{sy},{ey},{tot},'
        f'"{cf}",{rem_s},active,{url},{goal},{cut},{src},{conf},{path},{notes}\n'
    )


with open(root / "commitments.csv", "a", encoding="utf-8") as f:
    f.write(
        cmt(
            "cmt_cca_envelope_2023_24",
            "CCA FWB audiovisual envelope dual VAF Flanders",
            "cca_fwb",
            "Francophone Belgian film series producers operators festivals",
            "FWB culture cinema policy + SMA investment obligations editors",
            "2024-01-01",
            2023,
            2024,
            87150000,
            {
                "envelope_2023_m": 43.15,
                "envelope_2024_m": 44.0,
                "fwb_2024_m": 26.6,
                "editeurs_2024_m": 17.4,
                "rtbf_2024_m": 5.8,
                "private_editeurs_2024_m": 11.6,
                "commission_cinema_promises_2024_m": 13.24,
                "series_2024_m": 1.635,
                "operateurs_2024_m": 4.198,
                "promotion_2024_m": 0.712,
                "taxshelter_raised_2024_m": 84.73,
                "europe_creative_be_2024_m": 9.4,
                "dual_vaf_vl_dots_2024_m": 30.7,
                "note": "Envelope = FWB + legal private/RTBF investment; tax shelter raised is investor money not CCA budget; dual VAF Flanders",
            },
            None,
            "https://audiovisuel.cfwb.be/actualite/news/bilan-2024-du-centre-du-cinema-et-de-laudiovisuel/",
            "Support francophone Belgian audiovisual creation promotion operators",
            "Publish named award L5; dual unit-cost VAF; tax shelter is separate TE channel",
            "src_cca_bilan_2024",
            "strong",
            "FWB>Culture>CCA",
            "tick342: >44m envelope dual VAF culture AV",
        )
    )

with open(root / "leaderboard.csv", "a", encoding="utf-8") as f:
    f.write(
        "lb_cca_envelope_44m,CCA FWB AV envelope >44m 2024 dual VAF Flanders,regional,ops,"
        "FWB>Culture>CCA,44000000,87150000,"
        "Strong FWB bilan: envelope >44m (FWB 26.6 + editeurs 17.4); Commission Cinema 13.24m; dual VAF ~30.7m VL,"
        "strong,src_cca_bilan_2024,Francophone AV creators,"
        "Audiovisual creation series operators promotion,"
        "Core culture dual community not pure waste; private SMA investment is legal obligation; L5 residual,"
        "3,7.0,4,5.2,FOI named awards L5; dual VAF unit-cost table,seed,,tick342 dual culture AV\n"
    )
    f.write(
        "lb_av_dual_vaf_cca_class,Dual community AV funds VAF+CCA class ~75m 2024,regional,ops,"
        "BE>culture>AV_dual_VAF_CCA,75100000,75100000,"
        "Medium sum class: VAF VL dots 30.7m + CCA envelope 44m; different perimeters not pure additive TE,"
        "medium,src_cca_bilan_2024,Belgian AV sector dual NL/FR,"
        "Community audiovisual support dual structures,"
        "Mechanism dual culture; not automatic waste; transparency L5 FOI,"
        "4,7.5,5,6.0,Publish joint dual map VAF CCA federal Cinematek,seed,,tick342 dual culture\n"
    )

# refresh FOI gap_vaf_cca
foi_path = root / "foi_queue.csv"
foi = foi_path.read_text(encoding="utf-8")
m = re.search(r"gap_vaf_cca_dual_l5,[^\n]+", foi)
if m:
    new_row = (
        "gap_vaf_cca_dual_l5,BE>culture>AV_funds>VAF_CCA_L5,vaf,"
        "Named top20 VAF and CCA awards EUR 2023-2025; Cinematek structural Belspo dot series; "
        "Screen Flanders tax-shelter cash if public; reconcile CCA Commission 13.24m vs full envelope 44m L5,"
        "VAF dots 30.7m + CCA envelope >44m strong; residual named L5 and Cinematek base,5,"
        "VAF / CCA FWB / BELSPO / Team Openbaarheid,openbaarheid@vlaanderen.be,"
        "Havenlaan 88 bus 20 1000 Brussel,"
        "docs/doge/foi/drafts/gap_vaf_cca_dual_l5.md,ready,2026-07-31,,,,,"
        f"cmt_vaf_package_2024_25|cmt_cca_envelope_2023_24,lb_vaf_vl_dots_31m|lb_cca_envelope_44m,"
        f"2026-07-31T09:15:00Z,{now},"
        "tick341 VAF | tick342 CCA envelope filled; residual named L5 + Cinematek human send"
    )
    foi = foi[: m.start()] + new_row + foi[m.end() :]
    foi_path.write_text(foi, encoding="utf-8")

# append FOI draft note
draft = root.parent / "foi" / "drafts" / "gap_vaf_cca_dual_l5.md"
if draft.exists():
    with open(draft, "a", encoding="utf-8") as f:
        f.write(
            """

## Update tick342 — CCA FWB public fill

Source: FWB CCA Bilan 2024 official news (primary).

- Global AV envelope **>€44 m** 2024 (was **€43.15 m** 2023).
- Of which **FWB €26.6 m** + editors/distributors **€17.4 m** (RTBF **€5.8 m** + private **€11.6 m** legal SMA investment).
- Commission du Cinéma promises **€13.24 m**; Commission Séries **€1.635 m**; opérateurs **€4.198 m**.
- Tax shelter raised **€84.73 m** (investor money, not CCA budget).
- Dual VAF Flanders VL dots **~€30.7 m** same year class.

Residual FOI: named award L5 matrices + Cinematek Belspo structural series.
"""
        )

# research queue
rq_path = root / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_333,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-07-31T09:15:00Z,,Spawned tick341 after VAF dual culture; rq_116 SWA deferred"
)
new = (
    "rq_333,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,gap_vaf_cca_dual_l5,"
    f"2026-07-31T09:15:00Z,{now},"
    "tick342: CCA FWB envelope >44m dual VAF 30.7m culture AV; FOI L5 residual; spawn rq_334"
)
if old not in rq:
    raise SystemExit("rq_333 not found")
rq = rq.replace(old, new)
if "rq_334" not in rq:
    if not rq.endswith("\n"):
        rq += "\n"
    rq += (
        "rq_334,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        f"{now},,Spawned tick342 after CCA dual VAF; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_333,342,no,"
    "Scheduler 60s. Next prio5 rq_334; rq_116 SWA deferred. FOI ready. tick342 CCA >44m dual VAF.\n",
    encoding="utf-8",
)

print("OK tick342")
