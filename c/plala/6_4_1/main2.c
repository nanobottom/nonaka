#include <stdio.h>
#include <stdlib.h>

int main(void){
  char str1[256], str2[256];
  int i = 0;
  printf("文字列入力>>");
  scanf("%s", str1);

  do{
    str2[i] = str1[i];
  }while (str1[i++] != '\0');

  printf("str2 = %s\n", str2);

  return EXIT_SUCCESS;

}



