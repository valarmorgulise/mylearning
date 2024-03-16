#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

typedef struct Vector {
  int *data;
  int size, count;
} Vector;

Vector *getNewVector(int n) {
  Vector *p = (Vector *)malloc(sizeof(Vector));
  p->size = n;
  p->count = 0;
  p->data = (int *)malloc(sizeof(int) * n);
  return p;
}

int expand(Vector *v) {
  if (v == NULL)
    return 0;
  printf("expand v from %d to %d\n", v->size, v->size * 2);
  int *p = (int *)realloc(v->data, sizeof(int) * 2 * v->size);
  if (p == NULL)
    return 0;
  v->data = p;
  v->size *= 2;
  return 1;
}

int insert(Vector *v, int pos, int val) {
  if (v->count == v->size && !expand(v))
    return 0;
  if (pos < 0 || pos > v->count)
    return 0;
  for (int i = v->count - 1; i >= pos; --i) {
    v->data[i + 1] = v->data[i];
  }
  v->data[pos] = val;
  v->count += 1;
  return 1;
}

int erase(Vector *v, int pos) {
  if (pos < 0 || pos >= v->count)
    return 0;
  for (int i = pos + 1; i < v->count; ++i) {
    v->data[i - 1] = v->data[i];
  }
  v->count -= 1;
  return 1;
}

void output_vector(Vector *v) {
  int len = 0;
  for (int i = 0; i < v->size; ++i) {
    len += printf("%5d", i);
  }
  printf("\n");
  for (int i = 0; i < len; ++i)
    printf("-");
  printf("\n");
  for (int i = 0; i < v->count; ++i) {
    printf("%5d", v->data[i]);
  }
  printf("\n");
  return;
}

void clear(Vector *vec) {
  if (vec == NULL)
    return;
  free(vec->data);
  free(vec);
  return;
}

int main() {
  srand(time(0));
#define MAX_OP 20
  Vector *v = getNewVector(2);
  for (int i = 0; i < MAX_OP; ++i) {
    int op = rand() % 4, pos, val, ret;
    switch (op) {
    case 0:
    case 1:
    case 2:
      pos = rand() % (v->count + 2);
      val = rand() % 100;
      ret = insert(v, pos, val);
      printf("insert %d at %d to vector = %d\n", val, pos, ret);
      break;
    case 3:
      pos = rand() % (v->count + 2);
      ret = erase(v, pos);
      printf("erase item at %d in vector = %d\n", pos, ret);
      break;
    }
    output_vector(v);
  }
  clear(v);
  return 0;
}
