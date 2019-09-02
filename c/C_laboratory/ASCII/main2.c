#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void){
  unsigned char code = 0x00;
  
  printf("        +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F\n");

  for(;code < 0xFF; code++){
    if(code == 0){
      printf("%06X  ", code);
    }else if(code % 16 == 0 && code != 0){
      printf("\n%06X  ", code);
    }
    if(isprint((int)code)){
      printf("%c  ", code);
    }else{
      printf("  ");
    }
  }
}

