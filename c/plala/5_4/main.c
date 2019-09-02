#include <stdio.h>


int main(void){
  char str[80];
  printf("文字列の入力>>");
  fgets(str, 80, stdin);
  printf("入力文字列 = %s\n", str);

  return 0;
}
