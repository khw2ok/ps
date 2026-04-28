#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node *prev;
  struct Node *next;
} Node;

typedef struct {
  struct Node *front;
  struct Node *rear;
  int length;
} Queue;

void enqueue(Queue *q, int data) {
  //Node new = {data, q -> rear, NULL};
  Node *new = (Node*)malloc(sizeof(Node));
  new -> data = data;
  new -> prev = q -> rear;
  new -> next = NULL;

  q -> length++;

  if (q -> front == NULL) {
    q -> front = new;
    q -> rear = new;
    return;
  }

  q -> rear -> next = new;
  q -> rear = new;
}

int dequeue(Queue *q) {
  if (q -> front == NULL) return -1;

  Node *del = q -> front;
  int data = del -> data;

  q -> length--;

  q -> front = q -> front -> next;
  free(del);

  if (q -> front) q -> front -> prev = NULL;
  else q -> rear = NULL;

  return data;
}

int main() {
  int n, k, i;

  Queue q = {NULL, NULL, 0};
  int visited[100002] = {0};
  int t = 0;
  int cur;
  int qlen;

  scanf("%d %d", &n, &k);

  enqueue(&q, n);
  visited[n] = 1;

  while (!visited[k]) {
    qlen = q.length;

    for (i=0; i<qlen; i++) {
      cur = dequeue(&q);

      if (cur-1 >= 0 && !visited[cur-1]) {
        enqueue(&q, cur-1);
        visited[cur-1] = 1;
      }
      if (cur+1 <= 100000 && !visited[cur+1]) {
        enqueue(&q, cur+1);
        visited[cur+1] = 1;
      }
      if (cur*2 <= 100000 && !visited[cur*2]) {
        enqueue(&q, cur*2);
        visited[cur*2] = 1;
      }
    }

    t++;
  }

  printf("%d\n", t);

  return 0;
}
