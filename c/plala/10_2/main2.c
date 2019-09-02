#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){
  char str[] = "AbcDefGHijk1234lmNOP";
  char *p;
  p = str;
  while(*p != '\0'){
    *p = toupper(*p);
    p++;
  }

  printf("%s\n", str);
  return EXIT_SUCCESS;
}
