#include <stdio.h>
#include <stdlib.h>

int cnt_strlen(char *str);
void print_str(int len, char *str);
int main(int argc, char *argv[]){
  int len;

  for(int i = 1; i < argc; i++){
    len = cnt_strlen(argv[i]);
    print_str(len, argv[i]);
  }

  return EXIT_SUCCESS;
}

int cnt_strlen(char *str){
  int cnt = 0;
  while(*str != '\0'){
    str++;
    cnt++;
  }
  return cnt;
}

void print_str(int len, char *str){
  printf("length = %d, %s\n", len, str);
  return;
}
