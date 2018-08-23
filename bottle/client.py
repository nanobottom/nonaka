import pprint
import requests
import configparser
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
def main():
    ascii_lst = []
    ascii_str = 'http://test/'
    for s in ascii_str:
        ascii_lst.append(ord(s))
    # 100bytesの内、埋まらなかった箇所に0x00を付加
    zero_lst = [0] * (100 - len(ascii_lst))
    ascii_lst.extend(zero_lst)

    blist = [1, 2, 3, 255, 77, 89, 90]
    blist.extend(ascii_lst)
    count = 1
    for i in blist:
        if count % 16 == 0:
            print('%02x \n' % i, end = '')
        else:
            print('%02x ' % i, end = '')
            if len(blist) == count:
                print('\n')
        count += 1
    the_bytearray = bytearray(blist)
    response = requests.post(
        'http://' + inifile.get('settings', 'host')
        + ':' + inifile.get('settings', 'port') + '/post' 
        , the_bytearray)

    #pprint.pprint(response.json())
    print(response.text)

if __name__ == '__main__':
    main()
