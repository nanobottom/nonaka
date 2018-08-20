
import configparser
from bottle import route, template, run
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)
run(host = inifile.get('settings', 'host'), port = inifile.get('settings', 'port'))
