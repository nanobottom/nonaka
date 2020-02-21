import json
import io
import configparser
import os
from webdata import WebData

conf = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
try:
    if os.path.exists(conf_path) == False:
        raise SystemError('Missing "config.ini" file at {}.'.format(current_dir))
except SystemError as e:
    print("SystemError : {}".format(e))
conf.read(conf_path, 'UTF-8')

class ServerRequestData(WebData):

    def __init__(self, requests_instance):
        super().__init__(requests_instance)
        self.request = requests_instance
        self.data = requests_instance.data
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
        print('name               : {}'.format(self.get_data_as_str(0,100)))
        print('address            : {}'.format(self.get_data_as_str(100,100)))
        print('age                : {}'.format(self.get_data_as_big_endian(200,2)))
        print('birthday           : {}'.format(self.get_data_as_str(202,20)))

    def name_offset(self):
        return 0

    def name_size(self):
        return 100

    def get_name(self):
        return self.get_data_as_str(self.name_offset(), self.name_size())

    def set_name(self, param_str):
        self.set_data_as_str(self.name_offset(), self.name_size(), param_str)
        
    def address_offset(self):
        return self.name_offset() + self.name_size()

    def address_size(self):
        return 100

    def get_address(self):
        return self.get_data_as_str(self.address_offset(), self.address_size())

    def set_address(self, param_str):
        self.set_data_as_str(self.address_offset(), self.address_size(), param_str)

    def age_offset(self):
        return self.address_offset() + self.address_size()

    def age_size(self):
        return 2

    def get_age(self):
        return self.get_data_as_big_endian(self.age_offset(), self.age_size())

    def set_age(self, param_str):
        self.set_data_as_big_endian(self.age_offset(), self.age_size(), param_str)

    def birthday_offset(self):
        return self.age_offset() + self.age_size()

    def birthday_size(self):
        return 20

    def get_birthday(self):
        return self.get_data_as_str(self.birthday_offset(), self.birthday_size())

    def set_birthday(self, param_str):
        self.set_data_as_str(self.birthday_offset(), self.birthday_size(), param_str)
    def error_check(self):
        age = int(self.get_age())
        self.range_check(age, 'age' , 20, 80)

    # 受信したデータが仕様通りの範囲に収まっているか判断し、
    # 範囲外ならresponse_status_codeを400にする
    def range_check(self, param, param_name, lower, upper):
        # range関数は上限の値を含まないため1を足す
        upper += 1
        if (param in range(lower, upper)) == False:
            print('Parameter {} is over range of num.'.format(param_name))
            self.response_status_code = 400



"""
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
"""
class ServerResponseData(WebData):

    def __init__(self, requests_instance = None):
        super().__init__(requests_instance)
        self.data_size = 222
        self.response = requests_instance
        self.data = bytearray(self.data_size)
        self.is_setting_from_web = 0

    def name_offset(self):
        return 0

    def name_size(self):
        return 100

    def get_name(self):
        return self.get_data_as_str(self.name_offset(), self.name_size())

    def set_name(self, param_str):
        self.set_data_as_str(self.name_offset(), self.name_size(), param_str)
        
    def address_offset(self):
        return self.name_offset() + self.name_size()

    def address_size(self):
        return 100

    def get_address(self):
        return self.get_data_as_str(self.address_offset(), self.address_size())

    def set_address(self, param_str):
        self.set_data_as_str(self.address_offset(), self.address_size(), param_str)

    def age_offset(self):
        return self.address_offset() + self.address_size()

    def age_size(self):
        return 2

    def get_age(self):
        return self.get_data_as_little_endian(self.age_offset(), self.age_size())

    def set_age(self, param_str):
        self.set_data_as_little_endian(self.age_offset(), self.age_size(), param_str)

    def birthday_offset(self):
        return self.age_offset() + self.age_size()

    def birthday_size(self):
        return 20

    def get_birthday(self):
        return self.get_data_as_str(self.birthday_offset(), self.birthday_size())

    def set_birthday(self, param_str):
        self.set_data_as_str(self.birthday_offset(), self.birthday_size(), param_str)

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
    res = ResponseData()
    x = res.name_size()

    print(type(x))
    y = 0b10101010
    print(res.get_data_as_bit(y, 0))
    print(res.get_data_as_bit(y, 1))
    res.set_name('nonaka')
    # set_data_as_big_endianのテスト
    res.set_data_as_big_endian(8, 2, "1234")
    res.set_data_as_little_endian(10, 2, "1234")
    print(res.get_data_as_little_endian(0, 5)+"$")
    print(res.get_data_as_str(0, 10))
    print(res)

