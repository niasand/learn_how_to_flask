# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, request,abort,redirect,url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/people')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name: {0}; UA: {1}'.format(name,user_agent)

@app.route('/login/',method = ['GET','POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        return 'User: {0} login'.format(user_id)
    else:
        return 'Open login page'


@app.route('/select/')
def secert():
    abort(401)
    print 'This will never executed'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=app.debug)