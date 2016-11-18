import os
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Home !! </h1>"

# If URL change is there, you don't have to change in anywhere, specially in Templates
# url_for take 1 positional arg.
# if you change URL in one place, You Have to change in many places.
# Like Files, Templates, Configuration files etc.
@app.route('/urlfor/<UserName>')
def urlFor(UserName):
    return url_for('disp_name',name=UserName)
    
@app.route('/username/<name>')
def disp_name(name):
    # display username
    return "<h3> User : %s</h3>"%name

@app.route('/helloroute')
def hello_world():
    # pbd - python debugger
    # import pdb; pdb.set_trace()
    return "Hello EveryOne!!"
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # ID must be an integer. 
    return "Post:  %s"%str(post_id)
    
if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    # Don't do in production Environment.
    app.debug = True
    app.run(host=host,port=port)