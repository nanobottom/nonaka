#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void){
  char str[BUFFER_SIZE] = "";
  long x = 0;

  printf("16進数を入力:");
  fgets(str, BUFFER_SIZE, stdin);
  str[strlen(str) - 1] = '\0';

  /* データ変換処理 */
  x = strtol(str, NULL, 16);
  printf("10進数:%ld\n", x);
  return 0;
}
