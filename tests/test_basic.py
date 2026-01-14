from pymcl import Fr, G1, G2, GT, g1, g2, pairing


def test_fr():
    zero = Fr(0)
    one = Fr(1)
    x = Fr.random()
    y = Fr.random()
    z = Fr.random()

    w = Fr.deserialize(z.serialize())
    assert w == z
    assert hash(w) == hash(z)

    assert zero.is_zero() and not zero.is_one()
    assert one.is_one() and not one.is_zero()

    assert z + zero == z
    assert z * one == z
    assert (z + -z).is_zero()
    assert (z * ~z).is_one()
    assert (x + y) * z == x * z + y * z
    assert (x - y) * z == x * z - y * z

    s = z.sqr()
    r = s.sqrt()
    assert r is not None and r * r == s


def test_g1():
    p1 = G1.hash(b"pymcl-g1")
    z1 = G1()
    x = Fr.random()
    y = Fr.random()

    q1 = G1.deserialize(p1.serialize())
    assert q1 == p1
    assert hash(q1) == hash(p1)

    assert not p1.is_zero()
    assert z1.is_zero()

    assert p1 * x + p1 * y == p1 * (x + y)
    assert p1 * x - p1 * y == p1 * (x - y)
    assert -p1 + p1 == z1


def test_g2():
    p2 = G2.hash(b"pymcl-g2")
    z2 = G2()
    x = Fr.random()
    y = Fr.random()

    q2 = G2.deserialize(p2.serialize())
    assert q2 == p2
    assert hash(q2) == hash(p2)

    assert not p2.is_zero()
    assert z2.is_zero()

    assert p2 * x + p2 * y == p2 * (x + y)
    assert p2 * x - p2 * y == p2 * (x - y)
    assert -p2 + p2 == z2


def test_gt():
    zero = GT(False)
    one = GT(True)
    e = pairing(g1, g2)
    x = Fr.random()
    y = Fr.random()

    assert zero.is_zero() and not zero.is_one()
    assert one.is_one() and not one.is_zero()

    assert e * one == e
    assert e * ~e == one
    assert e ** x * e ** y == e ** (x + y)
    assert e ** x / e ** y == e ** (x - y)

    n = GT.deserialize(e.serialize())
    assert n == e
    assert hash(n) == hash(e)


def test_pairing():
    x1 = Fr.random()
    x2 = Fr.random()

    assert pairing(g1 * x1, g2 * x2) == pairing(g1, g2) ** (x1 * x2)
