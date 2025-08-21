#!/usr/bin/env python3
"""Simple type check test for pymcl type stubs."""

# This will test type checking without any runtime issues
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pymcl

def test_types() -> None:
    """Test type annotations work correctly."""
    if TYPE_CHECKING:
        # These should all pass type checking
        fr: pymcl.Fr = pymcl.Fr("123")
        g1: pymcl.G1 = pymcl.G1()
        g2: pymcl.G2 = pymcl.G2()
        gt: pymcl.GT = pymcl.GT()
        
        # Operations that should work
        fr_sum: pymcl.Fr = fr + fr
        g1_sum: pymcl.G1 = g1 + g1
        g1_scalar: pymcl.G1 = g1 * fr
        gt_pairing: pymcl.GT = pymcl.pairing(g1, g2)
        
        # These would be type errors if uncommented:
        # wrong1: pymcl.G1 = fr + fr  # Type error: Fr + Fr -> Fr, not G1
        # wrong2: pymcl.GT = pymcl.pairing(g2, g1)  # Type error: wrong argument order

if __name__ == "__main__":
    test_types()
    print("Type checking test completed successfully!")