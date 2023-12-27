
import inflect

names_l =[]
def main():
    # this cicle while is to saved input into a list
    while True:
        try:
            name = input("Name: ")
            if "Name:" in name:
                name = name[6:]
            if name != '':
                names_l.append(name)
            print(names_l)
        # If you want to exit from loop press[Ctrl+d]
        except EOFError:
            break
    #print(f"list: {names_l}")
    count_name = 0
    #This ciclio for is udeful to find the len of the list
    for name in names_l:
        count_name +=1
    #print(f"len of list:{count_name}")
    frame = bid_name(count_name)
    if "Name:" in frame:
        frame = frame.replace("Name:","")
    print(frame)



def bid_name(count_name):
    if count_name == 1:
        frame = (f"Adieu, adieu, to {names_l[0]}")
    if count_name == 2:
        frame = (f"Adieu, adieu, to {names_l[0]} and {names_l[1]}")
    if count_name == 3:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, and {names_l[2]}")
    if count_name == 4:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, {names_l[2]}, and {names_l[3]}")
    if count_name == 5:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, {names_l[2]}, {names_l[3]}, and {names_l[4]}")
    if count_name == 6:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, {names_l[2]}, {names_l[3]}, {names_l[4]}, and {names_l[5]}")
    if count_name == 7:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, {names_l[2]}, {names_l[3]}, {names_l[4]}, {names_l[5]}, and {names_l[6]}")
    if count_name == 8:
        frame = (f"Adieu, adieu, to {names_l[0]}, {names_l[1]}, {names_l[2]}, {names_l[3]}, {names_l[4]}, {names_l[5]}, {names_l[6]}, and {names_l[7]}")

    return frame







main()
