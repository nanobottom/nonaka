#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include "parse_url.h"

int main(){
  struct sockaddr_in server;
  int sockfd = 0; /*ソケット用のファイルディスクリプタ*/
  char send_buf[256] = "";
  char read_buf[1024] = "";
  int recv_data_size = 0;
  char err[32] = "";/*URLのparseに用いるエラー*/
  char *perr = err;
  struct URL url;
  struct addrinfo hints, *res;
  int err2 = 0;/*getaddinfoに用いるエラー*/
  int err3 = 0;/*connectに用いるエラー*/
  char url_str[] = "http://localhost:80/";

  /*構造体の初期化*/
  memset(&url, 0, sizeof(url));
  memset(&hints, 0, sizeof(hints));

  /* URLのparse*/
  parse_url(url_str, &url, err);
  /*
  if (err){
    printf("%s\n", err);
    return 1;
  }
  */
  /*アドレスの情報を取得する（IPv4とIPv6の違いに関する依存関係をなくすことができる）*/
  printf("アドレスの情報を取得中...\n");
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_family   = AF_INET;
  err2 = getaddrinfo(url.host, url.scheme, &hints, &res);
  if (err2 != 0){
    printf("Error at getaddrinfo(): %d\n", err2);
    return 1;
  }
  
  printf("ソケットを生成中...\n");
  /*ソケットを生成する*/
  sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);
  if (sockfd < 0){
    printf("ソケットの生成に失敗しました。\n");
    return 1;
  }
  /*サーバに接続する*/
  printf("サーバに接続中です...\n");
  err3 = connect(sockfd, res->ai_addr, res->ai_addrlen);
  if (err3 != 0){
    printf("connectに失敗しました。\n");
    return 1;
  }
  freeaddrinfo(res);

  /*HTTPプロトコルの開始、サーバに送信する*/
  sprintf(send_buf, "GET %s HTTP/1.0\r\n", url.path);
  write(sockfd, send_buf, strlen(send_buf));

  sprintf(send_buf, "Host: %s:%d\r\n", url.host, url.port);
  write(sockfd, send_buf, strlen(send_buf));

  sprintf(send_buf, "\r\n");
  write(sockfd, send_buf, strlen(send_buf));
  
  
  /*受信が終わるまでループする*/ 
  printf("データ受信中...\n");
  while(1){
    recv_data_size = read(sockfd, read_buf, sizeof(read_buf));
    printf("受信データ: \n%s\n", read_buf);
    if (recv_data_size > 0){
      write(1, read_buf, recv_data_size);
    }else{
      break;
    }
  }
  close(sockfd);
  return 0;
}  
