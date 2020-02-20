class WebData:
    """
    サーバが受信したデータ、送信するデータを扱う
    """
    def __init__(self):
       self.data = bytearray()

    def __str__(self):
        """データをバイト列と文字(hexdump -C形式)で表示する"""

        # バイト列の座標を表示する
        s = str()
        a = '|' # ASCII文字部
        s += '{0:08X}  '.format(0)
        for i, byte in enumerate(self.data, start=1):
            s += '{0:02X} '.format(byte)
            # ASCII文字の範囲外なら' '文字を表示
            if byte in range(32, 127):
                a += chr(byte)
            else:
                a += '.'
            # iが16の倍数でASCII部を追加する
            if i % 16 == 0:
                s += '{0}|\n{1:08X}  '.format(a, i)
                a = '|' # aをクリア
            elif i % 8 == 0:
                s += ' '
            # 最後のスペースを整形する
            if len(data) == i:
                if (16 - i % 16) < 8:
                    add_space = ''
                else:
                    add_space = ' '
                s += '   ' * (16 - i % 16)
                s += add_space
                a += ' ' * (16 - i % 16)
                a += '|'
                s += a
        return s
    
    def get_data_as_little_endian(self, offset, size):
        """
        指定した範囲（オフセット、サイズ）にあるデータを
        リトルエンディアンのバイト列（16進数）の文字で取得する
        (例)array = [0x0A, 0xC4, 0xFF]
            [表示]0xFF 0xC4 0x0A 
        """
        data_array = self.data[offset: offset+size]
        hex_str = str()
        data_array.reverse()
        for byte in data_array:
            hex_str += '0x{0:02X} '.format(byte)
        hex_str.rstrip()# 末尾の空白を削除
        return hex_str
    
    def get_data_as_big_endian(self, offset, size):
        """
        指定した範囲（オフセット、サイズ）にあるデータを
        ビッグエンディアンのバイト列（16進数）の文字で取得する
        (例)array = [0x0A, 0xC4, 0xFF]
            [表示]0x0A 0xC4 0xFF
        """
        data_array = self.data[offset: offset+size]
        hex_str = str()
        for byte in data_array:
            hex_str += '0x{0:02X} '.format(byte)
        hex_str.rstrip()# 末尾の空白を削除
        return hex_str

    def get_data_as_str(self, offset, size):
        """
        指定した範囲（オフセット、サイズ）にあるデータを
        アスキーコードで変換した文字列で取得する
        (例)[97, 98, 99] -> 'abc'
        """
        data_array = self.data[offset: offset+size]
        ascii_str = str()
        for byte in data_array:
            ascii_str += chr(byte)
        return ascii_str
    
    def get_data_as_bit(self, byte, digit):
        """
        ビット列から指定した桁数目のビットを取得する
        (例) 0x01101010
             digit = 1 -> 0b1
             digit = 2 -> 0b0
             digit = 3 -> 0b1
        """
        return bin(byte >> digit & 0b1)

    """
    # ビット列から指定したオフセットからの
    # 指定した桁数のビット列を取得する
    def get_data_as_bits(self, bits, offset, digit):
        mask = 0
        for i in range(digit):
            mask += 2**i
        return bin(bits>>offset & mask)
    """

    def set_data_as_little_endian(self, offset, size, value):
        """
        10進数または16進数の文字列をリトルエンディアンで
        指定した範囲（オフセット、サイズ）でdataのバイト列に格納する
        """
        assert value != '', 'Input value is blank.'
        if value[0:2] == '0x':
            self.data[offset: offset+size] = int(value, 16).to_bytes(size, 'little')
        else:
            self.data[offset: offset+size] = int(value).to_bytes(size, 'little')

    def set_data_as_big_endian(self, offset, size, value):
        """
        10進数または16進数の文字列をビッグエンディアンで
        指定した範囲（オフセット、サイズ）でdataのバイト列に格納する
        """
        assert value != '', 'Input value is blank.'
        if value[0:2] == '0x':
            self.data[offset: offset+size] = int(value, 16).to_bytes(size, 'big')
        else:
            self.data[offset: offset+size] = int(value).to_bytes(size, 'big')
    
    def set_data_as_str(self, offset, size, value):
        """
        指定した範囲（オフセット、サイズ）のdataのバイト列に
        アスキーコードを格納する。余ったサイズは0x00で埋める
        """
        assert value != '', 'Input value is blank.'
        self.data[offset: offset+size] = self.__str_to_ascii(value, size)

    def set_data_as_bit(self, offset, digit, change_bit):
        """
        指定したオフセットのdataバイト列の1バイトに対して
        指定した桁数目のビットを0/1に変更する
        """
        bits = self.data[offset : offset + 1]
        digit -= 1
        AND_BITS = (0b11111110, 0b11111101, 0b11111011, 0b11110111, 0b11101111, 0b11011111, 0b10111111, 0b01111111)
        OR_ONE_BITS = (0b1, 0b10, 0b100, 0b1000, 0b10000, 0b100000, 0b1000000, 0b10000000)

        if change_bit == 0:
            self.data[offset: offset + 1] = bin(bits & AND_BITS[digit])
        elif change_bit == 1:
            self.data[offset: offset + 1] = bin(bits & AND_BITS[digit] | OR_ONE_BITS[digit])

    def __str_to_ascii(self, string, size):
        """
        文字列をASCIIのバイト列に変換する。
        指定したサイズの内、埋まらなかったバイト列は0x00で埋める
        """
        ascii_array = bytearray(string, "ASCII")
        zero_list = [0]*(size - len(ascii_array))
        ascii_array.extend(zero_list)# 末尾にゼロの配列を追加
        return ascii_array
    

if __name__ == '__main__':
    data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 97, 98, 99]
    web_data = WebData()
    web_data.data = bytearray(data)
    print('期待値：0x02 0x01 0x00')
    print(web_data.get_data_as_little_endian(0, 3))
    print('期待値：0x00 0x01 0x02')
    print(web_data.get_data_as_big_endian(0, 3))
    print('期待値：abc')
    print(web_data.get_data_as_str(6, 3))
    print('---hexdump data---')
    print(web_data)
