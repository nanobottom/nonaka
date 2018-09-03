import pprint
import requests
import configparser
from web_data import ClientRequestData
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
def main():
    URL = 'http://' + inifile.get('settings', 'host') + ':' + inifile.get('settings', 'port') + '/post'
    request_data = ClientRequestData()
    response = requests.post(URL,request_data.set_param_to_body() )

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
