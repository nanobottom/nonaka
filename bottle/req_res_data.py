import json, io
import configparser
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
class RequestData:

    def __init__(self, request):
        self.request = request
        self.body_bytes = request.body.read()
        
    def hexdump_body(self):
        count = 1
        for i in self.body_bytes:
            if count % 16 == 0:
                print('%02x \n' % i, end = '')
            else:
                print('%02x ' % i, end = '')
            if len(self.body_bytes) == count:
                print('\n')
            count += 1

    def display_info(self):
        
        print('<リクエストを受信しました>')
        print('フォームパラメータ : {}'.format(self.request.params))
        print('HTTPメソッド : {}'.format(self.request.method))
        print('リクエスト本文 :')
        self.hexdump_body()
        print('アスセスされたURL : {}'.format(self.request.url))
        print('Host : {}'.format(self.request.get_header('Host')))
        print('Accept-Encoding : {}'.format(self.request.get_header('Accept-Encoding')))
        print('Accept-Language : {}'.format(self.request.get_header('Accept-Language')))
        print('Content-Type : {}'.format(self.request.content_type))
        print('Content-Length : {}'.format(self.request.content_length))
        print('User-Agent : {}'.format(self.request.get_header('User-Agent')))
        print('From : {}'.format(self.request.get_header('From')))
        print('Date : {}'.format(self.request.get_header('Date')))
        print('Content-Encoding : {}'.format(self.request.get_header('Content-Encoding')))


class ResponseJSONData:

    def __init__(self, response):
        self.response = response
        self.body_filename = 'res_data.json'

    def set_param(self): 
        with open(self.body_filename, 'r') as f:
            json_data = json.load(f)
            self.response.body = json.dumps(json_data)
        self.response.status = 200
        self.response.content_type = 'application/json'

class ResponseData:

    def __init__(self, response = 0):
        self.response = response
        self.body = bytearray()

    def set_param_to_body(self):
        # name
        name = [ord(s) for s in inifile.get('response', 'name')]
        # 20bytesの内、埋まらなかった箇所に0x00を付加
        zero_lst = [0] * (20 - len(name))
        name.extend(zero_lst)
        self.body.extend(name)

        # address
        address = [ord(s) for s in inifile.get('response', 'address')]
        # 100bytesの内、埋まらなかった箇所に0x00を付加
        zero_lst = [0] * (100 - len(address))
        address.extend(zero_lst)
        self.body.extend(address)
        
        # age
        self.body.append(int(inifile.get('response', 'age')))
        
        # birthday
        birthday = [ord(s) for s in inifile.get('response', 'birthday')]
        # 20bytesの内、埋まらなかった箇所に0x00を付加
        zero_lst = [0] * (20 - len(birthday))
        birthday.extend(zero_lst)
        self.body.extend(birthday)

        self.response.body = io.BytesIO(self.body)
        self.response.status = 200
        self.response.content_type = 'text/plain'
