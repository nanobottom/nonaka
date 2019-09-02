#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <limits.h>

#define BUFFER_SIZE 256

int isdigits(char str[]);
int strtoi(char str[]);
void reverse(char *msg, int maxsize);

int main(int argc, char *argv[]){
  
  int dec, shou, amari, pos = 0;
  char bin[BUFFER_SIZE];
  /* 入力データの個数が1個であるか確認する */
  if(argc != 2){
    fprintf(stderr, "Number of input value is NOT one.\n");
    exit(EXIT_FAILURE);
  }
  
  /* 入力データが数字だけで構成されているか確認する */
  if(isdigits(argv[1]) == 0){
    fprintf(stderr, "Input strings are NOT number.\n");
    exit(EXIT_FAILURE);
  }

  /* 10進数を2進数に変換する */
  printf("%d\n", strtoi(argv[1]));

  dec = strtoi(argv[1]);

  while(shou != 0){
    shou = dec / 2;
    amari = dec % 2;
    bin[pos] = amari ? '1': '0';
    printf("shou = %d, amari = %d\n", shou, amari);
    dec = shou;
    pos++;
  }
  bin[pos] = '\0';
  reverse(bin, strlen(bin));
  printf("%s\n", bin);

  return EXIT_SUCCESS;
}
  

int isdigits(char str[]){
  int count = 0;
  for (int i = 0; i < strlen(str); i++){
    if(isdigit(str[i]) == 0){
      count = 0;
      break;
    }else{
      count += 1;
    }
  }
  return count;
}

int strtoi(char str[]){
  char *endptr;
  long result_l;
  int result;

  result_l = strtol(str, &endptr, 10);
  
  /* 入力引数が数値がどうか確認する */
  if(str == endptr){
    fprintf(stderr, "Cannot convert to number.\n");
    exit(EXIT_FAILURE);
  }

  /* 入力引数がint型の範囲かどうか確認する */
  if(result_l > INT_MAX || result_l < INT_MIN){
    fprintf(stderr, "Cannot convert to int type.\n");
    exit(EXIT_FAILURE);
  }

  result = (int)result_l;

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
