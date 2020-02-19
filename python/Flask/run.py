import os
import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # $B:#F|$NF|IU$NJ8;zNs$r<hF@$9$k(B
    youbi = ('Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.')
    today = datetime.date.today()
    today_youbi ='(' +  youbi[today.weekday()] + ')'
    today = today.strftime("%Y/%m/%d")
    today = today + today_youbi
    print(today)
    # $B2hA|%U%!%$%kL>$r%j%9%H$H$7$F<hF@$9$k(B
    images = os.listdir(path='./static/')
    return render_template('index.html',today = today, images = images)

if __name__ == '__main__':
    app.run()
    # $B2hA|%U%!%$%kL>$r%j%9%H$H$7$F<hF@$9$k(B
    images = os.listdir(path='./static/')
    # static$B%G%#%l%/%H%jFb$N2hA|%U%!%$%k$r:o=|$9$k(B
    for image in images:
        os.remove('./static/' + image)
    print('static$B%G%#%l%/%H%jFb$N2hA|%U%!%$%k$r$9$Y$F:o=|$7$^$7$?!#(B')
