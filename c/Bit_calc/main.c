#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
#define MAX_BYTE 255
enum  bit_operation{AND = '&', OR = '|', XOR = '^', NOT = '~'};
void print_bit(unsigned int, int);
void print_unary_operation(unsigned int, unsigned int, int);
void print_binary_operation(unsigned int, unsigned int, unsigned int, int);

int main(void)
{
  unsigned int num1 = 0, num2 = 0, result = 0;
  char bit_ope[32] = "";
  char line[BUFFER_SIZE] = "";
  int ret = 0, digit = 0;
  
  while(1)
  {

    //Input [decimal] [bit operation] [decimal]
    printf(">>");
    fgets(line, BUFFER_SIZE, stdin);
    line[strlen(line) - 1] = '\0';//Delete "\n"

    //Read as unary operator
    ret = sscanf(line, "%s %u", bit_ope, &num1);

    if(strcmp(line, "q") == 0 || strcmp(line, "Q") == 0)
    {
      printf("Finish program.\n");
      exit(EXIT_SUCCESS);
    }
    else if((ret == 2) && (bit_ope[0] == NOT))
    {
      digit = (num1 > MAX_BYTE) ? 16 : 8;
      result = ~num1;

      print_unary_operation(num1, result, digit);

      exit(EXIT_SUCCESS);
    }
    else
    {
      //Read as binary operator
      if(sscanf(line, "%u %s %u", &num1, bit_ope, &num2) != 3)
      {
        fprintf(stderr, "Input value is nothing\n");
        continue;
      }

      printf("%u, %s, %u\n", num1, bit_ope, num2);
      //Calculate bit operation
      digit = ((num1 > MAX_BYTE) || (num2 > MAX_BYTE)) ? 16 : 8;
      switch(bit_ope[0])
      {
        case AND: result = num1 & num2; break;
        case OR:  result = num1 | num2; break;
        case XOR: result = num1 ^ num2; break;
        default: continue;
      }

      print_binary_operation(num1, num2, result, digit);

      exit(EXIT_SUCCESS);
    //Display bit operation
    }
  }
}
void print_bit(unsigned int num1, int digit)
{
  char bit[16] = "";
  int mask = 0x0001;
  for(int i = 0; i < digit; i++)
  {
   bit[i] = ((num1 >> i) & mask) ? '1': '0';
  }
  for(int i = (digit - 1); i > -1 ; i--)
  {
    putchar(bit[i]);
  }
  printf("\n");
}
void print_unary_operation(unsigned int num1, unsigned int result, int digit)
{
  printf("->%x(hex)/%u(dec)\n", result, result);
  printf("\t");
  print_bit(num1, digit);
  printf("\t");
  for (int i = 0; i < digit; i++)
  {
    putchar('-');
  }
  printf("\n\t");
  print_bit(result , digit);
}
void print_binary_operation(unsigned int num1, unsigned int num2, unsigned int result, int digit)
{
  printf("->%x(hex)/%u(dec)\n", result, result);
  printf("\t");
  print_bit(num1, digit);
  printf("\t");
  print_bit(num2, digit);
  printf("\t");
  for (int i = 0; i < digit; i++)
  {
    putchar('-');
  }
  printf("\n\t");
  print_bit(result , digit);
}
