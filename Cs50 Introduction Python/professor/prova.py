import random


def main():
    # insert the level of the play
    level = get_level()
    #print(f"level:{level}")

    #inatialization of score.
    score = 0
    # generation of answers
    for i in range(10):
        x,y = generate_integer(level)
        # this is the correct sum
        correct = x+y

        # this is the loop with 3 possibilities
        for tentativ in range(3):
            problems= input(f"{x} + {y} = ")
        #if "Level:" in problems:
        #    print("HELPPPPPPP")

            try:
                user_answer = int(problems)
            # This is the exception
            except ValueError:
                print("Please answer with correct")
                continue

            if user_answer == correct:
                print("Corerrect")
                score += 1
                break
            
        print(f"Score: {score}")








def get_level():
    level = input(" ")
    while level != "1" and level != "2" and level != "3":
        level = input(" ")
    return level



def generate_integer(level):
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
