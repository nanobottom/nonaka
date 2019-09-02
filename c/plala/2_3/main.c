#include <stdio.h>

#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))

int main(void){
  int data1[6] = {18, 25, 46, 11, 3, 76};
  int data2[6];
  int index[6] = {5, 3, 2, 0, 1, 4};

  for (int i = 0; i < ARRAY_SIZE(data1); i++){
    data2[i] = data1[index[i]];
    printf("data2[%d] = %d\n", i, data2[i]);
  }
  return 0;
}
