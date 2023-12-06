#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string convert(string plainitext, int numkey);

int main(int argc, string argv[])
{
    string key = argv[1];
    // Only argc == 2
    if (argc == 2)
    {
        printf("Key : %s\n", argv[1]);
    }
    else
    {
        // error message
        printf("Usage: ./caesar key");
    }

    // only digit in argv[1]
    int N = strlen(key);
    for (int i = 0; i < N; i++)
    {
        if (isdigit(key[i]))
        {
        }
        else
        {
            // error message
            printf("Usage: ./caesar key");
        }
    }
    // convert key in number
    int numkey = atoi(key);
    // get string from user
    string plainitext = get_string("Input: ");
    string cryptic = convert(plainitext, numkey);
    printf("ciphertext: %s\n", cryptic);
}

string convert(string plainitext, int numkey)
{
    // Definition of variables
    int ASCIIc;
    int ASCIIa;
    int a;
    int c;
    int index_upper;
    int index_lower;
    int z;
    // count number of char
    int S = strlen(plainitext);
    char *cryptic = (char *) malloc((S + 1) * sizeof(char));
    for (z = 0; z < S; z++)
        // if not alpha there's no crytography
        if (isalpha(plainitext[z]))
        {

            if (isupper(plainitext[z]))
            {
                index_upper = plainitext[z] - 65;
                c = (index_upper + numkey) % 26;
                ASCIIc = c + 65;
             cryptic[z] = ASCIIc;
            }
            if (islower(plainitext[z]))
            {
                index_lower = plainitext[z] - 97;
                a = (index_lower + numkey) % 26;
                ASCIIa = a + 97;
                cryptic[z] = ASCIIa;
            }
        }
        else
        {
            cryptic[z] = plainitext[z];
        }
    cryptic[S] = '\0';
    return cryptic;
}

// if (islower(plainitext[z]="." ||plainitext[z]=","||plainitext[z]="?"||plainitext[z]="!" ||plainitext[z]=" " ))