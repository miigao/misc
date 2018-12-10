#include"mpi.h"
#include<stdio.h>

MPI_Status status;
int rank, size, recvdata[32], recvdata2[32];
double starttime;
double endtime;
double time1;
double time2;


int main(argc, argv)
int argc;
char * *argv;
{
	int i, j, senddata, tmp, tag = 66;//
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	senddata = rank;
        if (rank == 0) {
            starttime = MPI_Wtime();
        }
        //My Allgather start.
        for (i = 0; i < size; i++) {
            if (rank != i) {
                    MPI_Send(&senddata, 1, MPI_INT, i, tag, MPI_COMM_WORLD);
            }
            else {
                for (j = 0; j < size; j++) {
                    if (j == i) {recvdata[j] = j; continue;}
                    MPI_Recv(&(recvdata[j]), 1, MPI_INT, j, tag, MPI_COMM_WORLD, &status);
                }
            }
        }
        //My Allgather end.
        if (rank == 0) {
            endtime = MPI_Wtime();
            printf("\nMy Allgather running time    = %f seconds\n",endtime-starttime);
        }
        if (rank == 0) {
            time1 = MPI_Wtime();
        }
        MPI_Allgather(&senddata, 1, MPI_INT, recvdata2, 1, MPI_INT, MPI_COMM_WORLD);
        if (rank == 0) {
            time2 = MPI_Wtime();
            printf("\nMPI_Allgather running time    = %f seconds\n",time2-time1);
        }
	for (i = 0; i < size; i++) {
		printf("rank= %d, recvdata[%d]= %d\n", rank, i, recvdata[i]);
	}
	MPI_Finalize();
	return (0);
}
