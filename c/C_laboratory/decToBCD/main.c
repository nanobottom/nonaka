#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
void print_binary(int num, int digit);

int main(void)
{
  char readline[BUFFER_SIZE] = "", c[BUFFER_SIZE] = "";

  printf("Input value>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';

  for(int pos = strlen(readline) - 1; pos >= 0; pos--)
  {
    snprintf(c, BUFFER_SIZE, "%c", readline[pos]);
    print_binary(atoi(c), 4);
  }

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
