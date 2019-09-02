#include <stdio.h>
#include <stdlib.h>

int main(void){
  int wa = 0, i = 1;

  while ( i <= 100){
    wa += i;
    i++;
  }
  printf("wa = %d\n", wa);

  return EXIT_SUCCESS;

}
