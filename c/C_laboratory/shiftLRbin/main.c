#include <stdio.h>

#define BUFFER_SIZE 256
void print_binary(unsigned long num, int digit)
{
  int binary[BUFFER_SIZE];

  for(int i = 0; i < digit; i++)
  {
    binary[i] = num % 2;
    num /= 2;
  }
  for(int i = digit -1; i >=0; i--)
  {
    printf("%d", binary[i]);
  }
  puts("");
}

int main(void)
{
  unsigned char uchar1 = 0xAA;
  signed char schar1 = 0xAA;
  puts("unsigned char");
  print_binary(uchar1, 8);
  puts("<<1");
  print_binary(uchar1 << 1, 8);
  puts(">>1");
  print_binary(uchar1 >> 1, 8);
  puts("");
  puts("signed char");
  print_binary(schar1, 8);
  puts("<<1");
  print_binary(schar1 << 1, 8);
  puts(">>1");
  print_binary(schar1 >> 1, 8);
}
