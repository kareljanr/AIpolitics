# Analysis: {proposal_id}

> Template for Proposal Radar. Copy to `analyses/{proposal_id}.md` and fill.  
> Rubric: [docs/09-proposal-radar.md](../../09-proposal-radar.md) · Pipeline: [docs/04-policy-framework.md](../../04-policy-framework.md)

| Field | Value |
|-------|-------|
| **Title** | |
| **Actor** | |
| **Party / body** | |
| **Jurisdiction** | federal / flanders / wallonia / brussels / … |
| **Instrument** | law / subsidy / tax / ban / pilot / … |
| **Status** | rumoured / announced / tabled / adopted / … |
| **First seen** | YYYY-MM-DD |
| **Analysis version** | 1 |
| **Primary source** | URL + class |

---

## Steelman (proponent’s best case)

3–5 lines. Write as if you want their idea to work.

---

## 1. Problem claim

- **Metric / baseline:**  
- **Who is hurt:**  
- **Type:** preference | market failure | state failure | transfer fight  
- **Truth of problem diagnosis (0–10):**  
- **Confidence:** Strong / Medium / Weak / Speculative  
- **Sources:**  

---

## 2. Mechanism

Named mechanism(s):  

Does the instrument actually attack that mechanism?  

**mechanism_fit (0–10):**  

---

## 3. Options considered

| ID | Option | One-line effect |
|----|--------|-----------------|
| A | Status quo | |
| B | Abolish / deregulate | |
| C | Price / tax reform | |
| D | Conditional transfer | |
| E | Public provision / invest | |
| F | Pilot | |
| G | **This proposal** | |

---

## 4. Evidence table

| Claim | Grade | Source class | Note |
|-------|-------|--------------|------|
| | | | |

**evidence_quality (0–10):**  

---

## 5. Distribution & transfer constraint

- Winners:  
- Losers:  
- Exit / entry risk for productive base:  
- New permanent clientele?  

**capture_risk (0–10):**  

---

## 6. Fiscal

| | Amount | Basis | Confidence |
|--|--------|-------|------------|
| Static cost / save | € … | annual / envelope | |
| Dynamic (behaviour) | qualitative | | speculative unless cited |

**fiscal_honesty (0–10):** how honest are proponent claims vs this table?

### 6b. Taxpayer pain (mandatory when € known)

Unit: `docs/proposal-radar/TAXPAYER_UNIT.md` + `data/taxpayer_unit.csv`  
(Average single FT employee — **employee labour tax only** ≈ €19.4k/yr; net take-home ≈ €29.5k/yr.)

| Metric | Value | Meaning |
|--------|------:|---------|
| **Belasting-FTE** (`pain_tax_fte`) | | Public € ÷ annual work-tax of one average employee. Negative if saving. |
| **Nettoloon-jaren** (`pain_net_years`) | | Public € ÷ annual net wage (one person). |
| **Werkminuten** (`pain_work_minutes`) | | Bill ÷ all BE employees → minutes of average work **each**. Most personal. |
| € / employee (`pain_eur_per_employee`) | | Public € ÷ N employees (~4.85m). |

- Do **not** invent € to fill pain columns.  
- Do **not** use full tax wedge (employer SSC) for “what the worker pays.”  
- Revenue instruments (new taxes): blank or separate incidence note — not fake labour-tax FTE.

---

## 7. Belgian competence & implementation

- Competent level:  
- EU constraint:  
- Admin capacity / dual-structure friction:  

**competence_fit (0–10):**  

---

## 8. Scores

| Subscore | 0–10 | One-line reason |
|----------|------|-----------------|
| truth_problem | | |
| mechanism_fit | | |
| abundance_ev | | |
| fiscal_honesty | | |
| incentive_quality | | |
| competence_fit | | |
| evidence_quality | | |
| capture_risk | | |

| Public | Score | Reason |
|--------|-------|--------|
| **Clownpoints** | /10 | |
| **Genius score** | /10 | |
| **policy_index** | genius − clown | |

**score_confidence:** strong / medium / weak / speculative  

---

## 9. Recommendation

`support` | `amend` | `reject` | `ignore` | `watch`

If amend: concrete minimum fix.

---

## 10. Falsifier

> We reverse this assessment if _____ within _____ .

---

## 11. Open questions

-  

## 12. DOGE links

- leaderboard / commitment IDs:  

## 13. Publish checklist

- [ ] Steelman **extensive** (not 3 lines)  
- [ ] Critique maps **stated ambition → mechanism → ROI/evidence**  
- [ ] Abolish / do nothing considered  
- [ ] Confidence tags on factual claims  
- [ ] Transfer/exit constraint checked  
- [ ] No invented euros  
- [ ] Taxpayer pain filled or honestly blank  
- [ ] Same rubric as other parties  
- [ ] Falsifier written
