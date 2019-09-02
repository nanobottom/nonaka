#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void){
  FILE *fp;
  char maker_name[BUFFER_SIZE], car_type[BUFFER_SIZE], displacement[BUFFER_SIZE];
  char filename[] = "car.dat";

  /* open file "car.dat" */
  if((fp = fopen(filename, "a")) == NULL){
    fprintf(stderr, "Cannot open %s.\n", filename);
    exit(EXIT_FAILURE);
  }
  for(;;){
    printf("Please enter maker name(finish conditions: enter \"end\")>>");
    fgets(maker_name, BUFFER_SIZE, stdin);
    maker_name[strlen(maker_name) - 1] = '\0';
    if(strcmp(maker_name, "end") == 0){
      break;
    }

    printf("Please enter car type>>");
    fgets(car_type, BUFFER_SIZE, stdin);
    car_type[strlen(car_type) - 1] = '\0';

    printf("Please enter displacement>>");
    fgets(displacement, BUFFER_SIZE, stdin);
    displacement[strlen(displacement) - 1] = '\0';

    fprintf(fp, "メーカー名：%s ", maker_name);
    fprintf(fp, "車種：%s ", car_type);
    fprintf(fp, "排気量：%s\n", displacement);
  }
  if(fclose(fp) == EOF){
    fprintf(stderr, "Cannot close file pointer.\n");
    exit(EXIT_FAILURE);
  }
  
  return EXIT_SUCCESS;
}


