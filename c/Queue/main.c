#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "queue.h"

#define QUEUE_SIZE 5
#define BUFFER_SIZE 256
int is_used_range(queue_t *, int);
void print_queue(queue_t *);

queue_t *create_queue(unsigned int size)
{
  queue_t *new_queue;

  new_queue = (queue_t*)malloc(sizeof(queue_t) + sizeof(int) * size);
  if(new_queue == NULL)
  {
    return NULL;
  }
  new_queue->head = 0;
  new_queue->tail = 0;
  new_queue->size = size + 1;

  return new_queue;
}

int enqueue(queue_t *queue, int num)
{
  char buffer[BUFFER_SIZE] = "";
  if(is_full_queue(queue))
  {
    return -1;
  }
  queue->data[queue->tail] = num;
  queue->tail = (queue->tail + 1) % queue->size;

  //Display moving enqueu
  snprintf(buffer, BUFFER_SIZE, "enqueue %d\t: ", num);
  printf(buffer);
  print_queue(queue);
  printf("\n");

  return 0;
}

int dequeue(queue_t *queue)
{
  char buffer[BUFFER_SIZE] = "";
  int value = 0;
  if(is_empty_queue(queue))
  {
    return -1;
  }
  value = queue->data[queue->head];
  queue->head = (queue->head + 1) % queue->size;

  //Display moving dequeu
  printf("dequeue \t: ");
  print_queue(queue);
  snprintf(buffer, BUFFER_SIZE, " -> data : %d\n", value);
  printf(buffer);

  return 0;
}
void print_queue(queue_t *queue)
{
  char c[5] = "";
  printf("queue [");
  for(int i = 0; i < queue->size; i++)
  {
    if(is_used_range(queue, i))
    {
      sprintf(c, "%d", queue->data[i]);
    }
    else
    {
      strcpy(c, ".");
    }
    printf("%s ", c);
  }
  printf("]");
}
int is_used_range(queue_t *queue, int i)
{
  if((i >= queue->head && i < queue->tail) ||
     (queue->head > queue->tail && i >= queue->head && i > queue->tail) ||
     (queue->head > queue->tail && i <  queue->head && i < queue->tail))
  {
    return 1;
  }
  else
  {
    return 0;
  }
}


int main(void)
{
  queue_t *queue;

  if((queue = create_queue(QUEUE_SIZE)) == NULL)
  {
    fprintf(stderr, "Failed to create queue.\n");
    exit(EXIT_FAILURE);
  }
  enqueue(queue, 3);
  enqueue(queue, 2);
  dequeue(queue);

}
