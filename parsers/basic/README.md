# JFP BASIC Parser

## Status

🟡 **Planned** — Retro easter egg for BASIC enthusiasts

## Overview

A fun, retro implementation of the JFP parser in BASIC (Commodore 64, AmigaBASIC, QB64, etc.).

## Why BASIC?

Because:
- 🎮 Nostalgia
- 🎨 Educational value
- 🚀 Fun marketing opportunity
- 📚 Demonstrates JFP flexibility

## Supported Variants

- QB64 (Modern BASIC)
- Commodore 64 BASIC (Via emulation)
- AmigaBASIC
- GW-BASIC

## Example Usage

```basic
REM JFP Parser in BASIC

FILE$ = "input.jfp"
OPEN FILE$ FOR INPUT AS #1

DO UNTIL EOF(1)
    LINE INPUT #1, LINE$
    REM Parse JFP line
LOOP

CLOSE #1
```

## Goals

1. **Fun** — Enjoy building this
2. **Educational** — Show JFP flexibility
3. **Canonical AST** — Output identical to other parsers (via JSON export if possible)
4. **Retro Vibes** — Celebrate computing history

## Timeline

Implementation scheduled after all serious parsers are complete. This is a pure fun project!

## Challenge

How do we output JSON from BASIC? 😄
Options:
- Export to JSON file via system call
- Pipe to external JSON generator
- Pure BASIC string manipulation (complex!)

## See Also

- [Canonical AST Schema](../ast/jfp_ast.schema.json)
- [Parser README](../README.md)
