from validator_collection import checkers
from validators import email


def main():
    result = validation(input("What's your email adress? "))
    # print results
    print(result)



def validation(s):
    s = s.replace("What's your email adress?","")
    # I use two method of two differents libraries to check the emails
    if not checkers.is_email(s):
        return "Invalid"
    elif not email(s):
        return "Invalid"
    else:
        return "Valid"

# python response.py
# mamma@68.gmail.com

if __name__ == "__main__":
    main()



