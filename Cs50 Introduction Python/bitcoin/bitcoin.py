# BITCOIN PRICE INDEX

import sys
import requests

def main():
    # this is the URL of API JSON
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # I want to handle the argv and convert it in a float.
    #lenght = len(sys.argv)
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        #print(f"check 1 = {lenght}")
        sys.exit(1)
    else:
        try:
            #print(f"check 2 = {lenght}")
            #print(f"bitcoin at the moment is {sys.argv[1]}")
            quantity = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    try:
        # i'm checking the responce of server via url
        response = requests.get(url)
        #this is an excepion
        response.raise_for_status()

        #I'm going to format jason() informations
        dict = response.json()
        # I want to create a small dict in wich takes the information of value of bitcoin
        rate = dict["bpi"]["USD"]["rate_float"]
    # Hear I'm handling the exceptions
    except requests.exceptions.RequestException as z:
        print(f"ERROR in request at server: {z}")
        sys.exit(1)
    except KeyError as p:
        print(f"ERROR in elaboration of data via API. p = {p}")
        sys.exit(1)


    #print(f"rate is {rate}")

    #this is the price for the quantities that i want to buy
    bitcoin = rate * quantity
    print(f"${bitcoin:,.4f}")

    #sum = 2 + quantity
    #print(f"bitcoin value is{quantity}, the check sum {sum}")















if __name__ == "__main__":
    main()
