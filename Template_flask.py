import os

from flask import Flask, render_template

app = Flask(__name__)


# Multiple route to specific function.
@app.route('/hello')
@app.route('/hello/<name>')
# name=None means name is not required.
def hello(name=None):
    return render_template('hello.html',name_template=name)

if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT','5050'))
    app.debug = True
    app.run(host=host,port=port)