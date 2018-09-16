#ifndef _PARSE_URL_H_
#define _PARSE_URL_H_
#define BUF_LEN 2048 /*IEでのURLの最大文字数を採用*/
/*構造体の宣言*/
struct URL{
  char scheme[BUF_LEN];
  char ip_addr[BUF_LEN];
  int  ip_addr_net;
  char host[BUF_LEN];
  char path[BUF_LEN];
  unsigned short port;
};
/*関数のプロトタイプ宣言*/
int parse_url(const char *, struct URL *, char *);
#endif
