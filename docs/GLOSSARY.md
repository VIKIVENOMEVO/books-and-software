# JFP Glossary

## Core Concepts

### Atomic Fact
A single, deterministic, irreducible statement of truth. Cannot be subdivided without losing meaning. Forms the foundation of all JFP documents.

**Example:** "System uptime is 99.9%" is atomic. "System is good" is not.

### Baseline
The canonical, verified state against which all deviations are measured. Established at the beginning of execution and maintained throughout.

### BUILD_GRAPH
The section of a JFP document that defines:
- All tasks to be executed
- Dependencies between tasks
- Execution order
- Parallel vs. sequential execution

### BUILD_SPEC
A JFP document type used to define how to create or construct a system, project, or artifact from scratch.

**Related:** PATCH_SPEC

### Canonical AST
The standardized, language-independent abstract syntax tree (AST) that represents any JFP document. All parsers must produce identical canonical AST.

**Format:** JSON (current standard)

### CONSTRAINTS
The section of a JFP document that defines:
- Safety rules and boundaries
- Resource limits
- Forbidden actions
- Baseline enforcement rules
- Decision gates

### Decision Gate
A checkpoint where execution is halted pending human decision or safety verification. Prevents automatic execution of potentially unsafe operations.

**Related:** Signal Orange

### Deterministic
Producing the same output every time from the same input. No randomness, speculation, or hallucination.

**In JFP:** All execution paths are predictable and reproducible.

### DSL (Domain-Specific Language)
A language designed specifically for JFP task definition and execution. Sits at the intersection of human readability and machine parsability.

### Evidence Chain
A documented sequence of proofs showing how a decision was made, what was verified, and why it was accepted. Forms the basis of audit trails.

### Execution Model
The formal specification of:
- How JFP documents are parsed
- How baseline is verified
- How tasks are ordered and executed
- How proof is generated
- When execution is halted

### Hallucination
Under JFP: A deviation from specified logic where the system produces output not justified by proof or baseline.

**JFP Goal:** Eliminate hallucinations through determinism and explicit proof.

### JFP (JARO Flash Protocol)
A deterministic specification protocol, DSL, and runtime framework for turning structured human intent into validated execution plans for AI agents, IDE assistants, and software automation.

### META Section
The first section of a JFP document containing:
- Protocol version
- Document type (BUILD_SPEC, PATCH_SPEC, etc)
- Creation timestamp
- Author information
- Related document references

### Output Map
A section that specifies:
- What outputs are expected
- How to verify correctness
- Acceptance criteria
- Success conditions

### PATCH_SPEC
A JFP document type used to specify modifications to an existing system or project. Differs from BUILD_SPEC in that it describes changes, not creation.

**Related:** BUILD_SPEC

### Proof Chain
A sequence of verifiable steps demonstrating that:
1. The task was executed
2. The output matches specifications
3. Constraints were respected
4. Baseline was maintained

### Protocol
In JFP: A formal, documented specification of how communication and execution must occur. Language-independent.

### Reproducibility
The ability to execute the same JFP document in different environments and get identical or predictable results.

### Runtime
The execution engine that:
- Parses JFP documents
- Validates against baseline
- Executes tasks in order
- Generates proof
- Halts on safety violations

### Safety Gate
A constraint that prevents execution of actions deemed unsafe until:
- Explicit human approval is given
- Verification conditions are met
- Risk is demonstrated to be below threshold

### Section
A top-level organizational unit within a JFP document (META, BUILD_GRAPH, OUTPUT_MAP, CONSTRAINTS, ACCEPTANCE).

### Signal Orange
A controlled halt state triggered by:
- Unresolved ambiguity
- Safety constraint violation
- Baseline deviation
- Failed verification
- Pending decision gate

Indicates the system cannot proceed safely and requires human intervention.

**Related:** Decision Gate

### Specification
Formal documentation of:
- Syntax rules
- Semantics (meaning)
- Execution model
- Proof requirements
- Constraint handling

### Task
An individual unit of work within a BUILD_GRAPH. Has:
- Unique identifier
- Prerequisites (dependencies)
- Inputs
- Execution specification
- Expected outputs

### Trace
A complete record of:
- All decisions made
- All proofs generated
- All constraints checked
- All outputs produced

Forms an auditable history of execution.

### Validation
The process of confirming that a JFP document:
- Conforms to syntax rules
- Maintains baseline
- Satisfies constraints
- Has achievable outputs
- Is internally consistent

### VIKI SYSTEMS
The organization/team behind JFP development. Part of VIKI VIPER (HTB/CTF team).

---

## Version-Specific Terms

### v1.0 Concepts
- **Conversation Compression** — Reducing long discussions to portable state
- **State Snapshot** — A point-in-time capture of conversation state

### v5.0+ Concepts
- **Deterministic Execution** — Reproducible, predictable task execution
- **Proof System** — Formal verification of task completion
- **Baseline Enforcement** — Strict adherence to initial conditions

### v13.0.0 Concepts
- **Agent Compatibility** — Integration with LLMs and AI systems
- **IDE Adapter** — Plugins for Continue, Cline, Aider
- **Canonical AST** — Universal abstract syntax tree format
- **Parser Ecosystem** — Multi-language parser support

---

## Related Concepts

### CI/CD (Continuous Integration/Continuous Deployment)
JFP documents can serve as:
- Build specifications
- Deployment plans
- Test specifications
- Verification frameworks

### Audit Trail
Automatic record generated by JFP execution showing:
- What was done
- When it was done
- Why it was done
- What proof exists

### Deterministic AI
AI systems that:
- Make decisions based on explicit rules
- Provide verifiable reasoning
- Never speculate or hallucinate
- Maintain transparent audit trails

---

## Acronyms

| Acronym | Full Form |
|---------|----------|
| AST | Abstract Syntax Tree |
| DSL | Domain-Specific Language |
| JFP | JARO Flash Protocol |
| LLM | Large Language Model |
| META | Metadata (section) |
| CI/CD | Continuous Integration/Deployment |
| IDE | Integrated Development Environment |

---

For questions or clarifications, please open an issue.
