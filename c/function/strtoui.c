#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
/* この関数は入力した文字列をunsigned int型の
 * 数値に変換する関数である*/
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
