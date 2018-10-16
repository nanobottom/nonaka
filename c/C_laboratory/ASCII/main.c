#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int is_shift_jis(unsigned char code);

int main(void)
{
  unsigned char code = 0x00;

  printf("    +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F\n");
  for(;code != 0xFF; code++)
  {
    if(code % 16 == 0)
    {
      printf("\n%02X  ",code);
    }
    if(isprint((int)code))
    {
      printf("%2c ", code);
    }
    else
    {
      printf("  ");
    }
  }
}

int is_shift_jis(unsigned char code)
{
  if((code >= 0x20 && 0x7E <= code) ||
    (code >= 0xA1 && 0xDF <= code))
  {
    return 1;
  }
  else
  {
    return 0;
  }
}

