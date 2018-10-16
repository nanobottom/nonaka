#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int count_one(char *data)
{
  char c[BUFFER_SIZE] = "";
  int cnt = 0;

  if(strlen(data) != 7)
  {
    fprintf(stderr, "Input character's length is not 7.\n");
    exit(EXIT_FAILURE);
  }

  while(*data != '\0')
  {
    snprintf(c, BUFFER_SIZE, "%c", *data);
    if(c[0] != '1' && c[0] != '0')
    {
      fprintf(stderr, "Input character is not '1' neither '0'.\n");
      exit(EXIT_FAILURE);
    }
    if(c[0] == '1')
    {
      cnt++;
    }
    data++;
  }
  return cnt;
}

int main(void)
{
  char readline[BUFFER_SIZE] = "";
  int cnt_one = 0;

  printf("Input binary(7digits)>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  cnt_one = count_one(readline);
  if(cnt_one % 2 == 0)
  {
    printf("Counting one from input character is even number(%d),\nso this is correct data.\n",cnt_one);
    printf("Result:%s0\n", readline);
  }
  else
  {
    printf("Counting one from input character is not even number(%d),\nso this is wrong data.\n",cnt_one);
    printf("Result:%s1\n", readline);
  }
}
