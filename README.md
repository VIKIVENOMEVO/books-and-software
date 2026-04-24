# JFP — JARO Flash Protocol

JFP is a deterministic specification protocol, DSL and runtime framework for turning structured human intent into validated execution plans for AI agents, IDE assistants and software automation.

## What is JFP?

**JFP — JARO Flash Protocol** is:

- **Deterministic protocol/specification** for communication and execution between humans, AI agents, and automation systems
- **Not just a library** — a comprehensive ecosystem
- **Classification:**
  - Protocol specification ✅
  - Technical standard ✅
  - Execution framework ✅ (runtime from v13)
  - Python CLI library ✅
  - DSL (Domain-Specific Language) ✅ (in development)

**Core concept:**
```
JFP = protocol + DSL + runtime framework
```

JFP structures facts, confidence levels, sections, and output **without hallucination**. It provides a deterministic layer that separates:
- Facts from opinions
- Options from decisions
- Actions from results
- Output from accountability

## Official Definition

**English:**
> JFP is a deterministic specification protocol and execution framework for structuring, validating, and running AI-agent tasks, software build plans, and machine-readable project instructions.

**Polish:**
> JFP to deterministyczny protokół specyfikacji i wykonania, służący do opisywania zadań, systemów, aplikacji i procesów w formacie czytelnym dla człowieka, parsera oraz agentów AI.

## Repository Purpose

This is the **official development home for JFP — JARO Flash Protocol**.

It contains:
- The JFP specification (multiple versions)
- Historical protocol versions
- Examples and documentation
- Validators and parsers
- Runtime engine
- CLI tools
- IDE-agent adapters (Continue, Cline, Aider)

**Goal:** Turn structured human intent into deterministic, validated execution plans for AI-assisted software development.

## Repository Structure

```
books-and-software/
├── README.md
├── LICENSE
├── docs/
│   ├── JFP_OVERVIEW.md
│   ├── ROADMAP.md
│   └── HISTORY.md
├── standards/
│   ├── jfp-v1.0/
│   │   ├── specification.md
│   │   ├── examples/
│   │   └── validators/
│   ├── jfp-v5.0/
│   │   ├── specification.md
│   │   ├── examples/
│   │   └── validators/
│   ├── jfp-v5.3/
│   │   ├── specification.md
│   │   ├── examples/
│   │   └── validators/
│   └── jfp-v13.0.0/
│       ├── specification.md
│       ├── examples/
│       ├── parsers/
│       └── validators/
├── runtime/
│   └── jfp_runtime_v0_8/
│       ├── engine.py
│       ├── cli.py
│       └── requirements.txt
├── examples/
│   ├── build_spec.jfp
│   ├── patch_spec.jfp
│   └── milestone_analysis.jfp
└── adapters/
    ├── continue/
    │   └── integration.md
    ├── cline/
    │   └── integration.md
    └── aider/
        └── integration.md
```

## JFP Versions

### v1.0 — Historical Foundation
The original protocol version that established the core concepts of deterministic state compression and validation.

### v5.x — Deterministic Foundation
The mature deterministic standard with refined protocol semantics, proof chains, and baseline detection.
- **v5.0** — Initial deterministic standard
- **v5.3** — Enhanced validation and safety gates

### v13.0.0 — Active Runtime/Agent Execution
Current active development version with:
- Full runtime engine support
- Agent execution framework
- IDE adapter integration
- Advanced deterministic proactivity

## Learning Resources

### Official Books

**📚 JFP for Beginners** — [Kindle Edition](https://amzn.eu/d/064Pgcvc)
by Jaroslaw Kuchta

A practical introduction to JFP for developers, AI users, and technical creators.

**Inside you'll learn:**
- JFP v1 — compress conversations into portable state
- JFP v2 — turn chaos into clear task flow
- JFP v3 — leave a decision trace using proof and review

**Includes:**
- Clear explanations of JFP mechanics
- Step-by-step learning path through v1, v2, v3
- Shared example across the whole book
- Exercises with ready-made solutions
- Educational JFP v3 parser for hands-on learning

---

**📚 JFP Architecture & Decision Systems** — [Kindle Edition](https://a.co/d/0eEcDZa0)
by Jaroslaw Kuchta

Deep dive into JFP decision architecture for readers who want to understand **why** the system works.

**Topics covered:**
- The problem of hallucination, drift, and loss of control
- JFP architecture step by step
- Deterministic proactivity without free-form speculation
- Baseline, proof chain, and safety gates
- Applications for edge systems, monitoring, and local runtime

## Quick Start

1. **Read the overview:** See [JFP_OVERVIEW.md](docs/JFP_OVERVIEW.md)
2. **Explore examples:** Check [examples/](examples/)
3. **Review specifications:** Start with [standards/jfp-v1.0/](standards/jfp-v1.0/)
4. **Integrate with your IDE:**
   - [Continue integration](adapters/continue/)
   - [Cline integration](adapters/cline/)
   - [Aider integration](adapters/aider/)

## VIKI SYSTEMS

Part of the VIKI ecosystem for deterministic AI systems and automation.

## License

See [LICENSE](LICENSE) for details.

## Topics

`ai-agents` • `dsl` • `protocol` • `runtime` • `developer-tools` • `automation` • `llm` • `specification` • `cli` • `deterministic-ai`

---

**JFP — JARO Flash Protocol** | Official Repository | v13.0.0 Active Development
