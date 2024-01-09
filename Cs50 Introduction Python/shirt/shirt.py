import csv
import sys
from PIL import Image,ImageOps



def main():
    # handle the difficulties
    print(f"argv[1] = {sys.argv[1]} , sys.argv[2] = {sys.argv[2]}")
    if len((sys.argv)) < 3:
        print("Too few command-line arguments")
        exit()
    elif len((sys.argv)) > 3:
        print("Too many command-line arguments")
        exit()
    elif ".jpg" in sys.argv[1] and ".png" in sys.argv[2]:
        print("Input and output have different extensions")
        exit()
    elif ".png" in sys.argv[1] and ".jpg" in sys.argv[2]:
        print("Input and output have different extensions")
        exit()


    try:
        # I want to open the input files

        # print(f"file open with succes {sys.argv[1]}")
        # I open the shirt immage
        input_image = Image.open(sys.argv[1])

        shirt = Image.open("shirt.png")

        # this command return (width,height)
        size = shirt.size

        # i want resize the input image
        input_image = ImageOps.fit(input_image,size)

        # i paste the shirt
        input_image.paste(shirt,shirt)

        #I saved the input image resize in after file
        input_image.save(sys.argv[2])






        #with open(sys.argv[2],"wb") as ofile:
        #    output_img.save(ofile)



    except FileNotFoundError as z:
        print(f"File does not exist = {z}")


# python shirt.py before1.jpg after.jpg












if __name__ == "__main__":
    main()
