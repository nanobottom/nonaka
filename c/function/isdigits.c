#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
/* 入力した文字列が数値のみで構成されているか確認する*/  
int isdigits(char *str){
  int result = 0;
  for(int i = 0; i < strlen(str); i++){
    if(isdigit(str[i])){
      result++;
    }else{
      result = 0;
      break;
    }
  }
  return result;
}
