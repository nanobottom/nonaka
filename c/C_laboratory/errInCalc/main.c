#include <stdio.h>
#include <math.h>

int main(void)
{
  unsigned char c1 = 0, c2 = 0, c3 = 0;
  double d1 = 0.0, d2 = 0.0, d3 = 0.0;
  float f1 = 0.0F, f2 = 0.0F, f3 = 0.0F;

  puts("桁あふれ");
  c1 = 100;
  c2 = 200;
  c3 = c1 + c2;
  printf("%d + %d = %d\n", c1, c2, c3);

  puts("打ち切り誤差");
  d1 = 2;
  d2 = sqrt(d1);
  printf("√%f = %f\n", d1, d2);

  puts("丸め誤差");
  d1 = 1.0;
  d2 = 3.0;
  d3 = d1 / d2;
  printf("%f ÷ %f = %.50f\n", d1, d2, d3);

  puts("情報落ち");
  f1 = 12345.0F;
  f2 = 0.00001F;
  f3 = f1 + f2;
  printf("%f + %f = %f\n",f1, f2, f3);

  puts("桁落ち");
  f1 = 1.23456F;
  f2 = 1.23450F;
  f3 = f1 - f2;
  printf("(%f - %f) = %f\n", f1, f2 ,f3);
  printf("(%f - %f) × 100000 = %f\n", f1, f2 ,f3 * 100000);

}
