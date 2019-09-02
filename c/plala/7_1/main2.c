#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 101

int main(void){
  char str_a[BUFFER_SIZE] = "", str_b[BUFFER_SIZE] = "", str_c[BUFFER_SIZE] = "";

  while(strlen(str_b) < 100){

    /* 文字をキーボードから入力する */
    puts("文字列を入力してください");
    fgets(str_a, BUFFER_SIZE, stdin);
    /* 改行文字を削除する */
    str_a[strlen(str_a) - 1] = '\0';
    
    /* 前回と今回のループで入力した文字列同士を結合する */
    if(strlen(str_a) + strlen(str_b) < BUFFER_SIZE){
      snprintf(str_c, BUFFER_SIZE, "%s%s", str_a, str_b);
    }else{
      puts("余計な長さの文字列を連結しようとしています");
      exit(EXIT_FAILURE);
    }
    printf("\nstr = %s\n", str_c);

    if(strlcpy(str_b, str_c, BUFFER_SIZE) >= BUFFER_SIZE){
      puts("配列変数str_bは不完全な文字列を指しています");
      exit(EXIT_FAILURE);
    }
    printf("文字列の長さ= %d\n", strlen(str_c));
  }
  return EXIT_SUCCESS;
}





