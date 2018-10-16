#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void display_binary(unsigned char num, int digit);

int main(void)
{
  unsigned char unsigned_num = 0;
  signed char signed_num = 0;
  char two_complement = 0;

  while(getchar() != 'q')
  {
    printf("Unsigned int = %d, Signed int = %d\nBinary = ", unsigned_num, signed_num);
    display_binary(unsigned_num, 8);

    //Calculation two complement.
    two_complement = ~unsigned_num + 1;
    printf("Two complement =");
    display_binary(two_complement, 8);
    unsigned_num++;
    signed_num++;
  }
}

void display_binary(unsigned char num, int digit)
{
  int binary[32];
  for(int i = 0; i < digit; i++)
  {
    binary[i] = num % 2;
    num /= 2;
  }
  for(int i = digit - 1; i >= 0; i--)
  {
    putchar(binary[i] ? '1' : '0');
  }
  printf("\n");
}


