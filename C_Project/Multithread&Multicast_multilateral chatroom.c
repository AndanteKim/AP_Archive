#pragma comment(lib,"ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>
#include <ws2tcpip.h>
#include <process.h>
	HANDLE hThread[2];
	SOCKET UDPs;
	SOCKADDR_IN SRVAddr;
unsigned __stdcall func1(void *arg);
unsigned __stdcall func2(void *arg);

int main(){

	/*start window socket*/
	WSADATA wsa;
	WSAStartup(MAKEWORD(2,2), &wsa);

	/*create socket*/

	UDPs = socket(AF_INET,SOCK_DGRAM,0);
	if(UDPs == INVALID_SOCKET){
		printf("SOCKET ERROR!!\n");
		return -1;
	}

	/*struct of server address*/
	
	SRVAddr.sin_family = AF_INET;
	SRVAddr.sin_port = htons(22222);
	/*This can be changed depending on Internet address*/
	SRVAddr.sin_addr.s_addr = inet_addr("192.168.222.129");


	/*bind address*/
	int error=0;
	error=bind(UDPs,(sockaddr *)(&SRVAddr),sizeof(SRVAddr));
	if(error == SOCKET_ERROR){
		printf("BIND ERROR!!\n");
		return -1;
	}

	hThread[0] = (HANDLE)_beginthreadex(NULL,0,func1,NULL,0,NULL);
	hThread[1] = (HANDLE)_beginthreadex(NULL,0,func2,NULL,0,NULL);
	
	WaitForMultipleObjects(2,hThread,TRUE,INFINITE);

	/*terminate socket*/
	closesocket(UDPs);

	/*end the window socket*/
	WSACleanup();
	return 0;
}

unsigned __stdcall func1(void *arg)
{

	/*Multicast TTL*/
	int ttl = 128;
	setsockopt(UDPs,IPPROTO_IP,IP_MULTICAST_TTL,(char*)ttl,sizeof(ttl));


	/*The address struct of who you communicate with*/
	/*Note : the port number or address can be different depending on environment*/
	SOCKADDR_IN sendAddr;
	sendAddr.sin_addr.s_addr = inet_addr("233.3.3.3");
	sendAddr.sin_port = htons(22222);
	sendAddr.sin_family = AF_INET;


	char sendBuf[512];
	memset(sendBuf,0,sizeof(sendBuf));
	int error=0;
	while(1)
	{
	printf("[Input] > ");
	gets(sendBuf);
	/*send data*/
	error=sendto(UDPs,sendBuf,sizeof(sendBuf),0,(sockaddr*)(&sendAddr),sizeof(sendAddr));
	if(error == SOCKET_ERROR){
		printf("SENDTO ERROR!!\n");
		return -1;
	}
	if(strcmp(sendBuf,"exit") == 0)
	{
		sprintf(sendBuf,"%s left the chatroom.",inet_ntoa(SRVAddr.sin_addr));
		sendto(UDPs,sendBuf,sizeof(sendBuf),0,(sockaddr*)(&sendAddr),sizeof(sendAddr));
		closesocket(UDPs);
		printf("Program ended!\n");
		break;
	}

	}
	
	return 0;
}

unsigned __stdcall func2(void *arg)
{

	struct ip_mreq mt;
	/* Note : Internet address is always different depending on device*/
	mt.imr_interface.s_addr = inet_addr("192.168.222.129");
	mt.imr_multiaddr.s_addr = inet_addr("233.3.3.3");


	setsockopt(UDPs,IPPROTO_IP,IP_ADD_MEMBERSHIP,(char*)&mt,sizeof(mt));

	/*The address struct of who you communicate with*/
	SOCKADDR_IN recvAddr;
	int recvLen = sizeof(recvAddr);

	/*receive data*/
	char recvBuf[512];
	memset(recvBuf,0,sizeof(recvBuf));
	int error=0;
	while(1){
	error=recvfrom(UDPs,recvBuf,sizeof(recvBuf),0,(sockaddr*)(&recvAddr),&recvLen);
	if(error == SOCKET_ERROR){
		printf("RECVFROM ERROR!!\n");
		return -1;
	}
	printf("[UDP %s:%d]\n", inet_ntoa(recvAddr.sin_addr), ntohs(recvAddr.sin_port));
	printf("[Output] > %s\n", recvBuf);

	}

	return 0;
}