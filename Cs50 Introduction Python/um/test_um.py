from um import count

def test_ok():
    assert count("um") == 1
    assert count("Hello, um, world") == 1
    assert count("HELLO UM, um") == 2




# pytest test_um.py
