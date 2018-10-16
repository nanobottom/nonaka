#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int mod10_weight3(char *str)
{
  int weight = 0, sum = 0, digit = 1;
  char c[BUFFER_SIZE] = "";

  if(strlen(str) != 12)
  {
    fprintf(stderr, "Input strings is not 12 digits.\n");
    exit(EXIT_FAILURE);
  }
  while(*str != '\0')
  {
    if(digit % 2 == 1)
    {
      weight = 3;
    }
    else
    {
      weight = 1;
    }
    snprintf(c, BUFFER_SIZE, "%c", *str);
    sum += atoi(c) * weight;
    str++;
    digit++;
  }
  return 10 - (sum % 10);
}

int main(void)
{
  char readline[BUFFER_SIZE] = "";
  int check_digit = 0;

  printf("Input number(12digits)>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  check_digit = mod10_weight3(readline);
  printf("check digit(modulus 10/weight 3) = %d\n", check_digit);
}
