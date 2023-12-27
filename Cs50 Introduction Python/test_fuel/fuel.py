import sys

def main():
    # This is the input
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(f"percentage: {percentage}")

    z = gauge(percentage)
    print(f"{z}")



def convert(fraction):
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
    try:
        #I'm going to handle the division
        percentage = (x_i/y_i)*100
    except ZeroDivisionError:
        sys.exit(0)
    except ValueError:
        sys.exit(0)

    return percentage





def gauge(percentage):
    if percentage >= 99:
        # F is fuel if I'm near to 99%
        return "F"
    elif percentage <= 1:
        # E is empty if I'm near to 1% or less
        return "E"
    else:
        return str(percentage) + "%"



if __name__ == "__main__":
    main()

# python fuel.py
