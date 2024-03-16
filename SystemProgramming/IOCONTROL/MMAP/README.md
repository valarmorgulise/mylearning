# mmap
mmap可以把磁盘文件的一部分直接映射到内存，这样文件中的位置直接有对应的内存地址，对文件的读写可以直接用指针来做而不需要read/write函数

``` c 
#include <sys/mman.h>
    void *mmap(void *addr, size_t len, int prot, int flag, int filedes, off_t off);
    int munmap(void *addr, size_t len);
```

``` c
    void *mmap(void *addr, size_t len, int prot, int flag, int filedes, off_t off);
addr
如果addr参数为NULL，内核会自己在进程地址空
间中选择合适的地址建立映射。如果addr不 是NULL
则给内核一个提示，应该从什么地址开始映射，内核
会选择addr之上的某个合适的地址开始映射。建立映
射后，真正的映射首地址通过返回值可以得到。

len:
是需要映射的那一部分文件的长度。off参数是
从文件的什么位置开始映射，必须是页大小的整数倍

filedes:
该文件的描述符

prot:有四种取值
PROT EXEC表示映射的这一段可执行，例如映射共享库
PROT READ表示映射的这一段可读
PROT WRITE表示映射的这一段可写
PROT_NONE表示映射的这一段不可访问
flag:
MAP_SHARED多个进程对相同文件映射共享
MAP_PRIVATE多个进程对相同文件映射不共享
```
od -tx1 -tc test.txt (16进制数)
