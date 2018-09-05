import json, io
import configparser
import os
conf = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
try:
    if os.path.exists(conf_path) == False:
        raise SystemError('Missing "config.ini" file at {}.'.format(current_dir))
except SystemError as e:
    print("SystemError : {}".format(e))
conf.read(conf_path, 'UTF-8')
class WebData:

    def __init__(self):
       self.data = bytearray()

    def hexdump_data(self):
        print('%08x  ' % 0, end = '')
        count = 1
        s = '|'
        for i in self.data:
            print('%02x ' % i, end = '') 
            # ASCII文字の範囲外なら' '文字を表示
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
            if len(self.data) == count :
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
        b = self.data[offset : offset + size]
        return str(int.from_bytes(b,'little'))

    def get_big_endian(self, offset, size):
        b = self.data[offset : offset + size]
        return str(int.from_bytes(b,'big'))

    def get_str(self, offset, size):
        b = self.data[offset : offset + size]
        strings = ''
        for s in b:
            strings += chr(s)
        return strings

    def get_bit(self, bits, digit):
        digit -= 1
        return bin(int(bin(bits >> digit), 2) & 0b1)

    def set_little_endian(self, offset, size, param_str):
        if param_str != "":
            if param_str[0:2] == '0x':
                self.data[offset : offset + size] = int(param_str, 16).to_bytes(size, 'little')
            else:
                self.data[offset : offset + size] = (int(param_str).to_bytes(size, 'little'))

    def set_big_endian(self, offset, size, param_str):
        if param_str != "":
            if param_str[0:2] == '0x':
                self.data[offset : offset + size] = int(param_str, 16).to_bytes(size, 'big')
            else:
                self.data[offset : offset + size] = (int(param_str).to_bytes(size, 'big'))

    def set_str(self, offset, size, param_str):
        if param_str != "":
            self.data[offset : offset + size] = self.str_to_ascii(param_str, size)

    def set_bit(self, offset, digit, change_bit):
        bits = self.data[offset : offset + 1]
        digit -= 1
        and_bits = (0b11111110, 0b11111101, 0b11111011, 0b11110111, 0b11101111, 0b11011111, 0b10111111, 0b01111111)
        or_one_bits = (0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000, 0b1000000, 0b10000000)

        if change_bit == 0:
            self.data[offset : offset + 1] = bin(bits & and_bits[digit])
        elif change_bit == 1:
            self.data[offset : offset + 1] = bin(bits & and_bits[digit] | or_one_bits[digit])

    def range_check(self, param, param_name, begin, end):
        if (param in range(begin, end)) == False:
            print('Parameter {} is over range of num.'.format(param_name))
        self.response_status_code = 400

class ClientRequestData(WebData):

    def __init__(self, request = 0):
        self.request = request
        self.data_size = 222
        self.data = bytearray(self.data_size)

    def set_data(self):
        offset, size = 0, 100
        # name
        name = conf.get('request', 'name')
        self.set_str(offset, size, name)
        offset +=size
        # address
        size = 100
        address = conf.get('request', 'address')
        self.set_str(offset, size, address)
        offset +=size
        # age
        size = 2
        age = conf.get('request', 'age')
        self.set_little_endian(offset, size, age)
        offset +=size
        # birthday
        size = 20
        birthday = conf.get('request', 'birthday')
        self.set_str(offset, size, birthday)
        # bytearrayをファイルオブジェクトとして扱うためにio.BytesIOを使用する
        return io.BytesIO(self.data)
