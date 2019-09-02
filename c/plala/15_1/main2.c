#include <stdio.h>
#include <stdlib.h>

struct students_score{
  long no;
  int nation_lang;
  int math;
  int science;
  int society;
  double ave_score;
  char evaluation;
};

int main(void){

  struct students_score scores[20] = {
    {1001, 85, 74, 63, 90, 0.0, '?'},
    {1002, 78, 65, 70, 62, 0.0, '?'},
    {1003, 89, 92, 88, 76, 0.0, '?'},
    {1004, 32, 48, 66, 25, 0.0, '?'},
    {1005, 92, 76, 81, 98, 0.0, '?'},
    {0   , 0 , 0 , 0 , 0 , 0.0, '?'},
  };
  
  printf("番号\t国語\t数学\t理科\t社会\t平均\t評価\n");
  for(int i = 0; scores[i].no != 0; i++){
    scores[i].ave_score = (double)((scores[i].nation_lang + scores[i].math +
                                   scores[i].science + scores[i].society) / 4);
    
    if(scores[i].ave_score >= 80){
      scores[i].evaluation = 'A';
    }else if(scores[i].ave_score >= 70){
      scores[i].evaluation = 'B';
    }else if(scores[i].ave_score >= 60){
      scores[i].evaluation = 'C';
    }else{
      scores[i].evaluation = 'D';
    }

    printf("%ld\t%d\t%d\t%d\t%d\t%f\t%c\n", scores[i].no, scores[i].nation_lang, scores[i].math,
                                            scores[i].science, scores[i].society,
                                            scores[i].ave_score, scores[i].evaluation);
  }
  return EXIT_SUCCESS;
}

