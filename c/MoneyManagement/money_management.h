#ifndef MONEY_MONEGEMENT_H_
#define MONEY_MONEGEMENT_H_

#include <stdio.h>
#include <string.h>

#define BUF_SIZE 1024
#define FILENAME "money_manage.csv"


struct money_info{
  char year[6];
  char month[6];
  char date[6];
  char day_of_week[6];
  char type[10];
  unsigned long money;
};
//Get current year, month ,date
extern int get_time(struct money_info *);

//Input type, money
extern int input_money(struct money_info *);

#endif
