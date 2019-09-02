#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define BUFFER_SIZE 256

struct st_library{
  char name[100];
  int year;
  int month;
  int day;
};
int strtoi(char *str);
int is_valid_date(int year, int month, int day);
void print_library_database(struct st_library *library, int cnt);


int main(void){
  struct st_library library[100];
  char readline[BUFFER_SIZE];
  int cnt = 0, year, month, day;
  
  for(;;){
    puts("Enter book name and returned date.(Finish: Ctrl + D)");
    int errflg = 0;
    
    /* enter book name */
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      puts("Finish.");
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    /* compare readline and registered book name */
    for(int j = 0; j < cnt; j++){
      if(strcmp(library[j].name, readline) == 0){
        errflg = 1;
      }
    }

    if(errflg == 1){
      puts("Rending now.");
      continue;
    }else{
      puts("Rending OK.");
    }

    if(strlcpy(library[cnt].name, readline, BUFFER_SIZE) >= BUFFER_SIZE){
      puts("Failed to copy strings of readline.");
      exit(EXIT_FAILURE);
    }

    printf("Year>>");
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      puts("Finish.");
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    year = strtoi(readline);

    printf("Month>>");
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      puts("Finish.");
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    month = strtoi(readline);
    printf("Date>>");
    if(fgets(readline, BUFFER_SIZE, stdin) == NULL){
      puts("Finish.");
      break;
    }
    readline[strlen(readline) - 1] = '\0';
    day = strtoi(readline);
    /* check entered date's validity */
    if(is_valid_date(year, month, day) == EXIT_FAILURE){
      fprintf(stderr, "Entered date is invalid.");
      exit(EXIT_FAILURE);
    }else{
      library[cnt].year = year;
      library[cnt].month = month;
      library[cnt].day = day;
    }

    cnt++;
  }
  print_library_database(library, cnt);
  return EXIT_SUCCESS;
}

int strtoi(char *str){
  long result_l;
  int result;
  char *endptr;
  result_l = strtol(str, &endptr, 0);
  /* in case of including other strings otherwise number */
  if(str == endptr){
    fprintf(stderr, "Cannot invert to number.");
    exit(EXIT_FAILURE);
  }
  /* in case of entering number over range of int type */
  if(result_l > INT_MAX || result_l < INT_MIN){
    fprintf(stderr, "Cannnot invert to int type.");
    exit(EXIT_FAILURE);
  }

  result = (int)result_l;

  return result;
}

int is_valid_date(int year, int month, int day){
  int last_day;
  int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

  /* check range of month */
  if(month < 1 || month > 12){
    return EXIT_FAILURE;
  }

  /* check range of day */
  last_day = days[month - 1];
  
  if(month == 2){
    if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){//is leap year
      last_day = 29;
    }
  }
  if(day < 1 || day > last_day){
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}

void print_library_database(struct st_library *library, int cnt){

  for(int i = 0; i < cnt; i++, library++){
    printf("Name:%s, Date:%d.%d.%d\n", library->name, library->year,
                                       library->month, library->day);
  }
  return;
}

