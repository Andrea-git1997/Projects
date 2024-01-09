import re
import sys


def main():
    result = count(input("Text: "))
    print(result)


def count(s):
    s = s.replace("Text:","")
    s = s.lower()
    # this is the pattern that I want to search
    pattern = r"um"

    # count all um inside the sentense
    matches = re.findall(pattern,s)
    if matches:
        result = len(matches)

    return result


# python um.py
# Hello UM, umum UM Marc

if __name__ == "__main__":
    main()
