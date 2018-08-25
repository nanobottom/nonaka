import pprint
import requests
import configparser
from web_data import WebData
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
def main():
    URL = 'http://' + inifile.get('settings', 'host') + ':' + inifile.get('settings', 'port') + '/post'
    web_data = WebData()
    ascii_lst = web_data.str_to_ascii('http://localhost:8080/test',100) 
    blist = [1, 2, 3, 255, 77, 89, 90]
    blist.extend(ascii_lst)
    the_bytearray = bytearray(blist)
    response = requests.post(URL, the_bytearray)

    #pprint.pprint(response.json())
    print('Message body :')
    print(response.content)
    print('URL : {} '.format(response.url))
    print('Status code : {} '.format(response.status_code))
    print('Date : {} '.format(response.headers['date']))
    print('Server : {} '.format(response.headers['server']))
    print('Content-Type : {} '.format(response.headers['content-type']))
if __name__ == '__main__':
    main()
