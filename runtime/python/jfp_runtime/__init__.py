# JFP v0.8 Runtime Structure

This directory contains the Python reference implementation of the JFP v13.0.0 runtime engine.

## Structure

```
jfp_runtime/
├── __init__.py
├── cli.py                    # CLI interface
├── parser.py                 # JFP text parser
├── validator.py              # Schema and semantic validation
├── planner.py                # DAG planner for execution
├── executor.py               # Task executor with proof
├── generator.py              # Smart spec generator
├── plugin.py                 # Plugin system
├── models/
│   ├── document.py          # JFP document model
│   ├── task.py              # Task model
│   ├── constraint.py        # Constraint model
│   └── proof.py             # Proof chain model
├── adapters/
│   ├── continue.py          # Continue.dev bridge
│   ├── cline.py             # Cline bridge
│   └── aider.py             # Aider bridge
├── templates/
│   ├── python-cli.jfp
│   └── fastapi.jfp
└── schemas/
    └── jfp_v13.schema.json
```

## Installation

```bash
pip install -e .
```

## Usage

```bash
jfp doctor
jfp validate examples/spec.jfp
jfp run examples/spec.jfp
```

## Development Status

- ✅ Parser skeleton
- ✅ Validator skeleton
- ✅ Planner skeleton
- ✅ Executor skeleton
- ✅ CLI skeleton
- 🔨 Full implementation in progress

## Next Phase

v0.9 will include:
- Complete parser implementation
- Plugin system refinement
- Enhanced adapter support
- Performance optimization

See [ROADMAP](../../docs/ROADMAP.md) for details.
