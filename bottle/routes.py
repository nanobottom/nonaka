
from bottle import route, template, request, response
from bottle import jinja2_template as template2
import json

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
    # display request data
    print('<リクエストを受信しました>')
    print('フォームパラメータ : {}'.format(request.params))
    print('HTTPメソッド : {}'.format(request.method))
    print('リクエスト本文 : {}'.format(request.body.read()))
    print('アスセスされたURL : {}'.format(request.url))
    print('Content-Type : {}'.format(request.content_type))
    print('Content-Length : {}'.format(request.content_length))
    print('User-Agent : {}'.format(request.get_header('User-Agent')))
    print('Date : {}'.format(request.get_header('Date')))
    print('Content-Encoding : {}'.format(request.get_header('Content-Encoding')))
    # request bodyの編集
    req_body_bytes = request.body.read()
    print('request body type : {}'.format(type(req_body_bytes)))
    req_body_bytearray = bytearray(req_body_bytes)
    req_body_bytearray[1] = 127
    print('request body : {}'.format(req_body_bytearray))
    print('request body[5] type: {}'.format(type(req_body_bytes[5])))

    # response
    res_body = json.dumps({'message':'hello world'})
    response.body = res_body
    response.status = 200
    response.content_type = 'application/json'
    return response
