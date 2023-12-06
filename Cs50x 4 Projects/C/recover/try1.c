#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;
const int MAX_FILENAME_LENGTH = 100 ;

int main(int argc, char *argv[])
{
    // I'm going to check the number of input by user
    if (argc != 2)
{
    printf("Usage: %s filename\n", argv[0]);
    return 1;
}

    //OPEN FILE . "r" is fo read
    FILE *input = fopen(argv[1], "rb");
    //check if file are going to open
        if (input == NULL)
     {
         printf("Could not open file %s\n", argv[1]);
            return 1;
        }

        // Calculation of the numbers of bytes of input files
        // I'm going to move the *char at the end of the file of input
         fseek(input, 0 , SEEK_END);


        //I'm going to calculate the total numbers of bytes of this card.raw file using the *char up
        long lenght = ftell(input);
        // I'm define the lenght of this input file using bytes

        // Check if input is empty
        if(lenght == 0)
        {
            fclose(input);
            printf("Raw of input is unfortunetly empty\n");
            return 1;
        }


        //Definition of 4 bytes that are the beggining of recover chuncks
        uint8_t buffer[BLOCK_SIZE] ;
        //Definition of jpg count
         int countjpg =  0 ;
        // add a contator of bytes
        // declaration of img befor ciclo for
        FILE *img = NULL;
            // I'm going to move the *char at the beggining
          fseek(input, 0, SEEK_SET);
            // I want to read all card.raw in chunck of 4 bytes
            for(int count_bytes = 0 ; count_bytes < lenght ; count_bytes += BLOCK_SIZE)
            // read the first 4 bytes
                fread(buffer, 1, BLOCK_SIZE, input);
            {
                   if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
                    {
                        // Increment countipat at the beginning of the loop before creating a new jpt file
                         countjpg++;
                    }
                // read the first 4 bytes
                fread(buffer, 1, BLOCK_SIZE, input);
                // I want to check the beggining of a chunck of files to nd store in jpeg.x
                if ((buffer[0] == 0xff) && (buffer[1] == 0xd8 )&& (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
                {

                          char filename[MAX_FILENAME_LENGTH];
                    // I want to open a jpagfile and store this chuncks of bites
                        sprintf( filename , "%03i.jpg" , countjpg);
                        // declaration of file name and definition of appropriate size of that


                      img = fopen(filename, "wb");
                       if (img == NULL)
                           {
                              printf("Could not open file jpg");
                             return 2;
                            }
                            // write bytes till the end of files
                            fwrite( buffer,1, BLOCK_SIZE, img );

                            // Till I don't find the stater points of new char
                            while (fread(buffer, 1, BLOCK_SIZE, input) == BLOCK_SIZE)
                            {
                           if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)

                                {
                                    // I want to check before closing jpg that I will have others bytes to store
                                     if(img != NULL)
                                     {
                                      // I want to close curret jpg file
                                     fclose (img);
                                     break;
                                     }
                                }

                                // Keep going to write actual jpg file that we opened
                                 fwrite( buffer, sizeof(uint8_t), BLOCK_SIZE, img );
                            }


                }
            }

                                     // After closing a jpg file add count++

                                     fclose (input);
                                     return 0;
}




#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BLOCK_SIZE = 512;             // Dimensione del blocco in byte
const int MAX_FILENAME_LENGTH = 100;    // Lunghezza massima del nome del file

typedef uint8_t BYTE;
FILE *input;                            // Puntatore al file di input

// Dichiarazione della funzione per aprire il file
int open_file(int argc, char *argv[]);

int main(int argc, char *argv[])
{
    // Controlla che ci siano esattamente due argomenti nella riga di comando
    if (argc != 2)
    {
        printf("Usage: %s [name of input]\n", argv[0]);
        return 1;  // Restituisci 1 in caso di errore nei parametri della riga di comando
    }

    // Apre il file di input
    if (open_file(argc, argv) != 0)
    {
        // Restituisci 1 in caso di errore nell'apertura del file
        return 1;
    }

    // Definizione della dimensione dei blocchi
    uint8_t buffer[BLOCK_SIZE];
    int counter = 0;
    FILE *img;
    // Definizione dell'array in cui verranno definiti i nomi dei file jpg
    char filename[MAX_FILENAME_LENGTH];

    // Lettura del file a blocchi di 512 byte
    while (fread(buffer, BLOCK_SIZE, 1, input) == 1)
    {
        // Controlla se il blocco inizia con l'header di un nuovo file JPEG
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
        {
            // Se non è il primo JPEG creato, chiudi il file precedente
            if (counter != 0)
            {
                fclose(img);
            }

            // Crea un nuovo nome di file JPEG
            sprintf(filename, "%03i.jpg", counter);

            // Apri un nuovo file JPEG in modalità scrittura binaria
            img = fopen(filename, "wb");
            if (img == NULL)
            {
                printf("Could not open file %s\n", filename);
                return 2;  // Restituisci 2 in caso di errore nell'apertura del file
            }

            // Scrivi il blocco nel nuovo file JPEG
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }

        // Incrementa il contatore se il blocco inizia con l'header di un nuovo file JPEG
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && (buffer[3] & 0xf0) == 0xe0)
        {
            counter++;
        }

        // Se il contatore è maggiore di 0, scrivi il blocco nel file JPEG corrente
        else if (counter > 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }
    }

    // Chiudi l'ultimo file JPEG aperto
    fclose(img);
    // Chiudi il file di input
    fclose(input);

    // Restituisci 0 per indicare il successo
    return 0;
}

// Funzione per aprire il file di input
int open_file(int argc, char *argv[])
{
    input = fopen(argv[1], "rb");

    // Verifica che il file non sia vuoto o non esista
    if (input == NULL)
    {
        printf("The input file is empty or does not exist.\n");
        return 1;  // Restituisci 1 in caso di errore nell'apertura del file
    }

    // Restituisci 0 per indicare il successo
    return 0;
}
