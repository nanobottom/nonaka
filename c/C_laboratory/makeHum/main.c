#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void)
{
  char readline[BUFFER_SIZE] = "", c[BUFFER_SIZE] = "";
  char p1, p2, p3, x1, x2, x3, x4;
  printf("Input binary(4bit)>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  snprintf(c, BUFFER_SIZE, "%c", readline[0]);
  x1 = atoi(c);
  snprintf(c, BUFFER_SIZE, "%c", readline[1]);
  x2 = atoi(c);
  snprintf(c, BUFFER_SIZE, "%c", readline[2]);
  x3 = atoi(c);
  snprintf(c, BUFFER_SIZE, "%c", readline[3]);
  x4 = atoi(c);

  p1 = x1 ^ x3 ^ x4;
  p2 = x1 ^ x2 ^ x4;
  p3 = x1 ^ x2 ^ x3;
  printf("Hamming code = %d%d%d%d%d%d%d\n", x1, x2, x3, p3, x4, p2, p1);
  return 0;
}

