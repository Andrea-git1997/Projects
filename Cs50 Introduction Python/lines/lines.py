import sys


def main():
    # I want to handle the errors or file not found
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        main()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        main()
    elif ".py" not in sys.argv[1]:
        print("Not a python file")
        main()
    #print(f"argv[1]:{sys.argv[1]}")
    try:
        with open(sys.argv[1],"r") as file:
            #print(f"Open correctly = {sys.argv[1]}")
            count_rows = 0
            for row in file:
                #print(f"row[0]:{row[0]}")
                # I count only the row that have not # or spaces
                if   row.lstrip() and  row.lstrip()[0] != "#":
                    count_rows +=1

        print(f"{count_rows}")


    except FileNotFoundError:
        print("File does not exist")


# python lines.py hello.py









if __name__ == "__main__":
    main()
