#include <stdio.h>
#include <stdlib.h>

int main(void){
  char str1[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char str2[256];
  char *p1, *p2;
  p1 = str1;
  p2 = str2;
  for(; *p1 != '\0';){
    p1++;
  }
  for(; p1 != str1; ){
    p1--;
    *p2 = *p1;
    p2++;
  }
  *p2 = '\0';
  printf("str1 = %s\n", str1);
  printf("str2 = %s\n", str2);

  return EXIT_SUCCESS;
}
