#include <stdio.h>
#include <stdlib.h>

int main(void){
  printf("  * * * 九九の表 * * *\n");
  printf("   | 1  2  3  4  5  6  7  8  9\n");
  printf("-----------------------------\n");
  for (int n = 1; n < 10; n++){
    printf("%d  |", n);
    for (int i = 1; i < 10; i++){
      printf("%2d ", n * i);
    }
    printf("\n");
  }

  return EXIT_SUCCESS;
}
