#!/usr/bin/env python3
"""
Basic smoke test to verify that pymcl can be imported.
This test will only pass if the library is properly built and installed.
"""

import sys
import os

def test_import():
    """Test that pymcl can be imported without errors."""
    try:
        import pymcl
        print("✓ pymcl import successful")
    except ImportError as e:
        print(f"✗ pymcl import failed: {e}")
        assert False, f"Failed to import pymcl: {e}"

def test_basic_functionality():
    """Test basic functionality if import succeeded."""
    import pymcl
    
    # Test that main classes exist
    assert hasattr(pymcl, 'Fr'), "Fr class not found"
    assert hasattr(pymcl, 'G1'), "G1 class not found" 
    assert hasattr(pymcl, 'G2'), "G2 class not found"
    assert hasattr(pymcl, 'GT'), "GT class not found"
    print("✓ All required classes are available")
    
    # Test that constants exist
    assert hasattr(pymcl, 'g1'), "g1 generator not found"
    assert hasattr(pymcl, 'g2'), "g2 generator not found"
    assert hasattr(pymcl, 'r'), "r constant not found"
    print("✓ All required constants are available")
    
    # Test that pairing function exists
    assert hasattr(pymcl, 'pairing'), "pairing function not found"
    print("✓ Pairing function is available")

def main():
    """Run basic smoke tests."""
    print("Running pymcl smoke tests...")
    
    # Test import
    try:
        import pymcl
        print("✓ pymcl import successful")
    except ImportError as e:
        print(f"✗ pymcl import failed: {e}")
        print("\nSMOKE TEST FAILED: Cannot import pymcl")
        print("This is expected if the mcl library hasn't been built yet.")
        print("To build and test:")
        print("1. Run: ./install.sh (on Linux/macOS) or install.bat (on Windows)")
        print("2. Then run: python run_tests.py")
        return 1
    
    # Test basic functionality
    try:
        # Test that main classes exist
        assert hasattr(pymcl, 'Fr'), "Fr class not found"
        assert hasattr(pymcl, 'G1'), "G1 class not found" 
        assert hasattr(pymcl, 'G2'), "G2 class not found"
        assert hasattr(pymcl, 'GT'), "GT class not found"
        print("✓ All required classes are available")
        
        # Test that constants exist
        assert hasattr(pymcl, 'g1'), "g1 generator not found"
        assert hasattr(pymcl, 'g2'), "g2 generator not found"
        assert hasattr(pymcl, 'r'), "r constant not found"
        print("✓ All required constants are available")
        
        # Test that pairing function exists
        assert hasattr(pymcl, 'pairing'), "pairing function not found"
        print("✓ Pairing function is available")
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return 1
    
    print("\n✓ All smoke tests passed!")
    print("Run 'pytest tests/' for the full test suite.")
    return 0

if __name__ == "__main__":
    sys.exit(main())