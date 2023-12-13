
def main():
    # This is the input
    fraction = input("Fraction: ")
    x_s, y_s = fraction.split("/")
    #print(x_s)
    #print(y_s)

    # I'm going yo convert x and y in integer
    try:
        x_i = int(x_s)
    # if in convertion there are errors I'm going to restart the main function
    except ValueError:
        main()

    try:
        y_i = int(y_s)
    except ValueError:
        main()


    #I'm going to handle the division
    try:
        z = int((x_i/y_i) * 100)
    # If I have ZeroDivisionException I recall main function to change input
    except ZeroDivisionError:
        main()
    except ValueError:
        main()
    if z >= 99:
        # F is fuel if I'm near to 99%
        print("F")
    elif z <= 1:
        # E is empty if I'm near to 1% or less
        print("E")
    else:
        print(f"{z}%")





main()
