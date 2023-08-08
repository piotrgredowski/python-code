"Playground for mutation tests"

import pytest

from src.clock_angle import angle


def test_twelve():
    assert angle.between("12:00") == 0


def test_three():
    assert angle.between("3:00") == 90


def test_six():
    assert angle.between("6:00") == 180


def test_nine():
    assert angle.between("9:00") == 270


def test_twelve_fifteen():
    assert angle.between("12:15") == 82.5


def test_twelve_thirty():
    assert angle.between("12:30") == 165


def test_twelve_thirty_one():
    assert angle.between("12:31") == 170.5


def test_invalid_time():
    with pytest.raises(ValueError, match="Invalid time: 24:00"):
        angle.between("24:00")
