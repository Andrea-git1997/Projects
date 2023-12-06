
def main():
    # input of coins
    ammount = 50
    print(f"Amount Due: {ammount}")
    insert_coin = input("Insert Coin: ")
    insert_coin_ok = check_input(ammount, insert_coin)
    #print(f"Result:{insert_coin_ok}")


    # This is the convertion of a int
    insert_coin_int = int(insert_coin_ok)

    # this is code test to see if variable_input is saved
    #print(f"insert_coin_int:{insert_coin_int}")

    i=0
    while (ammount != 0):
        if i == 0:
            # This is the calculation
            Change = ammount - insert_coin_int
            #Print the update of amount Due
            print(f"Amount Due: {Change}")
            # Ask again coin to reduce amount
            insert_coin = input("Insert Coin: ")
            insert_coin_int = int(insert_coin)
        elif i >= 1:
             # This is the calculation
            Change = Change  - insert_coin_int
            #Print the update of amount Due
            if Change == 0:
                print(f"Change Owed: {Change}")
                break
            elif Change > 0:
                print(f"Amount Due: {Change}")
            # Ask again coin to reduce amount
            insert_coin = input("Insert Coin: ")
            insert_coin_int = int(insert_coin)
            #print(f"result{Change}")
            if Change < 0:
                rest = Change - insert_coin_int
                print(f"Change Owed: {rest}")
                break
        i +=1






def check_input(ammount, insert_coin):
    # Cicle breaks only if values are 5,10,25
    while (insert_coin not in ["5","10","25"]):
        print(f"Amount Due: {ammount}")
        insert_coin = input("Insert Coin: ")
        # this is a try code to test if digit 10,5,25 is okay
    #print("End while")
    return insert_coin



init = "__main__"
main()
