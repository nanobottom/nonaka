#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int isbinary(char str[]);
int main(void){

  char readline[BUFFER_SIZE] = "";
  long dec;
  
  /* 値を入力する */
  printf("Input binary>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  
  /* 入力が2進数かどうか確認する */
  if (isbinary(readline) == 0){
    fprintf(stderr, "Input value is NOT binary.\n");
    exit(EXIT_FAILURE);
  }

  /* 2進数を10進数に変換する */
  dec = strtol(readline, NULL, 2);
  printf("%d\n", dec);

  return EXIT_SUCCESS;
}

int isbinary(char str[]){
  int count = 0;
  for(int i = 0; i < strlen(str); i++){
    if(str[i] == '1' || str[i] == '0'){
      count++;
    }else{
      count = 0;
      break;
    }
  }
  return count;
}
       
