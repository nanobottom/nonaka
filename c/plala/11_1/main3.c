#include <stdio.h>
#include <stdlib.h>

int multiplication(int a, int b);
int main(void){

  int a, b, c;

  a = 20;
  b = 10;

  c = multiplication(a, b);
  printf("c = %d\n", c);

  return EXIT_SUCCESS;
}

int multiplication(int a, int b){
  int c;
  c = a * b;

  return c;
}
