#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUF_LEN 2048 /*IEでのURLの最大文字数を採用*/
#include "socket_tool.h"
#include "parse_url.h"



int parse_url(const char *url_str, struct URL *url, char *error){

  char scheme[BUF_LEN] = "";
  char hostpath[BUF_LEN] = "";
  char *phostpath = hostpath;
  char host_and_port[BUF_LEN] = "";
  char host[BUF_LEN] = "";
  char path[BUF_LEN] = "";
  char ip_addr[BUF_LEN] = "";
  char *pip_addr = ip_addr;
  char *ppath = path;
  char *p = NULL;
  printf("URLをparseします...\n");
  printf("解析するURL: %s\n", url_str);
  
  if (strlen(url_str) > BUF_LEN){
    strcpy(error, "URLが長過ぎます。\n");
    return -1;
  }
  /* schemeを取得する */
  strcpy(scheme, url_str);
  strtok(scheme, ":");
  strcpy(url->scheme, scheme);
  if (strcmp(url->scheme,"http") != 0 && strcmp(url->scheme, "https") != 0){
    strcpy(error, "schemeがhttp/httpsではありません。\n");
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

  /*ip_addrを取得する*/
  pip_addr = hostname_to_ip_str(url->host);
  strcpy(url->ip_addr, pip_addr);
  printf("ip_addr: %s\n", url->ip_addr);
  url->ip_addr_net = hostname_to_network_byteorder(url->host);
  printf("ip_addr_net: %X\n", url->ip_addr_net);

  /* pathを取得する*/
  ppath = strchr(phostpath, '/');
  if (ppath == NULL){
    printf("pathが見つからないため\"/\"に設定します。\n");
    strcpy(url->path, "/");
  }else{
    strcpy(url->path, ppath);
  }
  printf("path: %s\n", url->path);
  return 0;
}
/*
int main(){
  struct URL url;
  char error[256];
  char *perror = error;
  char url_str[] = "https://www.google.com/file";
  memset(&url, 0, sizeof(url));
  parse_url(url_str, &url, perror);
  printf(perror);
  return 0;
}
*/
