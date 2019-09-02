#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void){
  char a[BUFFER_SIZE], b[BUFFER_SIZE], c[BUFFER_SIZE];

  if(strlcpy(a, "abcde", BUFFER_SIZE) >= BUFFER_SIZE){
    puts("配列変数aは不完全な文字列を指しています");
    exit(EXIT_FAILURE);
  }

  if(strlcpy(b, "vwxyz", BUFFER_SIZE) >= BUFFER_SIZE){
    puts("配列変数bは不完全な文字列を指しています");
    exit(EXIT_FAILURE);
  }
  
  printf("文字列a = %s\n", a);
  printf("文字列b = %s\n", b);

  if(strcmp(a, b) == 0){
    puts("文字列a、bは等しい");
  }else if(strcmp(a, b) > 0){
    puts("文字列aはbより大");
  }else{
    puts("文字列aはbより小");
  }
  
  if(strlen(a) + strlen(b) < BUFFER_SIZE){
    snprintf(c, BUFFER_SIZE, "%s%s", a, b);
  }else{
    puts("余計な長さの文字列を連結しようとしています");
    exit(EXIT_FAILURE);
  }
  printf("文字列c = %s\n", c);
  printf("文字列cの長さ= %d\n", (int)strlen(c));

  return EXIT_SUCCESS;
}
