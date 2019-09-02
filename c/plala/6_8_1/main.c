#include <stdio.h>
#include <stdlib.h>

int main(void){
  long data = 1;
  int cnt = 1;

  for(;;){
    data *= 2;
    printf("data = %ld\n", data);
    if(data > 32767){
      break;
    }else{
      cnt++;
    }
  }
  printf("cnt = %d\n", cnt);
}
