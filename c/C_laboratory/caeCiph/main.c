#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 256
void encrypt(char *plane, int key, char *crypt);
void decrypt(char *crypt, int key, char *plane);

int main(void)
{
  char readline[BUFFER_SIZE] = "";
  char plane[BUFFER_SIZE] = "";
  char crypt[BUFFER_SIZE] = "";
  int menu = 0, key = 0;

  do{
    printf("1:Encrypt, 2:Decrypt, 3:Finish >>");
    fgets(readline, BUFFER_SIZE, stdin);
    readline[strlen(readline) - 1] = '\0';
    if((menu = atoi(readline)) == 0)
    {
      printf("Input value is wrong.\n");
      continue;
    }
    switch(menu){
      case 1://Encrypt data.
        printf("Input filename for plane text>>");
        fgets(plane, BUFFER_SIZE, stdin);
        plane[strlen(plane) - 1] = '\0';
        printf("Input key>>");
        fgets(readline, BUFFER_SIZE, stdin);
        readline[strlen(readline) - 1] = '\0';
        if((key = atoi(readline)) == 0)
        {
          printf("Input value is not number or zero.\n");
          continue;
        }
        printf("Input filename for crypt text>>");
        fgets(crypt, BUFFER_SIZE, stdin);
        crypt[strlen(crypt) - 1] = '\0';
        encrypt(plane, key, crypt);
        break;

      case 2:
        printf("Input filename for crypt text>>");
        fgets(crypt, BUFFER_SIZE, stdin);
        crypt[strlen(crypt) - 1] = '\0';
        printf("Input key>>");
        fgets(readline, BUFFER_SIZE, stdin);
        readline[strlen(readline) - 1] = '\0';
        if((key = atoi(readline)) == 0)
        {
          printf("Input value is not number or zero.\n");
          continue;
        }
        printf("Input filename for plane text>>");
        fgets(plane, BUFFER_SIZE, stdin);
        plane[strlen(plane) - 1] = '\0';
        decrypt(crypt, key, plane);
        break;
    }
  }while(menu != 3);
  return 0;
}

void encrypt(char *plane, int key, char *crypt)
{
  FILE *fp_read = NULL, *fp_write = NULL;
  int data = 0;

  if((fp_read = fopen(plane, "rb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", plane);
    exit(EXIT_FAILURE);
  }
  if((fp_write = fopen(crypt, "wb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", crypt);
    exit(EXIT_FAILURE);
  }

  //Read data and encrypt plane text to crypt text.
  while((data = fgetc(fp_read)) != EOF)
  {
    fputc(data + key, fp_write);
  }
  
  if(fclose(fp_read) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", plane);
    exit(EXIT_FAILURE);
  }
  if(fclose(fp_write) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", crypt);
    exit(EXIT_FAILURE);
  }

  puts("Finish to encrypt data.");
}

void decrypt(char *crypt, int key, char *plane)
{
  FILE *fp_read = NULL, *fp_write = NULL;
  int data = 0;

  if((fp_read = fopen(crypt, "rb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", plane);
    exit(EXIT_FAILURE);
  }
  if((fp_write = fopen(plane, "wb")) == NULL)
  {
    fprintf(stderr, "Failed to open file(%s).\n", crypt);
    exit(EXIT_FAILURE);
  }

  //Read data and encrypt plane text to crypt text.
  while((data = fgetc(fp_read)) != EOF)
  {
    fputc(data - key, fp_write);
  }
  
  if(fclose(fp_read) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", plane);
    exit(EXIT_FAILURE);
  }
  if(fclose(fp_write) == EOF)
  {
    fprintf(stderr, "Failed to close file(%s).\n", crypt);
    exit(EXIT_FAILURE);
  }

  puts("Finish to decrypt data.");
}
