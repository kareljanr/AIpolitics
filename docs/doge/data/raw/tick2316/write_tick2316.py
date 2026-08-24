import csv
from pathlib import Path

csv.field_size_limit(10**7)
utc = "2026-08-27T22:30:00Z"
Path("docs/doge/data/raw/tick2316").mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


path_rq = "docs/doge/data/research_queue.csv"
with open(path_rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_2316" and row["status"] == "done":
        raise SystemExit("rq_2316 already done: " + (row.get("title") or "")[:90])

if not has_id("docs/doge/data/sources.csv", "source_id", "src_kindervriend_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_kindervriend_jr2025_cw_nl",
            "Companyweb NL MPI De Kindervriend YE2025 statutory",
            "https://www.companyweb.be/nl/0409988514/mpi-de-kindervriend-vzw",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2316; YE2025 omzet 406928 bruto 8083623 ~19.86x pnl LOSS -88717 equity 9787469 FTE 96.6",
        ),
        (
            "src_kindervriend_jr2025_cw_en",
            "Companyweb EN MPI De Kindervriend YE2025 statutory",
            "https://www.companyweb.be/en/0409988514/mpi-de-kindervriend-vzw",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2316; EN Medium; filed 22-05-2026; Turnover 406928 Gross 8083623 P/L -88717 Equity 9787469 FTE 96.6",
        ),
        (
            "src_kindervriend_jr2025_cw_fr",
            "Companyweb FR MPI De Kindervriend YE2025 statutory",
            "https://www.companyweb.be/fr/0409988514/mpi-de-kindervriend-vzw",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2316; FR mirror",
        ),
        (
            "src_kindervriend_kbo_2316",
            "KBO MPI De Kindervriend 0409.988.514",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409988514",
            "KBO FOD Economie",
            "official_register",
            "tick2316; Actief 3 VE mpi@kindervriend.be RSZ 87.201 Kortrijk",
        ),
        (
            "src_kindervriend_site_contact_2316",
            "De Kindervriend FOI mpi@kindervriend.be",
            "https://www.dekindervriend.be/",
            "MPI De Kindervriend VZW",
            "foi_contact",
            "tick2316; mpi@kindervriend.be; Rollegemkerkstraat 51 Kortrijk",
        ),
    ]:
        append_csv(
            "docs/doge/data/sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-27",
                source_class=klass,
                notes=notes,
            ),
        )

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_mpi_de_kindervriend_kortrijk"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_mpi_de_kindervriend_kortrijk",
            name_nl="MPI De Kindervriend VZW (Kortrijk / VAPH MFC)",
            name_fr="MPI De Kindervriend ASBL (Courtrai / MFC VAPH)",
            name_en="MPI De Kindervriend VZW (Kortrijk / VAPH MFC)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.dekindervriend.be/",
            foi_email="mpi@kindervriend.be",
            foi_postal="Rollegemkerkstraat 51, 8510 Kortrijk",
            notes=(
                "tick2316 YE2025 Medium CW + Strong KBO 0409.988.514 Actief 3 VE RSZ 87.201; "
                "omzet JUMP 406928; bruto JUMP 8083623 ~19.86x; pnl LOSS -88717; equity JUMP 9787469; "
                "FTE 96.6; FOI gap_kindervriend_*; Homevil YE2024 stall remap; after Havenzate@2315; not TE-additive"
            ),
        ),
    )

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_kindervriend_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        (
            "bud_kindervriend_omzet_jr2025_statutory",
            406928,
            "CW statutory omzet YE2025 JUMP",
            "tick2316; Medium CW; omzet +2.92% vs 395371",
        ),
        (
            "bud_kindervriend_bruto_jr2025_statutory",
            8083623,
            "CW statutory bruto_marge YE2025 ~19.86x omzet",
            "tick2316; Medium CW; bruto +4.17% vs 7759676",
        ),
        (
            "bud_kindervriend_pnl_jr2025_statutory",
            -88717,
            "CW statutory winst/verlies YE2025 LOSS",
            "tick2316; Medium CW; pnl LOSS -88717 vs -86586",
        ),
        (
            "bud_kindervriend_equity_jr2025_statutory",
            9787469,
            "CW statutory eigen_vermogen YE2025 JUMP",
            "tick2316; Medium CW; equity +1.03% vs 9687910",
        ),
        (
            "bud_kindervriend_fte_jr2025_statutory",
            96.6,
            "CW social-balance FTE 96.6",
            "tick2316; Medium CW; FTE 96.6 vs 95.9",
        ),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(
                budget_id=bid,
                entity_id="vzw_mpi_de_kindervriend_kortrijk",
                year="2025",
                amount_eur=str(amt),
                amount_min_eur=str(amt),
                amount_max_eur=str(amt),
                basis=basis,
                source_id="src_kindervriend_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

if not has_id(
    "docs/doge/data/commitments.csv",
    "commitment_id",
    "comm_kindervriend_jr2025_statutory_vaph_bruto_8_08m_19_86x",
):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_kindervriend_jr2025_statutory_vaph_bruto_8_08m_19_86x",
            title="MPI De Kindervriend YE2025 leftover dual (omzet 0.41m / bruto 8.08m ~19.86x / pnl LOSS / FTE 96.6 / Medium)",
            entity_id="vzw_mpi_de_kindervriend_kortrijk",
            beneficiary="kinderen met verstandelijke beperking Zuid-West-Vlaanderen / VAPH MFC",
            legal_basis="VZW MPI De Kindervriend (KBO 0409.988.514)",
            decision_date="2026-05-22",
            start_year="2025",
            end_year="2025",
            total_envelope_eur="8083623",
            cash_by_year=(
                '{"2025_omzet":406928,"2025_bruto":8083623,"2025_pnl":-88717,"2025_equity":9787469,"2025_fte":96.6,'
                '"2024_omzet":395371,"2024_bruto":7759676,"2024_pnl":-86586,"2024_equity":9687910,"2024_fte":95.9}'
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0409988514/mpi-de-kindervriend-vzw",
            stated_goal="VAPH MFC De Kindervriend",
            cut_option="Publish NBB PDF assets/debt FOI; explain bruto~19.86x omzet",
            source_id="src_kindervriend_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Kortrijk>MPI_De_Kindervriend>JR2025_statutory_L5",
            notes="tick2316; Medium CW; Homevil YE2024 stall remap; after Havenzate@2315; not TE-additive",
        ),
    )

