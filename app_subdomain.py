# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, g

app = Flask(__name__)
app.config['SERVER_NAME'] = 'yang.com:5000'

@app.url_value_preprocessor
def get_site(endpoint,values):
    g.site = values.pop('subdomain') + "  yang...."

@app.route('/',subdomain = '<subdomain>')
def index():
    return g.site

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000,debug = True)

