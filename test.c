#include"mpi.h"
#include<stdio.h>

MPI_Status status;
int rank, size, recvdata[32];

int MPI_Allgather_test(SendAddress, SendCount, SendDatatype,
						RecvAddress, RecvCount, RecvDatatype, comm)
void *SendAddress;
int SendCount;
MPI_Datatype SendDatatype;
void *RecvAddress;
int RecvCount;
MPI_Datatype RecvDatatype;
MPI_Comm comm;
{
	int i, j, tmp = 47, *p;
	for (i = 0; i < size; i++) {
		if (rank != i) {
        	MPI_Send(&SendAddress, 1, MPI_INT, i, 6, MPI_COMM_WORLD);
            printf("senddata= %d\n", *(int *)SendAddress);
        }
		else {
			for (j = 0; j < size; j++) {
                if (j == i) continue;
				MPI_Recv(&tmp, 1, MPI_INT, j, 6, MPI_COMM_WORLD, &status);
				printf("good, tmp= %d\n", (int)tmp);
				p = (int *)RecvAddress;
				p[i] = tmp;
			}
		}
	}
	return 0;
}

int main(argc, argv)
int argc;
char * *argv;
{
	int i, j, senddata, tmp;//
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	senddata = rank + 77;
	MPI_Allgather_test(&senddata, 1, MPI_INT, &recvdata, 1, MPI_INT, MPI_COMM_WORLD);
	for (i = 0; i < size; i++) {
		printf("rank= %d, recvdata[%d]= %d\n", rank, i, recvdata[i]);
	}
	MPI_Finalize();
	return (0);
}
