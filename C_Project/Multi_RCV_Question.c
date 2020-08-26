#pragma comment(lib,"ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>
#include <ws2tcpip.h>

typedef struct msg{
	int a_num;
	char q_str[512];
}_msg;


int main(){

	/*load dll winsocket*/
	WSADATA wsa;
	WSAStartup(MAKEWORD(2,2), &wsa);

	/*create socket*/
	SOCKET s;
	s = socket(AF_INET,SOCK_DGRAM,0);
	if(s == INVALID_SOCKET){
		printf("SOCKET ERROR!!\n");
		return -1;
	}

	/*struct of server address*/
	//Note : need to set ip address correctly depending on a device
	SOCKADDR_IN SRVAddr;
	SRVAddr.sin_family = AF_INET;
	SRVAddr.sin_port = htons(22222);
	SRVAddr.sin_addr.s_addr = inet_addr("192.168.222.134");


	/*bind address*/
	int error=0;
	error=bind(s,(sockaddr *)(&SRVAddr),sizeof(SRVAddr));
	if(error == SOCKET_ERROR){
		printf("BIND ERROR!!\n");
		return -1;
	}
	/*register multicast*/
	struct ip_mreq mr;
	mr.imr_interface.s_addr = inet_addr("192.168.222.134");
	mr.imr_multiaddr.s_addr = inet_addr("233.3.3.3");

	setsockopt(s,IPPROTO_IP,IP_ADD_MEMBERSHIP,(char*)&mr,sizeof(mr));

	/*address struct of who communicates with*/
	SOCKADDR_IN recvAddr;
	int recvLen = sizeof(recvAddr);

	/*receive data*/
	_msg msg;
	memset((char*)&msg,0,sizeof(msg));

	error=recvfrom(s,(char*)&msg,sizeof(msg),0,(sockaddr*)(&recvAddr),&recvLen);
	if(error == SOCKET_ERROR){
		printf("RECVFROM ERROR!!\n");
		return -1;
	}
	printf("%s", msg.q_str);
	printf("\nInput Answer(1-4): ");
	int an=0;
	scanf("%d", &an);



	memset((char*)&msg,0,sizeof(msg));
	msg.a_num = an;

error=sendto(s,(char*)&msg,sizeof(msg),0,(sockaddr*)(&recvAddr),recvLen);
	if(error == SOCKET_ERROR){
		printf("SENDTO ERROR!!\n");
		return -1;
	}

	/*leave multicast group*/
	setsockopt(s,IPPROTO_IP,IP_DROP_MEMBERSHIP,(char*)&mr, sizeof(mr));

	/*close socket*/
	closesocket(s);

	/*unload dll*/
	WSACleanup();
	return 0;
}