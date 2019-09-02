#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
void hexdump(FILE *fp){

  int data = 0, pos = 0, str_pos = 0, blank_num = 0;
  char str[19] = "";
  while((data = fgetc(fp)) != EOF)
  {
    
    if(pos % 8 == 0 && pos % 16 != 0)
    {
      printf(" ");
    }
    else if(pos % 16 == 0)
    {
      str[str_pos] = '|';
      str[str_pos + 1] = '\0';
      printf("%s\n%08X  ",str, pos);
      strcpy(str, " |");
      str_pos = 2;
    }
    printf("%02X ", data);
    str[str_pos] = isprint(data) ? data : '.';
    str_pos++;
    pos++;
  }
  //Make blank part.
  blank_num = 16 - (pos % 16);
  if(blank_num > 8)
  {
    printf(" ");
  }
  for(int i = 0; i < blank_num; i++)
  {
    printf("   ");
    str[str_pos] = ' ';
    str_pos++;
  }
  str[str_pos] = '|';
  str[str_pos + 1] = '\0';
  printf("%s\n", str);

  if(fclose(fp) == EOF)
  {
    fprintf(stderr, "Failed to close file.\n");
    exit(EXIT_FAILURE);
  }
}
