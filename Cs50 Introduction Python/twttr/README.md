Twitter Input Processor
Overview:
This Python script serves as a basic input processor for tweets by removing vowels (both uppercase and lowercase) from the input. The goal is to generate a modified version of the input text without vowels.

How to Use:
Run the script by executing the Python file:

bash

python twitter_input_processor.py
Enter a tweet or any text when prompted.

The program will process the input, removing vowels, and display the modified text.

Code Explanation:
main() Function:
Input Collection:

Prompt the user to input text (tweet or any other text).
Vowel Removal:

Iterate through each character in the input.
If the character is a vowel (either uppercase or lowercase), replace it with an empty string.
Display Result:

Print the modified text without vowels.
Example:
python

# Run the script
python twitter_input_processor.py
python

# Example Output:

Input: This is a sample tweet!
Ths s smpl twt!
This example demonstrates a user inputting a tweet, and the script processing the input by removing vowels and displaying the modified text.
