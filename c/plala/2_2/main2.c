#include <stdio.h>
int main(void){
  float a, b; /* 変数a とbを単精度浮動小数点型で宣言 */
  double c; /* 変数cを倍精度浮動小数点型で宣言 */
  long seki; /* 変数sekiを倍長整数型で宣言 */
  int i = 180; /* 変数iを単長整数型で宣言し、180で初期化 */
  int j = 500; /* 変数jを単長整数型で宣言し、500で初期化 */
  char ch = 'S'; /* 変数chを文字型で宣言し、文字定数Sで初期化 */

  a = 62.5;
  b = 23.3;

  c = a * b;
  seki = (long)i * j;

  printf("ch = %c\n", ch); /* chを出力 */
  printf("c = %f\n", c); /* cを出力 */
  printf("seki = %ld\n", seki); /* sekiを出力 */

  return 0;
}
