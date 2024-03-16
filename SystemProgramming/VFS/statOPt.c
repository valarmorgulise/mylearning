#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    struct stat st;
    if (argc < 2) {
        printf("usage: cmd + filename/dirname\n");
        exit(1);
    }
    stat(argv[1], &st);
    if (S_ISDIR(st.st_mode)) {
        printf("directory\n");
    } else {
        printf("othre file type\n");
    }
    switch (st.st_mode & S_IFMT) {
        case S_IFREG:
            printf("regular file\n");
            break;
        case S_IFDIR:
            printf("directory file\n");
            break;
        case S_IFCHR:
            printf("charactor file\n");
            break;
        default:
            printf("other file type\n");
    }
    return 0;
}
