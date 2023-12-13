

def main():
    menu = {
            "baja taco": 4.25,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.50,
            "super quesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00
            }

    total_cost = 0

    while True:
        try:
            # This is the input
            item = input("Item: ")
            item_c = item.lower()
            #print(item_c)
            # This is the key link to value
            total_cost += menu[item_c]
            # .2f is a method of f string to have exactly two decimals
            print(f"Total: ${total_cost:.2f}")
        except KeyError:
            #print("Key is not in dict")
            main()
        except EOFError:
            exit()





main()
