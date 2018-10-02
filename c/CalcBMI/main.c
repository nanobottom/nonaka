#include <stdio.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))

struct shape{
  char   name[50];
  float  height;
  float  weight;
  float  bmi;
};

void set_BMI(struct shape *p, int array_size)
{
  float height_meter = 0;

  for(int i_member = 0; i_member < array_size; i_member++ )
  {
    height_meter = p->height * 0.01;
    p->bmi = p->weight / (height_meter * height_meter);
    p++;
  }
}

int main(void)
{
  struct shape stars[] = {
    {"ブラッド・ピット", 183.2, 73.4},
    {"トム・クルーズ", 170.1, 67.2},
    {"ジョニー・デップ", 178.2, 70.5},
    {"サモ・ハン・キンポー", 172.0, 111.1},
    {"ウィル・スミス", 188.0, 78.3},
    {"アンジェリーナ・ジョリー", 173.0, 45.0},
  };

  struct shape *p_stars = stars;
  //Calculate BMI and set to structure shape.
  set_BMI(stars, ARRAY_SIZE(stars));

  for (int i_member = 0; i_member < ARRAY_SIZE(stars); i_member++)
  {
    printf("%s's BMI is %.1f.\n", p_stars->name, p_stars->bmi);
    if(p_stars->bmi < 18.5)
    {
      printf("Shape is slim.\n");
    }
    else if(p_stars->bmi < 25.0)
    {
      printf("Shape is standard.\n");
    }
    else
    {
      printf("Shape is fat,\n");
    }
    p_stars++;

  }
}    
