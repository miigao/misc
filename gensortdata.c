#include<stdio.h>

FILE *fd;
int main() {
    int i;
    fd = fopen("sortDataIn.txt","w");
    fprintf(fd, "100000\n");
    for (i = 0; i < 100000; i++) {
        fprintf(fd, "%d ", i%1000);
    }
    fclose(fd);
    return 0;
}
