from flask import Flask, request, render_template, make_response
from webdata import RequestData, ResponseData
import configparser
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
conf_path = os.path.join(current_dir, 'config.ini')
conf = configparser.ConfigParser()
conf.read(conf_path, 'UTF-8')

app = Flask(__name__)
response_data = ResponseData()

@app.route("/", methods = ['GET'])
def index():
    return "Hello World!"

@app.route("/post", methods = ["POST"])
def post():
    request_data = RequestData(request)
    request_data.display_header_info()
    request_data.display_data_info()

    response_data.response = make_response()
    response_data.set_header_info()

    if response_data.is_setting_from_web == 0:
        response_data.store_data()
    response_data.set_data()

    response_data.is_setting_from_web = 0
    return response_data.response

@app.route("/setting_post", methods = ["GET", "POST"])
def setting_post():
    if request.method == "GET":
        return render_template("setting_post.html")
    elif request.method == "POST":
        response_data.store_data()
        response_data.set_name(request.form["name"])
        response_data.set_address(request.form["address"])
        response_data.set_age(request.form["age"])
        response_data.set_birthday(request.form["birthday"])
        response_data.is_setting_from_web = 1
        return render_template("fin_setting_post.html")


if __name__ == "__main__":
    host = conf.get("settings", "host")
    port = conf.get("settings", "port")
    app.run(host, port)
