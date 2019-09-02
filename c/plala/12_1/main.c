#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))

int get_sum(void);
double get_var(double average);

int data[] = {80, 76, 59, 87, 66, 54, 40, 78, 94, 61};

int main(void){
  double average, variance = 0.0, deviation;
  int sum = 0;
  sum = get_sum();
  average = (double)sum/ ARRAY_SIZE(data);
  variance = get_var(average);
  deviation = sqrt(variance);

  printf("sum:%d\n", sum);
  printf("average:%f\n", average);
  printf("variance:%f\n", variance);
  printf("deviation:%f\n", deviation);
  
  return EXIT_SUCCESS;
}

int get_sum(void){
  int sum = 0;
  for(int i = 0; i < ARRAY_SIZE(data); i++){
    sum += data[i];
  }
  return sum;
}

double get_var(double average){
  double variance = 0.0;
  for(int i = 0; i < ARRAY_SIZE(data); i++){
    variance += pow((data[i] - average), 2);
  }
  variance /= ARRAY_SIZE(data);
  return variance;
}
