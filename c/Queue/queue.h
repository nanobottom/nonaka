typedef struct queue{
  int head;
  int tail;
  int size;
  int data[1];
}queue_t;

#define is_empty_queue(queue) ((queue)->head == (queue)->tail)
#define is_full_queue(queue)  (((queue)->tail + 1) % (queue)->size == (queue)->head)
#define init_queue(queue)     {(queue)->head = 0; (queue)->tail = 0;}

extern queue_t *create_queue(unsigned int size);
extern int enqueue(queue_t *queue, int num);
extern int dequeue(queue_t *queue);
