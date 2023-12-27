

# I want to import my file to test
from fuel import main,convert, gauge


def test_fuel():
    assert convert("1/100") == 1.0 and gauge(1) == "E"
    assert convert("99/100") == 99.0 and gauge(99) == "F"
    assert convert("50/100") == 50.0 and gauge(50.0) == "50.0%"




if __name__ == "__main__":
    test_fuel()







# pytest test_fuel.py
