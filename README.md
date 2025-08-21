# pymcl

A Python 3 wrapper for the [mcl](https://github.com/herumi/mcl) library. Currently support operations on BLS12-381 curve.

## Installation

First, clone this repository using following command:

```sh
git clone https://github.com/Jemtaly/pymcl
cd pymcl
```

Then install the library:

**For Debian-based systems (Debian, Ubuntu, Kali, etc.), you can simply install the library using the provided `install.sh` script.**

For other platforms, to use pymcl, you need to build the mcl library from source first, follow the instructions [here](https://github.com/herumi/mcl/blob/master/readme.md).

After building the mcl library, make sure you place the whole `mcl` library directory (which contains `lib` and `include` folders) in current directory, then, you can install the package using the following command:

```bash
pip install .
```

## Testing

The library includes a comprehensive test suite to ensure all functionality works correctly.

### Running Tests Locally

1. **Install test dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run the full test suite:**
   ```bash
   pytest tests/
   ```

3. **Run tests with coverage:**
   ```bash
   pytest tests/ --cov=pymcl --cov-report=html
   ```

4. **Use the convenient test runner script:**
   ```bash
   python run_tests.py
   ```

### Testing with Multiple Python Versions

If you have `tox` installed, you can test across multiple Python versions:

```bash
pip install tox
tox
```

### Continuous Integration

The repository includes GitHub Actions workflows that automatically test the library on:
- Multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
- Multiple operating systems (Ubuntu, macOS, Windows)

Tests are run on every push and pull request to ensure code quality and compatibility.

## Basic Usage

Here is an example of how to use pymcl:

```python
import pymcl

g1 = pymcl.g1 # generator of G1
g2 = pymcl.g2 # generator of G2
x1 = pymcl.Fr.random() # random element in Fr
x2 = pymcl.Fr.random() # random element in Fr

# check the correctness of the pairing
assert pymcl.pairing(g1 * x1, g2 * x2) == pymcl.pairing(g1, g2) ** (x1 * x2)
```

## Other Operations

There are 4 types of elements in pymcl: `Fr`, `G1`, `G2`, and `GT`. You can perform operations on these elements as follows:

### `Fr` Class

```python
Fr(s: str) -> Fr
```
Create an element in Fr from a string, which is the decimal representation of the element. The library does not supply a constructor for `Fr` from an integer, you can convert an integer to a string and then use this constructor, the integer should be in the range of $[0, r)$, where $r$ is the order of the Fr group.

```python
Fr.__str__(self: Fr) -> str
```
Convert the element to a string.

```python
Fr.random() -> Fr
```
Return a random element in Fr.

```python
Fr.__add__(self: Fr, other: Fr) -> Fr
Fr.__sub__(self: Fr, other: Fr) -> Fr
Fr.__neg__(self: Fr) -> Fr
Fr.__mul__(self: Fr, other: Fr) -> Fr
Fr.__truediv__(self: Fr, other: Fr) -> Fr
Fr.__invert__(self: Fr) -> Fr
```
Perform addition, subtraction, negation, multiplication, division, and inversion on the element.

```python
Fr.__eq__(self: Fr, other: Fr) -> bool
Fr.__ne__(self: Fr, other: Fr) -> bool
Fr.isZero(self: Fr) -> bool
Fr.isOne(self: Fr) -> bool
```
Check the equality and inequality of the element, and check if the element is the additive identity or the multiplicative identity.

```python
Fr.__hash__(self: Fr) -> int
```
Return the hash value of the element.

```python
Fr.serialize(self: Fr) -> bytes
Fr.deserialize(b: bytes) -> Fr
```
Serialize and deserialize the element.

### `G1` Class

```python
G1(s: str) -> G1
```
Create an element in G1 from its string representation.

```python
G1.__str__(self: G1) -> str
```
Convert the element to a string. (check [the API of mcl](https://github.com/herumi/mcl/blob/master/api.md#string-conversion) for the format of the string representation)

```python
G1.hash(b: bytes) -> G1
```
Hash a byte array to an element in G1. (check [here](https://github.com/herumi/mcl/blob/master/api.md#hash-to-curve-function))

```python
G1.__add__(self: G1, other: G1) -> G1
G1.__sub__(self: G1, other: G1) -> G1
G1.__neg__(self: G1) -> G1
G1.__mul__(self: G1, other: Fr) -> G1
```
Perform addition, subtraction, negation, and multiplication on the element. Note that for the multiplication of G1 and Fr, the Fr element should be on the right-hand side.

```python
G1.__eq__(self: G1, other: G1) -> bool
G1.__ne__(self: G1, other: G1) -> bool
G1.isZero(self: G1) -> bool
```
Check the equality and inequality of the element, and check if the element is the additive identity.

```python
G1.__hash__(self: G1) -> int
```
Return the hash value of the element.

```python
G1.serialize(self: G1) -> bytes
G1.deserialize(b: bytes) -> G1
```
Serialize and deserialize the element (in compressed form).

### `G2` Class

The `G2` class has the same methods as the [`G1`](#g1-class) class.

### `GT` Class

```python
GT(s: str) -> GT
```
Create an element in GT from its string representation.

```python
GT.__str__(self: GT) -> str
```
Convert the element to a string.

```python
GT.__mul__(self: GT, other: GT) -> GT
GT.__truediv__(self: GT, other: GT) -> GT
GT.__invert__(self: GT) -> GT
GT.__pow__(self: GT, other: Fr) -> GT
```
Perform multiplication, division, inversion, and exponentiation on the element.

```python
GT.__eq__(self: GT, other: GT) -> bool
GT.__ne__(self: GT, other: GT) -> bool
GT.isZero(self: GT) -> bool
GT.isOne(self: GT) -> bool
```
Check the equality and inequality of the element, and check if the element is the additive identity or the multiplicative identity.

```python
GT.__hash__(self: GT) -> int
```
Return the hash value of the element.

```python
GT.serialize(self: GT) -> bytes
GT.deserialize(b: bytes) -> GT
```
Serialize and deserialize the element.

### Other Function and Constants

```python
pairing(a: G1, b: G2) -> GT
```
Compute the pairing of two elements in G1 and G2, note that the first argument should be in G1 and the second argument should be in G2.

```python
g1: G1
g2: G2
```
The generator of G1 and G2.

```python
r: int
```
The order of the G1, G2, Fr, and GT groups.
