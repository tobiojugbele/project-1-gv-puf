import os
import sys

def test_setup():
    print("🔄 Running Day 2 System Diagnostics...")
    if "VIRTUAL_ENV" not in os.environ:
        print("❌ ERROR: Virtual environment (venv) is NOT activated!")
        sys.exit(1)
    if not os.path.exists("data/raw"):
        print("❌ ERROR: data/raw directory is missing!")
        sys.exit(1)
    print("✅ System paths and virtual environments are functional.")
    sys.exit(0)

if __name__ == "__main__":
    test_setup()
