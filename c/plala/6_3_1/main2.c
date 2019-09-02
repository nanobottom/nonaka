#include <stdio.h>
#include <stdlib.h>

int main(void){
  int wa = 0, data;
  printf("整数値入力>>");
  scanf("%d", &data);

  while(data != 0){
    wa += data;
    printf("wa = %d\n", wa);
    printf("整数値入力>>");
    scanf("%d", &data);
  }

  return EXIT_SUCCESS;
}
