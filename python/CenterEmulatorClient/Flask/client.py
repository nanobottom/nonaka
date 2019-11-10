import requests
import configparser
import os
from webdata import ClientRequestData, ResData

# コンフィグファイルから設定値を読み込む
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
conf = configparser.ConfigParser()
conf.read(conf_path, 'UTF-8')
def main():
    req = ClientRequestData()

    # POST通信によるデータの送受信
    res = requests.post(conf.get('settings', 'url'),req.set_data())
    res_data = ResData(res.content)
    
    print('Message body :')
    res_data.hexdump_data()
    print('URL : {} '.format(res.url))
    print('Status code : {} '.format(res.status_code))
    print('Date : {} '.format(res.headers['date']))
    print('Server : {} '.format(res.headers['server']))
    print('Content-Type : {} '.format(res.headers['content-type']))

if __name__ == '__main__':
    main()
