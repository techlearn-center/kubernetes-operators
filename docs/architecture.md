# Architecture Documentation

## Project Architecture

```
Module Flow:

01 Fundamentals ──▶ 02 Core Setup ──▶ 03 Basic Operations
                                              │
                                              ▼
04 Intermediate ──▶ 05 Advanced ──▶ 06 Integration
                                              │
                                              ▼
07 Security ──▶ 08 Testing ──▶ 09 Production Patterns
                                              │
                                              ▼
                                    10 Advanced Patterns
                                              │
                                              ▼
                                  CAPSTONE PROJECT
                              (All skills combined)
```

## Module Structure

Each module follows a consistent pattern:

```
module/
  README.md           # Concepts + step-by-step lab
  lab/
    starter/          # Starting point for exercises
    solution/         # Reference solution
  validation/
    validate.sh       # Automated completion check
```

## Key Design Decisions

1. **Docker-based labs** - No cloud account needed, runs locally
2. **Progressive difficulty** - Each module builds on previous ones
3. **Automated validation** - Scripts verify correct implementation
4. **Real-world patterns** - Production-grade, not toy examples
5. **Self-paced** - Clear completion criteria for each module
