# Grocery list

def main():
    # definition list and dict
    list_food = {}


    while True:
        try:
            # this is input is a list
            items = input().split()
            #upper case
            for i in items:
                item = i.upper()

            #print(new_list)
            for item in items:
                if item in list_food:
                    # I save the food list with count in dictionary
                    list_food[item] += 1
                else:

                    list_food[item] = 1
        # exit command
        except EOFError:
            break

#print count and food in dict 
    for item in sorted(list_food):
        print(list_food[item],item.upper())



main()


