#include "stdio.h"
#include "stdlib.h"
#include "mpi.h"
#include "omp.h"
#include "math.h"
#include "memory.h"

#define a(x,y) a[x*m+y]
#define b(x,y) b[x*m+y]
#define c(x,y) c[x*m+y]
#define tmp(x,y) tmp[x*m+y]
#define A(x,y) A[x*size+y]
#define B(x,y) B[x*size+y]
#define C(x,y) C[x*size+y]
#define floatsize sizeof(float)

int t;
int m;
float *A, *B, *C;
int p;					//number of processes.
int my_rank;
int src;
int dst;
int size;
int N;
MPI_Status status;
double time1, time2;
FILE *fdAB;

/* 运行结束前,调用本函数释放内存空间 */
void Environment_Finalize(float *a,float *b, float *c, float *d)
{
    free(a);
    free(b);
    free(c);
    free(d);
}

int main(argc, argv)
int argc;
char * *argv;
{
    float *a, *b, *c, *tmp;
    int i, j, k, u, v, n_threads, tid;
    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&p);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);

    /* 如果是主进程(rank=0的进程),则进行读文件的操作,
    将矩阵读入内存
    */
    if(my_rank==0)
    {
        time1=MPI_Wtime();
        fdAB=fopen("foxDataIn.txt","r");
        /* 读入矩阵的行数和列数,并保存到size和N中 */
        fscanf(fdAB,"%d %d", &size, &N);
        /* 判断是否是方阵,如果不是,程序退出 */
        if(size != N)
        {
            puts("The input is error!");
            exit(0);
        }
        A=(float*)malloc(floatsize*size*size);
        B=(float*)malloc(floatsize*size*size);
        C=(float*)malloc(floatsize*size*size);
        /* 将矩阵的所有值读入,保存到A, B中 */
        for(i = 0; i < size; i ++)
        {
            for(j = 0; j < size; j ++) fscanf(fdAB, "%f", A+i*size+j);
        }
        for(i = 0; i < size; i ++)
        {
            for(j = 0; j < size; j ++) fscanf(fdAB, "%f", B+i*size+j);
        }
        fclose(fdAB);
    }
    /* 广播矩阵的尺寸 */
    MPI_Bcast(&size,1,MPI_INT,0,MPI_COMM_WORLD);
	
    /* 获得棋盘划分的数目 */
    t=(int)sqrt(p);
    if (t>size)
        t=size;
    if(size%t!=0)
        for(;;) {
            t--;
            if(size%t==0) break;
        }
    /* 获得实际利用的处理器个数 */
    p=t*t;
    /* 每个子方阵的尺寸 */
    m=size/t;
	
    /* a保存A中对应的子方阵,b保存B中对应的子方阵,c保存相乘的结果,tmp用于暂存数据 */
    a=(float *)malloc(floatsize*m*m);
    b=(float *)malloc(floatsize*m*m);
    c=(float *)malloc(floatsize*m*m);
    tmp=(float *)malloc(floatsize*m*m);
	
    for(i=0;i<m;i++)
        for(j=0;j<m;j++)
            c(i,j)=0;
    if (a==NULL||b==NULL)
    printf("allocate space  fail!");
	
    /* 对主进程,获得自己的子方阵 */
    if (my_rank==0)
    {
        for(i=0;i<m;i++)
            for(j=0;j<m;j++) {
                a(i,j)=A(i,j);
                b(i,j)=B(i,j);
            }
    }
	
    /* 主进程向其他进程发送数据(A部分) */
    if (my_rank==0)
    {
        for(i=1;i<p;i++)
        {
            v=i/t;                                /* 子方阵的行号 */
            u=i%t;                                /* 子方阵的列号 */

            for(j=v*m;j<(v+1)*m;j++)
                for(k=u*m;k<(u+1)*m;k++)
                    tmp((j%m),(k%m))=A(j,k);        /* 将子方阵暂存在tmp中 */

                                                  /* 将子方阵发送到相应的进程 */
            MPI_Send(tmp,m*m,MPI_FLOAT,i,i,MPI_COMM_WORLD);
        }
    }
    else if (my_rank<p) {                           /* 对其他进程,从主进程接收数据 */
        MPI_Recv(a,m*m,MPI_FLOAT,0,my_rank,MPI_COMM_WORLD,&status);
    }
    /* 主进程向其他进程发送数据(B部分) */
    if (my_rank==0)
    {
        for(i=1;i<p;i++)
        {
            v=i/t;                                /* 子方阵的行号 */
            u=i%t;                                /* 子方阵的列号 */

            for(j=v*m;j<(v+1)*m;j++)
                for(k=u*m;k<(u+1)*m;k++)
                    tmp((j%m),(k%m))=B(j,k);        /* 将子方阵暂存在tmp中 */

                                                  /* 将子方阵发送到相应的进程 */
            MPI_Send(tmp,m*m,MPI_FLOAT,i,i,MPI_COMM_WORLD);
        }
    }
    else if (my_rank<p) {                           /* 对其他进程,从主进程接收数据 */
        MPI_Recv(b,m*m,MPI_FLOAT,0,my_rank,MPI_COMM_WORLD,&status);
    }
 
    for (i = 0; i < t; i++) {					/* 进行t轮操作 */
        if (my_rank%t == (my_rank/t + i)%t && my_rank<p) { /* 该轮需要发送 */
            for (j = 0; j < t; j++) {
                dst = (my_rank/t)*t + j;
                if (dst == my_rank) continue;
                MPI_Send(a,m*m,MPI_FLOAT,dst,dst,MPI_COMM_WORLD);
            }
            
            for (j = 0; j < m; j++) {
                for (k = 0; k < m; k++) {
                    tmp(j,k)=a(j,k);
                }
            }
        }
        else if (my_rank<p) {						/* 该轮需要接收 */
            src = (my_rank/t)*t + (my_rank/t + i)%t;
            MPI_Recv(tmp,m*m,MPI_FLOAT,src,my_rank,MPI_COMM_WORLD,&status);
        }
    #pragma omp parallel shared (c, tmp, b) private (tid, j, k, u, n_threads)
    {
        n_threads=omp_get_num_threads();
        tid=omp_get_thread_num();
        if (my_rank<p) {
            for (j = 0+tid; j < m; j+=n_threads) {
                for (k = 0; k < m; k++) {
                    for (u = 0; u < m; u++) {
                        c(j,k) += (tmp(j,u))*(b(u,k));
                    }
                }
            }
        }

    }
        /* 轮转B矩阵,奇数行先发后收,偶数行先收后发 */
        if (my_rank<p && i < t-1) {
            if ((my_rank/t)%2) {
                dst = (my_rank + p - t)%p;
                MPI_Send(b,m*m,MPI_FLOAT,dst,dst,MPI_COMM_WORLD);
                src = (my_rank + t)%p;
                MPI_Recv(b,m*m,MPI_FLOAT,src,my_rank,MPI_COMM_WORLD,&status);
            }
            else {
                src = (my_rank + t)%p;
                MPI_Recv(tmp,m*m,MPI_FLOAT,src,my_rank,MPI_COMM_WORLD,&status);
                dst = (my_rank + p - t)%p;
                MPI_Send(b,m*m,MPI_FLOAT,dst,dst,MPI_COMM_WORLD);
                //memcpy(b, tmp, sizeof(b));
                for (j = 0; j < m; j++) {
                    for (k = 0; k < m; k++) {
                        b(j,k)=tmp(j,k);
                    }
                }
            }
        }
    }
	
	/* 主进程从其他进程接收数据(C部分) */
    if (my_rank!=0 && my_rank<p) {
        MPI_Send(c,m*m,MPI_FLOAT,0,0,MPI_COMM_WORLD);
    }
    else if (my_rank==0) {                           /* 对主进程,从其它进程接收数据 */
        for(i=1;i<p;i++) {
            MPI_Recv(tmp,m*m,MPI_FLOAT,i,my_rank,MPI_COMM_WORLD,&status);
            v=i/t;                                /* 子方阵的行号 */
            u=i%t;                                /* 子方阵的列号 */

            for(j=v*m;j<(v+1)*m;j++)
                for(k=u*m;k<(u+1)*m;k++)
                    C(j,k)=tmp((j%m),(k%m));        /* 将结果存储到C中 */
        }
        for(i=0;i<m;i++)
            for(j=0;j<m;j++) {
                C(i,j)=c(i,j);
            }
        time2=MPI_Wtime();
    }
    
    /* 由主进程打印计算结果 */
    if (my_rank==-1) {
        printf("Input of file \"foxDataIn.txt\"\n");
        printf("%d\t%d\n", size, size);
        for(i=0;i<size;i++) {
            for(j=0;j<size;j++) printf("%f\t",A(i,j));
            printf("\n");
        }
        printf("\n");
        for(i=0;i<size;i++) {
            for(j=0;j<size;j++) printf("%f\t",B(i,j));
            printf("\n");
        }
        printf("\nOutput of Matrix A*B\n");
        for(i=0;i<size;i++) {
            for(j=0;j<size;j++) printf("%f\t",C(i,j));
            printf("\n");
        }
    }
    /* 时间信息 */
    if (my_rank==0) {
        printf("time: %f seconds\n", time2-time1);
    }

    MPI_Barrier(MPI_COMM_WORLD);
    MPI_Finalize();
    Environment_Finalize(a,b,c,tmp);
    return (0);
}
