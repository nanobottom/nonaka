#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* この関数は入力した文字列が2進数であるか確認する関数である */
int isbinary(char *str){
  int result = 0;
  for(int i = 0; i < strlen(str); i++){
    if(str[i] == '0' || str[i] == '1'){
      result++;
    }else{
      result = 0;
      break;
    }
  }
  return result;
}  
