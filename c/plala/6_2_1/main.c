#include <stdio.h>
#include <stdlib.h>

int main(void){
  int wa = 0;
  for (int i = 1; i <= 100; i++){
    wa += i;
  }
  printf("wa = %d\n", wa);

  return EXIT_SUCCESS;
}
