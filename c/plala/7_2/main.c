#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){
  for(int i = 0; i <=127; i++){
    if(isprint(i) != 0){
      if(isalnum(i) != 0){
        printf("%c", (char)i);
      }else{
        printf("[%c]", (char)i);
      }
    }
  }
  return EXIT_SUCCESS;
}
