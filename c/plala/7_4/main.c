#include <stdio.h>
#include <stdlib.h>

int main(void){
  int rand_num;

  for(int i = 0; i < 10; i++){
    rand_num = rand() % 80;
    for(int j = 0; j < rand_num; j++){
      putchar('*');
    }
    putchar('\n');
  }
  return EXIT_SUCCESS;
}
