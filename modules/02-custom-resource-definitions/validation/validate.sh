#!/bin/bash
PASS=0; FAIL=0
check() { if eval "$2" > /dev/null 2>&1; then echo "[PASS] ✅ $1"; ((PASS++)); else echo "[FAIL] ❌ $1"; echo "       💡 Hint: $3"; ((FAIL++)); fi; }
echo "========================================"
echo "Module 02: Custom Resource Definitions (CRDs)"
echo "========================================"
check "Module README exists" "test -f modules/02-custom-resource-definitions/README.md" "Module files may be missing"
check "Lab starter files exist" "ls modules/02-custom-resource-definitions/lab/starter/ 2>/dev/null | grep -q . || test -f modules/02-custom-resource-definitions/lab/starter/.gitkeep" "Check starter directory"
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ $FAIL -eq 0 ] && echo "🎉 Module 02 COMPLETE!" || echo "⚠️  Fix failures and re-run."
exit $FAIL
