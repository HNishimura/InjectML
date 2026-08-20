# **AML.md**

### *Aligned Meaning Layer — Structured Meaning Representation*

**Version:** 2026‑08‑19

---

## **Purpose**

AML (Aligned Meaning Layer) converts **stabilized meaning** into a **structured, deterministic, and domain‑agnostic** representation.  
It is the first stage in the pipeline where meaning becomes **formally organized**.

AML is:

- implementation‑free  
- domain‑agnostic in structure  
- derived solely from stabilized meaning  
- the semantic foundation for STS  
- the first fully structured artifact in the design‑time sequence  

AML ensures that meaning is expressed in a form that is:

- precise  
- ordered  
- explicit  
- complete  
- suitable for deterministic processing  

AML is the bridge between conceptual meaning and operational structure.

---

## **Role in the Online ↔ Offline Pairing**

AML belongs entirely to the **online (design‑time)** stage.

- **Online:** Meaning is structured into AML.  
- **Offline:** Deterministic execution relies on AML‑derived STS.

PairWise and InjectML both depend on AML to ensure that structured meaning is stable and reproducible.

---

## **Position in the HCMD Pipeline**

AML follows Meaning Stabilization and precedes STS:

1. Meaning  
2. Meaning Stabilization  
3. **AML**  
4. STS  
5. PSC  
6. Implementation  

AML is the first artifact where meaning becomes **explicitly structured**.

---

## **Requirements**

AML must satisfy the following requirements:

1. **Derived solely from stabilized meaning**  
   AML introduces no new semantics.

2. **Deterministic**  
   AML must be interpretable without ambiguity.

3. **Domain‑agnostic**  
   AML’s structure is universal, even though content is domain‑specific.

4. **Implementation‑free**  
   AML contains no algorithms, code, or operational logic.

5. **Explicit entities and relations**  
   AML must define the conceptual components of the domain.

6. **Explicit constraints and invariants**  
   AML must express what must always be true.

7. **Explicit preconditions and postconditions**  
   AML must define the semantic boundaries of operations.

8. **Complete before STS generation**  
   STS depends entirely on AML.

9. **No procedural content**  
   AML does not describe steps or workflows.

10. **Semantic preservation**  
    AML must preserve all meaning from stabilized intent without modification.

AML is the structured meaning foundation for deterministic behavior.

---

## **Why AML Is Necessary**

Meaning Stabilization produces clear intent, but it is still **unstructured**.

STS requires:

- entities  
- relations  
- constraints  
- invariants  
- preconditions  
- postconditions  

These cannot be extracted directly from natural language.

AML provides the **structured semantic scaffolding** needed for STS.

Without AML:

- STS would be inconsistent  
- deterministic execution would fail  
- InjectML packs would be unstable  
- PairWise would lose reproducibility  

AML is the structural backbone of deterministic meaning injection.

---

## **Connection to Deterministic Behavior**

Deterministic behavior requires:

- stable meaning (Meaning Stabilization)  
- structured meaning (AML)  
- operational structure (STS)  
- deterministic packs (InjectML)  
- deterministic runtime (offline execution)  

AML is the stage where meaning becomes **machine‑interpretable without ambiguity**.

If AML is unstable, STS becomes unstable.  
If STS is unstable, deterministic execution becomes impossible.

AML is the anchor of reproducibility.

---

## **Connection to Rule Normalization (PairWise)**

PairWise demonstrates AML implicitly.

Normalized rules:

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

map directly to AML concepts:

- **Entities:** Dish, Wine  
- **Relations:** pairs_with(dish, wine)  
- **Constraints:** each dish has exactly one wine in this pack  
- **Invariants:** reasons must be one sentence  
- **Preconditions:** dish must exist in the domain  
- **Postconditions:** output must include wine + reason  

PairWise’s deterministic behavior is possible because its normalized rules implicitly satisfy AML requirements.

AML is the conceptual layer that explains why PairWise works.

---

## **Structure**

AML is structured into the following sections:

### **1. Domain Definition**

Defines the domain scope and boundaries.  
Derived solely from stabilized meaning.

### **2. Entities**

Defines the conceptual entities relevant to the domain.  
Entities must be named deterministically.

### **3. Relations**

Defines relationships between entities.  
Relations must be explicit and unambiguous.

### **4. Constraints**

Defines domain constraints.  
Constraints must be declarative.

### **5. Semantic Invariants**

Defines conditions that must remain true across all operations.

### **6. Preconditions**

Defines conditions required before any STS operation.

### **7. Postconditions**

Defines conditions required after any STS operation.

### **8. Non‑Goals**

Defines what AML explicitly excludes.  
Prevents semantic drift.

These sections form the structured meaning foundation for STS.

---

## **Determinism**

AML must be deterministic.  
Determinism requires:

- no ambiguity  
- no optional semantics  
- no alternative interpretations  
- no unresolved references  
- no implicit assumptions  

Determinism ensures that STS generation is reproducible and InjectML packs behave consistently.

---

## **Domain‑Agnostic Representation**

AML’s structure is universal:

- entities  
- relations  
- constraints  
- invariants  
- preconditions  
- postconditions  

This structure applies to:

- food pairing  
- safety rules  
- compliance rules  
- medical triage  
- structured Q&A  
- domain‑specific decision systems  

AML expresses meaning in a form that can be used across domains.

---

## **Implementation‑Free Representation**

AML must not contain:

- programming constructs  
- data structures  
- control flow  
- algorithms  
- operational logic  

These appear later in PSC and Implementation.

AML describes **semantic structure**, not execution.

---

## **Example Structure (Template)**

This template defines the required AML structure.  
Content must be filled based on stabilized meaning.

### **Domain Definition**

[To be completed]

### **Entities**

[To be completed]

### **Relations**

[To be completed]

### **Constraints**

[To be completed]

### **Semantic Invariants**

[To be completed]

### **Preconditions**

[To be completed]

### **Postconditions**

[To be completed]

### **Non‑Goals**

[To be completed]

---

## **Status**

AML is a required public artifact.  
It must be completed before STS generation and before any deterministic execution.
