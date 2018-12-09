#include"mpi.h"
#include<stdio.h>

MPI_Status status;
int rank, size, recvdata[32];


int main(argc, argv)
int argc;
char * *argv;
{
	int i, j, senddata, tmp, tag = 66;//
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	senddata = rank;
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
	for (i = 0; i < size; i++) {
		printf("rank= %d, recvdata[%d]= %d\n", rank, i, recvdata[i]);
	}
	MPI_Finalize();
	return (0);
}
