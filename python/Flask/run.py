import os
import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # 今日の日付の文字列を取得する
    youbi = ('Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.')
    today = datetime.date.today()
    today_youbi ='(' +  youbi[today.weekday()] + ')'
    today = today.strftime("%Y/%m/%d")
    today = today + today_youbi
    print(today)
    # 画像ファイル名をリストとして取得する
    images = os.listdir(path='./static/')
    return render_template('index.html',today = today, images = images)

if __name__ == '__main__':
    app.run()
    # 画像ファイル名をリストとして取得する
    images = os.listdir(path='./static/')
    # staticディレクトリ内の画像ファイルを削除する
    for image in images:
        os.remove('./static/' + image)
    print('staticディレクトリ内の画像ファイルをすべて削除しました。')
