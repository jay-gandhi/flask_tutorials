import os
import pymysql
from flask import Flask, render_template,request,redirect,url_for, flash, make_response, session
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Multiple route to specific function.
@app.route('/login',methods=['GET','POST'])
# name=None means name is not required.
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            flash("Sucessfully Logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome_user'))
        else:
            error = "Error, Error"
            app.logger.warning('Incorrect Creds for %s'%request.form.get('username'))
            
    return render_template('login.html',error=error)
    
def valid_login(username,password):
    #MYSQL
    MYSQL_HOST=os.getenv('IP','0.0.0.0')
    MYSQL_USER='jay_gandhi'
    MYSQL_DB='c9'
    
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd='',
        db=MYSQL_DB
    )
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT * from user where username='%s' and password='%s'"%(username,password))
    data = cursor.fetchone()
    print(data)
    if data: return True
    else: return False
    
@app.route('/logout',methods=['GET'])
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))
    
@app.route('/',methods=['GET'])
def welcome_user(username=None):
    print(session)
    if 'username' in session:
        return render_template('welcome.html',username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT','5050'))
    app.debug = True
    app.secret_key=os.urandom(32)
    
    #logging
    handler = RotatingFileHandler('error.log',maxBytes=10000,backupCount=2)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=host,port=port)