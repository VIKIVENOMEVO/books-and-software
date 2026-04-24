# JFP v13.0.0 Standard

## Status

🟢 **Active Development** — Current standard for new projects

## Version

**13.0.0**

## Purpose

JFP v13.0.0 is the active runtime and agent execution standard designed for:
- AI agent task execution and coordination
- IDE assistant integration (Continue, Cline, Aider)
- Deterministic software build planning
- Proof-based decision records
- Enterprise-grade automation

## Core Philosophy

Everything is **deterministic, auditable, and reproducible**:
- No hallucinations hide in the logic
- All reasoning is transparent
- Deviations from baseline are detected
- Safety gates prevent unsafe execution
- Proof chains remain explicit and verifiable

## Overview

JFP v13.0.0 combines:
- **Protocol** — Formal communication specification
- **DSL** — Domain-specific language for task definition
- **Runtime** — Execution engine for deterministic task execution
- **Proof System** — Automatic audit trail generation

## Document Structure

### Required Sections

```
[META]
  version
  type
  timestamp
  author
  title (optional)
  description (optional)

[BUILD_GRAPH]
  tasks
  dependencies
  execution_order

[OUTPUT_MAP]
  expected_outputs
  delivery_criteria
  acceptance_rules

[CONSTRAINTS]
  safety_rules
  resource_limits
  baseline_enforcement
  decision_gates

[ACCEPTANCE]
  proof_chain
  verification_results
  audit_trail
```

## Document Types

### BUILD_SPEC
Define how to create or construct a system from scratch.

### PATCH_SPEC
Define modifications to an existing system.

### AGENT_TASK_PACKET
Define tasks for AI agent execution.

### DECISION_RECORD
Record decisions with proof and justification.

### CONVERSATION_COMPRESSION
Compress and preserve conversation state.

## Key Concepts

### Deterministic Execution
Same input always produces same output. No speculation, no randomness.

### Baseline
The canonical, verified state against which all deviations are measured.

### Proof Chain
A sequence of verifiable steps proving:
1. Task was executed
2. Output matches specifications
3. Constraints were respected
4. Baseline was maintained

### Safety Gate
A checkpoint preventing execution of unsafe operations until:
- Explicit human approval given
- Verification conditions met
- Risk demonstrated below threshold

### Signal Orange
Controlled halt state triggered by:
- Unresolved ambiguity
- Safety constraint violation
- Baseline deviation
- Failed verification
- Pending decision gate

## Syntax

### Basic Format

```
[SECTION]
key_1=value_1
key_2=value_2
task_id=task_name
```

### Key-Value Pairs

```
key=value
```

### Lists

```
list_item_1=value_1
list_item_2=value_2
```

### References

```
requires(task_id)
references(document_id)
```

## Semantics

### Task Execution
Tasks execute in order defined by dependencies:
1. Check preconditions
2. Execute task
3. Verify output
4. Record proof
5. Proceed to next task

### Constraint Evaluation
Constraints checked:
1. Before task execution (precondition)
2. During task execution (monitoring)
3. After task completion (verification)

### Proof Generation
Automatic proof chain records:
- When task started/ended
- What constraints were checked
- What outputs were produced
- Whether verification passed
- Any anomalies detected

## Compatibility

### Backward Compatibility
v13.0.0 is backward compatible with v5.3 documents.

### Forward Compatibility
Documents targeting v13.0.0 should remain compatible with v14+.

## Validation Rules

### Required Validations
1. All referenced tasks must exist
2. No circular dependencies
3. All constraints must be expressible
4. Acceptance criteria must be measurable
5. Proof chain must be complete

## Implementation Requirements

### Parser
Must produce canonical JSON AST matching schema.

### Validator
Must check:
- Syntax conformance
- Semantic validity
- Constraint expressibility
- Circular dependency detection

### Executor
Must:
- Execute tasks in dependency order
- Monitor constraints
- Generate proof chain
- Handle Signal Orange states
- Provide audit trail

## Security Considerations

### Constraint Safety
All constraints must be verifiable and enforced.

### Baseline Enforcement
No deviation from baseline without explicit proof and approval.

### Proof Immutability
Once recorded, proof cannot be modified or deleted.

### Audit Trail
Complete record of all decisions, changes, and executions.

## Performance

### Parsing
Document parsing should complete in < 100ms for typical documents.

### Validation
Validation should complete in < 50ms for typical documents.

### Execution
Task execution measured by task complexity, not protocol overhead.

## Examples

See `../../examples/` directory for complete examples:
- `task_state.jfp` — Simple build task
- `proof_v3.jfp` — Security patch with proof
- `agent_task_packet.jfp` — AI agent task

## See Also

- [JFP Overview](../../docs/JFP_OVERVIEW.md)
- [ROADMAP](../../docs/ROADMAP.md)
- [HISTORY](../../docs/HISTORY.md)
- [GLOSSARY](../../docs/GLOSSARY.md)
- [Canonical AST Schema](../../parsers/ast/jfp_ast.schema.json)
