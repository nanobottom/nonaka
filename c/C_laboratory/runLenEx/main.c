#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define RUN 0xFF
#define BUFFER_SIZE 256

void compress(void);


int main(void)
{
  compress();
}


void compress(void)
{
  char decomp_file[BUFFER_SIZE] = "";
  char comp_file[BUFFER_SIZE] = "";
  FILE *fp_decomp = NULL, *fp_comp = NULL;
  int data = 0, prev_data = 0, length = 0;

  printf("Decompress filename>>");
  gets(decomp_file);
  printf("Compress filename>>");
  gets(comp_file);

  if((fp_decomp = fopen(decomp_file, "rb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", decomp_file);
    exit(EXIT_FAILURE);
  }

  if((fp_comp = fopen(comp_file, "wb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", comp_file);
    exit(EXIT_FAILURE);
  }
  
  //Compress data used to run length method.
  length = 0;
  while((data = fgetc(fp_decomp)) != EOF)
  {
    if(length == 0)
    {
      //Start counting new data.
      prev_data = data;
      length = 1;
    }
    else
    {
      if(prev_data == data)
      {
        //In case of continuous data.
        length++;

        //When strings are continuous of 255, write it.
        if(length == 255)
        {
          fputc(RUN, fp_comp);
          fputc(prev_data, fp_comp);
          fputc(length, fp_comp);
          length = 0;
        }
      }
      else
      {
        if(length > 3 || prev_data == RUN)
        {
          fputc(RUN, fp_comp);
          fputc(prev_data, fp_comp);
          fputc(length, fp_comp);
        }
        else
        {
          while(length > 0)
          {
            fputc(prev_data, fp_comp);
            length++;
          }
        }
        prev_data = data;
        length = 1;
      }
    }
  }

  if(length != 0)
  {
    if(length > 3 || prev_data == RUN)
    {
      fputc(RUN, fp_comp);
      fputc(prev_data, fp_comp);
      fputc(length, fp_comp);
    }
    else
    {
      while(length > 0)
      {
        fputc(prev_data, fp_comp);
        length--;
      }
    }
  }

  if(fclose(fp_comp) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", comp_file);
    exit(EXIT_FAILURE);
  }
  if(fclose(fp_decomp) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", decomp_file);
    exit(EXIT_FAILURE);
  }
}
