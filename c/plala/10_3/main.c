#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 256
#define ARRAY_SIZE(a) (sizeof(a)/sizeof(a[0]))

int main(void){
  int data1[] = {10, 15, 22, 45, 9, 66, 71, 4, 37, 82};
  int data2[BUFFER_SIZE];
  int *p1, *p2, i, j, cnt = 0;
  p1 = data1;
  p2 = data2;

  for(i = 0; i < ARRAY_SIZE(data1); i++){
    if(*p1 % 2 == 1){
      *p2 = *p1;
      p2++;
      cnt++;
    }
    p1++;
  }
  for(j = 0; j < cnt; j++){
    printf("%d\n", data2[j]);
  }
  printf("格納個数= %d\n", cnt);

  return EXIT_SUCCESS;
}


