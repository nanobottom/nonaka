#include <stdio.h>

#define NUM 8

int main(void)
{
  char a[NUM] = "ABCDEF";

  for(int i = 0; i < NUM; i++)
  {
    printf("%08X [%02X] ...a[%d]\n", &a[i], a[i], i);
  }
  for(int i = 0; i < NUM; i++)
  {
    printf("%08X [%02X] ...a + %d\n", a + i, *(a + i), i);
  }
}