if not has_id(
    "docs/doge/data/leaderboard.csv",
    "item_id",
    "lb_kindervriend_bruto_8_08m_gt_omzet_19_86x_pnl_loss_jr2025",
):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_kindervriend_bruto_8_08m_gt_omzet_19_86x_pnl_loss_jr2025",
            name="MPI De Kindervriend bruto 8.08m / ~19.86x omzet 0.41m / pnl LOSS / FTE 96.6 (YE2025 VAPH Kortrijk)",
            level="L5",
            type="vaph_mpi_statutory",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Kortrijk>MPI_De_Kindervriend>JR2025",
            annual_cost_eur="8083623",
            total_cost_eur="8083623",
            tco_notes="CW omzet 406928 / bruto 8083623 ~19.86x / pnl LOSS -88717 / equity JUMP 9787469 / FTE 96.6",
            confidence="medium",
            source_id="src_kindervriend_jr2025_cw_en",
            beneficiaries="kinderen met verstandelijke beperking Kortrijk",
            stated_goal="VAPH MFC",
            measured_outcome="bruto~19.86x omzet; pnl LOSS; FTE 96.6; filed 22.05.2026",
            absurdity_score="7.8",
            cost_score="5.5",
            difficulty="3.0",
            priority_index="6.65",
            cut_proposal="Publish NBB PDF assets/debt FOI; VAPH subsidy matrix",
            status="open",
            struck_reason="",
            notes="tick2316; Medium CW; FOI gap_kindervriend_*; after Havenzate@2315",
        ),
    )

