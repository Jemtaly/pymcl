#!/usr/bin/env python3
"""
Comprehensive test suite for pymcl library.
Tests all the major functionality including Fr, G1, G2, GT classes and pairing operations.
"""

import pytest
import pymcl


class TestFr:
    """Test the Fr (field element) class."""
    
    def test_fr_creation(self):
        """Test creation of Fr elements."""
        # Create from integer
        fr1 = pymcl.Fr(42)
        assert str(fr1) == "42"
        
        # Create from string
        fr2 = pymcl.Fr("123")
        assert str(fr2) == "123"
        
        # Create random element
        fr_rand = pymcl.Fr.random()
        assert isinstance(fr_rand, pymcl.Fr)
    
    def test_fr_arithmetic(self):
        """Test Fr arithmetic operations."""
        fr1 = pymcl.Fr(10)
        fr2 = pymcl.Fr(5)
        
        # Addition
        result = fr1 + fr2
        assert isinstance(result, pymcl.Fr)
        
        # Subtraction  
        result = fr1 - fr2
        assert isinstance(result, pymcl.Fr)
        
        # Multiplication
        result = fr1 * fr2
        assert isinstance(result, pymcl.Fr)
        
        # Division
        result = fr1 / fr2
        assert isinstance(result, pymcl.Fr)
        
        # Negation
        result = -fr1
        assert isinstance(result, pymcl.Fr)
        
        # Inversion
        result = ~fr2  # fr2 != 0
        assert isinstance(result, pymcl.Fr)
    
    def test_fr_comparison(self):
        """Test Fr comparison operations."""
        fr1 = pymcl.Fr(42)
        fr2 = pymcl.Fr(42)
        fr3 = pymcl.Fr(24)
        
        assert fr1 == fr2
        assert fr1 != fr3
        assert not (fr1 == fr3)
        assert not (fr1 != fr2)
    
    def test_fr_identity_elements(self):
        """Test Fr identity elements."""
        fr_zero = pymcl.Fr(0)
        fr_one = pymcl.Fr(1)
        fr_other = pymcl.Fr(42)
        
        assert fr_zero.isZero()
        assert not fr_one.isZero()
        assert not fr_other.isZero()
        
        assert fr_one.isOne()
        assert not fr_zero.isOne()
        assert not fr_other.isOne()
    
    def test_fr_serialization(self):
        """Test Fr serialization and deserialization."""
        fr_orig = pymcl.Fr(12345)
        
        # Serialize
        serialized = fr_orig.serialize()
        assert isinstance(serialized, bytes)
        
        # Deserialize
        fr_restored = pymcl.Fr.deserialize(serialized)
        assert fr_orig == fr_restored
    
    def test_fr_hash(self):
        """Test Fr hash functionality."""
        fr1 = pymcl.Fr(42)
        fr2 = pymcl.Fr(42)
        fr3 = pymcl.Fr(24)
        
        # Equal elements should have same hash
        assert hash(fr1) == hash(fr2)
        # Different elements might have different hashes (not guaranteed but likely)
        # We just check that hash function works
        hash_val = hash(fr3)
        assert isinstance(hash_val, int)


