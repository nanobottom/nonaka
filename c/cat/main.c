#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <ctype.h>

#define BUFFER_SIZE 256

int main(int argc, char* argv[])
{
  FILE *fp = NULL;
  char line[BUFFER_SIZE] = "";
  int option = 0, line_num = 1, c = 0;

  //Read file.
  //Write each 1 line.
  if((fp = fopen(argv[1], "r")) == NULL && ((fp = fopen(argv[2], "r")) == NULL))
  {
    fprintf(stderr, "Failed to open file.\n");
    exit(EXIT_FAILURE);
  }
  
  while((option = getopt(argc, argv, "nbET")) != EOF)
  {
    switch(option){
    case 'n':
      while(fgets(line, BUFFER_SIZE, fp) != NULL)
      {
        printf("%3d\t", line_num);
        printf(line);
        line_num++;
      }
      break;
    case 'b':
      while(fgets(line, BUFFER_SIZE, fp) != NULL)
      {
        if(isspace((int)line[0]) != 0 && strlen(line) == 1)
        {
          printf("\t");
          printf(line);
        }
        else
        {
          printf("%3d\t", line_num);
          printf(line);
          line_num++;
        }
      }
      break;

    case 'E':
      while(fgets(line, BUFFER_SIZE, fp) != NULL)
      {
        line[strlen(line) - 1] = '\0';
        printf("%s$\n",line);

      }
      break;
    
    case 'T':
      while((c = fgetc(fp)) != EOF)
      {
        if(c == '\t')
        {
          printf("^I");
        }
        else
        {
          putchar(c);
        }
      }
      break;
      
    default:
      while(fgets(line, BUFFER_SIZE, fp) != NULL)
      {
        printf(line);
      }
      break;
    }
  }

  if(fclose(fp) == EOF)
  {
    fprintf(stderr, "Failed to close file.\n");
    exit(EXIT_FAILURE);
  }
}
