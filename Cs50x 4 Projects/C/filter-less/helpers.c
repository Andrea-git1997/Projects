#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{ // I'm going to definte every raws of type
    for (int i = 0; i < height; i++)
    {

       for (int j = 0; j < width; j++)
        {
            // I'm going to calculate the avarage of rgbt
            int avarage_rgb = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            // I'm goint to change the colors of every pixels of the image
            image[i][j].rgbtBlue = avarage_rgb;
            image[i][j].rgbtGreen = avarage_rgb;
            image[i][j].rgbtRed = avarage_rgb;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{ // for every rows

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // definitions of originals colors
            int original_Red = image[i][j].rgbtRed;
            int original_Green = image[i][j].rgbtGreen;
            int original_Blue = image[i][j].rgbtBlue;

            // int sepiaRed =  round( image[i][j].rgbtBlue * 0.189 +  image[i][j].rgbtGreen * 0.769 +  image[i][j].rgbtRed * 0.393);
            int sepiaRed = round(0.393 * original_Red + 0.769 * original_Green + 0.189 * original_Blue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            // I'm going to change the GREEN COLOR
            image[i][j].rgbtRed = sepiaRed;

   // int sepiaGreen = round( image[i][j].rgbtBlue * 0.168 +  image[i][j].rgbtGreen *0.686 +  image[i][j].rgbtRed * 0.349);
   // int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 *  image[i][j].rgbtBlue);
           int sepiaGreen = round(0.349 * original_Red + 0.686 * original_Green + 0.168 * original_Blue);
            //
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            // I'm going to apply sepiaGreen
            image[i][j].rgbtGreen = sepiaGreen;

            // I'm goint to modify normals colors in sepia's one .
   // int sepiaBlue = round( image[i][j].rgbtBlue * 0.131 +  image[i][j].rgbtGreen * 0.534 +  image[i][j].rgbtRed * 0.272 ) ;
   //  int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
    int sepiaBlue = round(0.272 * original_Red + 0.534 * original_Green + 0.131 * original_Blue);
            if (sepiaBlue > 255)
            // respect the bound number of rgbt
            {
                sepiaBlue = 255;
            }

            // I'm going to apply sepiaBlue
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // for every rows
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // It's the function to reflect pixel using a temporary variable
            RGBTRIPLE temp = image[i][width - j - 1];
            image[i][width - j - 1] = image[i][j];
            image[i][j] = temp;
        }
    }
    return;
}



// Declaration for function on blur
RGBTRIPLE  manage_corners(int height, int width, RGBTRIPLE image[height][width], int i, int j,  RGBTRIPLE  copy[height][width]);
RGBTRIPLE  manage_edge(int height, int width, RGBTRIPLE image[height][width], int i, int j,  RGBTRIPLE  copy[height][width]);
RGBTRIPLE  manage_standard(int height, int width, RGBTRIPLE image[height][height], int i, int j,  RGBTRIPLE  copy[height][width]);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])

{
    // declaration of copy
    RGBTRIPLE copy[height][height];
   // Copy l'array image in copy
for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
        copy[i][j] = image[i][j];
    }
}
    // for evry pixels
    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            // I want to create a copy of image in orfer to no touch the originals pixels
            copy[height][width] = image[height][width];

                }
    }
            for (int i = 0; i < height; i++)
             {

            for (int j = 0; j < width; j++)
        {

          if (((i == 0 || j == width - 1) && (i == 0 || j == 0)) || (i == height - 1 && j == width - 1) || (i == height - 1 && j == 0))


                {
                    // Pass copy in manage corners
                    image[i][j] =  manage_corners( height,width,image,i, j,copy);
                }
                 else if (i == 0 && ( j != 0  && j != width -1) && ((i == height - 1 && ( j != 0 && j != width - 1)) ||( (i != height -1 && i != 0 ) && j == 0 )|| ((i != height -1 && i != 0 ) && j == width-1)))
                {
                    // Pass copy in manage edge
                    image[i][j] = manage_edge(height,width,image,i, j,copy);
                }
                else
                {
                    // Pass copy in manage standard
                   image[i][j] = manage_standard(height,width,image,i, j,copy);
                }

        }


             }


}



