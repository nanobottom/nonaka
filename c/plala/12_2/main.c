#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define BUFFER_SIZE 256

int scores[100][2];

int strtoi(char *str){
  long result_l;
  int result;
  char *endptr;
  int base = 10;

  result_l = strtol(str, &endptr, base);
  if(str == endptr){
    fprintf(stderr, "Entered strings are NOT number.\n");
    exit(EXIT_FAILURE);
  }
  if(result_l > INT_MAX || result_l < INT_MIN){
    fprintf(stderr, "Cannot invert number of int type.\n");
    exit(EXIT_FAILURE);
  }
  result = (int)result_l;
  return result;
}

int set_score(int student_num, int score){
  static int errcnt = 0, setcnt = 0;

  if(score < 0 || score > 100){
    errcnt++;
    fprintf(stderr, "Entered score is abnormal value. errcnt:%d\n", errcnt);
  }else{
    scores[setcnt][0] = student_num;
    scores[setcnt][1] = score;
    setcnt++;
  }
  return setcnt;
}

void print_score(int setcnt){
  for(int i = 0; i < setcnt; i++){
    printf("student number = %d, score = %d\n", scores[i][0], scores[i][1]);
  }
  return;
}
  

int main(void){
  char readline[BUFFER_SIZE];
  int student_num, score, setcnt;
  
  for(;;){
    /* enter student number. */
    printf("Student No. (finish: Ctrl + D)>>");
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    student_num = strtoi(readline);

    /* enter score. */
    printf("Score (finish: Ctrl + D)>>");
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    score = strtoi(readline);

    setcnt = set_score(student_num, score);

  }

  print_score(setcnt);
  return EXIT_SUCCESS;
}




