
from bottle import route, template, request, response
from bottle import jinja2_template as template2
import json
from web_data import RequestData, ResponseJSONData, ResponseData

@route('/hello/<name>', method = 'GET')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/add', method = 'GET')
def add():
    return template2('add.html', title="jinja2では{{}}で囲まれた変数はpythonの変数として扱うことができる")
@route('/login', method = 'GET')
def login():
    return template('login.html')

@route('/login', method = 'POST')
def display_login_value():
    username = request.forms.username
    password = request.forms.password
    return template('{{username}}, {{password}}', username=username, password = password)

@route('/post', method = 'POST')
def post():
    # request
    req_data = RequestData(request)
    req_data.display_header_info()
    req_data.display_body_info()
    
    # response(in case of sending JSON data))
    #res_data = ResponseJSONData(response)
    #res_data.set_param()

    res_data = ResponseData(response)
    res_data.set_param_to_body()

    return res_data.response
