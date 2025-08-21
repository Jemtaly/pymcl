#!/usr/bin/env python3
"""
Simple test runner script for pymcl.
This script can be used to run tests locally before pushing to CI.
"""

import sys
import subprocess
import os

def main():
    """Run tests with pytest."""
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Install test dependencies
    print("Installing test dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements-dev.txt"], 
                      check=True)
    except subprocess.CalledProcessError:
        print("Failed to install test dependencies")
        return 1
    
    # Run tests
    print("\nRunning tests...")
    try:
        result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], 
                               check=False)
        return result.returncode
    except Exception as e:
        print(f"Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())