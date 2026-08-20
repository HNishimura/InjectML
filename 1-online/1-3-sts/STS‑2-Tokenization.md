# **STS‑2‑Tokenization**

### *Operational STS — Deterministic Tokenization*

**Version:** 2026‑08‑19

---

## **Purpose**

STS‑2 (Tokenization) is the **second operational subsystem** derived from the conceptual STS defined in **STS.md**.

Its purpose is to convert **normalized rules** (from STS‑1) into **deterministic token sequences** suitable for:

- InjectML pack assembly  
- deterministic offline execution  
- reproducible behavior across runs  

Tokenization ensures that every normalized rule is transformed into a **stable, ordered, reproducible** sequence of tokens.

---

## **Relation to STS.md**

STS‑2 is the **operational implementation** of the following STS sections:

- **Inputs**  
  STS‑2 receives normalized rules.

- **Outputs**  
  STS‑2 produces deterministic token sequences.

- **Responsibilities**  
  STS‑2 ensures rules are tokenized deterministically.

- **Constraints**  
  STS‑2 enforces domain constraints during tokenization.

- **Invariants**  
  STS‑2 preserves structural invariants (e.g., field order).

- **Boundaries**  
  STS‑2 ensures tokenization does not introduce new semantics.

- **Operational Flow**  
  STS‑2 defines the second step in the operational flow:  
  **normalize → tokenize → load → execute**

STS‑2 is the stage where structured meaning becomes structured tokens.

---

## **Role in the Online ↔ Offline Pairing**

STS‑2 belongs to the **online (design‑time)** stage.

- **Online:** Rules are tokenized deterministically.  
- **Offline:** Token sequences are executed deterministically.

PairWise and InjectML both rely on STS‑2 to ensure reproducible behavior.

---

## **Requirements**

Tokenization must satisfy the following requirements:

1. **Deterministic ordering**  
   Tokens must be produced in a stable, reproducible order.

2. **Derived solely from normalized rules**  
   No new semantics may be introduced.

3. **Domain‑consistent**  
   Tokenization must preserve AML and STS structure.

4. **Implementation‑free**  
   No algorithms or code appear in token sequences.

5. **Complete**  
   All fields must be tokenized.

6. **Explicit boundaries**  
   Tokenization must not rely on external knowledge.

7. **Explicit constraints**  
   Domain constraints must be preserved.

8. **Explicit invariants**  
   Structural invariants must be preserved.

Tokenization prepares rules for deterministic pack loading (STS‑3).

---

## **Tokenization Activities**

Tokenization consists of the following activities:

### **1. Field Ordering**

Tokens must follow a deterministic field order:

1. Dish  
2. Wine  
3. Reason  

This order is universal across all rules.

### **2. Field Label Tokenization**

Field labels must be tokenized consistently:

- “Dish:”  
- “Wine:”  
- “Reason:”  

### **3. Field Value Tokenization**

Field values must be tokenized deterministically.

Example:

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

### **4. Boundary Marker Insertion**

Boundary markers must be inserted to separate fields.

Example:

```
<DISH_START> sushi <DISH_END>
<WINE_START> dry Riesling <WINE_END>
<REASON_START> Its acidity complements the delicate flavors and umami of sushi. <REASON_END>
```

### **5. Constraint Preservation**

Tokenization must preserve domain constraints.

Example:

- One wine per dish  
- Reason must be one sentence  

### **6. Invariant Preservation**

Tokenization must preserve structural invariants.

Example:

- Field order must not change  
- Boundary markers must be present  
- No procedural content  

Tokenization produces deterministic token sequences ready for pack loading.

---

## **Connection to AML**

Tokenization maps directly to AML sections:

- **Entities:** Dish, Wine  
- **Relations:** pairs_with(dish, wine)  
- **Constraints:** one wine per dish  
- **Invariants:** reason must be one sentence  
- **Preconditions:** dish must exist  
- **Postconditions:** output must include wine + reason  

Tokenization ensures AML structure is preserved in token form.

---

## **Connection to Deterministic Behavior**

Deterministic behavior requires:

- normalized rules  
- deterministic tokenization  
- deterministic pack loading  
- deterministic execution  

If tokenization is unstable:

- pack loading becomes inconsistent  
- execution becomes unpredictable  
- reproducibility is lost  

Tokenization is the foundation of deterministic pack assembly.

---

## **Connection to InjectML**

InjectML uses tokenized rules to:

- assemble deterministic packs  
- enforce structural invariants  
- enforce domain constraints  
- ensure reproducible behavior  
- ensure offline execution matches online meaning  

Normalization → Tokenization → Pack Loading → Execution  
is the InjectML operational pipeline.

STS‑2 is the second step.

---

## **Connection to PairWise**

PairWise demonstrates tokenization implicitly.

Normalized rules:

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

map directly to token sequences:

```
<DISH_START> sushi <DISH_END>
<WINE_START> dry Riesling <WINE_END>
<REASON_START> Its acidity complements the delicate flavors and umami of sushi. <REASON_END>
```

PairWise’s reproducibility depends on:

- consistent field order  
- consistent boundary markers  
- consistent tokenization rules  

STS‑2 explains why PairWise works deterministically.

---

## **Structure**

Token sequences must follow this structure:

### **Dish Tokens**

```
<DISH_START> [dish-name] <DISH_END>
```

### **Wine Tokens**

```
<WINE_START> [wine-name] <WINE_END>
```

### **Reason Tokens**

```
<REASON_START> [one-sentence reason] <REASON_END>
```

This structure is universal across all tokenized rules.

---

## **Tokenization Template**

This template defines the required tokenization structure.

```
<DISH_START> [dish-name] <DISH_END>
<WINE_START> [wine-name] <WINE_END>
<REASON_START> [one-sentence reason] <REASON_END>
```

---

## **Tokenization Checklist**

Before pack loading (STS‑3), verify:

- [ ] Dish tokens present  
- [ ] Wine tokens present  
- [ ] Reason tokens present  
- [ ] Field order correct  
- [ ] Boundary markers correct  
- [ ] Terminology matches AML  
- [ ] Constraints preserved  
- [ ] Invariants preserved  
- [ ] No external knowledge  
- [ ] No procedural content  
- [ ] No ambiguity  

This checklist ensures deterministic behavior.

---

## **Status**

STS‑2 is a required operational artifact.  
It must be completed before STS‑3 (Knowledge‑Pack Loading) and before any deterministic execution.
