import sys
import datetime
import inflect
import re



def main():
    birth = input("Date of Birth: ")
    difference = get_birth(birth)
    # craction of inflect object
    w = inflect.engine()
    # i use the method of this library in order to convert number in words
    word_minutes = w.number_to_words(difference,andword ="")
    word_minutes_c = word_minutes.capitalize()
    print(f"{word_minutes_c} minutes")






def get_birth(birth):
    try:
        birth = birth.replace("Date of Birth:","")
        # with this method I want to rewrite data as 19900812 in 1990-08-12
        split_date = datetime.date.fromisoformat(birth)
        # I want have the string of split_date
        split_date = str(split_date)
        #print(split_date)
        # I want to check using regual exprections that input can be okay
        match = re.search((r"^\d{4}\-\d{2}\-\d{2}$"), split_date)
        if match:
            #print("ok")
            # I created a object call today, that say to users the actual data
            today = datetime.date.today()
            #print(f"today is {today}")
            year_s, month_s ,day_s = split_date.split("-")
            year_t, month_t ,day_t = today.year, today.month,today.day
            date_split = datetime.date(int(year_s),int(month_s),int(day_s))
            # I want to calculate minutes of two dates from 0 a.C or d.c.
            #minutes_today = int(year_t) * 365 * 24 * 60 + int(month_t) * 30 * 24 * 60 + int(day_t)* 24 * 60
            #minutes_s = int(year_s) * 365 * 24 * 60 + int(month_s) * 30 * 24 * 60 + int(day_s)* 24 * 60
            # i calculate the difference betweem the two dates
            #difference =  minutes_today - minutes_s
            # this is subctraction
            difference = today - date_split
            # convert the object
            minutes = difference.days *24* 60
            #print(f"minutes ={minutes}")

            return minutes


            #difference = today - split_date
            #print("difference = {difference}")
    except ValueError:
        sys.exit("Invalid date")

    return split_date

# python seasons.py






if __name__ == "__main__":
    main()
