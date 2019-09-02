#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

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
int main(int argc, char *argv[]){
  unsigned int num;
  if(argc != 2){
    fprintf(stderr, "Number of input arguments are differ.\n");
    exit(EXIT_SUCCESS);
  }
  
  num = strtoui(argv[1]);
  printf("%dは%s\n",num, (num % 2 == 0) ? "偶数": "奇数");
  return EXIT_SUCCESS;
}

