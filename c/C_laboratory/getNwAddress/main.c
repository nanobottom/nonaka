#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUFFER_SIZE 256
void print_binary(unsigned long num, int digit);
void print_bit_operation(unsigned long data, unsigned long mask, unsigned long result, char *ope);
unsigned long byte_swapping(unsigned long data);
int main(void)
{
  char buffer[BUFFER_SIZE] = "";
  struct sockaddr_in addr_ip, addr_subnet;
  unsigned long network_address = 0, ip_address = 0, subnetmask = 0;
  
  printf("IP address>>");
  fgets(buffer, BUFFER_SIZE, stdin);
  buffer[strlen(buffer) - 1] = '\0';
  if(inet_aton(buffer, &addr_ip.sin_addr) == 0)
  {
    fprintf(stderr, "Input is not address.\n");
    exit(EXIT_FAILURE);
  }

  printf("Subnet mask>>");
  fgets(buffer, BUFFER_SIZE, stdin);
  buffer[strlen(buffer) - 1] = '\0';
  if(inet_aton(buffer, &addr_subnet.sin_addr) == 0)
  {
    fprintf(stderr, "Input is not address.\n");
    exit(EXIT_FAILURE);
  }
  ip_address = byte_swapping(addr_ip.sin_addr.s_addr);
  subnetmask = byte_swapping(addr_subnet.sin_addr.s_addr); 
  network_address = ip_address & subnetmask;
  print_bit_operation(ip_address, subnetmask, network_address, "AND");

}
  
void print_binary(unsigned long num, int digit)
{
  int binary[BUFFER_SIZE];

  for(int i = 0; i < digit; i++)
  {
    binary[i] = num % 2;
    num /= 2;
  }
  for(int i = digit - 1; i >=0; i--)
  {
    printf("%d", binary[i]);
  }
}
void print_bit_operation(unsigned long data, unsigned long mask, unsigned long result, char *ope)
{
  int digit = 32;
  printf("\t");
  print_binary(data, digit);
  printf("\n");
  printf("   %s)\t", ope);
  print_binary(mask, digit);
  printf("\n\t");
  for(int i = 0; i < digit; i++)
  {
    printf("-");
  }
  printf("\n\t");
  print_binary(result, digit);
  printf("\n\n");
}

unsigned long byte_swapping(unsigned long data)
{
  unsigned long result = 0;
  result  = data               <<24;
  result |=(data & 0x0000FF00) << 8;
  result |=(data & 0x00FF0000) >> 8;
  result |= data               >>24;
  return result;
}

