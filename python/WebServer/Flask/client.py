import pprint
import requests
import configparser
from webdata import ClientRequestData
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
conf = configparser.ConfigParser()
conf.read(conf_path, 'UTF-8')
def main():
    URL = 'http://' + conf.get('settings', 'host') + ':' + conf.get('settings', 'port') + '/post'
    request_data = ClientRequestData()
    response = requests.post(URL,request_data.set_data() )

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
