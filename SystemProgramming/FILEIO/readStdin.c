#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  char buf[20];
  int n, i;
  n = read(STDIN_FILENO, buf, 10);
  if (n < 0) {
    perror("READ STDIN");
    exit(1);
  }
  printf("read %d bytes\n", n);
  write(STDOUT_FILENO, buf, n);
  write(STDOUT_FILENO, "\n", n);
  putchar(10);

  return 0;
}
