# JFP Python Parser

## Status

🟢 **In Progress** — Reference implementation under development

## Overview

The Python parser is the reference implementation for JFP document parsing. It must produce the canonical JSON AST defined in `../ast/jfp_ast.schema.json`.

## Goal

Convert JFP text documents into canonical JSON AST format:

```
input.jfp → Parser → canonical_ast.json
```

All JFP parsers (Rust, Java, C, etc.) must produce identical output for identical input.

## Usage

### Basic Usage

```bash
python3 jfp_parser.py input.jfp --output ast.json
```

### With Validation

```bash
python3 jfp_parser.py input.jfp --output ast.json --validate
```

### Verbose Output

```bash
python3 jfp_parser.py input.jfp --output ast.json --verbose
```

## Installation

```bash
cd python/
pip install -r requirements.txt
```

## Implementation Plan

### Phase 1: Lexer
- Tokenize JFP input
- Handle section headers
- Parse key-value pairs
- Error reporting with line numbers

### Phase 2: Parser
- Build AST from tokens
- Validate section structure
- Extract dependencies
- Resolve references

### Phase 3: Validator
- Check canonical AST schema
- Validate constraints
- Verify dependencies
- Detect circular references

### Phase 4: Output
- Generate JSON AST
- Pretty-print for readability
- Optionally compress

## Testing

Run tests against examples:

```bash
python3 -m pytest tests/
```

## Current Status

- [ ] Basic lexer implementation
- [ ] Section parser
- [ ] AST builder
- [ ] JSON serialization
- [ ] Validation
- [ ] Error handling
- [ ] Unit tests
- [ ] Integration tests

## Contributing

Contributions welcome! Please ensure:
1. All tests pass
2. Output matches canonical schema
3. Error messages are clear
4. Code is documented

## Next Phase

Once Python parser is stable, Rust implementation begins.
