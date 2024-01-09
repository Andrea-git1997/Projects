from fpdf import FPDF
from PIL import Image



class Shirt:
    Image.open("shirtificate.png")
    def __init__(self, name = input("Name: ", )):
        if name.isdigit():
            raise ValueError("Name could be only a string")
        self._name = name


    # decoration to avoid modification at code
    @property
    def name(self):
        return self._name



def main():

    shirt = Shirt()
    name = shirt.name
    #print(f"name is {name}")
    slogan = f"{name} took CS50"
    #print(f"Slogan is {slogan}")
    # importing the image of input
    shirt_image = Image.open("shirtificate.png")

    # coordinate
    x = 50
    y = 50
    w = 100

    # I want to create PDF
    pdf = FPDF(format = "A4")
    pdf.add_page()

    # shirt add
    pdf.image("shirtificate.png", x= x , y=y , w = w)

    pdf.set_font("Arial", size = 24)
    pdf.cell(0,60 ,"CS50 Shirtificate", new_x ="LMARGIN", new_y ="NEXT", align = "C")

    pdf.set_font("helvetica", size = 12)
    pdf.cell( 0, 40 ,slogan, align = "C")


    pdf.output("shirtificate.pdf")
    #print("ESEGUITO")













# python shirtificate.py
# cd shirtificate

if __name__ == "__main__":
    main()
