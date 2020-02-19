import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # $B2hA|%U%!%$%kL>$r%j%9%H$H$7$F<hF@$9$k(B
    images = os.listdir(path='./static/')
    return render_template('index.html', images = images)

if __name__ == '__main__':
    app.run()
    # $B2hA|%U%!%$%kL>$r%j%9%H$H$7$F<hF@$9$k(B
    images = os.listdir(path='./static/')
    # static$B%G%#%l%/%H%jFb$N2hA|%U%!%$%k$r:o=|$9$k(B
    for image in images:
        os.remove('./static/' + image)
    print('static$B%G%#%l%/%H%jFb$N2hA|%U%!%$%k$r$9$Y$F:o=|$7$^$7$?!#(B')
