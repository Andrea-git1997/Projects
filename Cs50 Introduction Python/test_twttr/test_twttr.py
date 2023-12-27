
from twttr import shorten
import sys
import pytest


def main():
    test_hello()
    test_HELLO()
    test_Marco()
    test_number()
    test_nl()




def test_hello():
        assert shorten("hello") == "hll"


def test_HELLO():
        assert shorten("HELLO") == "HLL"


def test_Marco():
        assert shorten("HELLO, Marco") == "HLL, Mrc"



def test_nl():
        assert shorten("AKL422") == "KL422"



def test_number():
        assert ("422") == "422"






if __name__ == "__main__":
    main()













