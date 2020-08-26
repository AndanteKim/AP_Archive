/*set preprocess*/
#pragma comment(lib, "ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>
#include <time.h>

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

	/* activate broadcast*/
	BOOL opt = TRUE;
	setsockopt(s,SOL_SOCKET,SO_BROADCAST,(char*)&opt,sizeof(opt));

	/*sending data*/
	SOCKADDR_IN SRVaddr;
	memset(&SRVaddr, 0, sizeof(SRVaddr));

	SRVaddr.sin_addr.s_addr = inet_addr("192.168.91.255");
	SRVaddr.sin_port = htons(12345);
	SRVaddr.sin_family = AF_INET;

	char sendbuf[1024];
	memset(sendbuf,0,sizeof(sendbuf));
	time_t tm;
	struct tm * lt;
	int sendsize=0;
	int i = 0;

	while(i<10){
		time(&tm);
		lt = localtime(&tm);
		sprintf(sendbuf, "%d년 %d월 %d일 %d시 %d분 %d초\n",
		lt->tm_year+1900, lt->tm_mon+1, lt->tm_mday, lt->tm_hour, lt->tm_min,
		lt->tm_sec);

	sendto(s,sendbuf,strlen(sendbuf),0,(SOCKADDR*)&SRVaddr,sizeof(SRVaddr));
		printf("Number %d send!\n", i+1);
		i++;
		Sleep(1000);
	}
//	printf("The size of sending data : %d\n", sendsize);

	/*close socket*/
	closesocket(s);

	/*unload dll */
	WSACleanup();

	return 0;
}
