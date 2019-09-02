#include <stdio.h>

int main(void){
  float a = 5.36, b = 8.47, c = 5.789;
  float result;

  result = (a + b) * c / b;
  printf("実行結果\n");
  printf("結果 = %f\n", result);

  return 0;
}
