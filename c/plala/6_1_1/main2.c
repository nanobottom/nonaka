#include <stdio.h>
#include <ctype.h>

int main(void){
  char ch;
  printf("文字を入力しなさい");
  scanf("%c", &ch);
  if (isupper(ch)){
    ch = tolower((int)ch);
  }
  printf("ch = %c\n", ch);

  return 0;
}
