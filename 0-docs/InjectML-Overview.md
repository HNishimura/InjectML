# **InjectML Overview**

## Purpose

InjectML is a deterministic meaning‑injection framework designed to embed human‑defined concepts, rules, and relationships directly into machine learning pipelines. It provides a structured way to ensure that model behavior remains interpretable, stable, and aligned with human intent.

InjectML does not rely on probabilistic training. Instead, it uses explicit knowledge packs, deterministic rules, and injection operators to produce reproducible behavior. InjectML is suitable for environments where semantic clarity, offline operation, and predictable outputs are required.

InjectML is conceptually compatible with the Human‑Centered Meta‑Development (HCMD) framework. HCMD provides the theoretical foundation for structured meaning and deterministic development. InjectML provides a practical implementation of meaning injection within ML systems.

## Conceptual Foundation

InjectML is grounded in three stable ideas:

### **1. Concepts**

Human‑defined semantic units that describe the domain. Concepts define the structure of meaning that will be injected into the ML pipeline.

### **2. Knowledge Packs**

Deterministic collections of rules, tokens, mappings, and relationships. Knowledge packs define how concepts interact and how they are applied to data.

### **3. Injection Operators**

Structured operators that apply concepts and knowledge packs to data, models, or outputs. Injection operators enforce semantic constraints and produce deterministic results.

These components form the operational surface of InjectML. They provide a clear, reproducible pathway from human intent to machine behavior.

## Deterministic Behavior

InjectML produces reproducible behavior through:

- Explicit rules  
- Deterministic tokenization  
- Stable knowledge packs  
- Structured injection operators  
- Clear interpretation flows  

InjectML does not use machine learning training. All behavior is derived from explicit human‑defined structure.

## Relationship to HCMD

InjectML is compatible with the HCMD framework, which will be described in detail in the upcoming HCMD arXiv paper. HCMD provides the conceptual stance for structured meaning, while InjectML provides a practical implementation of deterministic meaning injection.

InjectML can be viewed as:

- **HCMD’s application layer**  
- A concrete demonstration of structured meaning in action  
- A reproducible example of deterministic semantic control  
- A practical tool for developers and researchers

InjectML does not expose HCMD’s internal layers. Instead, it provides a clean, public‑safe interface built on HCMD’s principles.

## Training Without Training

InjectML demonstrates that structured meaning injection can replace local model training in constrained domains. InjectML uses deterministic rules, tokens, packs, and engines to produce stable outputs without probabilistic learning.

This approach is suitable for:

- Offline environments  
- Safety‑critical systems  
- Domains requiring interpretability  
- Systems with strict semantic constraints  
- Environments where training is impractical or undesirable

## Repository Structure

InjectML uses a fixed directory structure:

- **docs/** — Public documentation  
- **examples/** — Demonstrations and example pipelines  
- **injectml/** — Core implementation  
- **offline resources** — Deterministic rules, tokens, and packs  

This structure provides a clear separation between documentation, examples, 
and core functionality.

## Hands‑On Example

InjectML includes a complete, reproducible example that demonstrates how structured domain knowledge can be injected into an offline model without training. This example is called PairWise, and it acts as a kitchen class workbook for InjectML.

In the PairWise demo, you learn how to:

- normalize domain rules
- tokenize them using the model’s tokenizer
- assemble a deterministic knowledge pack
- run offline inference using Ollama
- reproduce results without training

PairWise shows how InjectML pairs online design‑time (with GitHub Copilot assisting you like a professional chef in class) with offline runtime (where you repeat the same steps at home using Ollama). This pairing is intentional and follows the HCMD method:

- online = guided structured design,
- offline = deterministic execution.

For the full step‑by‑step walkthrough, see [PairWise‑Demo‑Documentation.md](PairWise‑Demo‑Documentation.md) .

## Status

This document is a public artifact. It provides the conceptual overview required for understanding InjectML’s purpose, structure, and relationship to HCMD.
