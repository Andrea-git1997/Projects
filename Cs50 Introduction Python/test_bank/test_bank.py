import pytest
import sys
from bank import value







# pytest test_bank.py




def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HELLO , vi") == 0
    assert value("HeLlo") == 0



def test_hey():
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("HEY, vi") == 20


def test_goodby():
    assert value("goodby") == 100
    assert value("GOODBY") == 100
    assert value("GOODBY , vi") == 100
    assert value("What's your name?") == 100
    assert value("") == 100
    assert value("  goodby  ") == 100









