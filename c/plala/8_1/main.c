#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){
  int ch;
  int alpha_num[26] = {0};
  puts("文字を入力しなさい（終了条件：Ctrl + Z)");
  while((ch = getchar()) != EOF){
    if(isupper(ch) != 0){
      alpha_num[ch - 'A']++;
    }else if(islower(ch) != 0){
      alpha_num[ch - 'a']++;
    }
  }
  
  putchar('\n');
  /* 英字の入力個数を出力 */
  for(int i = 0; i < 26; i++){
    printf("%c : %3d個入力\t", i + 'a', alpha_num[i]);
    if(i % 3 == 2){
      putchar('\n');
    }
  }
  return EXIT_SUCCESS;
}



