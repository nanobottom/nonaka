# Makefile
program = main
obj = main.o send_header.o
CC = gcc

$(program): $(obj)
	$(CC) -o $(program) $^

.SUFFIXES: .c .o
.c.o:
	$(CC) -c -g $<
.PHONY: clean
clean:
	$(RM) $(program) $(obj)
