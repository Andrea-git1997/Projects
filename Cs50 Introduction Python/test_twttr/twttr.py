def main():
    # This is the function of input
    word = input("text: ")
    output = shorten(word)
    print(f"Output: {output}")





def shorten(word):

    new_text = ""
    list = ["a","e","i","o","u"]

    #I'm going to skip all word in the list
    for i in range(len(word)):
        if word[i].lower() not in list:
            new_text += word[i]

    #I want to return value
    return new_text


if __name__ == "__main__":
    main()
