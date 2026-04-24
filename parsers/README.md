# JFP Parsers

## Overview

Parsers convert JFP text documents into a **canonical JSON Abstract Syntax Tree (AST)**. This standardization ensures that all parsers, regardless of language, produce identical output for identical input.

## Core Principle

**All parsers must produce the same canonical AST format.**

This is what makes JFP a true standard, not just a format.

## Canonical AST Format

Every valid JFP document, regardless of which parser processes it, must produce:

```json
{
  "version": "13.0.0",
  "type": "BUILD_SPEC",
  "sections": {
    "META": [],
    "BUILD_GRAPH": [],
    "OUTPUT_MAP": [],
    "CONSTRAINTS": [],
    "ACCEPTANCE": []
  },
  "tasks": [],
  "dependencies": [],
  "proof_chain": []
}
```

## Parser Implementation Status

| Language | Status | Version | Maintainer |
|----------|--------|---------|------------|
| Python | 🟢 In Progress | 0.1-alpha | JFP Team |
| Rust | 🟡 Planned | TBD | Pending |
| Java | 🟡 Planned | TBD | Pending |
| C | 🟡 Planned | TBD | Pending |
| BASIC | 🟡 Planned | TBD | Pending |
| TypeScript | 🟡 Requested | TBD | Community |
| Go | 🟡 Requested | TBD | Community |

**Legend:** 🟢 Active | 🟡 Planned | 🔴 Not Started

## Current Phase: Foundation

### Now
- ✅ Canonical JSON AST schema finalized (see `ast/jfp_ast.schema.json`)
- ✅ Example canonical AST outputs (see `ast/canonical_ast_example.json`)
- 🟡 Python reference parser development started
- 🟡 Parser skeleton files created

### What's Next
1. **Python parser** — Complete reference implementation (Week 1-2)
2. **Rust parser** — High-performance implementation (Week 3-4)
3. **Java parser** — Enterprise-grade implementation (Week 4-6)
4. **C parser** — Systems integration (After v13 stabilization)
5. **BASIC parser** — Retro easter egg (Fun project)

## Using Parsers

### Python (Reference Implementation)

```bash
python3 jfp_parser.py input.jfp --output ast.json
```

Outputs canonical JSON AST to `ast.json`.

### Rust (When Available)

```bash
cargo run -- input.jfp --output ast.json
```

### Java (When Available)

```bash
java -jar jfp-parser.jar input.jfp --output ast.json
```

## Validation

All parsers should validate:
1. **Syntax** — Document conforms to JFP grammar
2. **Semantics** — All referenced sections are valid
3. **Constraints** — Safety rules are expressible
4. **AST** — Output matches canonical schema

## Error Handling

All parsers must handle and report:
- Syntax errors with line numbers
- Missing required sections
- Invalid constraint specifications
- Circular dependencies
- Undefined task references

## Testing

All parsers are tested against:
1. **Valid documents** — Ensure correct parsing
2. **Invalid documents** — Ensure error handling
3. **Canonical equivalence** — All parsers produce identical AST
4. **Performance** — Measure parsing speed
5. **Security** — Ensure no injection vulnerabilities

## Contributing a Parser

To implement a JFP parser:

1. **Study the canonical AST schema** (`ast/jfp_ast.schema.json`)
2. **Review examples** (`ast/canonical_ast_example.json`)
3. **Implement parser** in your language
4. **Test against examples** — Must produce identical AST
5. **Document usage** in language-specific README
6. **Submit for verification** — AST validation required

## Parser Roadmap

**Phase 1 (Now):** Foundation & AST schema
- JSON schema finalized
- Python reference parser
- Example AST outputs
- Documentation

**Phase 2 (Week 1-2):** Python Complete
- Python parser functional and tested
- Canonical AST examples validated
- Integration test suite

**Phase 3 (Week 3-4):** Rust & Java
- Rust parser (80%+ complete)
- Java parser skeleton
- Performance benchmarks

**Phase 4 (Month 2-3):** Expansion
- Rust parser production ready
- Java parser functional
- C parser planning begins

**Phase 5 (Month 3+):** Ecosystem
- C parser implementation
- BASIC parser (easter egg)
- Community parsers (TypeScript, Go, etc)
- IDE plugin support

## Questions?

Open an issue or check the main [README.md](../README.md) for more information.
