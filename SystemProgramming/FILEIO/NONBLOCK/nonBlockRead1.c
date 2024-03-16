#include <asm-generic/errno-base.h>
#include <errno.h>
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
  while (1) {
    n = read(fd, buf, 10);
    if (~n) {
      printf("read %ld bytes\n", n);
      write(STDOUT_FILENO, buf, n);
      break;
    }
    if (errno != EAGAIN) {
      perror("READ /dev/tty");
      exit(1);
    }
    write(STDOUT_FILENO, "Try Try?\n", 9);
    sleep(1);
  }

  close(fd);
  return 0;
}
