def main():
    # This is my input to handle
    time = input("What time is? ")
    # What I have to do to convert from this ##:## to this ##.##
    time_c = convert(time)
    # This is the ciclo for to handle the action link to houars
    if time_c >= "7.0" and time_c <= "8.0":
        print("breakfast time")
    elif time_c >= "12.0" and time_c <= "13.0":
        print("lunch time")
    elif time_c >= "18.0" and time_c <= "19.0":
        print("dinner time")
    ...


def convert(time):
    houars , minutes = time.split(":")
    #I'm doing the convert
    minutes_float = round((float(minutes)/60)*1.0,2)
    # I want to convert float in a string and eliminate the 0.
    minutes_c = str(minutes_float).replace("0.","")
    # i want to join the two parts
    time_c = ".".join([houars,minutes_c])
    # i want to return the converse time
    #print(f"time_c is:{time_c}")
    return time_c




if __name__ == "__main__":
    main()
