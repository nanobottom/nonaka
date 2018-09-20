#ifndef HTTP_SERVER_H
#define HTTP_SERVER_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <netdb.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// common macro
#define SERVER_NAME   "localhost" 
#define SERVER_PORT   80
#define BUF_SIZE      1024


// RFC 2616 HTTP status code
typedef enum{
  HTTP_OK            = 200,
  HTTP_BADREQ        = 400,
  HTTP_NOTFOUND      = 404,
  HTTP_INTERNALERR   = 500,
  HTTP_NOTIMPLE      = 501
} http_status_type;

extern char *hostname_to_ip_addr(char *hostname);
extern int hostname_to_ip_net(char *hostname);
extern int handle_error(int fd, http_status_type type, char *msg);
#endif  //end of HTTP_SERVER_H
