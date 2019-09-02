#include <stdio.h>
#include <stdlib.h>

void func(char *str);
int main(void){
  char str[] = "COMPUTER";

  func(str);
  return EXIT_SUCCESS;
}
void func(char *str){
  printf("%s\n", str);
}
