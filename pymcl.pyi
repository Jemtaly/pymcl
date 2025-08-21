"""
Type stubs for pymcl - Python bindings for the mcl library.

This file provides type hints for IDE autocompletion and type checking.
"""

from typing import Union, overload


class Fr:
    """
    Element in the finite field Fr.
    
    The Fr class represents elements in the finite field used in BLS12-381 curve.
    Supports arithmetic operations: addition, subtraction, multiplication, division,
    negation, and inversion.
    """
    
    def __init__(self, s: str = ...) -> None:
        """
        Create an element in Fr from a string.
        
        Args:
            s: String representation of the element (decimal). If not provided,
               creates the zero element.
        """
        ...
    
    def __str__(self) -> str:
        """Convert the element to its string representation."""
        ...
    
    def __repr__(self) -> str:
        """Return the string representation of the element."""
        ...
    
    def __add__(self, other: "Fr") -> "Fr":
        """Add two Fr elements."""
        ...
    
    def __sub__(self, other: "Fr") -> "Fr":
        """Subtract two Fr elements."""
        ...
    
    def __mul__(self, other: "Fr") -> "Fr":
        """Multiply two Fr elements."""
        ...
    
    def __truediv__(self, other: "Fr") -> "Fr":
        """Divide two Fr elements."""
        ...
    
    def __neg__(self) -> "Fr":
        """Negate the Fr element."""
        ...
    
    def __invert__(self) -> "Fr":
        """Compute the multiplicative inverse of the Fr element."""
        ...
    
    def __eq__(self, other: object) -> bool:
        """Check equality between Fr elements."""
        ...
    
    def __ne__(self, other: object) -> bool:
        """Check inequality between Fr elements."""
        ...
    
    def __hash__(self) -> int:
        """Return the hash value of the element."""
        ...
    
    def serialize(self) -> bytes:
        """Serialize the element to a byte string."""
        ...
    
    @classmethod
    def deserialize(cls, b: bytes) -> "Fr":
        """Deserialize the element from a byte string."""
        ...
    
    @classmethod
    def random(cls) -> "Fr":
        """Generate a random Fr element."""
        ...
    
    def isZero(self) -> bool:
        """Check if the element is the zero element (additive identity)."""
        ...
    
    def isOne(self) -> bool:
        """Check if the element is the one element (multiplicative identity)."""
        ...


class G1:
    """
    Element in the elliptic curve group G1.
    
    The G1 class represents points on the BLS12-381 G1 curve.
    Supports group operations: addition, subtraction, scalar multiplication, and negation.
    """
    
    def __init__(self, s: str = ...) -> None:
        """
        Create an element in G1 from its string representation.
        
        Args:
            s: String representation of the G1 element. If not provided,
               creates the zero element (point at infinity).
        """
        ...
    
    def __str__(self) -> str:
        """Convert the element to its string representation."""
        ...
    
    def __repr__(self) -> str:
        """Return the string representation of the element."""
        ...
    
    def __add__(self, other: "G1") -> "G1":
        """Add two G1 points (group operation)."""
        ...
    
    def __sub__(self, other: "G1") -> "G1":
        """Subtract two G1 points."""
        ...
    
    def __mul__(self, other: Fr) -> "G1":
        """Scalar multiplication of G1 point by Fr element."""
        ...
    
    def __neg__(self) -> "G1":
        """Negate the G1 point."""
        ...
    
    def __eq__(self, other: object) -> bool:
        """Check equality between G1 points."""
        ...
    
    def __ne__(self, other: object) -> bool:
        """Check inequality between G1 points."""
        ...
    
    def __hash__(self) -> int:
        """Return the hash value of the element."""
        ...
    
    def serialize(self) -> bytes:
        """Serialize the element to a byte string (compressed form)."""
        ...
    
    @classmethod
    def deserialize(cls, b: bytes) -> "G1":
        """Deserialize the element from a byte string."""
        ...
    
    @classmethod
    def hash(cls, b: bytes) -> "G1":
        """Hash a byte array to a G1 element."""
        ...
    
    def isZero(self) -> bool:
        """Check if the element is the zero element (point at infinity)."""
        ...


