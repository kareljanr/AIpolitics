# Middleman systems: cheques & union unemployment admin

**Status:** doctrine note for DOGE (truth-seeking). Not a finished cost audit.  
**Tone:** incentives and waste of layers — not culture-war abuse.

## North-star test

Does this structure create **more abundance per euro** than a simpler alternative (cash wages, direct state payment, or **no scheme**)?  
If the only justification is “we already have the intermediaries,” fail the test.

---

## 1. Cheque economy (eco-cheques, meal vouchers, gift cheques, etc.)

### Claim (mechanism)

The state and/or tax system **subsidises or tax-favours** compensation paid through **restricted vouchers**:

1. Employer / state forgoes full cash wage (or pays extra social cost).  
2. **Issuers / processors / retailers** take a cut or capture volume.  
3. Worker receives purchasing power **only for approved categories**.  
4. Result: people buy a **narrow basket** (sometimes low-priority goods) because **cash is fungible; cheques are not**.

### Why this fails the abundance test (strong on mechanism; medium on € totals)

| Problem | Effect |
|---------|--------|
| **Deadweight restriction** | Same euro as cash would let households optimise; cheques force category choice |
| **Admin sandwich** | Design, issuance, compliance, retailer acceptance — cost that is not consumption |
| **Wage distortion** | Favours fringe packages over transparent wages (same family as company cars) |
| **Political opacity** | Looks like a “gift” or “green” win while fiscal cost sits in tax expenditures / SSC exemptions |

### Related Belgian instruments (non-exhaustive)

- Eco-cheques (consumption restricted to “eco” product lists)  
- Meal vouchers / maaltijdcheques  
- Other sectoral cheques (varies over time by CBA)  
- **Dienstencheques** (different logic: household services market — still middleman-heavy; see `cmt_dienstencheques_*` + FOI TCO)

### DOGE stance (draft policy)

1. **Default: cash wages** (or neutral tax treatment of pay).  
2. If a social goal is real (e.g. low-income support): **cash transfer** or negative income tax — not retailer-restricted scrip.  
3. Score every cheque: fiscal cost + admin + deadweight vs stated goal.  
4. Leaderboard candidates: tax expenditure lines + SSC breaks on vouchers (FPS inventory + CBA inventory).

### Evidence status

| Item | Confidence |
|------|------------|
| Restriction reduces consumer surplus vs cash | **Strong** (basic price theory) |
| Industry capture / admin costs exist | **Strong** (mechanism); **€ magnitude case-by-case** |
| Eco-cheques specifically low climate ROI | **Medium** (need evaluation literature) |

**Open research / findings (tick 17):**

| Fact | Confidence | Source class |
|------|------------|--------------|
| Meal vouchers SSC + PIT exempt (conditions) | Strong | Payroll law / Partena |
| Max meal voucher EUR 10/day from 2026 (employer up to 8.91) | Strong | Royal decree / Partena |
| Eco-cheques up to EUR 250/yr tax+SSC free; restricted list | Strong | Payroll guides |
| Meal voucher **market volume** ~EUR 3bn/yr | Medium | Industry claim (~3m users) |
| Meal voucher **fiscal cost ~EUR 1.4bn/yr** | Medium | Sofie De Coster thesis via De Standaard (2024) |
| Expansion of max voucher could cost treasury **~EUR 1bn extra** | Weak–Medium | Same press scenario |
| **Official FPS inventory TE €** for meal/eco package | Weak / Unknown | Still FOI `gap_cheque_te` |
| Eco-cheques abolition discussed | Medium | Policy commentary — verify statute |

**Open research:** exact TE € for meal vouchers / eco-cheques (FOI + inventory microdata).

---

## 2. Unions as unemployment-benefit paymasters

### Claim (mechanism)

In Belgium’s classic model, **unemployment benefits (werkloosheid / chômage)** are often **paid out via union funds / payment institutions**, with the **state ultimately funding** the benefit. That is:

> Taxpayers fund the benefit → intermediate private/associative structure processes payment → jobseeker receives money.

The **core task** (income insurance for unemployment) is a **public social-security function**. Using unions as the default cashier is a **historical/political design**, not a technical necessity.

### Why this can be wasteful (or at least needs a burden of proof)

| Problem | Effect |
|---------|--------|
| **Duplication** | Multiple payment channels (union A, B, C, + Hulpkas / CAPAC for non-members) → fixed costs × N |
| **Capture** | Intermediary has interest in **membership and volume**, not only speed/accuracy of payment |
| **Accountability blur** | Citizen blames “the union” or “the state” interchangeably; hard to pin KPIs |
| **Opportunity cost** | Same euro could fund faster digital direct payment (one RSZ/ONEM pipeline) |

### What we are **not** claiming

- That unions have no legitimate role (collective bargaining, representation).  
- That every euro of union funding is “chômage admin” (many revenue sources).  
- That direct state payment is free (state also has admin costs) — only that **competing parallel cashiers** need a cost-benefit test.

### DOGE stance (draft policy)

1. **Publish unit cost** of paying unemployment benefits: per dossier, per channel (union funds vs Hulpkas).  
2. Prefer **one digital public payer** for the pure cash benefit (with appeals and control still public).  
3. Leave unions free to offer **optional services** funded by members — not by a captive public payment franchise without competitive tender.  
4. Any remaining public grant to intermediaries: **sunset + KPI** (error rate, time-to-pay, fraud detection).

### Evidence status

| Item | Confidence |
|------|------------|
| Multi-channel payment architecture exists | **Strong** (institutional fact) |
| Parallel channels raise admin cost vs single payer | **Medium–Strong** (public finance theory; need Rekenhof/ONEM unit costs) |
| Exact € waste of the dual/triple cashier model | **Weak–Medium** until unit-cost FOI |

**Open research / findings (tick 18):**

| Fact | Confidence | Source |
|------|------------|--------|
| Payment via union funds **or** Hulpkas/CAPAC | Strong | Institutional / RVA |
| Hulpkas **admin budget 2025 = €6,084,000** | Strong | hvwrva.be budget page |
| Union payment funds also receive public support for admin | Medium | Standard description; **€ TBD** |
| Benefit stock (€bn unemployment) is **separate** from cashier admin | Strong | Accounting identity |
| Unit cost / dossier by channel | Weak / Unknown | FOI `gap_unemp_pay_unit_cost` |

**Open research / FOI:** ONEM/RVA volumes by organism; public grants to **all** payment institutions (not only Hulpkas); unit cost comparisons.


---

## 3. Common pattern (generalise)

```text
Public goal (pay worker / jobseeker)
        ↓
  Tax / SSC / budget money
        ↓
  Private or associative middleman (issuer, union fund, processor)
        ↓
  Restricted or branded payout
        ↓
  Citizen + admin friction + capture
```

**Counterfactual always required:**  
“Could government (or pure cash wage) do this **directly** at lower cost and higher freedom?”

If yes → **abolish or open-tender the middleman**.  
If no → publish the proof.

---

## 4. Links into DOGE data

| Asset | Role |
|-------|------|
| Leaderboard `lb_cheque_economy` | Seed narrative + research hook |
| Leaderboard `lb_union_unemp_pay` | Seed narrative + FOI hook |
| `foi_queue` gaps | Exact € when unknown |
| `research_queue` | Next loop tasks |

Update this note when FOI or official unit costs arrive.