RGBTRIPLE  manage_corners(int height, int width, RGBTRIPLE image[height][width], int i, int j,  RGBTRIPLE  copy[height][width])
{
          if((i == 0 || j == 0))
          {
          // first corner on  left
          int sum_red_corner1 = copy[i][j].rgbtRed + copy[i+1][j].rgbtRed +copy[i+1][j+1].rgbtRed +copy[i][j+1].rgbtRed;
          int sum_green_corner1 = copy[i][j].rgbtGreen + copy[i+1][j].rgbtGreen +copy[i+1][j+1].rgbtGreen +copy[i][j+1].rgbtGreen;
          int sum_blue_corner1 = copy[i][j].rgbtBlue + copy[i+1][j].rgbtBlue +copy[i+1][j+1].rgbtBlue +copy[i][j+1].rgbtBlue;

          // finals results
          int red_corner1 = round(sum_red_corner1/ 4.0);
          int green_corner1 = round(sum_green_corner1/ 4.0);
          int blue_corner1 = round(sum_blue_corner1/ 4.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_corner1;
          result_corner1.rgbtRed = red_corner1;
         result_corner1.rgbtGreen = green_corner1;
         result_corner1.rgbtBlue = blue_corner1;
        return result_corner1;

          }
          // second corner handle
          if((i == 0 || j == width -1))
          {
             // first corner on  left
          int sum_red_corner2 = copy[i][j-1].rgbtRed + copy[i+1][j-1].rgbtRed +copy[i+1][j].rgbtRed +copy[i][j].rgbtRed;
          int sum_green_corner2 = copy[i][j-1].rgbtGreen + copy[i+1][j-1].rgbtGreen +copy[i+1][j].rgbtGreen +copy[i][j].rgbtGreen;
          int sum_blue_corner2 = copy[i][j-1].rgbtBlue + copy[i+1][j-1].rgbtBlue +copy[i+1][j].rgbtBlue +copy[i][j].rgbtBlue;

          // finals results
          int red_corner2 = round(sum_red_corner2/ 4.0);
          int green_corner2 = round(sum_green_corner2/ 4.0);
          int blue_corner2 = round(sum_blue_corner2/ 4.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_corner2;
        result_corner2.rgbtRed = red_corner2;
        result_corner2.rgbtGreen = green_corner2;
        result_corner2.rgbtBlue = blue_corner2;
          return result_corner2;
          }
          // third corner
          if((i == height-1 || j == 0))
          {
             // first corner on  left
          int sum_red_corner3 = copy[i][j].rgbtRed + copy[i-1][j].rgbtRed +copy[i-1][j+1].rgbtRed +copy[i][j+1].rgbtRed;
          int sum_green_corner3 = copy[i][j].rgbtGreen + copy[i-1][j].rgbtGreen +copy[i-1][j+1].rgbtGreen +copy[i][j+1].rgbtGreen;
          int sum_blue_corner3 = copy[i][j].rgbtBlue + copy[i-1][j].rgbtBlue +copy[i-1][j+1].rgbtBlue +copy[i][j+1].rgbtBlue;

          // finals results
          int red_corner3 = round(sum_red_corner3/ 4.0);
          int green_corner3 = round(sum_green_corner3/ 4.0);
          int blue_corner3 = round(sum_blue_corner3/ 4.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_corner3;
        result_corner3.rgbtRed = red_corner3;
        result_corner3.rgbtGreen = green_corner3;
        result_corner3.rgbtBlue = blue_corner3;
          return result_corner3;
          }
           // four corner
          if((i == height-1 || j == width-1))
          {
             // first corner on  left
          int sum_red_corner4 = copy[i][j].rgbtRed + copy[i][j-1].rgbtRed +copy[i+1][j-1].rgbtRed +copy[i-1][j].rgbtRed;
          int sum_green_corner4 = copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen +copy[i+1][j-1].rgbtGreen +copy[i-1][j].rgbtGreen;
          int sum_blue_corner4 = copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue +copy[i+1][j-1].rgbtBlue +copy[i-1][j].rgbtBlue;

          // finals results
          int red_corner4 = round(sum_red_corner4/ 4.0);
          int green_corner4 = round(sum_green_corner4/ 4.0);
          int blue_corner4 = round(sum_blue_corner4/ 4.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_corner4;
        result_corner4.rgbtRed = red_corner4;
        result_corner4.rgbtGreen = green_corner4;
        result_corner4.rgbtBlue = blue_corner4;
          return result_corner4;


    }
    return copy[i][j];
}

RGBTRIPLE  manage_edge(int height, int width, RGBTRIPLE image[height][width], int i, int j,  RGBTRIPLE  copy[height][width])
{
      // the edge up 1
      if(i == 0 && ( j != 0  && j != width -1))
      {
        // first corner on  left
          int sum_red_edge1 = copy[i][j].rgbtRed + copy[i][j-1].rgbtRed +copy[i+1][j-1].rgbtRed +copy[i+1][j].rgbtRed+copy[i+1][j+1].rgbtRed + copy[i][j+1].rgbtRed;
          int sum_green_edge1 = copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen +copy[i+1][j-1].rgbtGreen +copy[i+1][j].rgbtGreen+copy[i+1][j+1].rgbtGreen + copy[i][j+1].rgbtGreen;
          int sum_blue_edge1 = copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue +copy[i+1][j-1].rgbtBlue +copy[i+1][j].rgbtBlue+copy[i+1][j+1].rgbtBlue + copy[i][j+1].rgbtBlue;

          // finals results
          int red_edge1 = round(sum_red_edge1/ 6.0);
          int green_edge1 = round(sum_green_edge1/ 6.0);
          int blue_edge1 = round(sum_blue_edge1/ 6.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_edge1;
        result_edge1.rgbtRed = red_edge1;
        result_edge1.rgbtGreen = green_edge1;
        result_edge1.rgbtBlue = blue_edge1;
          return result_edge1;
      }
      if(i == height - 1 && ( j != 0 && j != width - 1))
      {
          // second edge down
          int sum_red_edge2 = copy[i][j].rgbtRed + copy[i][j-1].rgbtRed +copy[i-1][j-1].rgbtRed +copy[i-1][j].rgbtRed+copy[i-1][j+1].rgbtRed + copy[i][j+1].rgbtRed;
          int sum_green_edge2 = copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen +copy[i-1][j-1].rgbtGreen +copy[i-1][j].rgbtGreen+copy[i-1][j+1].rgbtGreen + copy[i][j+1].rgbtGreen;
          int sum_blue_edge2 = copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue +copy[i-1][j-1].rgbtBlue +copy[i-1][j].rgbtBlue+copy[i-1][j+1].rgbtBlue + copy[i][j+1].rgbtBlue;

          // finals results
          int red_edge2 = round(sum_red_edge2/ 6.0);
          int green_edge2 = round(sum_green_edge2/ 6.0);
          int blue_edge2 = round(sum_blue_edge2/ 6.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_edge2;
        result_edge2.rgbtRed = red_edge2;
        result_edge2.rgbtGreen = green_edge2;
        result_edge2.rgbtBlue = blue_edge2;
          return result_edge2;
      }

      if((i != height -1 && i != 0 ) && j == 0)
      {
        // third edge left
          int sum_red_edge3 = copy[i][j].rgbtRed + copy[i-1][j].rgbtRed +copy[i-1][j-1].rgbtRed +copy[i][j+1].rgbtRed+copy[i+1][j+1].rgbtRed + copy[i+1][j].rgbtRed;
          int sum_green_edge3 = copy[i][j].rgbtGreen + copy[i-1][j].rgbtGreen +copy[i-1][j-1].rgbtGreen +copy[i][j+1].rgbtGreen+copy[i+1][j+1].rgbtGreen + copy[i+1][j].rgbtGreen;
          int sum_blue_edge3 = copy[i][j].rgbtBlue + copy[i-1][j].rgbtBlue +copy[i-1][j-1].rgbtBlue +copy[i][j+1].rgbtBlue+copy[i+1][j+1].rgbtBlue + copy[i+1][j].rgbtBlue;

          // finals results
          int red_edge3 = round(sum_red_edge3/ 6.0);
          int green_edge3 = round(sum_green_edge3/ 6.0);
          int blue_edge3 = round(sum_blue_edge3/ 6.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_edge3;
        result_edge3.rgbtRed = red_edge3;
        result_edge3.rgbtGreen = green_edge3;
        result_edge3.rgbtBlue = blue_edge3;
          return result_edge3;
      }
      if((i != height -1 && i != 0 ) && j == 0)
      {
        // four edge left
          int sum_red_edge4 = copy[i][j].rgbtRed + copy[i-1][j].rgbtRed +copy[i-1][j-1].rgbtRed +copy[i][j-1].rgbtRed+copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed;
          int sum_green_edge4 = copy[i][j].rgbtGreen + copy[i-1][j].rgbtGreen +copy[i-1][j-1].rgbtGreen +copy[i][j-1].rgbtGreen+copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen;
          int sum_blue_edge4 = copy[i][j].rgbtBlue + copy[i-1][j].rgbtBlue +copy[i-1][j-1].rgbtBlue +copy[i][j-1].rgbtBlue+copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue;

          // finals results
          int red_edge4 = round(sum_red_edge4/ 6.0);
          int green_edge4 = round(sum_green_edge4/ 6.0);
          int blue_edge4 = round(sum_blue_edge4/ 6.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_edge4;
        result_edge4.rgbtRed = red_edge4;
        result_edge4.rgbtGreen = green_edge4;
        result_edge4.rgbtBlue = blue_edge4;
          return result_edge4;
      }
      // Return the copy pixels
    return copy[i][j];
}

RGBTRIPLE  manage_standard(int height, int width, RGBTRIPLE image[height][width], int i, int j,  RGBTRIPLE  copy[height][width])
{
  // four edge left

          int sum_red_standard = copy[i][j].rgbtRed + copy[i][j-1].rgbtRed + copy[i-1][j-1].rgbtRed + copy[i][j-1].rgbtRed + copy[i-1][j+1].rgbtRed + copy[i][j+1].rgbtRed + copy[i+1][j-1].rgbtRed + copy[i+1][j].rgbtRed + copy[i+1][j+1].rgbtRed;
          int sum_green_standard = copy[i][j].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i-1][j-1].rgbtGreen + copy[i][j-1].rgbtGreen + copy[i-1][j+1].rgbtGreen + copy[i][j+1].rgbtGreen + copy[i+1][j-1].rgbtGreen + copy[i+1][j].rgbtGreen + copy[i+1][j+1].rgbtGreen;
          int sum_blue_standard = copy[i][j].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i-1][j-1].rgbtBlue + copy[i][j-1].rgbtBlue + copy[i-1][j+1].rgbtBlue + copy[i][j+1].rgbtBlue + copy[i+1][j-1].rgbtBlue + copy[i+1][j].rgbtBlue + copy[i+1][j+1].rgbtBlue;


          // finals results
          int red_standard = round(sum_red_standard/ 9.0);
          int green_standard = round(sum_green_standard/ 9.0);
          int blue_standard = round(sum_blue_standard/ 9.0);

         // Crea e restituisci un nuovo RGBTRIPLE con i risultati
         RGBTRIPLE result_standard;
        result_standard.rgbtRed = red_standard;
        result_standard.rgbtGreen = green_standard;
        result_standard.rgbtBlue = blue_standard;
          return result_standard;
}






