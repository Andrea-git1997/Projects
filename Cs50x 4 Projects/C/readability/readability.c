#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Prototipy of functions, inside main
int count_letters(string words);
int count_words(string words);
int count_sentences(string words);
int calculate_index(int number_of_letters, int number_of_words, int number_of_sentences);

int main(void)
{ // promopt words
    string words = get_string("Text: ");
    // count number of letters
    int number_of_letters = count_letters(words);
    // count number of words
    int number_of_words = count_words(words);
    // count sentenses
    int number_of_sentences = count_sentences(words);
    // Parameter for index
    // Avarage number of letters evry 100 words.
    int index = calculate_index(number_of_letters, number_of_words, number_of_sentences);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string words)
{
    // definition of variables
    int i;
    int N;
    int number_of_letters = 0;
    // definition of leng word
    N = strlen(words);
    // Count of letter using loop for
    for (i = 0; i < N; i++)
        if (isalpha(words[i]))
        {

           number_of_letters += 1;
        }
        else
        {
        }
    // return value in main function
    return number_of_letters;
}

int count_words(string words)
{
    int z;
    int G;
    int number_of_words = 1;
    G = strlen(words);
    // Definition of leng word
    for (z = 0; z < G; z++)
    {
        if (words[z] == ' ')

       number_of_words += 1;
    }
    // return value in main function
    return number_of_words;
}

int count_sentences(string words)
{
    int f;
    int I;
    int number_of_sentences = 0;
    I = strlen(words);
    // Definition of leng word
    for (f = 0; f < I; f++)
    {
        if (words[f] == '.' || words[f] == '!' || words[f] == '?')

       number_of_sentences += 1;
    }
    // return value in main function
    return number_of_sentences;
}

int calculate_index(int number_of_letters, int number_of_words, int number_of_sentences)
{
    float L = (float) number_of_letters / number_of_words * 100;
    float S = (float) number_of_sentences / number_of_words * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    return index;
}