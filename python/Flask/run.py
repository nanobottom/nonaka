import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # 画像ファイル名をリストとして取得する
    images = os.listdir(path='./static/')
    return render_template('index.html', images = images)

if __name__ == '__main__':
    app.run()
    # 画像ファイル名をリストとして取得する
    images = os.listdir(path='./static/')
    # staticディレクトリ内の画像ファイルを削除する
    for image in images:
        os.remove('./static/' + image)
    print('staticディレクトリ内の画像ファイルをすべて削除しました。')
