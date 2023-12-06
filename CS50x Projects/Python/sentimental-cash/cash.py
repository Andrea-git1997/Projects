from cs50 import get_float



def main():
    # Ask how many cents the customer is owed
    owd = get_owd()
    cents = owd*100
    # Calculate the number of quarters to give the quarters
    quarters = calculate_quarters(cents)
    # Calculate the number of cents to use in order to calculate how many dimes
    cents = cents - quarters *25
   # print(f"Quarter: {quarters}")

    # Calculate the number of quarters to give the quarters
    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10
    #print(f"Dimes : {dimes}")


    # Calculate the number of quarters to give the quarters
    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5
    #print(f"Nickles {nickels}")


     # Calculate the number of quarters to give the quarters
    pennies = calculate_pennies(cents)
    pennies = cents - pennies * 1
    #print(f"Pennis :{pennies}")
    #print(f"Cents : {cents}")

    # calculation of total coins
    total_coins = cents + quarters +  dimes +  nickels +  pennies
    print(f"{total_coins}")










def calculate_quarters(cents):
    count_coins = 0
    ## if cents > 100 I have to subtract 25 and count how many coins of quarters
    while cents >= 25:
        cents = cents - 25
        count_coins +=1
    quarters = count_coins
    return  quarters

def calculate_dimes(cents):
    count_coins = 0
    while cents >= 10:
        cents = cents - 10
        count_coins +=1
    dimes = count_coins
    return  dimes

def calculate_nickels(cents):
    count_coins = 0
    while cents >= 5:
        cents = cents - 5
        count_coins +=1
    nickels = count_coins
    return nickels

def calculate_pennies(cents):
    count_coins = 0
    while cents >= 1:
        cents = cents - 1
        count_coins +=1
    pennies = count_coins
    return pennies















def get_owd():
    while True :
        try:
            owd = get_float("How many owed do you want? ")
            if owd > 0:
                break
        except ValueError:
            print("Digit as value a positve integer or float number")
    return owd




init = "__main__"
main()



