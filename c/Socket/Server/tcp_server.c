#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include "socket_tool.h"

int main(){
  int sock0;
  struct sockaddr_in server;
  struct sockaddr_in client;
  int len;
  int sock;
  char hostname[] = "localhost";
  char *ip_addr  = hostname_to_ip_str(hostname);
  int port = 80;
  char buf[1024]; //ソケットからデータを読み取るバッファ


  int send_msg(int sock, char *msg){
    int len;
    int result;
    len = strlen(msg);
    result = send(sock, msg, len, 0);
    if (result != len){
      fprintf(stderr, "writing error.");
    }
    return len;
  }
  /* ソケットの作成 */
  /* AF_INET: IPv4インターネットプロトコル */
  /* SOCK_STREAM: WWW, telnet, FTPなど*/
  /* IPPROTO_TCP: TCPプロトコル*/
  sock0 = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (sock0 < 0){
      perror("socket");
      return 1;
    }

  /* ソケットの設定 */
  server.sin_family = AF_INET;
  /* htons: 16ビット(short)ホストバイトオーダーをネットワークバイトオーダーに変換する */
  /* hostでのメモリ扱い方法をnetworkの世界での方法(network byte order = big endian)
   * に必要であれば変換する。複数バイト長の変数のメモリ上での取扱はCPUによってlittle/bigと異なる*/
  server.sin_port = htons(port);
  /* inet_addr: 小数点付き10進数のホストアドレスのstringをバイナリ値に変換する*/
  server.sin_addr.s_addr = inet_addr(ip_addr);
 if (bind(sock0, (struct sockaddr *)&server, sizeof(server)) != 0){
     perror("bind");
     return 1;
   }

  /* TCPクライアントからの接続要求を待てる状態にする */
  if (listen(sock0, 5) != 0){
      perror("listen");
      return 1;
    }


  while(1){
    /* TCPクライアントからの接続要求を受け付ける */
    len = sizeof(client);
    sock = accept(sock0, (struct sockaddr *)&client, &len);

    /* ntohs: 整数をネットワークバイトオーダーからホストバイトオーダーへ変換する*/
    printf("Accepted connection from %s, port=%d\n", inet_ntoa(client.sin_addr), ntohs(client.sin_port));
    
    /* HTTPリクエストをdumpする*/
    read(sock, buf, 1024);
    printf("Receive data:\n%s\n", buf);

    /* 文字送信 */
    send_msg(sock, "HTTP/1.0 200 OK\r\n");
    send_msg(sock, "Content-Type: text/html\r\n");
    send_msg(sock, "\r\n");
    send_msg(sock, "HELLO\r\n");

    /* TCPセッションの終了 */
    close(sock);
    
  }

  /* listenするsocketの終了 */
  close(sock0);

  return 0;

}
