#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))
#define BUFFER_SIZE 256

int main(void){
  char str[] = "AbcDefGHijk1234lmNOP";
  char str2[BUFFER_SIZE] = "";

  for(int i = 0; i < ARRAY_SIZE(str); i++){

    str2[i] = toupper(str[i]);
  }
  printf("変換した文字列= %s\n", str2);

  return EXIT_SUCCESS;
}

