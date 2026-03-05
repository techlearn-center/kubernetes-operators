#!/bin/bash
PASS=0; FAIL=0
check() { if eval "$2" > /dev/null 2>&1; then echo "[PASS] ✅ $1"; ((PASS++)); else echo "[FAIL] ❌ $1"; echo "       💡 Hint: $3"; ((FAIL++)); fi; }
echo "========================================"
echo "🏆 CAPSTONE VALIDATION"
echo "========================================"
check "Capstone README exists" "test -f capstone/README.md" "Check capstone directory"
check "Solution directory has files" "ls capstone/solution/ 2>/dev/null | grep -qv .gitkeep" "Complete the capstone project"
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "🎉 CAPSTONE COMPLETE!" || echo "⚠️  Fix failures and re-run."
exit $FAIL
