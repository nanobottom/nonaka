import json
import io
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
    """
    サーバが受信したデータ、送信するデータを扱う
    """
    def __init__(self):
       self.data = bytearray()

    # データをバイト列と文字で表示する
    def hexdump_data(self):

        # バイト列の座標を表示する
        print("%08x  " % 0, end="")
        s = "|"
        for i, byte in enumerate(self.data, start=1):
            print("%02x " % byte, end="") 
            # ASCII文字の範囲外なら' '文字を表示
            if byte in range(32, 127): 
                s += chr(byte)
            else:
                s += "."
            
            # スペースと座標、文字部分を整形する 
            if i % 16 == 0:
                s += "|"
                print(" %s\n%08x  " % (s, i), end="")
                s = '|'
            elif i % 8 == 0:
                print(" ", end="")

            # 最後のスペースを整形する
            if len(self.data) == i :
                if (16 - i % 16) < 8:
                    add_space = " "
                else:
                    add_space = "  "
                space = "   " * (16 - i % 16) + add_space
                s += " " * (16 - i % 16)
                s += "|" 
                print(space, end="")
                print(s)
    
    # 文字列をアスキーコードのバイト列に変換する。指定したサイズ
    # の範囲のうち、埋まらなかったバイト列は0x00で埋める
    def str_to_ascii(self, string, size):
        param = bytearray(string, "ASCII")
        zero_lst = [0]*(size - len(param))
        param.extend(zero_lst)
        return param
    
    # 指定したオフセットとサイズにあるデータを
    # リトルエンディアンのバイト列(16進数)の文字で取得する
    def get_data_as_little_endian(self, offset, size):
        data = self.data[offset: offset+size]
        strings = ""
        #data.reverse()
        for b in data:
            strings += format(b, "02x")
            strings += " "
        strings.rstrip()
        return strings
    
    # 指定したオフセットとサイズにあるデータを
    # ビッグエンディアンのバイト列(16進数)の文字で取得する
    def get_data_as_big_endian(self, offset, size):
        data = self.data[offset: offset+size]
        strings = ""
        for b in data:
            strings += format(b, "02x")
            strings += " "
        strings.rstrip()
        return strings

    # 指定したオフセットとサイズにあるデータを
    # アスキーコードで変換した文字列で取得する
    def get_data_as_str(self, offset, size):
        data = self.data[offset: offset+size]
        strings = ''
        for b in data:
            strings += chr(b)
        return strings
    
    # ビット列から指定した桁数目のビットを取得する
    def get_data_as_bit(self, bits, digit):
        return bin(int(bin(bits>>digit), 2)&0b1)

    # ビット列から指定したオフセットからの
    # 指定した桁数のビット列を取得する
    def get_data_as_bits(self, bits, offset, digit):
        mask = 0
        for i in range(digit):
            mask += 2**i
        return bin(bits>>offset & mask)

    # 10進数または16進数の文字列をリトルエンディアンで
    # 指定したオフセットとサイズでデータのバイト列に格納する
    def set_data_as_little_endian(self, offset, size, value):
        assert value != "", "Input value is blank."
        if value[0:2] == "0x":
            self.data[offset: offset + size] = int(value, 16).to_bytes(size, "little")
        else:
            self.data[offset: offset + size] = int(value).to_bytes(size, "little")

    # 10進数または16進数の文字列をビッグエンディアンで
    # 指定したオフセットとサイズでデータのバイト列に格納する
    def set_data_as_big_endian(self, offset, size, value):
        assert value != "", "Input value is blank."
        if value[0:2] == "0x":
            self.data[offset: offset + size] = int(value, 16).to_bytes(size, "big")
        else:
            self.data[offset: offset + size] = int(value).to_bytes(size, "big")
    
    # データのバイト列の指定したオフセットに入力した文字列を
    # アスキーコードに対応したバイト列に変換して格納する。
    # 余ったサイズは0x00で埋める。
    def set_data_as_str(self, offset, size, value):
        assert value != "", "Input value is blank."
        self.data[offset: offset + size] = self.str_to_ascii(value, size)
    
    
    def set_data_as_bit(self, offset, digit, change_bit):
        assert change_bit in range(2), "'change bit' is not 0/1."
        bits = self.data[offset]
        digit -= 1
        AND_BITS = (0b11111110, 0b11111101, 0b11111011, 0b11110111, 0b11101111, 0b11011111, 0b10111111, 0b01111111)
        OR_ONE_BITS = (0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000, 0b1000000, 0b10000000)

        if change_bit == 0:
            self.data[offset] = bits & AND_BITS[digit]
        elif change_bit == 1:
            self.data[offset] = bits & AND_BITS[digit] | OR_ONE_BITS[digit]


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
        return io.BytesIO(self.data)

class ResData(WebData):
    
    def __init__(self, res_data):
        self.data = res_data

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
    res = ClientRequestData()
    res.set_data()
    res.hexdump_data()

