#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int strtoi(char *str);

int main(int argc, char *argv[]){
  int sum;
  
  if(argc != 3){
    puts("Invalid argment is entered.");
    exit(EXIT_FAILURE);
  }

  
  sum = strtoi(argv[1]) + strtoi(argv[2]);
  printf("Sum = %d\n", sum);

  return EXIT_SUCCESS;
}

int strtoi(char *str){
  long result_l;
  int result;
  char *endptr;
  result_l = strtol(str, &endptr, 0);
  /* in case of including other strings otherwise number */
  if(str == endptr){
    fprintf(stderr, "Cannot invert to number.");
    exit(EXIT_FAILURE);
  }
  /* in case of entering number over range of int type */
  if(result_l > INT_MAX || result_l < INT_MIN){
    fprintf(stderr, "Cannnot invert to int type.");
    exit(EXIT_FAILURE);
  }

  result = (int)result_l;

  return result;
}



