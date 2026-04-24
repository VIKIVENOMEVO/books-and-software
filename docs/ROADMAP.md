# JFP Roadmap

## Vision

Transform JFP from a protocol specification into a complete, production-ready ecosystem with:
- Canonical specification and AST standard
- Parsers for major languages
- IDE integrations (Continue, Cline, Aider)
- Runtime engine for deterministic execution
- Commercial and enterprise features

## Phase 1: Foundation & Specification (NOW)

**Goal:** Establish canonical JFP specification and AST standard.

### Deliverables
- ✅ JFP Overview documentation
- ✅ Historical versions (v1.0, v5.0, v5.3)
- ✅ Current standard (v13.0.0) specification
- ✅ Example `.jfp` files
- ✅ Canonical JSON AST schema
- 🟡 Python reference parser (in progress)
- 🟡 Parser roadmap for other languages

## Phase 2: Core Parser Implementation (Q2-Q3 2026)

**Goal:** Deliver stable parsers that produce canonical AST.

### Deliverables
- **v0.1** Python reference parser (complete)
- **v0.2** Canonical JSON AST format (locked)
- **v0.3** Rust parser (deterministic, fast)
- **v0.4** Java parser (enterprise ready)
- **v0.5** C parser (systems integration)
- **v0.x** BASIC parser (easter egg, retro fun)

### Key Rule
**All parsers must produce identical canonical AST format.**

```json
{
  "version": "13.0.0",
  "type": "BUILD_SPEC",
  "sections": {
    "META": [],
    "BUILD_GRAPH": [],
    "OUTPUT_MAP": []
  },
  "tasks": [],
  "constraints": [],
  "acceptance": []
}
```

## Phase 3: Agent Adapters & IDE Integration (Q3-Q4 2026)

**Goal:** Integrate JFP into modern development tools.

### Deliverables
- **Continue integration** — Seamless code generation in Continue.dev
- **Cline integration** — AI-powered terminal and coding in Claude
- **Aider integration** — Autonomous code editor support
- **CLI tools** — `jfp validate`, `jfp execute`, `jfp proof`
- **Validator** — Real-time JFP document validation
- **Planner** — Automatic execution plan generation
- **Executor** — Deterministic task execution engine

## Phase 4: Runtime Engine (Q4 2026 - Q1 2027)

**Goal:** Full runtime execution with monitoring and proof.

### Deliverables
- **Local runtime** — Execute JFP specs locally
- **Agent compatibility** — Run with OpenAI, Claude, local models
- **Monitoring** — Real-time execution tracking
- **Proof chains** — Automatic audit trails
- **Safety gates** — Interrupt unsafe operations
- **Version control** — Track all JFP document changes

## Phase 5: Commercial Layer (Q1-Q2 2027)

**Goal:** Enterprise features and commercial offerings.

### Deliverables
- **JFP v14+** — Enhanced commercial standard
- **GUI/Dashboard** — Visual JFP editor and executor
- **Cloud Runner** — Hosted JFP execution
- **Enterprise Validation** — Advanced compliance checking
- **Team Collaboration** — Multi-user workflows
- **SLA & Support** — Professional support tiers

## Parser Implementation Timeline

### Now
- JSON AST schema finalized
- Python reference parser foundation
- Stub README files for future parsers

### Week 1-2
- Python parser complete and tested
- Canonical AST examples documented

### Week 3-4
- Rust parser (80% complete)
- Java parser skeleton

### Month 2
- Rust parser production ready
- Java parser functional
- C parser roadmap detailed

### Month 3+
- C parser implementation
- BASIC parser (fun project)
- TypeScript/JavaScript parser (if demand)

## Success Metrics

✅ **Specification** — JFP v13.0.0 is final and documented
✅ **AST** — Canonical JSON AST is the single source of truth
✅ **Parsers** — At least 3 language parsers producing identical AST
✅ **Integration** — JFP works in Continue, Cline, and Aider
✅ **Community** — Active usage and feedback from developers
✅ **Enterprise** — Commercial tier with customers

## Contributing

This roadmap is public and subject to community feedback. Have ideas? Open an issue or join the discussion.
