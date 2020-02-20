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

class ClientRequestData(WebData):

    def __init__(self, request = 0):
        self.request = request
        self.data_size = 222
        self.data = bytearray(self.data_size)

    def set_data(self):
        offset, size = 0, 100
        # name
        name = conf.get('request', 'name')
        self.set_data_as_str(offset, size, name)
        offset +=size
        # address
        size = 100
        address = conf.get('request', 'address')
        self.set_data_as_str(offset, size, address)
        offset +=size
        # age
        size = 2
        age = conf.get('request', 'age')
        self.set_data_as_little_endian(offset, size, age)
        offset +=size
        # birthday
        size = 20
        birthday = conf.get('request', 'birthday')
        self.set_data_as_str(offset, size, birthday)
        # bytearrayをファイルオブジェクトとして扱うためにio.BytesIOを使用する
        #return io.BytesIO(self.data)
        return self.data

