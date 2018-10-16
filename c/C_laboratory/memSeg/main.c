#include <stdio.h>
#include <stdlib.h>
//Coding memory
void func1(){}
void func2(){}
void func3(){}

//Static memory
int g1, g2, g3;

int main(void)
{
  //Stack memory
  int s1, s2, s3;

  //Heap memory
  int *h1, *h2, *h3;

  h1 = (int *)malloc(sizeof(int));
  h2 = (int *)malloc(sizeof(int));
  h3 = (int *)malloc(sizeof(int));
  
  printf("<Coding memory>\n");
  printf("Function1 : %08X\n", func1);
  printf("Function2 : %08X\n", func2);
  printf("Function3 : %08X\n", func3);

  printf("<Static memory>\n");
  printf("Value1 : %08X\n", &g1);
  printf("Value2 : %08X\n", &g2);
  printf("Value3 : %08X\n", &g3);

  printf("<Stack memory>\n");
  printf("Value1 : %08X\n", &s1);
  printf("Value2 : %08X\n", &s2);
  printf("Value3 : %08X\n", &s3);

  printf("<Heap memory>\n");
  printf("Value1 : %08X\n", h1);
  printf("Value2 : %08X\n", h2);
  printf("Value3 : %08X\n", h3);

  free(h1);
  free(h2);
  free(h3);

  return 0;
}
