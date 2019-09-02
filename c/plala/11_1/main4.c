#include <stdio.h>
#include <stdlib.h>

int cmp(int a, int b);

int main(void){
  int a, b, c;
  puts("２つの整数値を入力");
  scanf("%d %d", &a, &b);
  c = cmp(a, b);

  printf("小さい方=%d\n", c);

  return EXIT_SUCCESS;
}

int cmp(int a, int b){
  int c;
  if(a <= b){
    c = a;
  }else{
    c = b;
  }

  return c;
}
