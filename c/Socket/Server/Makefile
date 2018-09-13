# Makefile
obj = tcp_server.o socket_tool.o

tcp_server: $(obj)
	gcc -o tcp_server $(obj)
tcp_server.o: tcp_server.c
	gcc -c tcp_server.c
socket_tool.o: socket_tool.c
	gcc -c socket_tool.c
.PHONY: clean
clean:
	rm -f tcp_server tcp_server.o socket_tool.o
