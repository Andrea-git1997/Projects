import csv
import sys

def main():
    # handle error of argv
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        main()
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        main()
    elif sys.argv[1] != "before.csv":
        print(f"Could not read {sys.argv[1]}")
        main()

    try:
        # open file
        with open(sys.argv[1] , "r") as infile:
            #print(f"open correctly file {sys.argv[1]}")
            csv_reader = csv.DictReader(infile)
            for row in csv_reader:
                if "," in row["name"]:
                    # split value of key name in name and last
                    name , last = row["name"].split(",")
                    house = row["house"]
                    #write the variables in after.py
                    with open(sys.argv[2], "a") as outfile:
                        csv_writer = csv.DictWriter(outfile , fieldnames = ["name","last","house"])
                        csv_writer.writerow({"name": name , "last": last , "house": house})
                        #print(f"name = {name} and last = {last} the house = {house}")
                else:
                    # This is the path in wich I cannot split the variables.
                    name = row["name"]
                    house = row["house"]
                    with open(sys.argv[2], "a") as outfile:
                        csv_writer = csv.DictWriter(outfile , fieldnames = ["name","last","house"])
                        csv_writer.writerow({"name": name , "last": last , "house": house})
                        #print(f"name = {name} and last = {last} the house = {house}")

            #for row in csv_reader:
            #    print(f"{row}")
        #print(f"sys.argv[2] = {sys.argv[2]}")



    except FileNotFoundError as z:
        print(f"File does not exist = {z}")





# python scourgify.py before.csv after.csv














if __name__ == "__main__":
    main()
