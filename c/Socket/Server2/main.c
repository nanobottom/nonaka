#include "http_server.h"
#include <unistd.h>
#include <netinet/in.h>
#include <signal.h>
#include <string.h>
static int server_fd = -1;

// Change hostname to strings of IP address.
char *hostname_to_ip_addr(char *hostname){

  struct hostent *host;
  struct sockaddr_in addr;
  char *ip_str;

  host = gethostbyname(hostname);
  addr.sin_addr = *(struct in_addr *)(host->h_addr_list[0]);
  ip_str = inet_ntoa(addr.sin_addr);
  return ip_str;
}
// Hexdump
void hexdump(char *arr, int arr_size)
{
  char c[256] = "|";
  char buf[256] = "";
  int count = 0;
  for(int i = 0; i < arr_size; i++)
  {
    // If arr is range of ASCII...
    if (arr[i] > 31 && arr[i] < 127)
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%c", buf, arr[i]);
    }
    else
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%s", buf, ".");
    }

    if(i == 0)
    {
      printf("%08X  ",i);
      printf("%02X ", arr[i]);
    }
    else if((i+1) % 16 == 0 && i != 0 )
    {
      strcpy(buf, c);
      snprintf(c, 256, "%s%s", buf, "|\n");
      printf("%02X  ", arr[i]);
      printf("%s",c);
      printf("%08X  ",i + 1);
      strcpy(c, "|");
    }
    else if((i+1) % 8 == 0)
    {
      printf("%02X  ", arr[i]);
    }
    else
    {
      printf("%02X ", arr[i]);
    }
    count = i + 1;
  }
  //Create blank part.
  for(int i = 0; i < (16 - count % 16); i++ )
  {
    printf("   ");
    strcpy(buf,c);
    snprintf(c, 256, "%s ", buf);

  }
  if((16- count % 16) > 8)
  {
    printf("  ");
  }
  strcpy(buf,c);
  snprintf(c, 256, "%s|\n", buf);
  printf("%s", c);
}

// Change hostname to network byte order of IP address.
int hostname_to_ip_net(char *hostname){

  struct hostent *host;
  int addr;
  host = gethostbyname(hostname);
  addr = (int)host->h_addr_list[0];
  return addr;
}
static void close_server_fd(int unused){
  if(server_fd > 0){
    close(server_fd);
  }
  fprintf(stderr, "%s is terminated.\n", SERVER_NAME);
  exit(EXIT_SUCCESS);
}

static void init_signal(void){
  signal(SIGINT, close_server_fd);//in case of push Ctrl + C
  signal(SIGTERM, close_server_fd);//in case of terminate process from kill command
  return;
}

int server_process(int client_fd){
  char recv_data[BUF_SIZE] = "", method[BUF_SIZE] = "",
       url[BUF_SIZE] = "", protocol[BUF_SIZE] = "", res_data[BUF_SIZE] = "";
  char buf[BUF_SIZE] = "";
  char *pres_data = res_data;
  //int data_array[BUF_SIZE] = {0};
  char *p = NULL;
  int length = 0;

  length = read(client_fd, recv_data, BUF_SIZE);
  if (length <= 0){
    fprintf(stderr, "Failed to receive request.\n");
    return HTTP_INTERNALERR;
  }

  //Extract top line message.
  strcpy(buf, recv_data);
  strtok(buf, "\r\n");

  //Read method, url, protocol
  if (sscanf(buf, "%s %s %s", method, url, protocol) != 3){
    handle_error(client_fd, HTTP_BADREQ, NULL);
    return HTTP_BADREQ;
  }

  //Check protocol
  if (strcmp(protocol, "HTTP/1.0") && strcmp(protocol, "HTTP/1.1")){
    handle_error(client_fd, HTTP_BADREQ, NULL);
    return HTTP_BADREQ;
  }

  //Check method
  if(strcmp(method, "GET") && strcmp(method, "POST")){
    handle_error(client_fd, HTTP_NOTIMPLE, method);
    return HTTP_NOTIMPLE;
  }


  //Extract request body.
  p = strstr(recv_data, "\r\n\r\n") + 4;
  if(strlen(p) != 0){
    //for (int chr_i = 0; chr_i < (strlen(p) -1); chr_i++){
    //  data_array[chr_i] = (int)p[chr_i];
    //}
    //hexdump(data_array, sizeof(data_array)/sizeof(data_array[0]));
    hexdump(p, strlen(p)- 1);
  }
  //Response message.
  pres_data = "HTTP/1.1 200 OK\n";
  if(send(client_fd, pres_data, strlen(pres_data), 0) < 0){
    return -1;
  }
}
static int access_loop(void){
  fd_set read_fds;
  struct sockaddr_in sin;
  int client_fd = 0;

  while(1){
    // Initialize fd_set
    FD_ZERO(&read_fds);
    // Register server socket as reading socket from select function.
    FD_SET(server_fd, &read_fds);

    //select: Waiting connection from client.
    if (select(server_fd + 1, &read_fds, NULL, NULL, NULL) < 0){
      fprintf(stderr, "Failed to select server socket.\n");
      break;
    }
    // In case of existing connection request from client
    if (FD_ISSET(server_fd, &read_fds)){
      int addrlen = sizeof(sin);
      memset(&sin, 0, sizeof(sin));

      client_fd = accept(server_fd, (struct sockaddr *)&sin, &addrlen);
      if (client_fd < 0){
        fprintf(stderr, "Failed to accept.\n");
        break;
      }
      //HTTP server process
      server_process(client_fd);
    }
  }
  return EXIT_SUCCESS;
}
int main(){
  struct sockaddr_in sin;
  char *ip_addr = hostname_to_ip_addr(SERVER_NAME);
  //Initialize structure
  memset(&sin, 0, sizeof(sin));

  //Initialize server socket(TCP/IP communication)
  printf("Creating server socket...\n");
  server_fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (server_fd < 0){
    fprintf(stderr, "Failed to create server socket.\n");
    exit(EXIT_FAILURE);
  }

  //bind: Setting IP address and port to socket.
  sin.sin_family = AF_INET;//IPv4
  sin.sin_addr.s_addr = inet_addr(ip_addr);
  sin.sin_port = htons(SERVER_PORT);

  printf("Binding server socket...\n");
  if (bind(server_fd, (struct sockaddr *)&sin, sizeof(sin)) < 0){
    fprintf(stderr, "Failed to bind server socket.\n");
    close(server_fd);
    exit(EXIT_FAILURE);
  }
  
  //listen: Making status of waiting connection request from client.
  if (listen(server_fd, SOMAXCONN) < 0){
    fprintf(stderr, "Failed to listen client socket.\n");
    close(server_fd);
    exit(EXIT_FAILURE);
  }
  printf("%s listening port %d...\n", SERVER_NAME, SERVER_PORT);

  //Initialize signal processing function.
  init_signal();

  //Waiting access from client.
  access_loop();


}
