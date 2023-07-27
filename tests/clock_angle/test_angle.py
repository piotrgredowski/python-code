"Playground for mutation tests"

from src.clock_angle import angle


def test_twelve():
    assert angle.between("12:00") == 0
