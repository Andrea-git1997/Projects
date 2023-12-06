
camel = input("camelCase: ")

# These program allow camel case to be trasform in snakecase as rules of Pytrhon
for i in camel:
    if i == i.upper():
        print("_"+ i.lower(), end = "")
    else:
        print(i , end = "")


