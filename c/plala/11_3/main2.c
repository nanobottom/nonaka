#include <stdio.h>
#include <stdlib.h>

void keisan2(int x, int y, int *p);
int main(void){
  int x, y, result[4];
  puts("Please enter two values>>");
  scanf("%d %d", &x, &y);
  keisan2(x, y, result);
  printf("和=%d, 差=%d, 積=%d, 商=%d\n", result[0], result[1], result[2], result[3]);
  return EXIT_SUCCESS;
}

void keisan2(int x, int y, int *p){
  *p = x + y;
  *(p + 1) = x - y;
  *(p + 2) = x * y;
  if(y != 0){
    *(p + 3) = x / y;
  }else{
    puts("0で割り算はできません");
    exit(EXIT_FAILURE);
  }

  return;
}
