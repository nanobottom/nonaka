#include <stdio.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))
int main(void){

  char str[] = "SKY";

  for (int i = 0; i < ARRAY_SIZE(str); i++){
    printf("str[%d] = %d %x %c\n", i, str[i], str[i], str[i]);
  }
  printf("文字列 = %s\n", str);

  return 0;
}
