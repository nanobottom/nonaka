import json, io
import configparser
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
class WebData:

    def __init__(self):
       self.body = bytearray()

    def hexdump_body(self):
        print('%08x  ' % 0, end = '')
        count = 1
        s = '|'
        for i in self.body:
            print('%02x ' % i, end = '') 
            # ASCII文字の範囲外なら'.'文字を表示
            if i in range(32, 127): 
                s += chr(i)
            else:
                s += ' '
            
            # スペースと座標、文字部分を整形する 
            if count % 16 == 0:
                s += '|'
                print(' %s\n%08x  ' % (s, count), end = '')
                s = '|'
            elif count % 8 == 0:
                print(' ', end = '')

            # 最後のスペースを整形する
            if len(self.body) == count :
                if  (16 - count % 16) < 8:
                    add_space = ' '
                else:
                    add_space = '  '
                space = '   ' * (16 - count % 16) + add_space
                s += ' ' * (16 - count % 16)
                s += '|' 
                print(space, end = '')
                print(s)
            count += 1

    def str_to_ascii(self, string, size):
        param = bytearray(string, 'ASCII')
        # <size>bytesの内、埋まらなかった箇所に0x00を付加
        zero_lst = [0] * (size - len(param))
        param.extend(zero_lst)
        return param

    def get_little_endian(self, offset, size):
        b = self.body[offset : offset + size]
        return str(int.from_bytes(b,'little'))

    def get_big_endian(self, offset, size):
        b = self.body[offset : offset + size]
        return str(int.from_bytes(b,'big'))

    def get_str(self, offset, size):
        b = self.body[offset : offset + size]
        strings = ''
        for s in b:
            strings += chr(s)
        return strings

    def set_little_endian(self, offset, size, param_str):
        self.body[offset : offset + size] = (int(param_str).to_bytes(size, 'little'))

    def set_big_endian(self, offset, size, param_str):
        self.body[offset : offset + size] = (int(param_str).to_bytes(size, 'big'))

    def set_str(self, offset, size, param_str):
        self.body[offset : offset + size] = self.str_to_ascii(string = param_str, size = size)

class ClientRequestData(WebData):

    def __init__(self, request = 0):
        self.request = request
        self.body_size = 222
        self.body = bytearray(self.body_size)

    def set_param_to_body(self):
        # name
        name = inifile.get('request', 'name')
        self.set_str(0, 100, name)
        # address
        address = inifile.get('request', 'address')
        self.set_str(100, 100, address)
        # age
        age = inifile.get('request', 'age')
        self.set_little_endian(200, 2, age)
        # birthday
        birthday = inifile.get('request', 'birthday')
        self.set_str(202, 20, birthday)
        # bytearrayをファイルオブジェクトとして扱うためにio.BytesIOを使用する
        return io.BytesIO(self.body)
class RequestData(WebData):

    def __init__(self, request = 0):
        self.request = request
        self.body = request.body.read()
        
    def display_header_info(self):
        
        print('---<request header>---')
        # print('form parameter : {}'.format(self.request.params))
        print('HTTP method : {}'.format(self.request.method))
        # print('HTTP header : {}'.format(self.request.headers))
        print('Message body:')
        self.hexdump_body()
        print('URL                : {}'.format(self.request.url))
        print('Host               : {}'.format(self.request.get_header('Host')))
        print('Authorization      : {}'.format(self.request.get_header('Authorization')))
        print('User-Agent         : {}'.format(self.request.get_header('User-Agent')))
        print('Accept             : {}'.format(self.request.get_header('Accept')))
        print('Accept-Language    : {}'.format(self.request.get_header('Accept-Language')))
        print('Accept-Encoding    : {}'.format(self.request.get_header('Accept-Encoding')))
        print('Content-Type       : {}'.format(self.request.content_type))
        print('Content-Length     : {}'.format(self.request.content_length))
        print('Content-Encoding   : {}'.format(self.request.get_header('Content-Encoding')))
        print('Transfer-Encoding  : {}'.format(self.request.get_header('Transfer-Encoding')))
        print('From               : {}'.format(self.request.get_header('From')))
        print('Date               : {}'.format(self.request.get_header('Date')))

    def display_body_info(self):
        print('---<request message body>---')
        print('name               : {}'.format(self.get_str(0,100)))
        print('address            : {}'.format(self.get_str(100,100)))
        print('age                : {}'.format(self.get_little_endian(200,2)))
        print('birthday           : {}'.format(self.get_str(202,20)))

class ResponseJSONData:

    def __init__(self, response):
        self.response = response
        self.JSON_filename = 'res_data.json'
        self.response.status = 200
        self.response.content_type = 'application/json'

    def set_param(self): 
        with open(self.JSON_filename, 'r') as f:
            json_data = json.load(f)
            self.response.body = json.dumps(json_data)

class ResponseData(WebData):

    def __init__(self, response = 0):
        WebData.__init__(self)
        self.response = response
        self.body_size = 222
        self.body = bytearray(self.body_size)
        self.response.status = 200
        self.response.content_type = 'text/plain'

    def set_param_to_body(self):
        # name
        name = inifile.get('response', 'name')
        self.set_str(0, 100, name)
        # address
        address = inifile.get('response', 'address')
        self.set_str(100, 100, address)
        # age
        age = inifile.get('response', 'age')
        self.set_little_endian(200, 2, age)
        # birthday
        birthday = inifile.get('response', 'birthday')
        self.set_str(202, 20, birthday)
        # bytearrayをファイルオブジェクトとして扱うためにio.BytesIOを使用する
        self.response.body = io.BytesIO(self.body)
        
