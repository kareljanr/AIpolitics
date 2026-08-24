# tick 2344 — De Ark Gemeenschap Antwerpen YE2025 Medium
import csv
import re
from pathlib import Path

csv.field_size_limit(100 * 1024 * 1024)
UTC = "2026-08-28T03:35:00Z"
BRUTO = 3071134
PNL = -178168
EQUITY = 4556337
FTE = 39.9
GAP = "gap_de_ark_antwerpen_nbb_pdf_assets_debt_empty_omzet_bruto_3_07m_pnl_loss_vaph_matrix_l5"
PI = "5.1"
RAW = Path("docs/doge/data/raw/tick2344")
RAW.mkdir(parents=True, exist_ok=True)


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


if not has_id("docs/doge/data/sources.csv", "source_id", "src_de_ark_antwerpen_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_de_ark_antwerpen_jr2025_cw_nl",
            "Companyweb NL De Ark Gemeenschap Antwerpen YE2025",
            "https://www.companyweb.be/nl/0458809703/de-ark-gemeenschap-antwerpen",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2344; omzet empty bruto {BRUTO} pnl LOSS {PNL} equity DROP {EQUITY} FTE {FTE}",
        ),
        (
            "src_de_ark_antwerpen_jr2025_cw_en",
            "Companyweb EN De Ark Gemeenschap Antwerpen YE2025",
            "https://www.companyweb.be/en/0458809703/de-ark-gemeenschap-antwerpen",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2344; EN Medium; filed 23-07-2026; Gross {BRUTO} P/L {PNL} Equity {EQUITY} FTE {FTE}; turnover unpublished",
        ),
        (
            "src_de_ark_antwerpen_jr2025_cw_fr",
            "Companyweb FR De Ark Gemeenschap Antwerpen YE2025",
            "https://www.companyweb.be/fr/0458809703/de-ark-gemeenschap-antwerpen",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2344; FR mirror",
        ),
        (
            "src_de_ark_antwerpen_kbo_2344",
            "KBO De Ark Gemeenschap Antwerpen 0458.809.703",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458809703",
            "KBO FOD Economie",
            "official_register",
            "tick2344; Actief VZW 2 VE Mortsel RSZ 87.202; absorbed De Ark Vlaanderen 0547.875.695 14.05.2024",
        ),
        (
            "src_de_ark_antwerpen_site_contact_2344",
            "De Ark Antwerpen FOI info@arkantwerpen.be",
            "https://www.deark.be/wonen-en-werken-in-de-ark/",
            "De Ark Antwerpen",
            "foi_contact",
            "tick2344; Groenstraat 46 Mortsel; T 03 460 37 10; info@arkantwerpen.be",
        ),
    ]:
        append_csv(
            "docs/doge/data/sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-28",
                source_class=klass,
                notes=notes,
            ),
        )

if not has_id("docs/doge/data/entities.csv", "entity_id", "vzw_de_ark_antwerpen_mortsel"):
    append_csv(
        "docs/doge/data/entities.csv",
        dict(
            entity_id="vzw_de_ark_antwerpen_mortsel",
            name_nl="De Ark - Gemeenschap Antwerpen VZW (Mortsel / VAPH L'Arche)",
            name_fr="De Ark - Communauté Anvers ASBL (Mortsel / VAPH L'Arche)",
            name_en="De Ark - Antwerp Community VZW (Mortsel / VAPH L'Arche)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.arkantwerpen.be/",
            foi_email="info@arkantwerpen.be",
            foi_postal="Groenstraat 46, 2640 Mortsel",
            notes=(
                f"tick2344 YE2025 Medium CW + Strong KBO 0458.809.703 Actief 2 VE RSZ 87.202; "
                f"omzet empty; bruto JUMP {BRUTO}; pnl LOSS {PNL} (improved vs YE2024); equity DROP {EQUITY}; "
                f"FTE {FTE}; FOI {GAP}; after Perrekes@2343; not TE-additive"
            ),
        ),
    )

