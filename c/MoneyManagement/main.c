#include "money_management.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

//Get current year, month ,date
int get_time(struct money_info *money_info){
  struct tm tm;
  char *day_of_week[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
  time_t t = time(NULL);
  localtime_r(&t, &tm);
  strftime(money_info->year, sizeof(money_info->year), "%Y", localtime(&t));
  strftime(money_info->month, sizeof(money_info->month), "%m", localtime(&t));
  strftime(money_info->date, sizeof(money_info->date), "%d", localtime(&t));
  strcpy(money_info->day_of_week, day_of_week[tm.tm_wday]);
  printf("%s/%s/%s(%s)\n", money_info-> year, money_info->month, money_info->date, money_info->day_of_week);

  return 0;
}
//Input type, money
int input_money(struct money_info *money_info){
  char type[6] = "";
  int type_num = 0;
  char money[32] = "";
  unsigned long money_num = 0;
  char *type_of_money[] = {"ATM/Credit", "Gas", "Water", "Gym", "Salary", "Savings"};
  printf("What type of money?\n");
  printf("ATM/Credit:1, Gas:2, Water:3, Gym:4, Salary:5, Savings:6>>");
  fgets(type, sizeof(type), stdin);
  type_num = atoi(type); 
  if (type_num == 0){
    fprintf(stderr, "Input character is wrong : %s", type);
    return EXIT_FAILURE;
  }else if (type_num > sizeof(type_of_money) / sizeof(*type_of_money)){
    fprintf(stderr, "Input number is nothing of category.\n");
    return EXIT_FAILURE;
  }
  strcpy(money_info->type, type_of_money[type_num - 1]);
  printf("You choose \"%s\".\n", money_info->type);

  printf("How much is it (yen)?>>");
  fgets(money, sizeof(money), stdin);
  money_num = atoi(money);
  if (money_num == 0){
    fprintf(stderr, "Input character is not number or 0 yen.\n");
    return EXIT_FAILURE;
  }
  money_info->money = money_num;

  
  return EXIT_SUCCESS;
}

//Write file as CSV format
int write_data(struct money_info *money_info){
  FILE *fp = NULL;
  fp = fopen(FILENAME, "a");
  fprintf(fp, "%s, %s, %s, %s, %d\n", money_info->year, money_info->month, money_info->date, money_info->type, money_info->money);
  fclose(fp);
  return EXIT_SUCCESS;
}

//Read file and display all
int display_data(){
  FILE *fp = NULL;
  char buf[BUF_SIZE] = "";
  if((fp = fopen(FILENAME, "r")) == NULL){
    fprintf(stderr, "Can't read file: %s.\n", FILENAME);
    return EXIT_FAILURE;
  }
  while(fgets(buf, sizeof(buf), fp) != NULL){
    printf(buf);
  }
  fclose(fp);
  return EXIT_SUCCESS;
}

//Display total of money
int display_total_money(){
  FILE *fp = NULL;
  int sum = 0;
  int year = 0, month = 0, date = 0, money = 0, result = 0;
  char type[32] = "";
  if((fp = fopen(FILENAME, "r")) == NULL) {
    fprintf(stderr, "Can't read file: %s.\n", FILENAME);
    return EXIT_FAILURE;
  }
  while((result = fscanf(fp, "%d, %d, %d, %[^,], %d", &year, &month, &date, type, &money)) != EOF){
    sum += money;
  }
  printf("Total money: %d\n", sum);
  fclose(fp);
  return EXIT_SUCCESS;
}

int main(void){
  struct money_info money_info;
  char input[BUF_SIZE] = "";
  int input_num = 0;
  while(1){  
    memset(&money_info, 0, sizeof(money_info));
    get_time(&money_info);
    printf("1:input, 2:display data, 3:display total money, 4:end>>");
    fgets(input, sizeof(input), stdin);
    input_num = atoi(input); 
    if (input_num == 0){
      fprintf(stderr, "Input character is wrong : %s", input);
      return EXIT_FAILURE;
    }else if (input_num > 4){
      fprintf(stderr, "Input number is nothing of category.\n");
      return EXIT_FAILURE;
    }else if(input_num == 1){
      if(input_money(&money_info) == EXIT_FAILURE){
        fprintf(stderr, "Continue to begin.\n");
        continue;
      }
      write_data(&money_info);
    }else if(input_num == 2){
      if(display_data() == EXIT_FAILURE){
        fprintf(stderr, "Continue to begin.\n");
        continue;
      }
    }else if(input_num == 3){
      if(display_total_money() == EXIT_FAILURE){
      fprintf(stderr, "Continue to begin.\n");
      continue;
      }
    }else if(input_num == 4){
      printf("Program is finish.\n");
      break;
    }
  }
  return 0;
}
