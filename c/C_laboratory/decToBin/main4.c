#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 256

unsigned int strtoui(char *str);
int isdigits(char *str);
void reverse(char *msg, int maxsize);
void dec_to_bin(char *s_dec, char *bin);

int main(int argc, char *argv[]){
  char bin[BUFFER_SIZE] = "";
  
  /* if number of input value is differ. */
  if(argc != 2){
    fprintf(stderr, "Failed to enter number of input value.\n");
    exit(EXIT_FAILURE);
  }

  /* check input strings is value */
  if(isdigits(argv[1])){
  }else{
    fprintf(stderr, "Input strings is NOT value.\n");
    exit(EXIT_FAILURE);
  }

  /* transfer strings to value(unsigned int) */
  dec_to_bin(argv[1], bin);
  printf("%s\n", bin);

  return EXIT_SUCCESS;
}

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

/* 入力した文字列が数値のみで構成されているか確認する*/  
int isdigits(char *str){
  int result = 0;
  for(int i = 0; i < strlen(str); i++){
    if(isdigit(str[i])){
      result++;
    }else{
      result = 0;
      break;
    }
  }
  return result;
}

/* 文字列を反転する */
void reverse(char *msg, int maxsize){
  char tmp;

  for(int i = 0; i < maxsize / 2; i++){
    tmp = msg[i];
    msg[i] = msg[maxsize - 1 - i];
    msg[maxsize - 1 - i] = tmp;
  }
}

/* 10進数を2進数に変換する */
void dec_to_bin(char *s_dec, char *bin){
  char bit[BUFFER_SIZE] = "";
  unsigned int dec = 0;
  int remainder = 0;/* 余り */
  
  dec = strtoui(s_dec);
  /* 10進数を2進数に変換して変数に格納する */
  while(dec > 0){
    remainder = dec % 2;
    strncat(bin, remainder ? "1": "0", BUFFER_SIZE);
    dec /= 2;
  }
  reverse(bin, strlen(bin));
}