class G2:
    """
    Element in the elliptic curve group G2.
    
    The G2 class represents points on the BLS12-381 G2 curve.
    Supports group operations: addition, subtraction, scalar multiplication, and negation.
    """
    
    def __init__(self, s: str = ...) -> None:
        """
        Create an element in G2 from its string representation.
        
        Args:
            s: String representation of the G2 element. If not provided,
               creates the zero element (point at infinity).
        """
        ...
    
    def __str__(self) -> str:
        """Convert the element to its string representation."""
        ...
    
    def __repr__(self) -> str:
        """Return the string representation of the element."""
        ...
    
    def __add__(self, other: "G2") -> "G2":
        """Add two G2 points (group operation)."""
        ...
    
    def __sub__(self, other: "G2") -> "G2":
        """Subtract two G2 points."""
        ...
    
    def __mul__(self, other: Fr) -> "G2":
        """Scalar multiplication of G2 point by Fr element."""
        ...
    
    def __neg__(self) -> "G2":
        """Negate the G2 point."""
        ...
    
    def __eq__(self, other: object) -> bool:
        """Check equality between G2 points."""
        ...
    
    def __ne__(self, other: object) -> bool:
        """Check inequality between G2 points."""
        ...
    
    def __hash__(self) -> int:
        """Return the hash value of the element."""
        ...
    
    def serialize(self) -> bytes:
        """Serialize the element to a byte string (compressed form)."""
        ...
    
    @classmethod
    def deserialize(cls, b: bytes) -> "G2":
        """Deserialize the element from a byte string."""
        ...
    
    @classmethod
    def hash(cls, b: bytes) -> "G2":
        """Hash a byte array to a G2 element."""
        ...
    
    def isZero(self) -> bool:
        """Check if the element is the zero element (point at infinity)."""
        ...


class GT:
    """
    Element in the target group GT.
    
    The GT class represents elements in the multiplicative group GT,
    which is the target of the pairing function.
    Supports multiplicative operations: multiplication, division, exponentiation, and inversion.
    """
    
    def __init__(self, s: str = ...) -> None:
        """
        Create an element in GT from its string representation.
        
        Args:
            s: String representation of the GT element. If not provided,
               creates the identity element.
        """
        ...
    
    def __str__(self) -> str:
        """Convert the element to its string representation."""
        ...
    
    def __repr__(self) -> str:
        """Return the string representation of the element."""
        ...
    
    def __mul__(self, other: "GT") -> "GT":
        """Multiply two GT elements."""
        ...
    
    def __truediv__(self, other: "GT") -> "GT":
        """Divide two GT elements."""
        ...
    
    def __pow__(self, other: Fr) -> "GT":
        """Exponentiate GT element by Fr element."""
        ...
    
    def __invert__(self) -> "GT":
        """Compute the multiplicative inverse of the GT element."""
        ...
    
    def __eq__(self, other: object) -> bool:
        """Check equality between GT elements."""
        ...
    
    def __ne__(self, other: object) -> bool:
        """Check inequality between GT elements."""
        ...
    
    def __hash__(self) -> int:
        """Return the hash value of the element."""
        ...
    
    def serialize(self) -> bytes:
        """Serialize the element to a byte string."""
        ...
    
    @classmethod
    def deserialize(cls, b: bytes) -> "GT":
        """Deserialize the element from a byte string."""
        ...
    
    def isZero(self) -> bool:
        """Check if the element is the zero element."""
        ...
    
    def isOne(self) -> bool:
        """Check if the element is the one element (multiplicative identity)."""
        ...


def pairing(a: G1, b: G2) -> GT:
    """
    Compute the pairing between a G1 and a G2 element.
    
    Args:
        a: Element from G1 (first argument)
        b: Element from G2 (second argument)
    
    Returns:
        Element in GT representing the pairing result
    """
    ...


# Module constants
g1: G1  # Generator of G1
g2: G2  # Generator of G2
r: int  # Order of the G1, G2, Fr, and GT groups