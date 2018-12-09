#include"mpi.h"
#include<stdio.h>

MPI_Status status;
int rank, size, recvdata[32];

int MPI_Gather_test(SendAddress, SendCount, SendDatatype,
						RecvAddress, RecvCount, RecvDatatype, Root, comm)
void *SendAddress;
int SendCount;
MPI_Datatype SendDatatype;
void *RecvAddress;
int RecvCount;
MPI_Datatype RecvDatatype;
int Root;
MPI_Comm comm;
{
	int i, tmp = 47;
	int *p;
        if (rank != Root) {
        	MPI_Send(&SendAddress, 1, MPI_INT, Root, 6, MPI_COMM_WORLD);
                printf("senddata= %d\n", *(int *)SendAddress);
        }
	else {
		for (i = 0; i < size; i++) {
                    if (i == Root) continue;
			MPI_Recv(&tmp, 1, MPI_INT, i, 6, MPI_COMM_WORLD, &status);
			printf("good, tmp= %d\n", (int)tmp);
			p = (int *)RecvAddress;
			p[i] = tmp;
		}
	}
	return 0;
}

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
	int i;
	for (i = 0; i < size; i++) {
		MPI_Gather_test(SendAddress, SendCount, SendDatatype,
							RecvAddress, RecvCount, RecvDatatype, i, comm);
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
	//MPI_Allgather_test(&senddata, 1, MPI_INT,
	//			&recvdata, 1, MPI_INT, MPI_COMM_WORLD);
        if (rank == 0)
        MPI_Send(&senddata, 1, MPI_INT, 1, 6, MPI_COMM_WORLD);
        else{
        MPI_Recv(&tmp, 1, MPI_INT, i, 6, MPI_COMM_WORLD, &status);
        recvdata[rank] = tmp;}
	for (i = 0; i < size; i++) {
		printf("rank= %d, recvdata[%d]= %d\n", rank, i, recvdata[i]);
	}
	MPI_Finalize();
	return (0);
}
