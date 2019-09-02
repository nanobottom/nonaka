#include <stdio.h>
#include <stdlib.h>

int main(void){
  char c;
  char *p;

  c = 'A';
  p = &c;
  printf("%c\n", *p);
  return EXIT_SUCCESS;
}
