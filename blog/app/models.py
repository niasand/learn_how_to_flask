# -*- coding: utf-8 -*-
from app import db
import arrow
import datetime
import time
from flask_mongoengine.wtf import model_form

class BillRecord(db.Document):
    content = db.StringField(required=True, max_length=20)   #备注 买了啥，在哪里买的
    shop = db.StringField(required=True,max_length=20)  # 商家
    money = db.FloatField(required=True,max_length=20)  #花了多少钱
    now = arrow.utcnow().to('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")
    time = db.DateTimeField(default=now) # 记录的时间
    status = db.IntField(default=0) #暂时用不着

BillRecord_Form = model_form(BillRecord)
