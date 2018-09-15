#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUF_LEN 256

struct URL{
  char scheme[BUF_LEN];
  char host[BUF_LEN];
  char path[BUF_LEN];
  unsigned short port;
};

int parse_url(const char *url_str, struct URL *url){

  char scheme[BUF_LEN];
  char hostpath[BUF_LEN];
  char *phostpath = hostpath;
  char host_and_port[BUF_LEN];
  char host[BUF_LEN];
  char path[BUF_LEN];
  char *ppath = path;
  char error[BUF_LEN];
  char *p;
  printf("URL: %s\n", url_str);
  /* schemeを取得する */
  strcpy(scheme, url_str);
  strtok(scheme, ":");
  strcpy(url->scheme, scheme);
  if (strcmp(url->scheme,"http") != 0 && strcmp(url->scheme, "https") != 0){
    printf("schemeがhttp/httpsではありません。\n");
    return -1;
  }
  printf("scheme: %s\n", url->scheme);

  /* hostとportを取得する*/
  p = strchr(url_str, '/');
  phostpath = p + 2;/* http://の"//"以降のポインタを指定する*/
  printf("hostpath: %s\n", phostpath);
  strcpy(host_and_port, phostpath);
  strtok(host_and_port, "/");
  p = strchr(host_and_port, ':');
  if (p == NULL){
    printf("ポート番号が見つからないため80に設定します。\n");
    url->port = 80;
    strcpy(url->host, host_and_port);
  }else{
    url->port = atoi(p + 1);
    strcpy(host, host_and_port);
    strtok(host, ":");
    strcpy(url->host, host);
  }
  printf("host: %s\n", url->host);
  printf("port: %d\n", url->port);

  /* pathを取得する*/
  ppath = strchr(phostpath, '/');
  strcpy(url->path, ppath);
  printf("path: %s\n", url->path);
  return 0;
}

int main(){
  struct URL url;
  char url_str[] = "https://www.google.com/file";
  parse_url(url_str, &url);
  return 0;
}
