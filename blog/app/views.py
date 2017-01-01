# -*- coding: utf-8 -*-

from app import app
from flask import render_template,request
from models import BillRecord,BillRecord_Form



@app.route('/')
def index():
    form = BillRecord_Form()
    todos = BillRecord.objects.order_by('-time')

    return render_template("index.html", todos=todos,form=form)
    # return render_template("index.html",text="Hello world")

@app.route('/add', methods=['POST', 'GET'])
def add():
    # content = request.form.get("content")
    form = BillRecord_Form(request.form)
    if form.validate():
        money = form.money.data
        shop = form.shop.data
        content = form.content.data
        todo = BillRecord(money=money,shop=shop,content=content)
        todo.save()

    todos = BillRecord.objects.order_by('-time')
    return  render_template("index.html",todos=todos,form=form)


@app.route('/done/<string:todo_id>')
def done(todo_id):
    form = BillRecord_Form()
    todo = BillRecord.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()

    todos = BillRecord.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
    form = BillRecord_Form()
    todo = BillRecord.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()

    todos = BillRecord.objects.order_by('-time')
    return  render_template("index.html", todos=todos,form=form)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    form = BillRecord_Form()
    todo = BillRecord.objects.get_or_404(id=todo_id)
    todo.delete()
    todos = BillRecord.objects.order_by('-time')
    return render_template("index.html",todos=todos,form=form)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404
