

# answer is my input is case insensitive thank the method lower()
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
#print(f"answer {answer}")
# .casfold is an method for case insensitive
if answer == "forty-two" or answer == "forty two" or answer == "42":
    print("Yes")
else:
    print("No")

