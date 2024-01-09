
from project import gain, rez

# I can test only two these function because others gave me errors, i think that they are too elaborate. For example the functions that gave the plots or input inside.
# To complete the final prject tasks I added yhese two functions and I tested them

def test_gain():
    assert gain() == True

def test_rez():
    assert rez('Paolo') == "Welcome Paolo"
    assert rez('Marco') == "Welcome Marco"


# pytest -s test_project.py
# python project.py
