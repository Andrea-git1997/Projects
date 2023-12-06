// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>




#include "dictionary.h"

// Global variables definition
int hash_value;
// inizialization and definition of word_count
int word_count = 0;





// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // I'm figure out the nubers of hash of the word that I want to check
    hash_value = hash(word);
    // Definition of a new checking node
    node *cursor = table[hash_value];

    // Because when I see NULL I'm at the end of the hash table
    while(cursor != 0)
    {
        if(strcasecmp(word, cursor -> word )== 0)
        // I want try to figure out if in my hash there are all word of dictionaty
        {
             return true;
        }

        cursor = cursor -> next  ;

    }
        // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // I'm going to calculate the lenght of a word
    int s = strlen(word);
    int total_letter = 0;
    char  new_word[LENGTH + 1];
        for(int i = 0 ; i <s ; i++)
        {
            new_word[i] = tolower(word[i]);
            // I'm going to have the sum of lower case of total letter of the word that I had load
            total_letter += new_word[i];
        }
            // This is my hash integer value
            hash_value = round(total_letter % N);
            return true;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    //open file dictionary
    FILE *file = fopen(dictionary , "r");
        if(file == NULL)
             {
                printf("The file is empty or there's difficulties in open it");
                fclose(file);
                return false;
            }
    // definition of word
    char word[LENGTH + 1];

    // read word from file
    while(fscanf(file , "%s", word ) != EOF)
        {
            //space of memory to allocate nodes
            node *n = malloc(sizeof(node));
            if(n == NULL)
            {
                return false;
            }
            strcpy(n -> word, word);
            // I'm going to calculate the number who correspond at hash table

            hash_value = hash(word);
            n -> next = table[hash_value];
            table[hash_value] = n ;

            // count the word loaded
            word_count++;

        }
            fclose(file);
            return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size (void)
{
     if (word_count >0)
    {
        // I'm doing a checking of value calculate in load function
        return word_count;
    }

     return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{    // external declaration of cursor
    for(int i = 0 ; i < N ; i++)
    {
        // definition of a new pointer

        // for evry table
        node *cursor = table[i];

            while (cursor != 0)
        {
            // When cursor and tmp are pointers of the same link, cursor must be alongside
            node *tmp  = cursor;
            cursor = cursor -> next;
            free(tmp);
        }
        if(cursor == NULL)
        {
            return true;
        }

    }

    return false;

}
