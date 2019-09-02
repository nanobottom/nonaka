#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
/* 文字列を反転する */
void reverse_msg(char *msg, int maxsize){
  char tmp;

  for(int i = 0; i < maxsize / 2; i++){
    tmp = msg[i];
    msg[i] = msg[maxsize - 1 - i];
    msg[maxsize - 1 - i] = tmp;
  }
}