if not has_id(
    "docs/doge/data/foi_queue.csv",
    "gap_id",
    "gap_kindervriend_nbb_pdf_assets_debt_bruto_gt_omzet_19_86x_pnl_loss_vaph_matrix_l5",
):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id="gap_kindervriend_nbb_pdf_assets_debt_bruto_gt_omzet_19_86x_pnl_loss_vaph_matrix_l5",
            hierarchy_path="Vlaanderen>West-Vlaanderen>Kortrijk>MPI_De_Kindervriend>NBB_PDF",
            entity_id="vzw_mpi_de_kindervriend_kortrijk",
            what_is_missing="NBB PDF YE2025 assets/debt; bruto 8083623 ~19.86x omzet 406928; pnl LOSS -88717; VAPH subsidy matrix; FTE 96.6",
            why_it_matters="Medium CW VAPH MPI Kortrijk bruto~19.86x omzet; assets/debt unknown; recurring LOSS",
            priority="8",
            recipient_body="MPI De Kindervriend VZW",
            recipient_email="mpi@kindervriend.be",
            recipient_postal="Rollegemkerkstraat 51, 8510 Kortrijk",
            draft_letter_path="docs/doge/foi/drafts/gap_kindervriend_nbb_pdf_assets_debt_bruto_gt_omzet_19_86x_pnl_loss_vaph_matrix_l5.md",
            status="ready",
            date_ready="2026-08-27",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_kindervriend_jr2025_statutory_vaph_bruto_8_08m_19_86x",
            linked_leaderboard_id="lb_kindervriend_bruto_8_08m_gt_omzet_19_86x_pnl_loss_jr2025",
            created_utc=utc,
            updated_utc=utc,
            notes="tick2316; ready NOT sent",
        ),
    )

for row in rows:
    if row["task_id"] == "rq_2316":
        row.update(
            {
                "title": "leftover dual — MPI De Kindervriend YE2025 Medium (bruto JUMP 8.08m / ~19.86x omzet / pnl LOSS / FTE 96.6)",
                "status": "done",
                "entity_id": "vzw_mpi_de_kindervriend_kortrijk",
                "blocked_gap_id": "gap_kindervriend_nbb_pdf_assets_debt_bruto_gt_omzet_19_86x_pnl_loss_vaph_matrix_l5",
                "updated_utc": utc,
                "instructions": "leftover dual Kindervriend YE2025 FREE VAPH MPI after Havenzate; Homevil YE2024 stall remap",
                "notes": "tick2316; Kindervriend 0409.988.514 YE2025 Medium; omzet JUMP 406928; bruto JUMP 8083623 ~19.86x; pnl LOSS -88717; equity JUMP 9787469; FTE 96.6; FOI ready NOT sent; Homevil YE2024 stall; next EVERY-10 2320",
            }
        )

if not any(row["task_id"] == "rq_2317" for row in rows):
    rows.append(
        {
            "task_id": "rq_2317",
            "title": "leftover dual after Kindervriend — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "After Kindervriend. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae/De Ploeg/Homevil if YE2025). Do NOT redo Kindervriend/Havenzate/Iris/Hejmen stack.",
            "blocked_gap_id": "",
            "created_utc": utc,
            "updated_utc": utc,
            "notes": "spawned after tick2316 Kindervriend; next every-10 2320",
        }
    )

with open(path_rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    for row in rows:
        w.writerow({k: row.get(k, "") for k in fields})

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": utc,
            "last_unit_id": "rq_2316",
            "ticks_completed": "2316",
            "paused": "no",
            "notes": (
                "tick2316 leftover dual MPI De Kindervriend 0409.988.514 Medium (omzet JUMP 406928; bruto JUMP 8083623 ~19.86x; "
                "pnl LOSS -88717; equity JUMP 9787469; FTE 96.6; 3 VE Kortrijk VAPH); Homevil YE2024 stall remap; "
                "after Havenzate@2315; AGB Bornem JR2024; FARO/AIESH YE2024; next rq_2317; next EVERY-10 2320; continuous hole_fill"
            ),
        }
    )

print("tick2316 OK")
