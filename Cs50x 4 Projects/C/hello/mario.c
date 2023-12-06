// Import lists
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt of choicer
    int height;
    do
    {
        height = get_int("Height: ");
    }

    while (height < 1 || height > 8);

    // colums
    for (int i = 0; i != height; i++)
    {

       // dot is use to make the spaces that I needed to have the goal. For evry line, I'm going to print #, as the height - i -1
        // said
        for (int d = 0; height - i - 1 > d; d++)
        {
            printf(" ");
        }
        // raw. For evry raw I have the same number of #
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }

        // It's a function to go in the next raw
        printf("\n");
    }
}
