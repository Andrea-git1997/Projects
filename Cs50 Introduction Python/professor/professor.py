import random
import sys


def main():
    # insert the level of the play
    level = get_level()
    #print(f"level:{level}")
    # I have 10 questions generated
    for i in range(10):
        x,y = generate_integer(level)

        #this is the answer
        problems= input(f"{x} + {y} = ")
        #if "Level:" in problems:
        #    print("HELPPPPPPP")
        #I wabt to clean answer and have only the sum value as a string
        problems = problems.replace(f"{x }+ {y} =", "")
        #problems = problems.replace(f"Level:", "")

        #print(f"check problems = {problems}")

        if problems != "":
            problems = int(problems)
        # if answer if not correct print(EEE)
        if x + y != problems:
            print("EEE")
            problems= input(f"{x} + {y} = ")

            #if "Level:" in problems:
            #    print("Levellllllll is thereeeee")



            problems = problems.replace(f"{x} + {y} =", "")
            if problems != "":
                problems = int(problems)
            if x + y != problems:
                print("EEE")
                problems= input(f"{x}+{y}= ")
                problems = problems.replace(f"{x} + {y} =", "")
                if problems != "":
                    problems = int(problems)
                if x + y != problems:
                    print("EEE")
                    solution = x+y

                    print(f"{x} + {y} = {solution}")

        sys.exit()




def get_level():
    level = input(" ")
    while level != "1" and level != "2" and level != "3":
        level = input(" ")
    return level



def generate_integer(level):
    # for each levels I want to print differents questionms
    if level == "1":
        x = random.randrange(0,9)
        y = random.randrange(0,9)
        x = int(x)
        y = int(y)
        #print(f"x is {x}")
        #print(f"y is {y}")
    elif level == "2":
        x = random.randrange(10,99)
        y = random.randrange(10,99)
        x = int(x)
        y = int(y)
        #print(f"x is {x}")
        #print(f"y is {y}")
    elif level == "3":
        x = random.randrange(100,999)
        y = random.randrange(100,999)
        x = int(x)
        y = int(y)
        #print(f"x is {x}")
        #print(f"y is {y}")


    return x,y
    ...


if __name__ == "__main__":
    main()