class TestG1:
    """Test the G1 (elliptic curve group) class."""
    
    def test_g1_creation(self):
        """Test creation of G1 elements."""
        # Get generator
        g1_gen = pymcl.g1
        assert isinstance(g1_gen, pymcl.G1)
        
        # Create from string representation
        g1_str = str(g1_gen)
        g1_from_str = pymcl.G1(g1_str)
        assert g1_gen == g1_from_str
    
    def test_g1_arithmetic(self):
        """Test G1 arithmetic operations."""
        g1 = pymcl.g1
        fr1 = pymcl.Fr(10)
        fr2 = pymcl.Fr(5)
        
        # Scalar multiplication
        result = g1 * fr1
        assert isinstance(result, pymcl.G1)
        
        # Addition
        g1_2 = g1 * fr2
        result = g1 + g1_2
        assert isinstance(result, pymcl.G1)
        
        # Subtraction
        result = g1 - g1_2
        assert isinstance(result, pymcl.G1)
        
        # Negation
        result = -g1
        assert isinstance(result, pymcl.G1)
    
    def test_g1_comparison(self):
        """Test G1 comparison operations."""
        g1 = pymcl.g1
        g1_copy = pymcl.G1(str(g1))
        g1_diff = g1 * pymcl.Fr(2)
        
        assert g1 == g1_copy
        assert g1 != g1_diff
    
    def test_g1_identity_elements(self):
        """Test G1 identity elements."""
        g1_zero = pymcl.g1 * pymcl.Fr(0)  # Should be zero element
        g1_nonzero = pymcl.g1
        
        assert g1_zero.isZero()
        assert not g1_nonzero.isZero()
    
    def test_g1_serialization(self):
        """Test G1 serialization and deserialization."""
        g1_orig = pymcl.g1 * pymcl.Fr(42)
        
        # Serialize
        serialized = g1_orig.serialize()
        assert isinstance(serialized, bytes)
        
        # Deserialize
        g1_restored = pymcl.G1.deserialize(serialized)
        assert g1_orig == g1_restored


class TestG2:
    """Test the G2 (elliptic curve group) class."""
    
    def test_g2_creation(self):
        """Test creation of G2 elements."""
        # Get generator
        g2_gen = pymcl.g2
        assert isinstance(g2_gen, pymcl.G2)
        
        # Create from string representation
        g2_str = str(g2_gen)
        g2_from_str = pymcl.G2(g2_str)
        assert g2_gen == g2_from_str
    
    def test_g2_arithmetic(self):
        """Test G2 arithmetic operations."""
        g2 = pymcl.g2
        fr1 = pymcl.Fr(10)
        fr2 = pymcl.Fr(5)
        
        # Scalar multiplication
        result = g2 * fr1
        assert isinstance(result, pymcl.G2)
        
        # Addition
        g2_2 = g2 * fr2
        result = g2 + g2_2
        assert isinstance(result, pymcl.G2)
        
        # Subtraction
        result = g2 - g2_2
        assert isinstance(result, pymcl.G2)
        
        # Negation
        result = -g2
        assert isinstance(result, pymcl.G2)
    
    def test_g2_comparison(self):
        """Test G2 comparison operations."""
        g2 = pymcl.g2
        g2_copy = pymcl.G2(str(g2))
        g2_diff = g2 * pymcl.Fr(2)
        
        assert g2 == g2_copy
        assert g2 != g2_diff
    
    def test_g2_identity_elements(self):
        """Test G2 identity elements."""
        g2_zero = pymcl.g2 * pymcl.Fr(0)  # Should be zero element
        g2_nonzero = pymcl.g2
        
        assert g2_zero.isZero()
        assert not g2_nonzero.isZero()
    
    def test_g2_serialization(self):
        """Test G2 serialization and deserialization."""
        g2_orig = pymcl.g2 * pymcl.Fr(42)
        
        # Serialize
        serialized = g2_orig.serialize()
        assert isinstance(serialized, bytes)
        
        # Deserialize
        g2_restored = pymcl.G2.deserialize(serialized)
        assert g2_orig == g2_restored


