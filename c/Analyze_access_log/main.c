#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define IN_FILENAME "access.log"
#define OUT_FILENAME "ranking.txt"
#define BUFFER_SIZE 256
#define MAX_ARRAY 32

typedef struct access_log{
  char address[BUFFER_SIZE];
  long count;
}AccessRank_t;


void Analyze_log_and_count_access(AccessRank_t *, char *, int *);
void Sort_access_rank(AccessRank_t *, int *);
void write_access_rank(FILE *, AccessRank_t *, int *);

int main(void)
{
  static AccessRank_t access_rank[MAX_ARRAY];
  FILE *fpin = NULL, *fpout = NULL;
  char readline[BUFFER_SIZE] = "";
  int count = 0, max_address = 0;
  //Open file.
  if((fpin = fopen(IN_FILENAME, "r")) == NULL)
  {
    fprintf(stderr, "Cannot open file \"%s\"\n", IN_FILENAME);
    exit(EXIT_FAILURE);
  }
  //Read each 1 line.
  while(fgets(readline, BUFFER_SIZE, fpin) != NULL)
  {
    //Analyze string and count.
    Analyze_log_and_count_access(access_rank, readline, &max_address);
  }
  //Sort and make ranking.
  Sort_access_rank(access_rank,&max_address);

  if((fpout = fopen(OUT_FILENAME, "w")) == NULL)
  {
    fclose(fpin);
    fprintf(stderr, "Cannot open file.\n");
    exit(EXIT_FAILURE);
  }
  //Write access ranking for file.
  write_access_rank(fpout, access_rank, &max_address);

  //File close.
  if(fclose(fpin) == EOF)
  {
    fprintf(stderr, "Failed to close file.\n");
    exit(EXIT_FAILURE);
  }
  if(fclose(fpout) == EOF)
  {
    fprintf(stderr, "Failed to close file.\n");
    exit(EXIT_FAILURE);
  }
}
//Analyze string and count.
void Analyze_log_and_count_access(AccessRank_t *access_rank, char *readline, int *max_address)
{
  char address[BUFFER_SIZE] = "";
  sscanf(readline, "%*s %*s %*s %s", address);
  for (int i = 0; i < MAX_ARRAY; i++, access_rank++)
  {
    
    if(strcmp(access_rank->address, address) == 0)
    {
      access_rank->count++;
      break;
    }
    else if(strcmp(access_rank->address, "") == 0)
    {
      strcpy(access_rank->address,address);
      access_rank->count = 1;
      (*max_address)++;
      break;
    }
  }
}
//Sort and make ranking.
void Sort_access_rank(AccessRank_t *access_rank, int *max_address)
{
  AccessRank_t *tmp;
  AccessRank_t *p_former = access_rank;
  AccessRank_t *p_latter = access_rank;

  for (int i = 0; i < *max_address - 1; i++, p_former++)
  {
    p_latter+=(i + 1);
    for (int j = i + 1; j < *max_address; j++, p_latter++)
    {
      if(p_latter->count > p_former->count)
      {
        tmp = p_latter;
        p_latter = p_former;
        p_former = tmp;
      }
    }
  }
}
//Write access ranking for file.
void write_access_rank(FILE *fpout, AccessRank_t *access_rank, int *max_address)
{
  fprintf(fpout, "rank\tcount\taddress\n");
  fprintf(fpout, "------------------------------\n");

  for (int i = 0; i < *max_address; i++, access_rank++)
  {
    fprintf(fpout, "%d\t%d\t\"%s\"\n", i + 1, access_rank->count, access_rank->address);
  }
}
