"""
FooBar tests for example_pack
"""
from example_pack.foobar import FooBar


def test_nofoobar():
    """
    Test basic case
    """
    fbar = FooBar(n_bar=7)
    assert fbar(1) == "1"
    assert fbar(2) == "2"
    assert fbar(22) == "22"
    assert fbar(29) == "29"


def test_foo():
    """
    Test Foo case (divisible by 5)
    """
    fbar = FooBar(n_bar=7)
    assert fbar(5) == "Foo"
    assert fbar(45) == "Foo"


def test_bar():
    """
    Test Bar case (divisible by n_bar)
    """
    fbar = FooBar(n_bar=7)
    assert fbar(7) == "Bar"
    assert fbar(11) == "11"

    fbar = FooBar(n_bar=11)
    assert fbar(7) == "7"
    assert fbar(11) == "Bar"


def test_foobar():
    """
    Test FooBar case (divisible by 5 and n_bar)
    """
    fbar = FooBar(n_bar=7)
    assert fbar(35) == "FooBar"
    assert fbar(105) == "FooBar"
