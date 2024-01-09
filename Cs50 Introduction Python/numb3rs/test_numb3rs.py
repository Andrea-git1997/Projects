from numb3rs import validate


def test_valid():
    assert validate("44.55.66.44") == "True"
    assert validate("233.134.200.44") == "True"




def test_invalid():
    assert validate("44.55.66.277") == "False"
    assert validate("233.134.200.678") == "False"



# pytest test_numb3rs.py









if __name__ == "__main__":
    main()
