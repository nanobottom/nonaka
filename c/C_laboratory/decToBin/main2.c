#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256

int enter_data(void);
void dec_to_bin(int);

int main(void){
  int dec;
  dec = enter_data();
  dec_to_bin(dec);
}

// データを入力する関数
int enter_data(void){
  int dec;
  char readline[BUFFER_SIZE] = "";
  printf("Enter data>>");
  fgets(readline, BUFFER_SIZE, stdin);
  readline[strlen(readline) - 1] = '\0';
  if((dec = atoi(readline)) == 0){
    fprintf(stderr, "Input data is not number or zero.\n");
    exit(EXIT_FAILURE);
  }
  printf("%d is entered.\n", dec);
  return dec;
}

// 10進数を2進数に変換する関数
void dec_to_bin(int dec){
  int bin[BUFFER_SIZE], digit = 0;
  char bin_s[BUFFER_SIZE] = "";
  while(dec > 0){
    printf("%3d / 2 = %3d ... %d\n", dec, dec / 2, dec % 2);
    bin[digit] = dec % 2;
    dec /= 2;
    digit++;
  }
  while(digit >= 0){
    strncat(bin_s, bin[digit] ? "1" : "0", BUFFER_SIZE);
    digit--;
  }
  printf("Binary:%s\n", bin_s);
}
