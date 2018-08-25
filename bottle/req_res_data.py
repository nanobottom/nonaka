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
         
        param = [ord(s) for s in string]
        # <size>bytesの内、埋まらなかった箇所に0x00を付加
        zero_lst = [0] * (size - len(param))
        param.extend(zero_lst)
        return param

class RequestData(WebData):

    def __init__(self, request):
        self.request = request
        self.body = request.body.read()
        
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
        self.response.status = 200
        self.response.content_type = 'text/plain'

    def set_param_to_body(self):
        # name
        name = inifile.get('response', 'name')
        self.body.extend(self.str_to_ascii(name, 100))
        # address
        address = inifile.get('response', 'address')
        self.body.extend(self.str_to_ascii(address, 100))
        # age
        age = inifile.get('response', 'age')
        self.body.append(int(age))
        # birthday
        birthday = inifile.get('response', 'birthday')
        self.body.extend(self.str_to_ascii(birthday, 20))
        # bytearrayをファイルオブジェクトとして扱うためにio.BytesIOを使用する
        self.response.body = io.BytesIO(self.body)
