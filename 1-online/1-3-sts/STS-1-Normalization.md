# **STS‑1‑Normalization.md**

### *Operational STS — Rule Normalization*

**Version:** 2026‑08‑19

---

## **Purpose**

STS‑1 (Normalization) is the **first operational subsystem** derived from the conceptual STS defined in **STS.md**.

Its purpose is to convert domain rules into a **deterministic, consistent, and structurally aligned** format suitable for:

- AML interpretation  
- STS operational flow  
- InjectML pack assembly  
- deterministic offline execution  

Normalization ensures that all rules follow a **single, stable, reproducible structure**.

---

## **Relation to STS.md**

STS‑1 is the **operational implementation** of the following STS sections:

- **Responsibilities**  
  STS‑1 ensures rules are prepared for deterministic operation.

- **Constraints**  
  STS‑1 enforces domain constraints (e.g., one wine per dish).

- **Invariants**  
  STS‑1 enforces structural invariants (e.g., reason must be one sentence).

- **Boundaries**  
  STS‑1 ensures rules do not introduce external knowledge or inference.

- **Operational Flow**  
  STS‑1 defines the first step in the operational flow:  
  **normalize → tokenize → load → execute**

STS‑1 is the first concrete step where STS becomes operational.

---

## **Role in the Online ↔ Offline Pairing**

STS‑1 belongs to the **online (design‑time)** stage.

- **Online:** Rules are normalized deterministically.  
- **Offline:** Normalized rules are executed deterministically.

PairWise and InjectML both rely on STS‑1 to ensure reproducible behavior.

---

## **Requirements**

Normalization must satisfy the following requirements:

1. **Deterministic structure**  
   Every rule must follow the same format.

2. **Derived solely from stabilized meaning**  
   No new semantics may be introduced.

3. **Domain‑consistent**  
   Terminology must match AML and STS definitions.

4. **Implementation‑free**  
   No algorithms or code appear in normalized rules.

5. **Complete**  
   All required fields must be present.

6. **Explicit boundaries**  
   Rules must not rely on external knowledge.

7. **Explicit constraints**  
   Domain constraints must be enforced.

8. **Explicit invariants**  
   Structural invariants must be preserved.

Normalization prepares rules for deterministic tokenization (STS‑2).

---

## **Normalization Activities**

Normalization consists of the following activities:

### **1. Structural Alignment**

Convert rules into a consistent structure.

Example (PairWise):

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

### **2. Terminology Alignment**

Ensure entity names match AML definitions.

- “Food” → “Dish”  
- “Drink” → “Wine”

### **3. Field Completeness**

Ensure all required fields are present.

- Dish  
- Wine  
- Reason

### **4. Constraint Enforcement**

Ensure domain constraints are satisfied.

Example:

- One wine per dish  
- Reason must be one sentence

### **5. Invariant Enforcement**

Ensure structural invariants are preserved.

Example:

- Reason must be declarative  
- Reason must not contain procedural content

### **6. Boundary Enforcement**

Ensure rules do not rely on external knowledge.

Example:

- No inference beyond the rule  
- No probabilistic reasoning  
- No contextual guessing

Normalization produces rules ready for deterministic tokenization.

---

## **Connection to AML**

Normalized rules map directly to AML sections:

- **Entities:** Dish, Wine  
- **Relations:** pairs_with(dish, wine)  
- **Constraints:** one wine per dish  
- **Invariants:** reason must be one sentence  
- **Preconditions:** dish must exist  
- **Postconditions:** output must include wine + reason  

Normalization ensures AML can be derived deterministically.

---

## **Connection to Deterministic Behavior**

Deterministic behavior requires:

- normalized rules  
- deterministic tokenization  
- deterministic pack loading  
- deterministic execution  

If rules are not normalized:

- tokenization becomes unstable  
- pack loading becomes inconsistent  
- execution becomes unpredictable  

Normalization is the foundation of deterministic execution.

---

## **Connection to InjectML**

InjectML uses normalized rules to:

- assemble deterministic packs  
- enforce structural invariants  
- enforce domain constraints  
- ensure reproducible behavior  
- ensure offline execution matches online meaning  

Normalization → Tokenization → Pack Loading → Execution  
is the InjectML operational pipeline.

STS‑1 is the first step.

---

## **Connection to PairWise**

PairWise demonstrates normalization explicitly.

Every rule in PairWise follows the normalized structure:

```
Dish: <dish>
Wine: <wine>
Reason: <one-sentence reason>
```

PairWise’s reproducibility depends on:

- consistent rule structure  
- consistent terminology  
- consistent constraints  
- consistent invariants  

STS‑1 explains why PairWise works deterministically.

---

## **Structure**

Normalized rules must follow this structure:

### **Dish**

The dish name.  
Must match domain terminology.

### **Wine**

The recommended wine.  
Must satisfy domain constraints.

### **Reason**

A one‑sentence explanation.  
Must satisfy structural invariants.

This structure is universal across all normalized rules.

---

## **Normalization Template**

This template defines the required normalized rule structure.

```
Dish: [dish-name]
Wine: [wine-name]
Reason: [one-sentence explanation]
```

---

## **Normalization Checklist**

Before tokenization (STS‑2), verify:

- [ ] Dish is present  
- [ ] Wine is present  
- [ ] Reason is present  
- [ ] Reason is one sentence  
- [ ] Terminology matches AML  
- [ ] Constraints are satisfied  
- [ ] Invariants are satisfied  
- [ ] No external knowledge  
- [ ] No procedural content  
- [ ] No ambiguity  

This checklist ensures deterministic behavior.

---

## **Status**

STS‑1 is a required operational artifact.  
It must be completed before STS‑2 (Tokenization) and before any deterministic execution.


