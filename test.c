#include"mpi.h"
#include<stdio.h>

MPI_Status status;
int rank, size;
/*
int MPI_Gather_test(SendAddress, SendCount, SendDatatype,
						RecvAddress, RecvCount, RecvDatatype, Root, Comm)
MPI_INT SendAddress;
MPI_UNSIGNED SendCount;
MPI_Datatype SendDatatype;
MPI_INT RecvAddress;
MPI_UNSIGNED RecvCount;
MPI_Datatype RecvDatatype;
MPI_INT Root;
MPI_Comm comm;
{
	int i, tmp;
		MPI_Send(&SendAddress, SendCount, SendDatatype, Root, i, comm);
	if (rank == Root) {
		for (i = 0; i < RecvCount; i++) {
			MPI_Recv(&tmp, SendCount, RecvDatatype, i, i, comm, &status);
			RecvAddress[i] = tmp;
		}
	}
	return 0;
}

int MPI_Allgather_test(SendAddress, SendCount, SendDatatype,
						RecvAddress, RecvCount, RecvDatatype, Comm)
MPI_INT SendAddress;
MPI_UNSIGNED SendCount;
MPI_Datatype SendDatatype;
MPI_INT RecvAddress;
MPI_UNSIGNED RecvCount;
MPI_Datatype RecvDatatype;
MPI_Comm comm;
{
	MPI_Gather_test(SendAddress, SendCount, SendDatatype,
						RecvAddress, RecvCount, RecvDatatype, rank, Comm);
	return 0;
}
*/
int main(argc, argv)
int argc;
char * *argv;
{
	int i, j, senddata, recvdata[32];//
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	senddata = rank + 1;
	//MPI_Allgather_test(&senddata, 1, MPI_INT,
		//				&recvdata, 1, MPI_INT, MPI_COMM_WORLD);
	for (i = 0; i < size; i++) {
		printf("rank= %d, recvdata[%d]= %d\n", rank, i, recvdata[i]);
	}
	MPI_Finalize();
}