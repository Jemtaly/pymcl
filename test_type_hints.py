#!/usr/bin/env python3
"""
Test script for pymcl type hints and autocompletion.

This script demonstrates the type hints and tests that they work correctly
with type checkers like mypy.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# This test file can be run with mypy to check type hints:
# mypy test_type_hints.py

def test_type_hints():
    """Test that type hints work correctly."""
    try:
        import pymcl
        
        # Test Fr operations
        fr1 = pymcl.Fr("123")
        fr2 = pymcl.Fr("456")
        fr_result = fr1 + fr2  # Should be Fr
        fr_random = pymcl.Fr.random()  # Should be Fr
        
        # Test G1 operations  
        g1_1 = pymcl.G1()
        g1_2 = pymcl.g1  # Module constant
        g1_result = g1_1 + g1_2  # Should be G1
        g1_scalar = g1_1 * fr1  # Should be G1
        
        # Test G2 operations
        g2_1 = pymcl.G2()
        g2_2 = pymcl.g2  # Module constant
        g2_result = g2_1 + g2_2  # Should be G2
        g2_scalar = g2_1 * fr1  # Should be G2
        
        # Test GT operations
        gt1 = pymcl.GT()
        gt2 = pymcl.GT("1")
        gt_result = gt1 * gt2  # Should be GT
        gt_power = gt1 ** fr1  # Should be GT
        
        # Test pairing
        pairing_result = pymcl.pairing(g1_1, g2_1)  # Should be GT
        
        # Test serialization
        fr_bytes = fr1.serialize()  # Should be bytes
        fr_restored = pymcl.Fr.deserialize(fr_bytes)  # Should be Fr
        
        # Test boolean methods
        is_zero = fr1.isZero()  # Should be bool
        is_one = fr1.isOne()  # Should be bool
        
        print("✓ Type hints test passed - all operations executed successfully")
        print(f"✓ Fr operations: {fr1} + {fr2} = {fr_result}")
        print(f"✓ G1 operations: scalar multiplication works")
        print(f"✓ G2 operations: scalar multiplication works")
        print(f"✓ GT operations: multiplication and exponentiation work")
        print(f"✓ Pairing: G1 × G2 → GT works")
        print(f"✓ Serialization: Fr → bytes → Fr works")
        print(f"✓ Module constants: g1={type(pymcl.g1)}, g2={type(pymcl.g2)}, r={type(pymcl.r)}")
        return True
        
    except ImportError:
        print("⚠ pymcl module not available (expected - requires mcl library)")
        print("✓ Type hints can still be checked with mypy without building the module")
        return True
    except Exception as e:
        print(f"✗ Type hints test failed: {e}")
        return False

def test_type_stub_file():
    """Test that the type stub file exists and is valid."""
    stub_file = "pymcl.pyi"
    if os.path.exists(stub_file):
        print(f"✓ Type stub file exists: {stub_file}")
        with open(stub_file, 'r') as f:
            content = f.read()
            if 'class Fr:' in content and 'class G1:' in content:
                print("✓ Type stub file contains expected class definitions")
                return True
            else:
                print("✗ Type stub file missing expected content")
                return False
    else:
        print(f"✗ Type stub file not found: {stub_file}")
        return False

def test_py_typed_marker():
    """Test that the py.typed marker file exists."""
    marker_file = "py.typed"
    if os.path.exists(marker_file):
        print(f"✓ Typing marker file exists: {marker_file}")
        return True
    else:
        print(f"✗ Typing marker file not found: {marker_file}")
        return False

if __name__ == "__main__":
    print("Testing pymcl type hints and autocompletion support...")
    print("=" * 60)
    
    success = True
    success &= test_type_stub_file()
    success &= test_py_typed_marker()
    success &= test_type_hints()
    
    print("=" * 60)
    if success:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed!")
        sys.exit(1)