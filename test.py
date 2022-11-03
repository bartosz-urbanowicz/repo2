import pytest
from add import add
from subtract import subtract

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(5, 3) == 2