


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    # I have to delate $
    #I'm going to replace $ with nothing
    dollars_w = dollars.replace("$","")
    dollars = float(dollars_w)
    #print(f"dollars :{dollars}")
    return dollars


def percent_to_float(percent):
    # I have to delate %
    substring = "%"
    if substring in percent:
        percent_w = percent.replace("%", "")
    else:
        percent_w = percent
    percent = float(percent_w)/100
    #print(f"percent:{percent}")
    return percent



main()
