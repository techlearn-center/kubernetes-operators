#!/bin/bash
echo "========================================"; echo "  FULL VALIDATION"; echo "========================================"
TOTAL=0
for v in modules/*/validation/validate.sh; do [ -f "$v" ] && bash "$v"; TOTAL=$((TOTAL + $?)); done
[ -f capstone/validation/validate.sh ] && bash capstone/validation/validate.sh; TOTAL=$((TOTAL + $?))
echo ""; [ $TOTAL -eq 0 ] && echo "🎉 ALL MODULES PASSED!" || echo "⚠️  $TOTAL total failures."
