#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define BUFFER_SIZE 256
unsigned int strtoui(char *str){
  long result_l;
  unsigned int result;
  char *endptr;
  int base = 0;

  result_l = strtol(str, &endptr, base);
  if(str == endptr){
    fprintf(stderr, "Entered strings are NOT number.\n");
    exit(EXIT_FAILURE);
  }

  if(result_l > UINT_MAX || result_l < 0){
    fprintf(stderr, "Cannot invert number of unsigned int type.\n");
    exit(EXIT_FAILURE);
  }
  result = (unsigned int)result_l;
  return result;
}

void display_binary(unsigned char num, int digit)
{
  int binary[32];
  for(int i = 0; i < digit; i++)
  {
    binary[i] = num % 2;
    num /= 2;
  }
  for(int i = digit - 1; i >= 0; i--)
  {
    putchar(binary[i] ? '1' : '0');
  }
  printf("\n");
}

int main(void){
  unsigned int a;
  char readline[BUFFER_SIZE];

  printf("Enter integer value range of 0 - %u (finish: Ctrl + D)\n", UINT_MAX);
  while(fgets(readline, BUFFER_SIZE, stdin) != NULL){
    readline[strlen(readline) - 1] = '\0';
    a = strtoui(readline);
    display_binary(a, sizeof(a) * CHAR_BIT);
  }

  return EXIT_SUCCESS;
}
