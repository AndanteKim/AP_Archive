#pragma comment(lib,"ws2_32.lib")
#include <winsock2.h>
#include <stdio.h>
#include <ws2tcpip.h>

typedef struct msg{
	int a_num;
	char q_str[512];
}_msg;

int main()
{
	/*load winsocket*/
	WSADATA wsa;
	WSAStartup(MAKEWORD(2,2),&wsa);
	
	/*create socket*/
	SOCKET s;
	s=socket(AF_INET, SOCK_DGRAM,0);
	if(s == INVALID_SOCKET){
		printf("SOCKET ERROR!!\n");
		return -1;
	}
	
	/*set socket option*/
	int ttl;
	setsockopt(s,IPPROTO_IP,IP_MULTICAST_TTL,(char*)&ttl,sizeof(ttl));
	
	/*address struct of who communicates with*/
	SOCKADDR_IN sendAddr;
	sendAddr.sin_addr.s_addr = inet_addr("233.3.3.3");
	sendAddr.sin_port = htons(22222);
	sendAddr.sin_family = AF_INET;
	
	/*send data*/
	int error=0;
	_msg msg;
	memset(&msg,0,sizeof(msg));
	sprintf(msg.q_str, "[Question] What job do you want to be?\n1.Programmer\n2.Network Engineer\n3.System Engineer\n4.Security Engineer\n");
	printf("%s", msg.q_str);
	
	error=sendto(s,(char*)&msg,sizeof(msg),0,(sockaddr*)(&sendAddr),sizeof(sendAddr));
	if(error == SOCKET_ERROR){
		printf("SENDTO ERROR!!\n");
		return -1;
	}	
	
	
	/*Address struct of who communicates with*/
	SOCKADDR_IN recvAddr;
	int recvLen = sizeof(recvAddr);
	
	/*receive data*/
	int total[5];
	memset(total,0,sizeof(total));
	int numAn=0;
	int i=0;
	
	printf("\n### The Result of Survey ###\n");
	
	int rcvtime=3000;
	setsockopt(s,SOL_SOCKET,SO_RCVTIMEO,(char*)&rcvtime,sizeof(rcvtime));
	
	while(1)
	{	
		error=recvfrom(s,(char*)&msg,sizeof(msg),0,(sockaddr*)(&recvAddr), &recvLen);
		if(error == SOCKET_ERROR)
			break;
		
		
		if(msg.a_num >=1 && msg.a_num<=4)
		{
			total[msg.a_num]++;
		}
	
	}

	for(i=1;i<5;i++)
	{	
		printf("Number %d : %d\n",i, total[i]);
	}
	
	/*close socket*/
	closesocket(s);
	
	/*unload dll*/
	WSACleanup();
	
	return 0;
}