#include <stdio.h>

int main(void){
  char *p1, *p2;
  p1 = p2 = "Winter";
  while(*p1){
    p1++;
  }
  while(p1 > p2){
    --p1;
    putchar(*p1);
  }
  putchar('\n');

  return 0;
}

