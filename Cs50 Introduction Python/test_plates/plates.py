def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# list of number
number_list = []
list_allnumber = []

def is_valid(plate):
    # checking the condictions for validate
    #1 len must be inside 2 and 6 digit and the first two must be letter
    if len(plate)>=2 and len(plate) <= 6  and plate[0:2].isalpha():
        # There aren't this special digit
        if not " " in plate and  not "." in plate and  not "," in plate and  not ":" in plate and  not";" in plate:
            is_number_valid , count = number(plate)
            #print(f"Count:{count}")
            #print(f"PLATE:{plate[count:]}")
            # The first number can not be 0 and after the first number I cannot have alpha only numbers
            if is_number_valid and number_list[0] != "0" and  plate[count:].isdigit():
                #print(number_list[0])
                #print("BOHHH")
                #print(number_list)
                return True

    return False


def number(plate):
    # I want to check if the's numbers
    count = 0
    for i in plate:
        count += 1
        if i.isdigit():
            number_list.append(i)
            #print(i)
            #print(f"Count:{count}")
            return True , count



    return False

# I want to save a list off all input digit from the first number





if __name__ == "__main__":
    main()



# python plates.py