if not has_id("docs/doge/data/budgets.csv", "budget_id", "bud_de_ark_antwerpen_bruto_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_de_ark_antwerpen_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge YE2025 JUMP", "tick2344; Medium CW; bruto +8.36% vs 2834317; omzet empty"),
        ("bud_de_ark_antwerpen_pnl_jr2025_statutory", PNL, "CW statutory winst/verlies YE2025 LOSS", "tick2344; Medium CW; LOSS improved +17.39% vs -215675"),
        ("bud_de_ark_antwerpen_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen YE2025 DROP", "tick2344; Medium CW; equity -4.29% vs 4760681"),
        ("bud_de_ark_antwerpen_fte_jr2025_statutory", FTE, "CW social-balance FTE 39.9", "tick2344; Medium CW; FTE 39.9 vs 39.4"),
    ]:
        append_csv(
            "docs/doge/data/budgets.csv",
            dict(
                budget_id=bid,
                entity_id="vzw_de_ark_antwerpen_mortsel",
                year="2025",
                amount_eur=str(amt),
                amount_min_eur=str(amt),
                amount_max_eur=str(amt),
                basis=basis,
                source_id="src_de_ark_antwerpen_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

cash = (
    f'{{"2025_omzet":"empty","2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
    f'"2024_bruto":2834317,"2024_pnl":-215675,"2024_equity":4760681,"2024_fte":39.4}}'
)

if not has_id(
    "docs/doge/data/commitments.csv",
    "commitment_id",
    "comm_de_ark_antwerpen_jr2025_statutory_empty_omzet_bruto_3_07m",
):
    append_csv(
        "docs/doge/data/commitments.csv",
        dict(
            commitment_id="comm_de_ark_antwerpen_jr2025_statutory_empty_omzet_bruto_3_07m",
            title="De Ark Antwerpen YE2025 leftover dual (empty omzet / bruto 3.07m / pnl LOSS / Medium)",
            entity_id="vzw_de_ark_antwerpen_mortsel",
            beneficiary="adults mental disability Mortsel-Boechout / L'Arche VAPH",
            legal_basis="VZW De Ark Gemeenschap Antwerpen (KBO 0458.809.703; Actief; 2 VE; RSZ 87.202)",
            decision_date="2026-07-23",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=cash,
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0458809703/de-ark-gemeenschap-antwerpen",
            stated_goal="L'Arche residential community care mental disability",
            cut_option="Publish NBB PDF assets/debt; reconcile empty omzet vs bruto 3.07m + VAPH/PVF matrix",
            source_id="src_de_ark_antwerpen_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Mortsel>De_Ark_Antwerpen>JR2025_statutory_L5",
            notes=f"tick2344; Medium CW; bruto primary {BRUTO}; after Perrekes@2343",
        ),
    )

if not has_id(
    "docs/doge/data/leaderboard.csv",
    "item_id",
    "lb_de_ark_antwerpen_empty_omzet_bruto_3_07m_pnl_loss_jr2025",
):
    append_csv(
        "docs/doge/data/leaderboard.csv",
        dict(
            item_id="lb_de_ark_antwerpen_empty_omzet_bruto_3_07m_pnl_loss_jr2025",
            name="De Ark Antwerpen empty omzet / bruto 3.07m / pnl LOSS (YE2025)",
            level="L5",
            type="vaph_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Mortsel>De_Ark_Antwerpen>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=(
                f"CW omzet empty / bruto JUMP {BRUTO} / pnl LOSS {PNL} (improved) / "
                f"equity DROP {EQUITY} / FTE {FTE} / filed 23.07.2026"
            ),
            confidence="medium",
            source_id="src_de_ark_antwerpen_jr2025_cw_en",
            beneficiaries="L'Arche adults Mortsel-Boechout",
            stated_goal="VAPH L'Arche community living",
            measured_outcome="empty omzet; bruto 3.07m; pnl LOSS improved; equity DROP",
            absurdity_score="7.0",
            cost_score="3.5",
            difficulty="3.0",
            priority_index=PI,
            cut_proposal="Publish NBB PDF assets/debt FOI; reconcile empty omzet vs bruto + VAPH flows",
            status="open",
            struck_reason="",
            notes=f"tick2344; Medium CW; FOI {GAP}; after Perrekes@2343",
        ),
    )

if not has_id("docs/doge/data/foi_queue.csv", "gap_id", GAP):
    append_csv(
        "docs/doge/data/foi_queue.csv",
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>Antwerpen>Mortsel>De_Ark_Antwerpen>NBB_PDF_assets_debt_empty_omzet",
            entity_id="vzw_de_ark_antwerpen_mortsel",
            what_is_missing=(
                f"NBB PDF YE2025 full (assets/debt/cash); why omzet empty while bruto EUR{BRUTO}; "
                f"pnl LOSS EUR{PNL} (improved vs YE2024); VAPH/PVF matrix"
            ),
            why_it_matters=(
                f"Medium CW shows L'Arche VAPH community Mortsel (empty omzet / bruto 3.07m / pnl LOSS / FTE {FTE}) "
                "under public care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="De Ark - Gemeenschap Antwerpen VZW",
            recipient_email="info@arkantwerpen.be",
            recipient_postal="Groenstraat 46, 2640 Mortsel",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-28",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_de_ark_antwerpen_jr2025_statutory_empty_omzet_bruto_3_07m",
            linked_leaderboard_id="lb_de_ark_antwerpen_empty_omzet_bruto_3_07m_pnl_loss_jr2025",
            created_utc=UTC,
            updated_utc=UTC,
            notes="tick2344; ready NOT sent; Medium CW + Strong KBO; after Perrekes@2343",
        ),
    )

rq = Path("docs/doge/data/research_queue.csv")
data = rq.read_bytes()
row2344 = (
    "rq_2344,leftover dual — De Ark Antwerpen YE2025 Medium (empty omzet / bruto JUMP 3.07m / pnl LOSS / FTE 39.9),"
    "hole_fill,8,done,L5,vzw_de_ark_antwerpen_mortsel,After Perrekes@2343. Prefer AGB/FARO YE2025 else unused. Do NOT redo Perrekes/Aurelia/Eyckerheyde stack.,"
    f"{GAP},2026-08-28T03:20:00Z,{UTC},tick2344 De Ark 0458.809.703 YE2025 Medium; bruto {BRUTO} pnl LOSS {PNL}; FOI ready not sent; next rq_2345; next EVERY-10 2350"
).encode("utf-8")
m = re.search(rb"rq_2344,[^\n]*", data)
if m:
    data = data[: m.start()] + row2344 + data[m.end() :]
else:
    if not data.endswith(b"\n"):
        data += b"\n"
    data += row2344 + b"\n"

if b"rq_2345," not in data:
    spawn = (
        "\nrq_2345,leftover dual after De Ark Antwerpen — prefer AGB/FARO-YE2025/AIESH/or-unused ETA-VAPH-WZC-maatwerk,"
        "hole_fill,8,open,L5,,After De Ark Antwerpen YE2025 Medium@2344. Prefer AGB Bornem/FARO/AIESH/REW/Citeco if YE2025 "
        "else FREE (Blijdorp/Gandae/Aralea/Manupal/Vlotter if YE2025). Do NOT redo De Ark/Perrekes/Aurelia/Eyckerheyde stack.,,"
        f"{UTC},{UTC},spawned after tick2344; next EVERY-10 2350\n"
    ).encode("utf-8")
    if not data.endswith(b"\n"):
        data += b"\n"
    data += spawn

rq.write_bytes(data)

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},rq_2344,2344,no,"
    f"tick2344 leftover dual De Ark Antwerpen 0458.809.703 Medium (omzet empty; bruto JUMP {BRUTO}; pnl LOSS {PNL}; "
    f"equity DROP {EQUITY}; FTE {FTE}; 2 VE Mortsel VAPH L'Arche); after Perrekes@2343; AGB/FARO YE2024; "
    f"next rq_2345; next EVERY-10 2350\n",
    encoding="utf-8",
    newline="\n",
)

(RAW / "cw_summary.json").write_text(
    "{\n"
    '  "kbo": "0458.809.703",\n'
    '  "entity": "vzw_de_ark_antwerpen_mortsel",\n'
    '  "omzet": "empty",\n'
    f'  "bruto": {BRUTO},\n'
    f'  "pnl": {PNL},\n'
    f'  "equity": {EQUITY},\n'
    f'  "fte": {FTE},\n'
    '  "filed": "2026-07-23",\n'
    '  "confidence": "medium",\n'
    f'  "pi": {PI}\n'
    "}\n",
    encoding="utf-8",
)

print("OK tick2344 De Ark", BRUTO, PI)
