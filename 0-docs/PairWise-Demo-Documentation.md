# **PairWise‑Demo‑Documentation**

### *Kitchen Class Workbook — InjectML Example*

**Version:** 2026‑08‑19  
**Model:** llama3:8b (Ollama)

---

# **1. Introduction — Welcome to the Kitchen Class**

PairWise is the *kitchen class* of InjectML.  
It teaches you how to inject structured domain knowledge into an offline model **without training**, using deterministic rules and token packs.

You will learn the method the same way you learn a dish in a cooking class:

- **Online (in class):** GitHub Copilot stands beside you like a professional chef, helping you prepare the ingredients and refine the steps.  
- **Offline (at home):** You repeat the same steps using Ollama, confirming you can reproduce the dish independently.

This pairing — **online ↔ offline** — mirrors the culinary pairing at the heart of the example — **wine ↔ dish**.  
Two complementary components, matched correctly, produce a successful outcome.

PairWise is your first dish.

---

# **2. What PairWise Demonstrates**

PairWise shows how InjectML can make an offline model behave as if it were trained on domain knowledge — **without training**.

We use:

- 40 Wine–Dish pairing rules  
- deterministic normalization  
- model‑specific tokenization  
- structured pack assembly  
- offline execution via Ollama  

The model answers pairing questions using **only** the injected knowledge.

This is InjectML’s promise:

> **Training without training.  
> Meaning without fine‑tuning.  
> Determinism without randomness.**

---

# **3. The PairWise Knowledge Pack**

A knowledge pack is a structured set of rules prepared like ingredients in a kitchen.

Each rule has three lines:

```
Dish: <value>
Wine: <value>
Reason: <value>
```

Why this structure?

- easy for humans  
- easy for tokenizers  
- easy for deterministic assembly  
- easy for reproducible inference  

This is your ingredient list.

---

# **4. The Deterministic Pipeline**

PairWise uses a four‑step pipeline:

```
[1] Rule Normalization
[2] Tokenization
[3] Knowledge Pack Assembly
[4] Deterministic Execution
```

### ASCII Diagram

```
 ┌────────────────────┐
 │  Normalized Rules  │  (human-readable)
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │    Tokenization    │  (model-specific IDs)
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │ Knowledge Pack     │  (augmented context)
 └─────────┬──────────┘
           │
           ▼
 ┌────────────────────┐
 │ Deterministic Run  │  (temperature=0)
 └────────────────────┘
```

This is your recipe.

---

# **5. Step 1 — Rule Normalization**

### Artifact: `pairwise_rules_normalized.txt`

We normalize 40 Wine–Dish rules.

### Requirements

- ASCII‑only  
- three‑line structure  
- one blank line between rules  
- alphabetical sorting by dish  
- no duplicates  
- no trailing whitespace  
- one‑sentence reasons ending with a period  

Normalization ensures:

- deterministic tokenization  
- deterministic pack assembly  
- deterministic inference  

This is your **mise en place** — preparing ingredients.

---

# **6. Step 2 — Tokenization**

### Artifact: `pairwise_tokens.json`

### Tokenizer: LLaMA‑3 tokenizer

We convert each normalized rule into **model‑specific token IDs**.

### Key details

- **Model:** llama3:8b  
- **Tokenizer:** `meta-llama/Llama-3-8B`  
- **BOS token ID:** `128000`  
- **Boundary marker:** `128009` (`<|eot_id|>`)  
- **Output:** JSON array of token‑ID arrays  

Token IDs are model‑specific.  
A pack built for llama3:8b will **not** work for phi‑3 or qwen2.5.

This is your **ingredient measurement** step.

---

# **7. Step 3 — Knowledge Pack Assembly**

### Artifact: `pairwise_loader.py`

We assemble the augmented context:

```
128000
<rule_1_tokens>
128009
<rule_2_tokens>
128009
...
<rule_40_tokens>
128009
<tokenized_user_prompt>
```

### Requirements

- deterministic concatenation  
- correct boundary markers  
- no extra whitespace  
- no reordering  
- total context length: **1,059 tokens**

This is your **mixing ingredients** step.

---

# **8. Step 4 — Deterministic Execution**

### Environment

Offline Ollama + llama3:8b

### Inference settings

- `temperature = 0`  
- `top_p = 1`  
- no sampling  
- no randomness  

### Example query

> “What wine pairs best with sushi?”

### Deterministic output

> **dry Riesling**  
> because its acidity complements delicate flavors and umami.

Matches the rule:

```
Dish: sushi
Wine: dry Riesling
Reason: Its acidity complements the delicate flavors and umami of sushi.
```

This is your **serving the dish** step.

---

# **9. Online ↔ Offline Pairing (HCMD‑Compatible)**

PairWise teaches the HCMD pairing through the kitchen class metaphor:

### **Online = Cooking class**

GitHub Copilot stands beside you like a professional chef:

- stabilizing meaning  
- refining structure  
- helping with normalization  
- helping with tokenization  
- helping with pack assembly  
- helping you avoid mistakes  

### **Offline = Home kitchen**

Ollama executes the same structured steps:

- deterministic loading  
- deterministic inference  
- reproducible outputs  
- no training  
- no cloud  
- no Copilot  

This pairing mirrors the **wine ↔ dish** pairing:

> **Two complementary components  
> matched correctly  
> produce a successful outcome.**

This is the quiet educational challenge built into PairWise.

---

# **10. Common Mistakes**

Beginners often:

- use the wrong tokenizer  
- forget boundary markers  
- skip normalization  
- mix tokens from different models  
- exceed context length  
- use non‑deterministic inference settings  

Avoid these and your dish will come out perfectly.

---

# **11. Generalizing PairWise**

You can build your own knowledge pack by:

1. writing domain rules  
2. normalizing them  
3. tokenizing them  
4. assembling them  
5. running deterministic inference  

InjectML works for:

- food pairing  
- safety rules  
- compliance checks  
- medical triage  
- structured decision systems  
- domain‑specific Q&A  

PairWise is just the first dish.

---

# **12. Design‑Time vs Runtime**

### **Design‑time (online)**

- GitHub Copilot  
- normalization  
- tokenization  
- pack assembly  
- determinism testing  

### **Runtime (offline)**

- Ollama  
- llama3:8b  
- deterministic inference  

This separation ensures reproducibility.

---

# **13. Summary**

You have learned:

- how to normalize domain rules  
- how to tokenize them deterministically  
- how to assemble a knowledge pack  
- how to run offline deterministic inference  
- how InjectML achieves training without training  
- how the online ↔ offline pairing mirrors the wine ↔ dish pairing  

PairWise is your first InjectML dish.  
More dishes await in InjectML‑Examples.
