#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void)
{
  char read_line[BUFFER_SIZE] = "";
  char upper[BUFFER_SIZE] = "";
  char lower[BUFFER_SIZE] = "";
  int pos = 0;

  printf("Input character>>");
  fgets(read_line, BUFFER_SIZE, stdin);
  read_line[strlen(read_line) - 1] = '\0';

  while(read_line[pos] != '\0')
  {
    if(read_line[pos] >= 'A' && read_line[pos] <= 'Z')
    {
      upper[pos] = read_line[pos];
      //Transfer upper to lower.
      lower[pos] = read_line[pos] + 0x20;
    }
    else if (read_line[pos] >= 'a' && read_line[pos] <= 'z')
    {
      //Transfer lower to upper
      upper[pos] = read_line[pos] - 0x20;
      lower[pos] = read_line[pos];
    }
    else
    {
      upper[pos] = read_line[pos];
      lower[pos] = read_line[pos];
    }
    pos++;
  }
  upper[pos] = '\0';
  lower[pos] = '\0';

  printf("Upper: %s\n", upper);
  printf("Lower: %s\n" ,lower);
}

