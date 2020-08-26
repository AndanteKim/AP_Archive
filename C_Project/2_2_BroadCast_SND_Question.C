/*set preprocess*/
#pragma comment(lib, "ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>

int main(){
	/* load dll */
	WSADATA wsa;
	WSAStartup(MAKEWORD(2,2), &wsa);

	/*create socket*/
	SOCKET s;
	s = socket(AF_INET, SOCK_DGRAM, 0);
	if(s == INVALID_SOCKET){
		printf("socket error!\n");
		return -1;
	}

	/*activate broadcast*/
	BOOL opt = TRUE;
	setsockopt(s,SOL_SOCKET,SO_BROADCAST,(char*)&opt,sizeof(opt));

	/*send data*/
	SOCKADDR_IN SRVaddr;
	memset(&SRVaddr, 0, sizeof(SRVaddr));

	SRVaddr.sin_addr.s_addr = inet_addr("192.168.91.255");
	SRVaddr.sin_port = htons(12345);
	SRVaddr.sin_family = AF_INET;

	char sendbuf[1024];
	memset(sendbuf,0,sizeof(sendbuf));

	sprintf(sendbuf,"[Question] What job best fits your life? \n1.Programmer\n2.Network Engineer\n3.System Engineer\n4.System Security Administrator\n");

	sendto(s,sendbuf,strlen(sendbuf),0,(SOCKADDR*)&SRVaddr,sizeof(SRVaddr));
	
	int result=0;
	int errch=0;

	int timeopt=10000;
	setsockopt(s,SOL_SOCKET,SO_RCVTIMEO, (char*)&timeopt,sizeof(timeopt));

	int data[5]={0,0,0,0,0};

	while(1)
	{
		errch = recvfrom(s,(char*)&result,sizeof(result),0,NULL,0);
		if(errch == SOCKET_ERROR)
			break;
		printf("%d\n", result);
		data[result]++;
	}
	int i=1;

	/*show the result of survey*/
	printf("################The Result of Survey#####################\n");
	for(;i<5;i++)
	{
		printf("Number %d : %d \n", i, data[i]);
	}
	

	/*close socket*/
	closesocket(s);

	/*unload dll */
	WSACleanup();

	return 0;
}
