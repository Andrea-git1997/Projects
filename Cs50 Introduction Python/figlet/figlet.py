#I imports the library
from pyfiglet import Figlet
import sys

def main():
    # I'm checing if users digit the font
    if len(sys.argv) < 2:
        #print("[ERROR]: insert python figlet.py <font>")
        exit()
    # I saved argv[2] in one variable that is call as font
    font = sys.argv[2]
    # This is the impostetion of font and ec...
    figlet = Figlet(font= font, width = 100, justify = "left")
    # input from users
    text = input("Input: ")
    # this variable apply font and ec.. at the usr input
    render_text = figlet.renderText(text)
    print(f"Output: {render_text}")



main()
