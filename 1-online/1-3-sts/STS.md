# **STS**

### *Structured Task Specification — Deterministic Operational Meaning*

**Version:** 2026‑08‑19

---

## **Purpose**

STS (Structured Task Specification) converts AML’s structured meaning into a **deterministic, implementation‑free operational description** of *what must be done*.

STS defines:

- the operational structure  
- the responsibilities  
- the flows  
- the boundaries  
- the constraints  
- the invariants  
- the required outputs  

STS does **not** define *how* to implement the task.  
It defines *what must be true* for any correct implementation.

STS is the final design‑time artifact before PSC and Implementation.

---

## **Role in the Online ↔ Offline Pairing**

STS belongs entirely to the **online (design‑time)** stage.

- **Online:** STS defines the deterministic operational meaning.  
- **Offline:** deterministic execution follows STS through InjectML packs.

PairWise and InjectML both rely on STS to ensure reproducible behavior.

---

## **Position in the HCMD Pipeline**

STS follows AML and precedes PSC:

1. Meaning  
2. Meaning Stabilization  
3. AML  
4. **STS**  
5. PSC  
6. Implementation  

STS is the first artifact that defines **operational structure**.

---

## **Requirements**

STS must satisfy the following requirements:

1. **Derived solely from AML**  
   STS introduces no new semantics.

2. **Deterministic**  
   STS must be interpretable without ambiguity.

3. **Implementation‑free**  
   STS contains no algorithms, code, or control flow.

4. **Operational**  
   STS defines *what must be done*, not *how* to do it.

5. **Complete**  
   All operational requirements must be present.

6. **Explicit boundaries**  
   STS must define what is inside and outside the task.

7. **Explicit constraints and invariants**  
   STS must preserve AML’s constraints and invariants.

8. **Explicit inputs and outputs**  
   STS must define the operational interface.

9. **Suitable for PSC generation**  
   PSC depends entirely on STS.

STS is the operational backbone of deterministic meaning injection.

---

## **Why STS Is Necessary**

AML defines structured meaning, but it is still **semantic**, not operational.

InjectML and deterministic execution require:

- operational responsibilities  
- operational boundaries  
- operational constraints  
- operational invariants  
- operational flows  
- operational outputs  

These cannot be extracted directly from AML.

STS provides the **operational structure** needed for PSC and Implementation.

Without STS:

- PSC would be inconsistent  
- deterministic execution would fail  
- InjectML packs would be unstable  
- PairWise would lose reproducibility  

STS is the operational foundation of deterministic behavior.

---

## **Connection to Deterministic Behavior**

Deterministic behavior requires:

- stabilized meaning  
- structured meaning (AML)  
- operational meaning (STS)  
- deterministic packs (InjectML)  
- deterministic runtime (offline execution)  

STS is the stage where meaning becomes **operationally deterministic**.

If STS is unstable, PSC becomes unstable.  
If PSC is unstable, implementation becomes unstable.  
If implementation is unstable, deterministic execution becomes impossible.

STS is the anchor of operational reproducibility.

---

## **Connection to InjectML**

InjectML uses STS to define:

- how rules must be normalized  
- how tokens must be assembled  
- how packs must be structured  
- how boundaries must be enforced  
- how deterministic execution must behave  

InjectML’s deterministic pipeline is a **runtime reflection** of STS.

STS → PSC → Implementation → InjectML packs  
is the operational chain.

---

## **Connection to PairWise**

PairWise demonstrates STS implicitly.

Normalized rules:

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

map directly to STS concepts:

- **Inputs:** dish  
- **Outputs:** wine + reason  
- **Constraints:** one wine per dish  
- **Invariants:** reasons must be one sentence  
- **Operational flow:**  
  - read dish  
  - locate rule  
  - output wine + reason  
- **Boundaries:**  
  - no inference beyond rules  
  - no probabilistic reasoning  
  - no external knowledge  

PairWise’s deterministic behavior is possible because its normalized rules implicitly satisfy STS requirements.

STS is the conceptual layer that explains why PairWise works.

---

## **Structure**

STS is structured into the following sections:

### **1. Operational Domain**

Defines the operational scope and boundaries.

### **2. Inputs**

Defines the required inputs for the task.

### **3. Outputs**

Defines the required outputs for the task.

### **4. Responsibilities**

Defines what the system must do.

### **5. Constraints**

Defines operational constraints derived from AML.

### **6. Invariants**

Defines conditions that must remain true across all operations.

### **7. Boundaries**

Defines what is inside and outside the operational scope.

### **8. Operational Flow**

Defines the required sequence of conceptual operations  
(*not* algorithms or control flow).

### **9. Non‑Goals**

Defines what STS explicitly excludes.

These sections form the operational meaning foundation for PSC.

---

## **Determinism**

STS must be deterministic.  
Determinism requires:

- no ambiguity  
- no optional semantics  
- no alternative interpretations  
- no unresolved references  
- no implicit assumptions  
- no procedural drift  

Determinism ensures that PSC and Implementation are reproducible.

---

## **Domain‑Agnostic Representation**

STS’s structure is universal:

- operational domain  
- inputs  
- outputs  
- responsibilities  
- constraints  
- invariants  
- boundaries  
- operational flow  
- non‑goals  

This structure applies to:

- food pairing  
- safety rules  
- compliance rules  
- medical triage  
- structured Q&A  
- domain‑specific decision systems  

STS expresses operational meaning in a form that can be used across domains.

---

## **Implementation‑Free Representation**

STS must not contain:

- programming constructs  
- data structures  
- control flow  
- algorithms  
- operational logic  

These appear later in PSC and Implementation.

STS describes **operational meaning**, not execution.

---

## **Example Structure (Template)**

This template defines the required STS structure.  
Content must be filled based on AML.

### **Operational Domain**

[To be completed]

### **Inputs**

[To be completed]

### **Outputs**

[To be completed]

### **Responsibilities**

[To be completed]

### **Constraints**

[To be completed]

### **Invariants**

[To be completed]

### **Boundaries**

[To be completed]

### **Operational Flow**

[To be completed]

### **Non‑Goals**

[To be completed]

---

## **Status**

STS is a required public artifact.  
It must be completed before PSC generation and before any deterministic execution.
