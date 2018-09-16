#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(){
    int sockfd, new_sockfd;
    int port = 80;
    struct sockaddr_in addr, client_addr;
    socklen_t len;
    char c[1];
    // socketシステムコール
    // エラーが発生した場合は-1を返す
    // AF_INETはIPv4インターネットプロトコル
    // SOCK_STREAMはTCP通信
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        perror("socket");
        exit(-1);
      }

      addr.sin_family = AF_INET;  // AF_INETを指定
      addr.sin_port = htons(port);// ポート番号の指定
      addr.sin_addr.s_addr = 0;   // 自動的に自分のIPを割り当てる
      
      // bindシステムコール：socketシステムコールで作成したソケットに
      // アドレスを割り当てる。
      if(bind(sockfd, (struct sockaddr *)&addr, sizeof(addr)) == -1){
        perror("bind");
        exit(-1);
      }
      // listenシステムコール：ソケットを接続待ちソケットとする。
      if(listen(sockfd, 5) == -1){
          perror("listen");
          exit(-1);
        }

      while(1){
        len = sizeof(client_addr);
        // acceptシステムコール：接続待ちソケット宛の接続要求のキューから
        // 先頭の接続要求を取り出し、接続済みソケットを作成する。
        new_sockfd = accept(sockfd, (struct sockaddr *)&client_addr, &len);
        if(new_sockfd == -1){
            perror("accept");
            continue;
        }

        printf("from %s port %d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        while(read(new_sockfd, c, 1) > 0){
            write(1, c, 1);
        }

        close(new_sockfd);
      }

      close(sockfd);

      return 0;

  }

