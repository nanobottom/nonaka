#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

#define BUFFER_SIZE 256

int main(void){
  char str[BUFFER_SIZE] = {'\0'}, *endptr;
  int score_range[11];
  long long score_l;
  int score;
  puts("点数を入力しなさい（終了条件：'e'あるいは'E'");
  for(;;){
    fgets(str, BUFFER_SIZE, stdin);
    str[strlen(str) - 1] = '\0';
    if(strcmp(str, "e") == 0 || strcmp(str, "E") == 0){
      break;
    }
    score_l = strtol(str, &endptr, 10);
    if(str == endptr){
      puts("数値に変換できませんでした");
      continue;
    }
    if(score_l > INT_MAX || score_l < INT_MIN){
      puts("int型に変換できません");
      continue;
    }
    score = (int)score_l;
    if(score >= 0 && score <= 100){
      printf("入力した点数：%d\n", score);
    }else{
      puts("入力した点数は範囲外です");
      continue;
    }


  }
}


