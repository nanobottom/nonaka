import pprint
import requests
import configparser
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
def main():
    blist = [1, 2, 3, 255, 77, 89, 90 ]
    the_bytearray = bytearray(blist)
    response = requests.post(
        'http://' + inifile.get('settings', 'host')
        + ':' + inifile.get('settings', 'port') + '/post' 
        , the_bytearray)

    pprint.pprint(response.json())

if __name__ == '__main__':
    main()
