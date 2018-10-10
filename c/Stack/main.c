#include <stdlib.h>
#include <stdio.h>
#include "stack.h"

#define STACK_SIZE 100
#define BUFFER_SIZE 256
stack_t *create_stack(unsigned int size)
{
  stack_t *new_stack;

  new_stack = (stack_t*)malloc(sizeof(stack_t) + sizeof(int) * (size -1));
  if(new_stack == NULL)
  {
    return NULL;
  }
  new_stack->top = 0;
  new_stack->size = size;

  return new_stack;
}

void push(stack_t *stack, int num)
{
  char buffer[BUFFER_SIZE] = "";

  if(is_full(stack))
  {
    fprintf(stderr, "Stack overflow.\n");
    exit(EXIT_FAILURE);
  }
  stack->data[stack->top++] = num;

  //Display stack status.
  snprintf(buffer, BUFFER_SIZE, "(push %d) stack : [", num);
  printf(buffer);
  for (int i = 0; i < stack->top; i++)
  {
    printf("%d ", stack->data[i]);
  }
  printf("]\n");

}

int pop(stack_t *stack)
{
  char buffer[BUFFER_SIZE] = "";
  if(is_empty(stack))
  {
    fprintf(stderr, "Stack underflow.\n");
    exit(EXIT_FAILURE);
  }
  
  //Display stack status.
  printf("(pop)    stack : [");
  for(int i = 0; i < stack->top - 1; i++)
  {
    printf("%d ", stack->data[i]);
  }
  snprintf(buffer, BUFFER_SIZE, "]\t->data : %d\n", stack->data[stack->top - 1]);
  printf(buffer);
  return stack->data[--stack->top];
}

int main(void)
{
  stack_t *stack;

  if((stack = create_stack(STACK_SIZE)) == NULL)
  {
    fprintf(stderr, "Cannot create new stack.\n");
    exit(EXIT_FAILURE);
  }
  push(stack, 3);
  push(stack, 1);
  push(stack, 4);
  pop(stack);
  push(stack, 5);
  pop(stack);
  push(stack, 1);
  return EXIT_SUCCESS;
}

