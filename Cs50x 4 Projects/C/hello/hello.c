#include <cs50.h>
#include <stdio.h>

// Print hello

int main(void)
{
    string name = get_string("What's your name? ");
    printf("Hello, %s\n", name);
}
