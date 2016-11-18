import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    print(request.values)
    if request.method == 'POST':
        return "<h1>UserName is %s</h1>"%request.values["username"]
    else:
        return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></p>'
    


if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT','5050'))
    app.debug = True
    app.run(host=host,port=port)