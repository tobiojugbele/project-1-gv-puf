import os
import sys

def test_setup():
    print("🔄 Running Day 1 System Diagnostics...")
    
    # 1. Verify Python Environment Isolation
    if not hasattr(sys, 'real_prefix') and 'VIRTUAL_ENV' not in os.environ:
        print("❌ ERROR: Virtual environment (venv) is NOT activated!")
        sys.exit(1)
    print("✅ Virtual environment status: Active")

    # 2. Verify Raw Data Folder Architecture
    if not os.path.exists("data/raw"):
        print("❌ ERROR: 'data/raw' directory is missing!")
        sys.exit(1)
    print("✅ Architecture status: 'data/raw/' directory exists")
    
    print("🎉 ALL TESTS PASSED: System is stable for shutdown.")
    sys.exit(0)

if __name__ == "__main__":
    test_setup()
