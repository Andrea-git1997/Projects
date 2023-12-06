#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9



// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];



// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;




// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(int vote_counts[]);
int find_min(int vote_counts[]);
bool is_tie(int min,int vote_counts[]);
void eliminate(int min , int vote_counts[]);

int main(int argc, string argv[])
{   int vote_counts[candidate_count];
    // Initialisation
    for (int i = 0; i < candidate_count; i++)
    {
        vote_counts[i] = 0;
    }
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner( vote_counts);
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min(vote_counts);
        bool tie = is_tie(min, vote_counts);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min, vote_counts);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{


    // Confront of valid candidate
    for (int i = 0; i < candidate_count;i++)
    {
        // Check if I have the valid candidte in votes'paper
        if (strcmp(candidates[i].name, name) == 0)
        {
            // register votes if names in papers are correct
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;

}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
        // Definition of a new array
        // Definicion of malloc with different size in order to register the preferences
        int *vote_counts = malloc(candidate_count * sizeof(int));
       for (int i = 0;i < voter_count; i++)
    {
           int prefer_candidate_index = preferences[i][0];
         // for evry voters I want to count the preferences of prefer candidate
         vote_counts[prefer_candidate_index]++;

    }

}

// Print the winner of the election, if there is one
bool print_winner(int vote_counts[])
{
    // for evry candidate
    for ( int i = 0; i < candidate_count; i++)
    {
        if(vote_counts[i] > voter_count/2 )
        {
         // Winner
        printf("The winner is : %s " , candidates[i].name );
     return true;
     }
    }
  return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(int vote_counts[])
{   // I'm going to initialize the value of minimum at the first input on the array
    int min_votes = vote_counts[0];
    // I want using a ciclo for in order to find the minimum value in array
    for (int i = 0; i < candidate_count ; i++)
    { if ( vote_counts[i] < min_votes && min_votes > 0)
         min_votes = vote_counts[i];
    }
        // return the minimum value inside the array
        return min_votes;



}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min ,int vote_counts[])
{
    // I want to check if minimum value have different value in all candidates
    for(int i = 0; i < candidate_count ; i++)
    {
         if (vote_counts[i] != min)
    {
        // if yes there's no tie
        return false;
    }
    }
    // if all euqla I have a tie value or values
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min,int vote_counts[])
{
    // I wnat to eliminated the candidates that had smalest numbers of votes using for loop
    for(int i = 0 ; i < candidate_count ; i++)
    {
    if(vote_counts[i] == min)
    {
        candidates[i].eliminated = true;
    }
    }
}
