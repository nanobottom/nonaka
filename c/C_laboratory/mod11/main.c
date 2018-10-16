#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int mod11(char *str)
{
  int weight = 10, sum = 0;
  char c[BUFFER_SIZE] = "";

  if(strlen(str) != 9)
  {
    fprintf(stderr, "Input strings is not 9 digits.\n");
    exit(EXIT_FAILURE);
  }
  while(*str != '\0')
  {
    snprintf(c, BUFFER_SIZE, "%c", *str);
    sum += atoi(c) * weight;
    weight--;
    str++;
  }
  return 11 - (sum % 11);
}

int main(void)
{
  char readline[BUFFER_SIZE] = "";
  int check_digit = 0;

  printf("Input number(9digits)>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  check_digit = mod11(readline);
  printf("check digit(modulus 11) = %d\n", check_digit);
}
