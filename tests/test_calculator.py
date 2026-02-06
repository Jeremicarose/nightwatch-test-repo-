import pytest
import sys
sys.path.insert(0, 'src')
from calculator import add, square

def test_add():
    assert add(2, 3) == 5

def test_square():
    assert square(4) == 16

def test_square_none():
    with pytest.raises(TypeError, match="Cannot square None"):
        square(None)
