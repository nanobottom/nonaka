#include <stdio.h>
#include <stdlib.h>

struct st_score{
  int high_score;
  int low_score;
  double average_score;
};

void get_grade_data(int scores[], struct st_score *score_data);
int main(void){
  int scores[] = {78, 86, 56, 77, 47, 63, 94, 37, 50, 74, -1};
  struct st_score score_data;
  get_grade_data(scores, &score_data);

  printf("High:%d, Low:%d, Ave.:%.2f\n", score_data.high_score, score_data.low_score,
                                        score_data.average_score);
  return EXIT_SUCCESS;

}

void get_grade_data(int scores[], struct st_score *score_data){
  int i = 0, sum = 0;
  double average_score;
  score_data->high_score = 0;
  score_data->low_score = 100;
  while(scores[i] != -1){
    if(scores[i] > score_data->high_score){
      score_data->high_score = scores[i];
    }
    if(scores[i] < score_data->low_score){
      score_data->low_score = scores[i];
    }
    sum += scores[i];
    i++;
  }
  score_data->average_score = (double)sum / i;
  return;
}

