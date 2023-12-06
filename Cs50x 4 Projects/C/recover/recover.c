#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;
const int MAX_FILENAME_LENGTH = 100 ;

typedef uint8_t BYTE;
FILE *input;

// definition of functions
int  open_file(int argc, char *argv[]);

int main(int argc, char *argv[])
{
   // check lenght of argv
   if(argc != 2)
   {
        printf("Numbers of input are not 2, please write in terminal ./recover [name of input]");
        return 1;
   }
        // open input file
        open_file(argc,argv);

        // definition of blocks size

        //Definition of 4 bytes that are the beggining of recover chuncks
        uint8_t buffer[BLOCK_SIZE] ;
        int counter = 0;
        FILE *img;
        // I'm going to define the array in wich I will define the name of jpg files
        char  filename[8];



        // reading
        while (fread( buffer, BLOCK_SIZE , 1, input) == 1)
        {
              if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
              {

            // If is no the first jpag that i created I have to close it
            if (counter != 0)
            {
                fclose(img);
            }
            // I want to open a jpagfile and store this chuncks of bites
                    sprintf( filename , "%03i.jpg" , counter);
                    // declaration of file name and definition of appropriate size of that


                    img = fopen(filename, "w");
                    // Keep going to write actual jpg file that we opened
                    fwrite( buffer, BLOCK_SIZE , 1, img );
                    }

            // Count counter++ every time that I encounter start block indicators
            if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
                    {
                        // Increment countipat at the beginning of the loop before creating a new jpt file
                         counter++;
                    }
            // if counter > 0 keep going to write jpg, the open one
            else if (counter > 0 )
            {
                fwrite( buffer, BLOCK_SIZE , 1, img );
            }







        }
        // Close the last opened file
        fclose(img);
        // Close input file
        fclose(input);
}










int  open_file(int argc, char *argv[])
{
    input = fopen(argv[1] , "rb");

    // Check that file is not empty and exist
    if(input == NULL)
    {
        printf("the files of input is empty or not exist");
        return 1;
    }
    return 0 ;
}



