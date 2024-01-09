from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(6)
    assert jar.capacity == 6




def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(9)
    assert jar.size == 9
    jar.deposit(2)
    assert jar.size == 11



def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7




# pytest test_jar.py
