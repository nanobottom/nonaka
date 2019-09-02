#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

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

int main(void){
  unsigned int x, y, ret_and, ret_or, ret_xor;
  char readline[BUFFER_SIZE];

  printf("Enter unsigned int(0 - %u)>>", UINT_MAX);
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  x = strtoui(readline);
  printf("Enter unsigned int(0 - %u)>>", UINT_MAX);
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  y = strtoui(readline);

  ret_and = x & y;
  printf("%u(%#x) AND %u(%#x) = %#x\n", x, x, y, y, ret_and);
  ret_or = x | y;
  printf("%u(%#x) OR %u(%#x) = %#x\n", x, x, y, y, ret_or);
  ret_xor = x ^ y;
  printf("%u(%#x) XOR %u(%#x) = %#x\n", x, x, y, y, ret_xor);

  return EXIT_SUCCESS;
}

