#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Hexdump
void hexdump(int *arr, int arr_size)
{
  char c[256] = "|";
  char buf[256] = "";
  int count = 0;
  for(int i = 0; i < arr_size; i++)
  {
    // If arr is range of ASCII...
    if (arr[i] > 31 && arr[i] < 127)
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%c", buf, (char)arr[i]);
    }
    else
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%s", buf, ".");
    }

    if(i == 0)
    {
      printf("%08X  ",i);
      printf("%02X ", arr[i]);
    }
    else if((i+1) % 16 == 0 && i != 0 )
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%s", buf, "|\n");
      printf("%02X  ", arr[i]);
      printf("%s",c);
      printf("%08X  ",i + 1);
      strcpy(c, "|");
    }
    else if((i+1) % 8 == 0)
    {
      printf("%02X  ", arr[i]);
    }
    else
    {
      printf("%02X ", arr[i]);
    }
    count = i + 1;
  }
  //Create blank part.
  for(int i = 0; i < (16 - count % 16); i++ )
  {
    printf("   ");
    strcpy(buf,c);
    snprintf(c, 256, "%s ", buf);

  }
  if((16- count % 16) > 8)
  {
    printf("  ");
  }
  strcpy(buf,c);
  snprintf(c, 256, "%s|\n", buf);
  printf("%s", c);
}

int main(void)
{
  int arr[] = {1, 2, 3, 20, 34,5,  56,0,35, 60, 55, 67, 23, 1, 4, 5,6 ,7, 88, 90};
  hexdump(arr, sizeof(arr)/ sizeof(arr[0]));
  return 0;
}
