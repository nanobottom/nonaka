#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]){

  int purchase_money, change, sheets;
  if (argc != 2){
    fprintf(stderr, "Commandline argument is differ.\n");
    exit(EXIT_FAILURE);
  }

  purchase_money = atoi(argv[1]);
  printf("購入金額= %d円\n", purchase_money);
  change = 10000 - purchase_money;

  /* 5千円札の計算 */
  sheets = change / 5000;
  change = change % 5000;
  printf("五千円札の枚数 \t= %d\n", sheets);
  
  /* 千円札の計算 */
  sheets = change / 1000;
  change = change % 1000;
  printf("千円札の枚数 \t= %d\n", sheets);
  
  /* 五百円玉の計算 */
  sheets = change / 500;
  change = change % 500;
  printf("五百円玉の枚数 \t= %d\n", sheets);
  
  /* 百円玉の計算 */
  sheets = change / 100;
  change = change % 100;
  printf("百円玉の枚数 \t= %d\n", sheets);
  
  return 0;
}
