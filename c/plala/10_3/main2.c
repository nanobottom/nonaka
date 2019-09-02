#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 100
int main(void){
  int a[BUFFER_SIZE], *p;
  p = a;
  *p = 0;
  p++;
  for(int i = 0; i < BUFFER_SIZE; i++){
    *p = *(p - 1) + i;
    printf("%d\t", *p);
    if(i % 10 == 0){
      putchar('\n');
    }
    p++;
  }
  return EXIT_SUCCESS;
}

