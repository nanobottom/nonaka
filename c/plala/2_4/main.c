#include <stdio.h>

int main(void){
  char str[] = "ABCD";
  for (int i = 0; str[i] != '\0'; i++){
    str[i] += 32;
  }
  printf("str = %s\n", str);
  return 0;
}
    
  
