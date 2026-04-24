# JFP — JARO Flash Protocol Overview

## What is JFP?

**JFP (JARO Flash Protocol)** is a deterministic specification protocol, DSL, and runtime framework for turning structured human intent into validated execution plans for AI agents, IDE assistants, and software automation.

### Core Philosophy

JFP separates:
- **Facts** from opinions
- **Options** from decisions
- **Actions** from results
- **Output** from accountability

This creates a **deterministic, auditable, and reproducible** system where:
- No hallucinations hide in the logic
- Deviations from baseline are detected
- Proof chains remain explicit
- Safety gates prevent unsafe execution

## What JFP Is NOT

❌ **Not a general AI system** — JFP doesn't guess or speculate freely
❌ **Not just a framework** — It's a specification standard
❌ **Not vague productivity advice** — Everything is structured and measurable
❌ **Not a black box** — All reasoning is transparent and reproducible

## Core Use Cases

### 1. AI Agent Task Execution
Structure complex AI workflows with explicit state, decisions, and proof.

### 2. Software Build Specifications
Define reproducible build plans that survive system changes.

### 3. Patch and Modification Specs
Clear, auditable records of what changed and why.

### 4. Decision Records
Leave a permanent trace of decisions with proof and review attached.

### 5. Conversation Compression
Compress long discussions into portable, parseable state.

## Classification

**JFP = Protocol + DSL + Runtime Framework**

- ✅ **Protocol** — Deterministic communication specification
- ✅ **Technical Standard** — Formal syntax and semantics
- ✅ **Execution Framework** — Runtime engine from v13+
- ✅ **Library** — Python CLI implementation
- ✅ **DSL** — Domain-Specific Language (in development)

## How JFP Works

### The JFP Process

```
Human Intent
    ↓
Structured Input (JFP Document)
    ↓
Canonical AST (JSON)
    ↓
Validation & Baseline Check
    ↓
Execution Plan
    ↓
Deterministic Execution
    ↓
Proof & Audit Trail
```

### Key Components

1. **META Section** — Document metadata, version, type
2. **BUILD_GRAPH** — Task dependencies and execution order
3. **OUTPUT_MAP** — Expected outputs and acceptance criteria
4. **CONSTRAINTS** — Safety rules and boundaries
5. **ACCEPTANCE** — Proof of successful execution

## JFP Versions

### v1.0 — Conversation Compression
Original protocol establishing conversation state compression.

### v5.0 — Deterministic Foundation
Mature deterministic standard with refined semantics.

### v5.3 — Open Standard Candidate
Enhanced validation, safety gates, and proof chains.

### v13.0.0 — Active Runtime/Agent Execution
Current active development with:
- Full runtime engine
- Agent execution framework
- IDE adapter integration
- Deterministic proactivity

## Learning Resources

### Official Books by Jaroslaw Kuchta

**📚 JFP for Beginners** — [Kindle Edition](https://amzn.eu/d/064Pgcvc)
- Practical introduction to JFP
- Learn v1, v2, v3 versions
- Step-by-step learning path
- Exercises with solutions
- Educational JFP v3 parser

**📚 JFP Architecture & Decision Systems** — [Kindle Edition](https://a.co/d/0eEcDZa0)
- Deep dive into decision architecture
- Deterministic proactivity without speculation
- Baseline, proof chain, and safety gates
- Applications for edge systems and monitoring

## Next Steps

1. **Read JFP_OVERVIEW.md** (you are here)
2. **Explore examples/** folder
3. **Review standards/** for your version
4. **Check ROADMAP.md** for development plans
5. **See HISTORY.md** for version evolution

## Community

- **Team:** VIKI VIPER (HTB/CTF)
- **License:** MIT
- **Contributing:** Open for discussion and standards proposals
