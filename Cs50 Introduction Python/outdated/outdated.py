
def main():

    # lists of monts
    months ={
    "January": "01" ,
    "February": "02" ,
    "March":"03" ,
    "April":"04" ,
    "May":"05" ,
    "June":"06" ,
    "July":"07" ,
    "August":"08" ,
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
    }

    data = input("Data: ")

    #try:
    if "/" in data:
        month , day , year = data.split("/")
    elif "-" in data:
        month , day , year = data.split("-")
    else:
        month , day , year = data.split(" ")

    #print(f"month: {month}")
    #print(f"day {day}")
    #print(f"year {year}")
    #if "," in month or "," in day or "," in year :
    #    main()

    #except:
        #print("[Error]-retry prompt")
        #main()

    #cleaning variables
    if ","  in month:
        month = month.replace("," , "")
    elif "."  in month:
        month = month.replace("." , "")
    elif ","  in month:
        month = month.replace("," , "")

    if ","  in day:
        day = day.replace("," , "")
    elif "."  in day:
        month = day.replace("." , "")
    elif ","  in day:
        day = day.replace("," , "")



    if ","  in year:
        year = year.replace("," , "")
    elif "."  in year:
        year = year.replace("." , "")
    elif ","  in year:
        year = year.replace("," , "")
    elif " "  in year:
        year = year.replace(" " , "")



    # Print of controls
    #print(f"month {month}")
    #print(f"day {day}")
    #print(f"year {year}")

    #If I have day inside dict of months
    if day.isalpha():
        if day in months:
            main()

    #if I have write months I WANT TO CONVERT MONTHS IN MONTH
    if month in months:
        month = months[month]
        # control check if in loop
        #print("enter in loop")
        #print(month)

    # convertion of month in an integer
    if len(month) <= 2:
        month = int(month)
        if month > 12 or month < 1:
            main()

    if len(day) <= 2:
        day = int(day)
        if day < 1 or day > 31:
            main()




    #reconvertion in strings
    month = str(month)
    day = str(day)

    #print final result

    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")














main()
