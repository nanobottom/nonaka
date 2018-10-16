#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 256

int check_sum(char *str);

int main(void)
{
  char readline[BUFFER_SIZE] = "";
  int check_sum1 = 0, check_sum2 = 0;

  printf("Input character>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  check_sum1 = check_sum(readline);

  printf("Input character again>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  check_sum2 = check_sum(readline);
  
  printf("check sum1 = %d, check sum2 = %d\n", check_sum1, check_sum2);

  if(check_sum1 == check_sum2)
  {
    printf("Two strings is same.\n");
  }
  else
  {
    printf("Two strings is differ.\n");
  }
  return 0;
}

int check_sum(char *str)
{
  int ret = 0, cnt = 0;
  while(*str != '\0')
  {
    if(cnt % 2 == 0)
    {
      ret += (int)(*str) * 256;
    }
    else
    {
      ret += (int)*str;
    }
    str++;
    cnt++;
  }
  return ret;
}

