#include <stdio.h>
#define NUM 5

char cData[NUM] = {0x11, 0x22, 0x33, 0x44 ,0x55};
short sData[NUM] = {0x1111, 0x2222, 0x3333, 0x4444, 0x5555};
long lData[NUM] =  {0x11111111, 0x22222222, 0x33333333, 0x44444444, 0x55555555};

int main(void)
{
  char *pc;
  short *sc;
  long *lc;
  
  pc = cData;
  sc = sData;
  lc = lData;

  puts("<Char type>");
  for (int i = 0; i < NUM; i++)
  {
    printf("%08X [%02X]\n", pc, *pc);
    pc++;
  }
  puts("<Short type>");
  for (int i = 0; i < NUM; i++)
  {
    printf("%08X [%02X]\n", sc, *sc);
    sc++;
  }
  puts("<Long type>");
  for (int i = 0; i < NUM; i++)
  {
    printf("%08X [%02X]\n", lc, *lc);
    lc++;
  }
}

