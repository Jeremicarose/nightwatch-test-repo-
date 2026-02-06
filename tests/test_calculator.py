"""Calculator tests."""
import pytest
import sys
sys.path.insert(0, 'src')

from calculator import add, negate

def test_add():
    assert add(2, 3) == 5

def test_negate():
    assert negate(5) == -5

def test_negate_none():
    """FAIL: negate() crashes on None."""
    with pytest.raises(TypeError, match="Cannot negate None"):
        negate(None)
