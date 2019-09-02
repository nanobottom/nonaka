#include <stdio.h>
#include <stdlib.h>

void keisan1(int x, int y, int *wa, int *sa, int *seki, int *shou);
int main(void){

  int x, y, wa, sa, seki, shou;
  puts("２つの数値を入力>>");
  scanf("%d %d", &x, &y);
  
  keisan1(x, y, &wa, &sa, &seki, &shou);
  printf("和= %d, 差= %d, 積 = %d, 商 = %d\n", wa, sa, seki, shou);

  return EXIT_SUCCESS;
}

void keisan1(int x, int y, int *wa, int *sa, int *seki, int *shou){
  *wa = x + y;
  *sa = x - y;
  *seki = x * y;
  if(y != 0){
  *shou = x / y;
  }else{
    puts("0で割り算はできません");
    exit(EXIT_FAILURE);
  }
  return;
}

