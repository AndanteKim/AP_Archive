#include <winsock2.h>
#include <stdio.h>
#pragma comment(lib,"ws2_32.lib") 

SOCKADDR_IN port_info;
SOCKET sock1, sock2;

DWORD WINAPI portscan1(LPVOID arg)
{
	FILE * fp1;
	char buf[20];
	memset(buf,0,sizeof(buf));
	int port=((int*)arg)[0];

	WSADATA wsa;
	if(WSAStartup(MAKEWORD(2,2), &wsa)!=0){ 
		printf("WSAStartup error!");  
		return -1; 
	}

	for(;port<=((int*)arg)[1];port++)
	{
		sock1=socket(AF_INET, SOCK_STREAM, 0);
		if(sock1==INVALID_SOCKET)
		{ 
			printf("socket error!\n"); 
			return -1; 
		}

		port_info.sin_port =htons(port);
	
		int error=connect(sock1, (struct sockaddr*)&port_info, sizeof(port_info));
		if(error==SOCKET_ERROR)
		{
			sprintf(buf,"%d port close!!\n",port);
		}	
		else
		{
			sprintf(buf,"%d port open!!\n", port);
		}
		
		fp1=fopen("C:\\port1.txt","a");
		fwrite(buf,sizeof(buf),1,fp1);
		fclose(fp1);
		
	}
	return 0;
}
DWORD WINAPI portscan2(LPVOID arg)
{
	FILE * fp2;
	char buf[20];
	memset(buf,0,sizeof(buf));
	int port=((int*)arg)[0];

	WSADATA wsa;
	if(WSAStartup(MAKEWORD(2,2), &wsa)!=0){ 
		printf("WSAStartup error!");  
		return -1; 
	}
	
	for(;port<=((int*)arg)[1];port++)
	{
		sock2=socket(AF_INET, SOCK_STREAM, 0);
		if(sock2==INVALID_SOCKET)
		{ 
			printf("socket error!\n"); 
			return -1; 
		}
		
		port_info.sin_port =htons(port);

		int error=connect(sock2, (struct sockaddr*)&port_info, sizeof(port_info));
		if(error==SOCKET_ERROR)
		{
			sprintf(buf,"%d port close!!\n",port);
		}	
		else
		{
			sprintf(buf,"%d port open!!\n", port);
		}
		
		fp2=fopen("C:\\port2.txt","a");
		fwrite(buf,sizeof(buf),1,fp2);
		fclose(fp2);
	}
	
	return 0;
}

int main(int argc, char ** argv)
{
	memset(&port_info , 0 , sizeof(port_info));
	port_info.sin_family = AF_INET;
	port_info.sin_addr.s_addr = inet_addr("192.168.222.134");

	int portsu = atoi(argv[2])-atoi(argv[1])+1;
	int port1[2], port2[2];
	int len = portsu/2;

	port1[0] = atoi(argv[1]);
	port1[1] = atoi(argv[1])+len;
	port2[0] = port1[1]+1;
	port2[1] =atoi(argv[2]);

	HANDLE handles[2]; 
	handles[0] = CreateThread(NULL,0,portscan1,(LPVOID)port1,0,NULL);
	handles[1] = CreateThread(NULL,0,portscan2,(LPVOID)port2,0,NULL);
	
	printf("Scanning......\n");
	
	WaitForMultipleObjects(2, handles, TRUE, INFINITE);
	
	WSACleanup();
	return 0;
}