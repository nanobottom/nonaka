#include "http_server.h"
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <sys/stat.h>

static char *err_badreq_template =
"HTTP/1.1 400 Bad Request\n"
"Content-type: text/html\n"
"\n"
"<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n"
"<html>\n"
"<head><title>400 Bad Request</title></head>"
"<body>\n"
"<h1>400 Bad Request</h1>\n"
"<p>This server could not understand your request.</p>\n"
"</body>\n"
"</html>\n";

static char *err_notfound_template =
"HTTP/1.1 404 Not Found\n"
"Content-type: text/html\n"
"\n"
"<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n"
"<html>\n"
"<head><title>404 Not Found</title></head>"
"<body>\n"
"<h1>404 Not Found</h1>\n"
"<p>No such file %s.</p>\n"
"</body>\n"
"</html>\n";


static char *err_notimple_template =
"HTTP/1.1 501 Method Not Implemented\n"
"Content-type: text/html\n"
"\n"
"<!DOCTYPE HTML PUBLIC \"-//IETF//DTD HTML 2.0//EN\">\n"
"<html>\n"
"<head><title>501 Method Not Implemented</title></head>"
"<body>\n"
"<h1>501 Method Not Implemented</h1>\n"
"<p>%s method not implemented.</p>\n"
"</body>\n"
"</html>\n";

int handle_error(int fd, http_status_type type, char *msg){
  char buf[BUF_SIZE] = "";
  switch (type){
    case HTTP_NOTFOUND:
      snprintf(buf, sizeof(buf), err_notfound_template, msg);
      break;
    case HTTP_BADREQ:
      snprintf(buf, sizeof(buf), err_badreq_template);
      break;
    case HTTP_NOTIMPLE:
      snprintf(buf, sizeof(buf), err_notimple_template, msg);
      break;
  }
  send(fd, buf, strlen(buf), 0);
  return EXIT_SUCCESS;
}
