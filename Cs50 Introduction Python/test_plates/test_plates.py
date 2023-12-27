# test of plate
# pytest test_plates.py

from plates import is_valid
import pytest



def test_plate_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True


def test_plate_invalid():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("CS05") == False
    assert is_valid("50") == False

# pytest test_plates.py
# python plates.py