class RequestData(WebData):

    def __init__(self, request = 0):
        self.request = request
        self.data = request.data
        self.response_status_code = 200

    def display_header_info(self):
        
        print('---<Request header>---')
        print('Message data:')
        self.hexdump_data()
        print('URL                : {}'.format(self.request.url))
        print('Host               : {}'.format(self.request.headers.get('Host')))
        print('Authorization      : {}'.format(self.request.headers.get('Authorization')))
        print('User-Agent         : {}'.format(self.request.headers.get('User-Agent')))
        print('Accept             : {}'.format(self.request.headers.get('Accept')))
        print('Accept-Language    : {}'.format(self.request.headers.get('Accept-Language')))
        print('Accept-Encoding    : {}'.format(self.request.headers.get('Accept-Encoding')))
        print('Content-Type       : {}'.format(self.request.content_type))
        print('Content-Length     : {}'.format(self.request.content_length))
        print('Content-Encoding   : {}'.format(self.request.headers.get('Content-Encoding')))
        print('Transfer-Encoding  : {}'.format(self.request.headers.get('Transfer-Encoding')))
        print('From               : {}'.format(self.request.headers.get('From')))
        print('Date               : {}'.format(self.request.headers.get('Date')))

    def display_data_info(self):
        print('---<Request message data>---')
        print('name               : {}'.format(self.get_str(0,100)))
        print('address            : {}'.format(self.get_str(100,100)))
        print('age                : {}'.format(self.get_little_endian(200,2)))
        print('birthday           : {}'.format(self.get_str(202,20)))

    def name_offset(self):
        return 0

    def name_size(self):
        return 100

    def get_name(self):
        return self.get_str(self.name_offset(), self.name_size())

    def set_name(self, param_str):
        self.set_str(self.name_offset(), self.name_size(), param_str)
        
    def address_offset(self):
        return self.name_offset() + self.name_size()

    def address_size(self):
        return 100

    def get_address(self):
        return self.get_str(self.address_offset(), self.address_size())

    def set_address(self, param_str):
        self.set_str(self.address_offset(), self.address_size(), param_str)

    def age_offset(self):
        return self.address_offset() + self.address_size()

    def age_size(self):
        return 2

    def get_age(self):
        return self.get_little_endian(self.age_offset(), self.age_size())

    def set_age(self, param_str):
        self.set_little_endian(self.age_offset(), self.age_size(), param_str)

    def birthday_offset(self):
        return self.age_offset() + self.age_size()

    def birthday_size(self):
        return 20

    def get_birthday(self):
        return self.get_str(self.birthday_offset(), self.birthday_size())

    def set_birthday(self, param_str):
        self.set_str(self.birthday_offset(), self.birthday_size(), param_str)
    def error_check(self):
        age = int(self.get_age())
        self.range_check(age, 'age' , 20, 80)

class ResponseJSONData:

    def __init__(self, response):
        self.response = response
        self.JSON_filename = 'res_data.json'
        self.response.status_code = 200
        self.response.content_type = 'application/json'

    def set_param(self): 
        with open(self.JSON_filename, 'r') as f:
            json_data = json.load(f)
            self.response.data = json.dumps(json_data)

class ResponseData(WebData):

    def __init__(self, response = 0):
        WebData.__init__(self)
        self.response = response
        self.data_size = 222
        self.data = bytearray(self.data_size)
        self.is_setting_from_web = 0

    def name_offset(self):
        return 0

    def name_size(self):
        return 100

    def get_name(self):
        return self.get_str(self.name_offset(), self.name_size())

    def set_name(self, param_str):
        self.set_str(self.name_offset(), self.name_size(), param_str)
        
    def address_offset(self):
        return self.name_offset() + self.name_size()

    def address_size(self):
        return 100

    def get_address(self):
        return self.get_str(self.address_offset(), self.address_size())

    def set_address(self, param_str):
        self.set_str(self.address_offset(), self.address_size(), param_str)

    def age_offset(self):
        return self.address_offset() + self.address_size()

    def age_size(self):
        return 2

    def get_age(self):
        return self.get_little_endian(self.age_offset(), self.age_size())

    def set_age(self, param_str):
        self.set_little_endian(self.age_offset(), self.age_size(), param_str)

    def birthday_offset(self):
        return self.age_offset() + self.age_size()

    def birthday_size(self):
        return 20

    def get_birthday(self):
        return self.get_str(self.birthday_offset(), self.birthday_size())

    def set_birthday(self, param_str):
        self.set_str(self.birthday_offset(), self.birthday_size(), param_str)

    def set_header_info(self):
        self.response.status_code = 200
        self.response.content_type = 'text/plain'

    def store_data(self):
        # name
        name = conf.get('response', 'name')
        self.set_name(name)
        # address
        address = conf.get('response', 'address')
        self.set_address(address)
        # age
        age = conf.get('response', 'age')
        self.set_age(age)
        # birthday
        birthday = conf.get('response', 'birthday')
        self.set_birthday(birthday)
        
        self.is_setting_from_web = 0

    def set_data(self):
        self.response.data = self.data


if __name__ == '__main__':
    response_data = ResponseData()
    x = response_data.name_size()
    print(type(x))
    response_data.set_name('nonaka')
    response_data.hexdump_data()

