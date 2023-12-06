# TODO

# Loop to accept height only from 0 to 8
while True:
    try:
        height = int(input("Which height do you want? "))
        if (height > 0 and height <= 8):
            break
    # if is a string the input print the error
    except ValueError:
        print("Inserire un numero per favore")

# I'm going to create a pyramid

for i in range(height):
    # first print spaces and in second moment print #
    print(" " * ((height-1)-i) + "#" * (i+1))












