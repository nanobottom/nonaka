#include <stdio.h>
#include <string.h>

int main(void)
{
  float data = 0.0F;
  unsigned long work;
  int binary[32];
  int pos = 0;


  printf("Input decimal point>>");
  scanf("%f", &data);

  memcpy(&work, &data, sizeof(data));

  for(; pos < 32; pos++)
  {
    binary[pos] = work % 2;
    work /= 2;
  }
  for(pos = 31; pos >=0; pos--)
  {
    if(pos == 30 || pos == 22)
    {
      printf("-");
    }
    printf("%d", binary[pos]);
  }
}
