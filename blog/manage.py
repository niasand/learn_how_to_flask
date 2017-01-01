# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from app import app
from app.models import BillRecord

manager = Manager(app)

manager.add_command("runserver",Server(host='0.0.0.0',port=9000,use_debugger=True))

@manager.command
def save_todo():
    todo = BillRecord(money="19.89",shop="amazon",content="Kindle")
    todo.save()


if __name__ == "__main__":
    manager.run()
