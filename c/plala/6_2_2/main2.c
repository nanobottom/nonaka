#include <stdio.h>
#include <stdlib.h>

int main(void){
  for (int n = 0; n < 10; n++){
    for (int i = 0; i <= n; i++){
      printf("%d", i);
    }
    printf("\n");
  }

  return EXIT_SUCCESS;
}
