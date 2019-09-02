#include <stdio.h>
/* http://www9.plala.or.jp/sgwr-t/c/A/rei02-2.htmli */
int main(void){
  int a, b;
  double c, d;
  char e, f;
  char str[] = "COMPUTER"; /* 文字列定数COMPUTERの設定 */

  a = 5; /* 10進定数5の設定 */
  b = 0x2fb; /* 16進定数2fbの設定 */
  c = 3.14; /* 浮動小数点定数3.14の設定 */
  d = 2.548e2; /* 浮動小数点定数2.548 ×10^2設定 */
  e = 'A'; /* 文字定数Aの設定 */
  f = '8'; /* 文字定数8の設定 */

  printf("str = %s\n", str);
  printf("a = %d\n", a);
  printf("b = %x\n", b);
  printf("c = %f\n", c);
  printf("d = %f\n", d);
  printf("e = %c\n", e);
  printf("f = %c\n", f);

  return 0;
}


