
# this is input

#z = len("Greeting: ")
#print(f"z={z}")
greeting = input("Greeting: ")
greeting_l = greeting.lower()
#y = len(greeting)
#print(f"y:{y}")

if greeting_l[0:5] == "hello":
    print("$0")
elif  greeting_l[0] == "h" and greeting_l[0:5] != "hello":
    print("$20")
else:
    print("$100")

print(f"Hello?{greeting_l[0:5]}")
