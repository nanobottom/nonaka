#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){
  char moji;
  scanf("%c", &moji);

  if (isupper(moji)){
    printf("英大文字です\n");
  }else if(islower(moji)){
    printf("英小文字です\n");
  }else if(isdigit(moji)){
    printf("数字です\n");
  }else{
    printf("英字でも数字でもありません\n");
  }

  return EXIT_SUCCESS;
}

