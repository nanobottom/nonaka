#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
int main(void){
  FILE *fp_in, *fp_out;
  char infile[BUFFER_SIZE], outfile[BUFFER_SIZE];
  int c;
  printf("Input filename>>");
  fgets(infile, BUFFER_SIZE, stdin);
  infile[strlen(infile) - 1] = '\0';
  printf("Output filename>>");
  fgets(outfile, BUFFER_SIZE, stdin);
  outfile[strlen(outfile) - 1] = '\0';

  if((fp_in = fopen(infile, "r")) == NULL){
    fprintf(stderr, "Cannot open %s.\n", infile);
    exit(EXIT_FAILURE);
  }

  if((fp_out = fopen(outfile, "w")) == NULL){
    fprintf(stderr, "Cannot open %s.\n", outfile);
    exit(EXIT_FAILURE);
  }
  while((c = getc(fp_in)) != EOF){
    putc(c, fp_out);
  }
  if(fclose(fp_in) == EOF){
    fprintf(stderr, "Failed to close file pointer.\n");
    exit(EXIT_FAILURE);
  }
  if(fclose(fp_out) == EOF){
    fprintf(stderr, "Failed to close file pointer.\n");
    exit(EXIT_FAILURE);
  }

  return EXIT_SUCCESS;
}
