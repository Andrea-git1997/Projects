import re
import sys


def main():
    s = parse(input("HTML: "))

    print(f"{s}")
    #print(f"src is {src}")


def parse(s):
    if re.search(r"<iframe\s*.*><\/iframe>",s):
        #print("okkkkk")
        # this is the regular exprection thtat are searching src in input string
        src = re.search (r"^.*\s*(http(s)*:\/\/(www\.)*youtube\.com\/embed\/([a-zA-Z0-9_]+)).*\s*$", s)
        if src :
            #print("OKKKKK")
            # if src exist return the first group() inside the () [group start to count from 1 not 0!!!!]
            split = src.groups()
            #print(f"split is {s}")
            # I add at the third parts the right
            u = split[3]
            return "https://youtu.be/"+ u

# python watch.py




if __name__ == "__main__":
    main()


