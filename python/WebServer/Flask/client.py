import pprint
import requests
import configparser
from client_data import ClientRequestData, ClientResponseData
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
conf = configparser.ConfigParser()
conf.read(conf_path, 'UTF-8')
def main():
    URL = 'http://' + conf.get('settings', 'host') + ':' + conf.get('settings', 'port') + '/test'
    request_data = ClientRequestData()
    response = requests.post(URL,request_data.set_data())
    response_data = ClientResponseData(response)
    print('Message body:')
    response_data.hexdump_data()
    response_data.display_header_info()
if __name__ == '__main__':
    main()
