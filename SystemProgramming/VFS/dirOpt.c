#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>


int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("usage:cmd + path");
        return 1;
    }

    DIR *dir;
    struct dirent *dp;
    if (!(dir == opendir(argv[1]))) {
        perror("opendir");
        exit(1);
    }
    while (dp = readdir(dir)) 
        printf("%s ", dp->d_name);
    putchar(10);
    closedir(dir);
    return 0;
}
