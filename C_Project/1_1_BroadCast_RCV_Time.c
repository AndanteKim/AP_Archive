#pragma comment(lib, "ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>

int main()
{
	WSADATA wsa;
	
	/* load dll winsocket*/ 
	WSAStartup( MAKEWORD(2,2) ,&wsa);

	/* create socket*/
	SOCKET s;
	s = socket(AF_INET, SOCK_DGRAM,0);
	if(s == INVALID_SOCKET){
		printf("socket error!\n");
		return -1;
	}
	
	/* bind address*/
	//struct sockaddr_in
	SOCKADDR_IN SRVaddr;
	memset(&SRVaddr, 0, sizeof(SRVaddr));

	SRVaddr.sin_family = AF_INET;
	SRVaddr.sin_port = htons(12345);
	SRVaddr.sin_addr.s_addr = inet_addr("192.168.91.132");
	//SRVaddr.sin_addr.S_un.S_addr = "IP address";

	int errch = 0;
	errch = bind(s, (SOCKADDR*)&SRVaddr, sizeof(SRVaddr));
	if(errch == SOCKET_ERROR){
		printf("bind error!\n");
		return -1;
	}
	
	/* receiving data */
	char recvbuf[1024];
	memset(recvbuf, 0, sizeof(recvbuf));
	
	SOCKADDR_IN CLTaddr;
	int CLTlen = sizeof(CLTaddr);
	memset(&CLTaddr, 0, CLTlen);

	int recvlen=0;

	/* set receiving timeout about survey as 5000s around 1 hour*/
	int opt=5000;
	setsockopt(s,SOL_SOCKET,SO_RCVTIMEO,(char*)&opt,sizeof(opt));

	while(1)
	{
		recvlen = recvfrom(s,recvbuf,sizeof(recvbuf),0,
				   (SOCKADDR*)&CLTaddr, &CLTlen);
		if(recvlen == SOCKET_ERROR)
			break;

		printf("receive data  : %s\n", recvbuf);
	}
	/*close socket and unload dll */
	closesocket(s);
	WSACleanup();
	return 0;
}
