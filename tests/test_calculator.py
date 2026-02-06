"""Calculator tests."""
import pytest
import sys
sys.path.insert(0, 'src')

from calculator import add, increment

def test_add():
    assert add(2, 3) == 5

def test_increment():
    assert increment(5) == 6

def test_increment_none():
    """FAIL: increment() crashes on None."""
    with pytest.raises(TypeError, match="Cannot increment None"):
        increment(None)
