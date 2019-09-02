#include <stdio.h>
#include <stdlib.h>

int main(void){
  int input;

  printf("1~3の整数値入力（終了条件: Ctrl + Z)");
  while(input != EOF){

    scanf("%d", &input);
    switch(input){
      case 1:
        printf("apple\n");
        break;
      case 2:
        printf("banana\n");
        break;
      case 3:
        printf("cherry\n");
        break;
      default:
        printf("???\n");
        break;
    }
  }
  return EXIT_SUCCESS;
}

        
