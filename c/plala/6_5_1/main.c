#include <stdio.h>
#include <stdlib.h>

int main(void){
  char calc_mark;
  int value1, value2, result;

  printf("計算方法の入力(+ - * /)>>");
  scanf("%c", &calc_mark);
  printf("整数値1の入力>>");
  scanf("%d", &value1);
  printf("整数値2の入力>>");
  scanf("%d", &value2);

  switch (calc_mark){
    case '+':
      result = value1 + value2;
      break;
    case '-':
      result = value1 - value2;
      break;
    case '*':
      result = value1 * value2;
      break;
    case '/':
      if(value2 == 0){
        printf("0では割り算できません\n");
        exit(EXIT_FAILURE);
      }else{
        result = value1 / value2;
        break;
      }
    default:
      printf("計算方法の入力エラーです\n");
      break;
  }

  printf("result = %d", result);

  return 0;
}



