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
  char data[3][9] = {
    "1110000",
    "0110010",
    "1010101"
  };
  char bcc[9];
  int cnt = 0;
  //Give vertical parity.
  for(int i = 0; i < 3; i++)
  {
    cnt = count_one(data[i]);
    if(cnt % 2 == 0)
    {
      data[i][7] = '0';
    }
    else
    {
      data[i][7] = '1';
    }
    data[i][8] = '\0';
    printf("%s...vertical parity\n", data[i]);
  }

  //Give horizontal parity.
  for(int i = 0; i < 8; i++)
  {
    cnt = 0;
    for(int j = 0; j < 3; j++)
    {
      if(data[j][i] == '1')
      {
        cnt++;
      }
    }
    if(cnt % 2 == 0)
    {
      bcc[i] = '0';
    }
    else
    {
      bcc[i] = '1';
    }
  }
  bcc[8] = '\0';
  printf("%s...horizontal parity\n", bcc);
}


