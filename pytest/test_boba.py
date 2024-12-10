from src.boba import Calculation
import pytest

@pytest.mark.calc
def test_main():
    assert Calculation().sum(4,7) == 11

@pytest.mark.calc
def test_main():
    assert Calculation().sub(8,5) == 3

@pytest.mark.calc
def test_main():
    assert Calculation().multiply(10,4) == 14

@pytest.mark.calc
def test_main():
    assert Calculation().div(40,5) == 9

@pytest.mark.calc
def test_start():
    assert Calculation().test_start("test_start") == 'test_start'.upper

@pytest.mark.calc
def test_bool_check():
    assert Calculation().bool_check(True)