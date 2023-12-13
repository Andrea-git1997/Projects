# Grocery list

def main():
    # definition list and dict
    list_upper = []
    list_food = {}

    count = 0
    while True:
        try:
            # this is input is a list
            items = input().split()
            #upper case
            for i in items:
                items_m = i.upper()
                list_upper.append(items_m)
                #print(items_m)
            #print(list_upper)
            # sorted list input
            new_list = sorted(list_upper)
            #print(new_list)
            for fruit in new_list:
                if fruit in list_food:
                    # This if block print in dict the value and quantyty

                    # I save the food list with count in dictionary
                    list_food[fruit] += 1
                else:

                    list_food[fruit] = 1

            #print(list_food)
            for fruit in list_food:
                print(list_food[fruit],fruit)
        except EOFError:
            break



main()


