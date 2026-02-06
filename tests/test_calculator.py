import pytest
import sys
sys.path.insert(0, 'src')
from calculator import add, invert

def test_add():
    assert add(2, 3) == 5

def test_invert():
    assert invert(2) == 0.5

def test_invert_zero():
    with pytest.raises(ValueError, match="Cannot invert zero"):
        invert(0)
