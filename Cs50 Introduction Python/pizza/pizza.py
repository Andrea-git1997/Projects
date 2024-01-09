import sys
import csv
import tabulate


def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        main()
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        main()
    elif ".csv" not in sys.argv[1]:
        print("Not a CSV file")
        main()
    try:
        with open(sys.argv[1] ,"r") as file:
            #print(f"open correctly = {sys.argv[1]}"
            csv_reader = csv.DictReader(file)
            #for row in csv_reader:
            #    print(row)
            # i want to create a table with grind format in witch headers are keys of dict
            table = tabulate.tabulate(csv_reader, headers = "keys",tablefmt = "grid")
            print(table)



    except FileNotFoundError:
        print("File does not exist")








if __name__ == "__main__":
    main()

# python pizza.py regular.csv
# python pizza.py sicilian.csv

