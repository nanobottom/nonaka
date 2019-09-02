#include <stdio.h>

int main(void){
  int a, b;
  printf("整数値を2つ入力");
  scanf("%d %d", &a, &b);

  if (a > 10){
    printf("aは10より大きい\n");
  }else{
    printf("aは10以下\n");
  }

  if (a == b){
    printf("aとbは等しい\n");
  }

  if (b >= 10){
    printf("bは10以上\n");
    a = 0;
    b = 0;
  }else{
    printf("bは10より小さい\n");
    a += 1;
    b += 1;
  }
  printf("a = %d, b = %d\n", a, b);

  return 0;
}
