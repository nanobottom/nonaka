#include <stdio.h>

int main(void){
  float a = 53.6, b = 84.7, c = 57.89;
  float result;
  result = (a + b) / (c * b);

  printf("小数形式 = %f\n", result);
  printf("指数形式 = %e\n", result);

  return 0;

}
