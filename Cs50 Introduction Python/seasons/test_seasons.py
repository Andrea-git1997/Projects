from seasons import get_birth


def test_ok():
    assert get_birth("19970422") == 14045760
    assert get_birth("1997-04-22") == 14045760

# pytest test_seasons.py
