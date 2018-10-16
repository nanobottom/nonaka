#include <stdio.h>

char data[8] = {0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88};

int main(void)
{
  char c;
  short s;
  long l;

  char *pc;
  short *ps;
  long *pl;

  puts("<Value's size>");
  printf("char type = %d\n", sizeof(c));
  printf("short type = %d\n", sizeof(s));
  printf("long type = %d\n", sizeof(l));

  puts("<Pointer's size>");
  printf("char type = %d\n", sizeof(pc));
  printf("short type = %d\n", sizeof(ps));
  printf("long type = %d\n", sizeof(pl));

  pc = data;
  ps = (short *)data;
  pl = (long *)data;
  puts("<Read pointer>");
  printf("char type = %02X\n", *pc);
  printf("short type = %04X\n", *ps);
  printf("long type = %08X\n", *pl);
}
