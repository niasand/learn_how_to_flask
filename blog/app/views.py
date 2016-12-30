# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Todo

@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template("index.html", todos=todos)
    # return render_template("index.html",text="Hello world")
