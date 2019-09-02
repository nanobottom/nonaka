#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <ctype.h>

#define BUFFER_SIZE 256
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
