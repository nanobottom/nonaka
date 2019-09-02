#include <stdio.h>

void putchar_asterisk(char x);
int main(void){
  char n;
  n = '*';
  putchar_asterisk(n);
  return 0;
}

void putchar_asterisk(char x){
  putchar(x);
  return;
}
