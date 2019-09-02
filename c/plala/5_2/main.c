#include <stdio.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))
int main(void){
  int data1[] = {1, 22, 333, 4444};
  float data2[] = {12.34, 0.002, 5678.12, 912.1};

  for (int i = 0; i < ARRAY_SIZE(data1); i++){
    printf("data1[%d] = %4d\n", i, data1[i]);
  }
  for (int i = 0; i < ARRAY_SIZE(data2); i++){
    printf("data2[%d] = %8.3f\n", i, data2[i]);
  }
  return 0;
}
