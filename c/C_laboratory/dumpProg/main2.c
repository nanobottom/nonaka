#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hexdump(FILE *);
int main(int argc, char *argv[]){
  FILE *fp = NULL;
  
  // ファイルをオープンする
  if((fp = fopen(argv[1], "r")) == NULL){
    fprintf(stderr, "Failed to open file.\n");
    exit(EXIT_FAILURE);
  }
  hexdump(fp);
}  
// ファイルから1文字ずつ文字を取り出し、
// 16進表記で出力する
void hexdump(FILE *fp){
  int data, pos = 0;
  while((data = fgetc(fp)) != EOF){
    if(pos % 8 == 0 && pos % 16 != 0){
      printf(" ");
    }else if(pos % 16 == 0){
      printf("\n%08X  ", pos);
    }
    printf("%02X ", data);
    pos++;
  }
}

