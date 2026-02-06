"""Calculator tests."""
import pytest
from calculator import add, subtract, multiply, divide, square


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_square():
    assert square(4) == 16


def test_square_none():
    """FAIL: square() crashes on None."""
    with pytest.raises(TypeError, match="Cannot square None"):
        square(None)
