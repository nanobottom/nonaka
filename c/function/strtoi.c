
int strtoi(char str[]){
  char *endptr;
  long result_l;
  int result;

  result_l = strtol(str, &endptr, 10);
  
  /* 入力引数が数値がどうか確認する */
  if(str == endptr){
    fprintf(stderr, "Cannot convert to number.\n");
    exit(EXIT_FAILURE);
  }

  /* 入力引数がint型の範囲かどうか確認する */
  if(result_l > INT_MAX || result_l < INT_MIN){
    fprintf(stderr, "Cannot convert to int type.\n");
    exit(EXIT_FAILURE);
  }

  result = (int)result_l;

  return result;
}
