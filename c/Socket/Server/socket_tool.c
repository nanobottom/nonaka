#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "socket_tool.h"

char *hostname_to_ip_str(char *ip_addr){

    struct hostent *host;
    struct sockaddr_in addr;
    char *ip_str;

    host = gethostbyname(ip_addr);
    addr.sin_addr = *(struct in_addr *)(host->h_addr_list[0]);
    /* inet_ntoa: ネットワークバイトオーダーの32ビットとして表現された
     * IPアドレスを、小数点付き10進数表記で表されたstringとして返す*/
    ip_str = inet_ntoa(addr.sin_addr);
    return ip_str;
  }

int hostname_to_network_byteorder(char *ip_addr){

    struct hostent *host;
    int addr;

    host = gethostbyname(ip_addr);
    addr = (int)host->h_addr_list[0];
    return addr;
  }

/*
int main(){
    char hostname[] = "localhost";
    printf("IP=%X\n",hostname_to_network_byteorder(hostname));
    printf("IP(str)=%s\n",hostname_to_ip_str(hostname));
  }
*/
