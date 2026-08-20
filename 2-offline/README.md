# 2-offline — Runtime Artifacts

This folder contains the **runtime artifacts** produced by the InjectML design-time
pipeline (Meaning → AML → STS → STS‑1/2/3). These files are **not documentation**.
They are the deterministic resources used by the offline execution engine.

## Why these files exist

GitHub Copilot generated these files automatically from the design-time
specifications. They represent the “compiled firmware” of the PairWise demo.

- The normalized rules come from STS‑1.
- The tokenized rules come from STS‑2.
- The knowledge pack comes from STS‑3.

The offline execution engine (in `injectml/`) loads these files to perform
deterministic execution as described in STS‑4.

## The Arduino Analogy

Think of:

- **Ollama + model** as an Arduino board.
- **Knowledge pack** as the firmware.
- **injectml runtime** as the flashed program.
- **2-offline** as the compiled firmware files.
- **GitHub Copilot** as the compiler/programmer.

This folder contains the firmware that the runtime engine uses.

## What each file is

- `pairwise_rules.txt`  
  Raw rules before normalization.

- `pairwise_rules_normalized.txt`  
  Rules after STS‑1 normalization.

- `pairwise_tokens.json`  
  Deterministic token sequences from STS‑2.

- `pairwise_loader.py`  
  Loader used by the runtime engine to assemble the pack.

## Important

These files are **not** part of the public documentation pipeline.
They should **not** be edited manually.
They are used only by the offline runtime engine.
