#include <stdio.h>
#include <stdlib.h>

int main(void){
  char str[] = "Computer";
  char *ptr;
  ptr = str;
  while(*ptr != '\0'){
    putchar(*ptr);
    ptr++;
  }
  putchar('\n');
  return EXIT_SUCCESS;
}