class TestGT:
    """Test the GT (target group) class."""
    
    def test_gt_creation(self):
        """Test creation of GT elements."""
        # Create from pairing
        g1 = pymcl.g1
        g2 = pymcl.g2
        gt = pymcl.pairing(g1, g2)
        assert isinstance(gt, pymcl.GT)
        
        # Create from string representation
        gt_str = str(gt)
        gt_from_str = pymcl.GT(gt_str)
        assert gt == gt_from_str
    
    def test_gt_arithmetic(self):
        """Test GT arithmetic operations."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        gt1 = pymcl.pairing(g1, g2)
        gt2 = pymcl.pairing(g1 * pymcl.Fr(2), g2)
        fr = pymcl.Fr(3)
        
        # Multiplication
        result = gt1 * gt2
        assert isinstance(result, pymcl.GT)
        
        # Division
        result = gt1 / gt2
        assert isinstance(result, pymcl.GT)
        
        # Inversion
        result = ~gt1
        assert isinstance(result, pymcl.GT)
        
        # Exponentiation
        result = gt1 ** fr
        assert isinstance(result, pymcl.GT)
    
    def test_gt_comparison(self):
        """Test GT comparison operations."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        gt1 = pymcl.pairing(g1, g2)
        gt2 = pymcl.pairing(g1, g2)
        gt3 = pymcl.pairing(g1 * pymcl.Fr(2), g2)
        
        assert gt1 == gt2
        assert gt1 != gt3
    
    def test_gt_identity_elements(self):
        """Test GT identity elements."""
        g1_zero = pymcl.g1 * pymcl.Fr(0)
        g2 = pymcl.g2
        gt_one = pymcl.pairing(g1_zero, g2)  # Should give identity in GT
        
        gt_nonone = pymcl.pairing(pymcl.g1, g2)
        
        assert gt_one.isOne()
        assert not gt_nonone.isOne()
    
    def test_gt_serialization(self):
        """Test GT serialization and deserialization."""
        g1 = pymcl.g1 * pymcl.Fr(42)
        g2 = pymcl.g2 * pymcl.Fr(24)
        gt_orig = pymcl.pairing(g1, g2)
        
        # Serialize
        serialized = gt_orig.serialize()
        assert isinstance(serialized, bytes)
        
        # Deserialize
        gt_restored = pymcl.GT.deserialize(serialized)
        assert gt_orig == gt_restored


class TestPairing:
    """Test pairing operations."""
    
    def test_basic_pairing(self):
        """Test basic pairing functionality."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        
        # Basic pairing
        gt = pymcl.pairing(g1, g2)
        assert isinstance(gt, pymcl.GT)
    
    def test_pairing_bilinearity(self):
        """Test pairing bilinearity property."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        x1 = pymcl.Fr.random()
        x2 = pymcl.Fr.random()
        
        # e(g1^x1, g2^x2) = e(g1, g2)^(x1*x2)
        left = pymcl.pairing(g1 * x1, g2 * x2)
        right = pymcl.pairing(g1, g2) ** (x1 * x2)
        
        assert left == right
    
    def test_pairing_linearity_first_arg(self):
        """Test pairing linearity in first argument."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        x = pymcl.Fr.random()
        y = pymcl.Fr.random()
        
        # e(g1^x + g1^y, g2) = e(g1^x, g2) * e(g1^y, g2)
        left = pymcl.pairing(g1 * x + g1 * y, g2)
        right = pymcl.pairing(g1 * x, g2) * pymcl.pairing(g1 * y, g2)
        
        assert left == right
    
    def test_pairing_linearity_second_arg(self):
        """Test pairing linearity in second argument."""
        g1 = pymcl.g1
        g2 = pymcl.g2
        x = pymcl.Fr.random()
        y = pymcl.Fr.random()
        
        # e(g1, g2^x + g2^y) = e(g1, g2^x) * e(g1, g2^y)
        left = pymcl.pairing(g1, g2 * x + g2 * y)
        right = pymcl.pairing(g1, g2 * x) * pymcl.pairing(g1, g2 * y)
        
        assert left == right


class TestConstants:
    """Test module constants."""
    
    def test_generators(self):
        """Test that generators are available and correct type."""
        assert hasattr(pymcl, 'g1')
        assert hasattr(pymcl, 'g2')
        assert isinstance(pymcl.g1, pymcl.G1)
        assert isinstance(pymcl.g2, pymcl.G2)
    
    def test_group_order(self):
        """Test that group order constant is available."""
        assert hasattr(pymcl, 'r')
        assert isinstance(pymcl.r, int)
        assert pymcl.r > 0


if __name__ == "__main__":
    pytest.main([__file__])