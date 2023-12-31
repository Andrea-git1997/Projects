#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Confront of valida candidate
    for (int i = 0; i < candidate_count; i++)
    {
        // Check if name for voting is valid
        if (strcmp(candidates[i].name, name) == 0)
        {
            // Add one vote at the candidate
            candidates[i].votes++;
     return true;
     }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Initialisacion of max votes
    int max_vote = 0;
    int other;
    string Max_name;
    string other_name;

    // Repet for all candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // Check Max Votes in Array
        if (candidates[i].votes > max_vote)
        {
            // save Max votes
            max_vote = candidates[i].votes;
        }
    }
    // For to compare max_votes to other candidate, if fine two or three candidate with the same votes, print tipe
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == max_vote)
        {

            printf("%s\n", candidates[i].name);
        }
    }
}