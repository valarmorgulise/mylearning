#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
  int fd = open("test.txt", O_RDWR);
  if (fd < 0) {
    perror("open file");
    exit(1);
  }
  int *p = mmap(NULL, 6, PROT_WRITE, MAP_SHARED, fd, 0);
  ((int *)(((char *)p) + 1))[0] = 0x30313233;
  // p[0] = 0x30313233;
  munmap(p, 6);
  return 0;
}
