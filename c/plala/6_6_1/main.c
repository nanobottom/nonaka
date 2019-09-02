#include <stdio.h>
#include <stdlib.h>

int main(void){
  int result[51], a, b, rest;
  
  printf("整数値を2つ入力してください>>");
  scanf("%d %d", &a, &b);
  if(b == 0){
    exit(EXIT_FAILURE);
  }
  result[0] = a / b;
  rest = a % b;
  for(int i = 1; i < 51; i++){
    a = rest * 10;
    result[i] = a / b;
    rest = a % b;
    if(rest == 0){
      break;
    }
  }
  /* Output result of calculation */
  for(int i = 0; i < 51; i++){
    printf("result[%d] = %d\n", i, result[i]);
  }
}

