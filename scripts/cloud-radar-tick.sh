#!/usr/bin/env bash
# Score one Proposal Radar item with Grok. The workflow commits afterwards.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# shellcheck source=cloud-grok-auth.sh
source "${ROOT}/scripts/cloud-grok-auth.sh"

grok --version

UNIT_FILE="${ROOT}/.radar-unit.txt"
python scripts/next_radar_unit.py > "${UNIT_FILE}"
if grep -q '^NO_UNIT$' "${UNIT_FILE}" || grep -q '^PAUSED$' "${UNIT_FILE}"; then
  echo "No Proposal Radar unit to score."
  rm -f "${UNIT_FILE}"
  exit 0
fi

grok \
  --cwd "$ROOT" \
  --permission-mode bypassPermissions \
  --max-turns 36 \
  --output-format plain \
  -p "Score exactly one Belgian policy proposal. The unit is already in .radar-unit.txt. Read that file and nothing else from the queue. Do not open ingest_queue.csv or proposals.csv except to append one row with Python's csv module.

Rules:
- Belgium only. If the item is not a Belgian policy proposal, set that ingest row status to rejected_noise and stop.
- Do not invent euros or poll numbers. Press-only evidence means score_confidence weak.
- policy_index = genius_score - clownpoints. Both scores are 0-10. Score the instrument, not the person.
- genius_score is approximately 0.25*abundance_ev + 0.20*mechanism_fit + 0.15*incentive_quality + 0.15*fiscal_honesty + 0.10*truth_problem + 0.10*competence_fit + 0.05*evidence_quality - 0.15*capture_risk, then clamped to 0-10.
- Write docs/proposal-radar/analyses/{proposal_id}.md from the section headings in docs/proposal-radar/templates/analysis-memo.md. Include a steelman, options A-G with abolish, a falsifier, and the subscores.
- Append one proposals.csv row with every header column. publish_ok=yes only when score_confidence is medium or strong; otherwise needs_human.
- Mark the ingest row status=scored and set its proposal_id.
- If a public euro amount is sourced, run: python docs/proposal-radar/scripts/recompute_pain.py
- Update docs/proposal-radar/data/loop_state.csv: ticks_completed + 1, proposals_scored + 1, last_unit_id, last_tick_utc, mode=analyse, paused unchanged. Append 5 lines to docs/proposal-radar/loop_log.md.
- Do not commit, push, or score a second item. Stop when the files are written."

rm -f "${UNIT_FILE}"
