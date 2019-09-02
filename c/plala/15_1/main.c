#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 256
struct employer_info{
  int no;
  char name[BUFFER_SIZE];
  char post[BUFFER_SIZE];
  int year;
  long salary;
};

int main(void){
  struct employer_info syomu[20] = {
    { 78027, "神保直樹", "課長", 21, 346780 },
    { 84004, "相原彰子", "主任", 15, 223640 },
    { 87022, "本郷幸子", "", 12, 208760 },
    { 93042, "三上葵", "", 6, 176530 },
    { 95005, "佐々木翠", "", 4, 166700 },
    { 99009, "長崎宏美", "", 1, 150140 },
    { 0, "", "", 0, 0 },
  };

  for(int i = 0; syomu[i].no != 0; i++){
    printf("%5d\t%s\t%s\t%6d\t%6ld\n", 
           syomu[i].no, syomu[i].name, syomu[i].post, syomu[i].year,syomu[i].salary);
  }

  return EXIT_SUCCESS;
}
