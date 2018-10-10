typedef struct stack{
  int top;
  int size;
  int data[1];
}stack_t;

#define is_empty(stack) ((stack)->top == 0)
#define is_full(stack)  ((stack)->top == (stack)->size)
#define top_read(stack) ((stack)->top)

#define init_stack(stack) ((stack)->top = 0)

extern stack_t *create_stack(unsigned int size);
extern void push(stack_t *stack, int num);
extern int pop(stack_t *stack);
