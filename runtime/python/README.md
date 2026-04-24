# JFP Runtime v0.8

**Deterministic execution engine for JFP v13.0.0**

JFP v13 runtime with:
- Parser (reference implementation)
- Validator with schema checking
- DAG planner for task execution
- Deterministic executor with proof generation
- Plugin system for extensibility
- Patch spec support
- Signal Orange (safety halt)
- Acceptance criteria verification
- IDE adapter bridges (Continue, Cline, Aider)
- Smart spec generator

## Quick Start

### Install

```bash
cd runtime/python
pip install -e .
```

### Verify Installation

```bash
jfp doctor --json
```

## Commands

### Initialization & Generation

```bash
# Create new CLI project
jfp init my_cli --template python-cli --with-adapters --with-examples

# Create new FastAPI project
jfp init my_api --template fastapi --with-adapters

# Generate spec from natural language
jfp generate "fastapi api z auth" --template fastapi --output SPEC.jfp
```

### Validation & Inspection

```bash
# Validate JFP document
jfp validate examples/spec.jfp --json

# Inspect document structure
jfp inspect examples/spec.jfp --json

# Generate execution plan
jfp plan examples/spec.jfp --json
```

### Execution

```bash
# Dry-run execution
jfp run examples/spec.jfp --dry-run --json

# Execute document
jfp run examples/spec.jfp --json

# Apply patch specification
jfp apply examples/patch_spec.jfp --root . --dry-run --json
```

### IDE Adapter Bridges

```bash
# Generate Continue.dev integration
jfp emit continue examples/spec.jfp

# Generate Cline packet
jfp emit cline examples/spec.jfp --output cline_packet.txt

# Generate Aider integration
jfp emit aider examples/patch_spec.jfp
```

## Architecture

```
JFP Document (text)
      ↓
   Parser (Python)
      ↓
Canonical JSON AST
      ↓
   Validator
      ↓
   Planner (DAG)
      ↓
   Executor
      ↓
Proof Chain & Audit Trail
```

## Components

### Parser
Reference implementation that converts JFP text to canonical JSON AST.

**Location:** `jfp_runtime/parser.py`

### Validator
Validates document against schema and semantic rules.

**Location:** `jfp_runtime/validator.py`

### Planner
Builds deterministic execution plan (DAG) from task dependencies.

**Location:** `jfp_runtime/planner.py`

### Executor
Executes tasks in dependency order with:
- Constraint checking
- Baseline verification
- Proof generation
- Safety gates (Signal Orange)

**Location:** `jfp_runtime/executor.py`

### CLI
Command-line interface for all operations.

**Location:** `jfp_runtime/cli.py`

### Adapters
Bridges to IDE assistants and external tools.

**Location:** `jfp_runtime/adapters/`

## Parser Ecosystem

JFP now includes a parser roadmap and canonical JSON AST definition.

### Canonical AST Standard

All parsers must produce identical JSON AST:

```json
{
  "version": "13.0.0",
  "type": "BUILD_SPEC",
  "meta": {...},
  "sections": {...},
  "tasks": [...],
  "dependencies": [...],
  "constraints": [...],
  "proof_chain": [...]
}
```

**See:** `parsers/ast/jfp_ast.schema.json`

### Parser Strategy

- **Python** — Reference implementation
- **JSON AST** — Canonical interchange format
- **Rust** — High-performance parser
- **Java** — Enterprise support
- **C** — Systems integration
- **BASIC** — Retro easter egg

**See:** `docs/ROADMAP.md` and `parsers/README.md`

## Patch Specs

Apply modifications to existing systems:

```bash
jfp apply examples/patch_spec.jfp --root .
```

Patch specs are full JFP documents that describe changes, not creation.

## Signal Orange

Controlled halt state triggered by:
- Safety constraint violation
- Baseline deviation
- Failed verification
- Unresolved ambiguity

```bash
jfp run spec.jfp --on-signal-orange pause  # Pause for user decision
jfp run spec.jfp --on-signal-orange abort  # Abort immediately
```

## Acceptance Criteria

Verify task completion:

```bash
jfp run spec.jfp --verify-acceptance --json
```

Returns detailed acceptance report with proof chain.

## Plugins

Extend JFP runtime with custom plugins:

```python
from jfp_runtime.plugin import JFPPlugin

class MyPlugin(JFPPlugin):
    def on_task_complete(self, task, output):
        # Custom logic
        pass
```

## Configuration

Create `.jfprc` in project root:

```ini
[runtime]
verbose = true
validate_on_load = true
generate_proof_chain = true

[adapters]
continue_enabled = true
cline_enabled = true
aider_enabled = true

[constraints]
strict_mode = true
safety_gates = true
```

## Examples

**See:** `examples/` directory

- `task_state.jfp` — Simple build task
- `proof_v3.jfp` — Security patch with proof
- `agent_task_packet.jfp` — AI agent task
- `compression_v1.jfp` — Conversation compression

## Testing

```bash
python -m pytest tests/
```

## Development

Clone and install in development mode:

```bash
git clone https://github.com/VIKIVENOMEVO/books-and-software.git
cd runtime/python
pip install -e ".[dev]"
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT License — See [LICENSE](../../LICENSE)

## Links

- [JFP Overview](../../docs/JFP_OVERVIEW.md)
- [JFP Roadmap](../../docs/ROADMAP.md)
- [Parser Documentation](../../parsers/README.md)
- [Canonical AST Schema](../../parsers/ast/jfp_ast.schema.json)
- [JFP Glossary](../../docs/GLOSSARY.md)

## Status

**v0.8.0** — Beta (Parser, Validator, Planner, Executor stable)

**Next:** v0.9 will add plugin system and enhanced adapter support.

---

**JFP Runtime** | Part of [JARO Flash Protocol](../../docs/JFP_OVERVIEW.md) | VIKI SYSTEMS
