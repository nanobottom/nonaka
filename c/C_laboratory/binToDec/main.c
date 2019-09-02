#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define BUFFER_SIZE 256

unsigned int strtoui(char *str);
int isbinary(char *str);

int main(int argc, char *argv[]){

  int dec;
  /* check number of input strings */
  if(argc != 2){
    fprintf(stderr, "Number of input strings are differ.\n");
    exit(EXIT_FAILURE);
  }
  /* check input strings is binary. */
  if(isbinary(argv[1]) == 0){
    fprintf(stderr, "Input strings are NOT binary.\n");
    exit(EXIT_FAILURE);
  } 

  /* transfer binary to decimal */
  dec = strtoui(argv[1]);
  printf("%d\n", dec);

  return EXIT_SUCCESS;
}

/* この関数は入力した文字列をunsigned int型の
 * 数値に変換する関数である*/
unsigned int strtoui(char *str){
  long result_l;
  unsigned int result;
  char *endptr;
  int base = 2;

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

/* この関数は入力した文字列が2進数であるか確認する関数である */
int isbinary(char *str){
  int result = 0;
  for(int i = 0; i < strlen(str); i++){
    if(str[i] == '0' || str[i] == '1'){
      result++;
    }else{
      result = 0;
      break;
    }
  }
  return result;
}  

