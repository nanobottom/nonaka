#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
void print_binary(int num, int digit);
void print_bit_operation(unsigned char data, unsigned char mask, unsigned char result, char *ope);

int main(void)
{
  unsigned char data = 0x55;
  unsigned char mask = 0x0F;
  print_bit_operation(data, mask, data & mask, "AND");
  print_bit_operation(data, mask, data | mask, "OR");
  print_bit_operation(data, mask, data ^ mask, "XOR");
}

void print_bit_operation(unsigned char data, unsigned char mask, unsigned char result, char *ope)
{
  printf("\t");
  print_binary(data, 8);
  printf("\n");
  printf("   %s)\t", ope);
  print_binary(mask, 8);
  printf("\n\t");
  for(int i = 0; i < 8; i++)
  {
    printf("-");
  }
  printf("\n\t");
  print_binary(result, 8);
  printf("\n\n");
}


void print_binary(int num, int digit)
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
}
