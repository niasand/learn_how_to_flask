# -*- coding: utf-8 -*-
from app import db
import arrow
import datetime
import time
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    #time = db.DateTimeField(default=datetime.datetime.now())
    now = arrow.utcnow().to('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")
    time = db.DateTimeField(default=now)
    status = db.IntField(default=0)

TodoForm = model_form(Todo)
