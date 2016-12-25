# coding: utf-8
from __future__ import unicode_literals

from flask import Flask    # Flask 实现了wsgi应用
from flask import url_for
from backports.shutil_get_terminal_size import get_terminal_size as _get_terminal_size

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/item/1')
def item(id):
    #return  'Item: {0}'.format(id)
    pass

with app.test_request_context():
    print url_for('item',id='1')
    print url_for('item',id=2,next='/')

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000, debug = True)