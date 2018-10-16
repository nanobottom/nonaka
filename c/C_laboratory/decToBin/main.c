#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define BUFFER_SIZE 256

int main(void)
{
  char read_line[BUFFER_SIZE] = "";
  int decimal = 0, digit = 0, binary[32], fundamental_num = 0;
  printf("Input decimal>>");
  fgets(read_line, BUFFER_SIZE, stdin);
  read_line[strlen(read_line) - 1] = '\0';
  if((decimal = atoi(read_line)) == 0)
  {
    fprintf(stderr, "Input is not number or zero.\n");
    exit(EXIT_FAILURE);
  }
  while(decimal > 0)
  {
    printf("%3d ÷ 2 = %3d ... %d\n", decimal, decimal/2, decimal % 2);
    binary[digit] = decimal % 2;
    decimal /= 2;
    digit++;
  }
  decimal = 0;
  digit--;
  printf("Binary = ");
  while(digit >= 0)
  {
    putchar(binary[digit] ? '1' : '0');
    fundamental_num = pow(2, digit);
    decimal += (fundamental_num * binary[digit]);
    digit--;
  }
  printf("\n");
  printf("Decimal = %d\n", decimal);
}


