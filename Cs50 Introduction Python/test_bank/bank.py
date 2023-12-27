
# this is input

#z = len("Greeting: ")
#print(f"z={z}")
def main():
    greeting = input("Greeting: ")
    output = value(greeting)
    print(f"${output}")








def value(greeting):
    greeting_l = greeting.lower().strip()
    #y = len(greeting)
    #print(f"y:{y}")

    if len(greeting_l) > 0 :
        if greeting_l[0:5] == "hello":
            return 0
        elif  greeting_l[0] == "h" and greeting_l[0:5] != "hello":
            return 20
        else:
            return 100
    else:
        return 100

    #print(f"Hello?{greeting_l[0:5]}")


# python bank.py



if __name__ == "__main__":
    main()
