#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word1);
int compute_score2(string word2);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score2(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word1)
{

    // definition of variables
    int t;
    int T;
    int score1 = 0;
    int N = strlen(word1);
    // First loop to unpack the string of arguments into array[]
    for (int i = 0; i < N; i++)
    {
        if (isalpha(word1[i]))
        {
            // Loops to create index of Array POINTS, from upper and lower case of array[word].Sum of points of differents
            // array letter
       if (isupper(word1[i]))
            {
                      T = word1[i] - 65;
        score1 += POINTS[T];
        }
        else
        {
        t = word1[i] - 97;

                score1 += POINTS[t];
         }
        }
        else
        {
        }
    }

    // return integer value to function in abstraction
    return score1;
}

int compute_score2(string word2)
{ // definition of variables
    int z;
    int Z;
    int score2 = 0;
    int N = strlen(word2);

    //
    for (int i = 0; i < N; i++)
        // First loop to unpack the string of arguments into array[]

        if (isalpha(word2[i]))
        {
            {
                // Loops to create index of Array POINTS, from upper and lower case of array[word].Sum of points of differents
                // array letters
                if (isupper(word2[i]))
                {
                    Z = word2[i] - 65;
                    score2 += POINTS[Z];
                }
                else
                {
                 z = word2[i] - 97;
         score2 += POINTS[z];
                }
            }
         // return integer value to function in abstraction
        }
        else
        {
            // non far nulla se l'array [] ha un valore non numerico
        }
    // restituisci valore di score
    return score2;
}