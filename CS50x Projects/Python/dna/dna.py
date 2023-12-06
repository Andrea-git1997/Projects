import csv
import sys


def main():

    # TODO: Check for command-line usage I have to have at least 3 argv
    if len(sys.argv) != 3:
        sys.exit("Please write: python dna.py small.csv 1.txt")

    DNA_frame = []
    # TODO: Read database file into a variable and save them into DNA_frame
    file_name = sys.argv[1]
    #print(f"{file_name}")
    with open(file_name, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for name in reader:
            #print( name["name"], name["AGATC"] , name["AATG"] , name["TATC"])

            # Saved in list DNA_frame a dictionary
            DNA_frame.append(name)
    #print(DNA_frame)


    # TODO: Read DNA sequence file into a variable
    # open txt files and save the string inside list sequences = []
    text_name = sys.argv[2]
    with open(text_name, "r") as file:
        contenuto = file.read()




    # TODO: Find longest match of each STR in DNA sequence
   # I'm define the list of STR that I want to search.
   # DNA_frame[0].keys())[1:] I'm going to save in a list of name subsequences evry STR of a list of dictionary from csv file
   # in these case for small.csv subsequences = ["AGATC" , "TTTTTTTCT" , "AATG" , " TCTAG" , "GATA" , "TATC" , "GAAA" , " TCTG"]
    subsequences = list(DNA_frame[0].keys())[1:]
    #print(f"{subsequences}")

    risultato = {}
    for subsequence in subsequences:
        risultato[subsequence] = longest_match(contenuto, subsequence)
       # print(f"{risultato[subsequence]}")

# for each subsequence I'm going to count the number of corresponding subsequence that we found in risultato
    for name in DNA_frame:
        correspond = 0
        for subsequence in subsequences:
            if int(name[subsequence]) == risultato[subsequence]:
                correspond += 1

        # I'm going to check all subsequence correspond and I'm going to print the name of match
        if correspond == len(subsequences):
            print(name["name"])
            return
    print("No match")


# print(f"{name_count}")

# return


def longest_match(sequences, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequences)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequences[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
