import pytest
import argparse
from mklicense.__main__ import valid_year

def test_valid_year_returns_int():
    assert valid_year("2020") == 2020

def test_valid_year_current_year_passes():
    from datetime import datetime
    assert valid_year(str(datetime.now().year)) == datetime.now().year

def test_valid_year_future_raises():
    with pytest.raises(argparse.ArgumentTypeError):
        valid_year("2099")

def tes_valid_year_pre_1970_raises():
    with pytest.raises(argparse.ArgumentTypeError):
        valid_year("1969")

def test_valid_year_non_numeric_raises():
    with pytest.raises(ValueError):
        valid_year("abc")


