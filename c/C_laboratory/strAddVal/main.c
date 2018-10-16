#include <stdio.h>

struct my_struct{
  unsigned char m1;
  unsigned long m4;
  unsigned short m2;
}ms;

int main(void)
{
  unsigned char *p;

  ms.m1 = 0xFF;
  ms.m4 = 0x12345678;
  ms.m2 = 0xABCD;

  p = (unsigned char *)&ms;
  
  for(int i = 0; i < sizeof(ms); i++)
  {
    printf("%08X [%02X]\n", p, *p);
    p++;
  }
}
