#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))

int get_sum(int *data, int array_size);
double get_var(int *data, int array_size, double average);


int main(void){
  int data[] = {80, 76, 59, 87, 66, 54, 40, 78, 94, 61};
  double average, variance = 0.0, deviation;
  int sum = 0;
  sum = get_sum(data, ARRAY_SIZE(data));
  average = (double)sum/ ARRAY_SIZE(data);
  variance = get_var(data, ARRAY_SIZE(data), average);
  deviation = sqrt(variance);

  printf("sum:%d\n", sum);
  printf("average:%f\n", average);
  printf("variance:%f\n", variance);
  printf("deviation:%f\n", deviation);
  
  return EXIT_SUCCESS;
}

int get_sum(int *data, int array_size){
  int sum = 0;
  for(int i = 0; i < array_size; i++){
    sum += data[i];
  }
  return sum;
}

double get_var(int *data, int array_size, double average){
  double variance = 0.0;
  for(int i = 0; i < array_size; i++){
    variance += pow((data[i] - average), 2);
  }
  variance /= array_size;
  return variance;
}
