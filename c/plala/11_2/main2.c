#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void oomoji(char *str);

int main(void){
  char str[3][10] = {
    "computer",
    "lsi-c",
    "ms-dos"
  };
  int i;

  for(i = 0; i < 3; i++){
    oomoji(str[i]);
  }

  return EXIT_SUCCESS;
}

void oomoji(char *str){
  int i = 0;

  while(str[i] != '\0'){
    str[i] = toupper(str[i]);
    i++;
  }
  printf("%s\n", str);
}

