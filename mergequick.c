#include "stdio.h"
#include "stdlib.h"
#include "mpi.h"
#include "math.h"
#include "memory.h"

#define intsize sizeof(int)
#define nodesize sizeof(node)
typedef struct node{
    int x;
    int y;
}node;

int p;					//number of processes.
int my_rank;
int t;
int m;
int size;
int *A, *B;
MPI_Status status;
FILE *fdA;

int main(argc, argv)
int argc;
char * *argv;
{
    int *a, *tmp;
    node *my_stack;
    int i, j, k, u, v, top = -1, turn;
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&p);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
    
    /* 如果是主进程(rank=0的进程),则进行读文件的操作,
    将数组读入内存
    */
    if(my_rank==0) {
        fdA=fopen("sortDataIn.txt","r");
        /* 读入数组的长度,并保存到size中 */
        fscanf(fdA,"%d", &size);

        A=(int*)malloc(intsize*size);
        B=(int*)malloc(intsize*size);
        
        /* 将数组的所有值读入,保存到A中 */
        for(i = 0; i < size; i ++) {
            fscanf(fdA, "%d", A+i);
        }
        
        fclose(fdA);
    }
    
    /* 广播数组的尺寸 */
    MPI_Bcast(&size,1,MPI_INT,0,MPI_COMM_WORLD);
    /* 设定数组划分的数目 */
    t=4;
    /* 获得实际利用的处理器个数 */
    p=t;
    /* 每个子段的长度 */
    m=size/t;
    /* a保存A中对应的子段,tmp用于暂存数据,my_stack用于快排 */
    a=(int *)malloc(intsize*m+4);
    tmp=(int *)malloc(intsize*m+4);
    my_stack=(node *)malloc(nodesize*m+4);
    
    /* 对主进程,获得自己的子段 */
    if (my_rank==0) {
        for(i=0;i<m;i++)
            a[i]=A[i];
        for (i=0;i<(size)%t;i++) {
            a[i+m]=A[i+m];
        }
        m = i;
    }
	/* 主进程向其他进程发送数据 */
    if (my_rank==0) {
        for(i=1;i<p;i++) {
            for(j=i*(size/t);j<(i+1)*(size/t);j++)
                tmp[(j%(size/t))]=A[j+(size%t)];        /* 将子段暂存在tmp中 */
            /* 将子段发送到相应的进程 */
            MPI_Send(tmp,size/t,MPI_INT,i,i,MPI_COMM_WORLD);
        }
    }
    else if (my_rank<p) {                           /* 对其他进程,从主进程接收数据 */
        MPI_Recv(a,m,MPI_INT,0,my_rank,MPI_COMM_WORLD,&status);
    }
    /* 各节点内部进行快排 */
    my_stack[++top].x = 0; my_stack[top].y = m;
    while (top >= 0) {
        u = my_stack[top].x; v=my_stack[top].y;
        top--;
        i = u; j = v-1; k = a[u]; turn = 1;
        while (i < j) {
            if (turn%2) {
                while (i < j && a[j] >= k) j--;
                if (i < j) {
                    a[i] = a[j];
                    turn = 0;
                }
            }
            else {
                while (i < j && a[i] <= k) i++;
                if (i < j) {
                    a[j] = a[i];
                    turn = 1;
                }
            }
        }
        a[i] = k;
        if (i < v-2) {
            my_stack[++top].x = i+1; my_stack[top].y = v;
        }
        if (i > u+1) {
            my_stack[++top].x = u; my_stack[top].y = i;
        }
    }
    /* 主进程从其他进程接收数据 */
    if (my_rank!=0 && my_rank<p) {
        MPI_Send(a,m,MPI_INT,0,0,MPI_COMM_WORLD);
    }
    else if (my_rank==0) {                           /* 对主进程,从其它进程接收数据 */
        for(i=1;i<p;i++) {
            MPI_Recv(tmp,m,MPI_INT,i,my_rank,MPI_COMM_WORLD,&status);
            
            for(j=i*(size/t);j<(i+1)*(size/t);j++)
                B[j+(size%t)]=tmp[j%(size/t)];        /* 将结果存储到B中 */
        }
        for(i=0;i<m;i++)
            B[i]=a[i];
    }
    /* 由主进程打印计算结果 */
    if (my_rank==0) {
        printf("Input of file \"sortDataIn.txt\"\n");
        printf("size:%d\n", size);
        for(i=0;i<size;i++) {
            printf("%d\t",A[i]);
        }
        printf("\n");
        printf("\nOutput after sort\n");
        for(i=0;i<size;i++) {
            printf("%d\t",B[i]);
        }
        printf("\n");
    }
    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
    //Environment_Finalize(a,b,c,tmp);
    return (0);
}