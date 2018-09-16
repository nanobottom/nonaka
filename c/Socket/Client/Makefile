# Makefile
program = tcp_client
obj = tcp_client.o parse_url.o socket_tool.o
CC = gcc

$(program): $(obj)
	$(CC) -o $(program) $^

.SUFFIXES: .c .o
.c.o:
	$(CC) -c -g $<
.PHONY: clean
clean:
	$(RM) $(program) $(obj)
