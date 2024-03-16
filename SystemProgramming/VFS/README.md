# 虚拟文件系统


![avatar](https://gitee.com/valarmorgulis1/picture/blob/master/block.png)

文件系统中存储的最小单位是块 (Block)
一个块究竟多大是在格式化时确定的，例如mke2fs的-b选项可以设定块大小为1024、2048或4096字节。

启动块 (Boot Block)
大小就是1KB，由PC标准规定，用来存储磁盘分区信息和启动信息，任何文件系统都不能使用该块

NTFS, FATS32

超级块(Super Block)
描述整个分区的文件系统信息，例如块大小、文件系统版本号、上次mount的时间等等.超级块在每个块组的开头都有一份拷贝。
块组描述符表 (GDT，Group Descriptor Table)
由很多块组描述符组成，整个分区分成多少个块组就对应有多少个块组描述符。每个块
组描述符存储一个块组的描述信息，包括inode表哪里开始，数据块从哪里开始，空闲
的inode和数据块还有多少个等。块组描述符表在每个块组的开头也都有一份拷贝，这
些信息是非常重要的，因此它们都有多份拷贝。

块位图 (Block Bitmap)
块位图就是用来描述整个块组中哪些块已用哪些块空闲的，本身占一个块。其中的每个
bit代表本块组中的一个块，这个bit为1表示该块已用，这个bit为0表示该块空闲可用

块组描述符表(GDT，Group Descriptor Table)
由很多块组描述符组成，整个分区分成多少个块组就对应有多少个块组描述符。
每个块组描述符存储一个块组的描述信息，包括inode表哪里开始，数据块从哪里开始，空闲
的inode和数据块还有多少个等。块组描述符表在每个块组的开头也都有一份拷贝，这
些信息是非常重要的，因此它们都有多份拷贝。

inode位图(inode Bitmap)
和块位图类似，本身占一个块，其中每个bit表示一个inode是否空闲可用

inode表(inode Table)
文件类型(常规、目录、符号链接等)，权限，文件大小，创建/修改/访问时间等信息
存在inode中，每个文件都有一个inode。

数据块(Data Block)
常规文件:文件的数据存储在数据块中。
目录:该目录下的所有文件名和目录名存储在数据块中。(注意:文件名保存在它所在目录的数据块中，其它信息都保存在该文件的inode中)
符号链接，如果目标路径名较短则直接保存在inode中以便更快地查找，否则分配一个
数据块来保存
设备文件、FIFO和socket等特殊文件: 没有数据块，设备文件的主设备号和次设备号
保存在inode中

# stat
读取文件的inode，然后把inode中的各种文件属性填入一个struct stat结构体传出
给调用者。stat(1)命令是基于stat函数实现的。stat需要根据传入的文件路径找到inode

``` c
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <unist.h>

    int stat(const char *path, struct stat * buf);
    int fstat(int fd, struct stat *buf);
    int lstat(const char *path, struct stat *buf);

```

## access

## chmod fchmod
chmod 修改文件， 
fchmod fd 文件描述符

##truncate
