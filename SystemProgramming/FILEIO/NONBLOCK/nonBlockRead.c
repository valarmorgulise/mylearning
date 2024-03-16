#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main(void) {
  int fd = open("/dev/tty", O_RDONLY /*| O_NONBLOCK*/);
  if (fd < 0) {
    perror("OPEN /dev/tty");
    exit(1);
  }

  ssize_t n;
  char buf[10];
  n = read(fd, buf, 10);
  if (n < 0) {
    perror("READ /dev/tty");
    exit(1);
  } else {
    printf("read %ld bytes\n", n);
  }

  close(fd);
  return 0;
}
