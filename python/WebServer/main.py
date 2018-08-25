import configparser
from bottle import run
import routes
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

print('host : {}'.format(inifile.get('settings', 'host')))
print('port : {}'.format(inifile.get('settings', 'port')))
if __name__ == '__main__':
    run(host = inifile.get('settings', 'host'), port = inifile.get('settings', 'port'))
