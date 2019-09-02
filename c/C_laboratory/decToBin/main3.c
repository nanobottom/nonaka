#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 256

int isdigits(char *str);
void dec_to_bin(char *s_dec, char *bin);
void reverse(char *msg, int maxsize);

int main(void){
  int dec;
  char bin[BUFFER_SIZE] = "";
  char readline[BUFFER_SIZE] = "";

  /* 10進数を入力する*/
  printf("10進数を入力してください>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  
  /* 入力した文字列が数値かどうかチェックする */
  if(isdigits(readline)){
  }else{
    printf("入力した文字列は数値ではない。\n");
    return EXIT_FAILURE;
  }

  /* 10進数を2進数へ変換する*/
  dec_to_bin(readline, bin);
  printf("2進数:%s\n", bin);
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

/* 10進数を2進数に変換する */
void dec_to_bin(char *s_dec, char *bin){
  char bit[BUFFER_SIZE] = "";
  int dec = 0;
  int remainder = 0;/* 余り */
  
  dec = atoi(s_dec);
  /* 10進数を2進数に変換して変数に格納する */
  while(dec > 0){
    remainder = dec % 2;
    strncat(bin, remainder ? "1": "0", BUFFER_SIZE);
    dec /= 2;
  }
  reverse(bin, strlen(bin));
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
  
