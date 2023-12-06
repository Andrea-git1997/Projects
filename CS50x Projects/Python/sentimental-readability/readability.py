from cs50 import get_string


def main():
    # Ask for an input
    word = input()
    #print(f"Word of input is : {word}")

    # count number of letters
    n_letters = count_letters(word)
    print(f"Number of letters is : {n_letters}")

    # count number of words
    n_words = count_words(word)
    print(f"Number of letters words : {n_words}")

    n_sentences = count_sentences(word)
    print(f"Number of letters sentence : {n_sentences}")

    index = calculate_index(n_letters, n_words, n_sentences)
    #print(f"Index is  : {index}")
    if index < 1:
        print("Before Grade 1")
    elif (index > 16):
        print("Grade 16+")
    else:
        print(f"Grade {index}")











# fuction to have input
def input():
        try:
            word = get_string("Text: ")
            return word
        except ErrorValue:
            print("Error : axept only a string")


def count_letters(word):
    # calculation len
    N = len(word)
    n_letters = 0
    # Iterate through all characters in the word
    n = 0
    while n != N:
        if word[n].isalpha():
            n_letters += 1
        n += 1

    return n_letters


def count_words(word):
      # calculation len
    N = len(word)
    n_words = 1
    # Iterate through all characters in the word
    z = 0
    while z != N:
        if word[z] == " ":
            n_words += 1
        z += 1

    return n_words


def count_sentences(word):
      # calculation len
    N = len(word)
    n_sentences = 0
    # Iterate through all characters in the word
    r = 0
    while r != N:
        if word[r] == "." or word[r] == "!" or word[r] == "?" :
            n_sentences += 1
        r += 1

    return n_sentences



def calculate_index(n_letters, n_words, n_sentences):
    L = n_letters / n_words * 100
    S = n_sentences / n_words * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index











init = "__main__"
main()

