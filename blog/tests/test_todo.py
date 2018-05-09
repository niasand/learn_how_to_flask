#: -*- coding: utf-8 -*-
import unittest
from app import app
from app.models import BillRecord
from werkzeug.exceptions import HTTPException

class BillTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        # clear data for each test
        bills = BillRecord.objects.all()
        for bill in bills:
            bill.delete()

    def test_index(self):
        rv = self.app.get("/")
        assert "Bill Record" in rv.data

    def test_empty(self):
        rv = self.app.get("/")
        assert "No bills ,please add it" in rv.data

    def test_addtodo(self):
        rv = self.app.post("/add",data=dict(money=1.65,content="add a todo to test",shop="amazon"))
        todo = BillRecord.objects.get_or_404(money=1.65,content="add a todo to test",shop="amazon")
        assert todo is not None

    def test_none_todo(self):
        try:
            todo = BillRecord.objects.get_or_404(money=1.65,content="add a todo to test",shop="amazon")
        except HTTPException as e:
            assert e.code == 404

    @unittest.skip("skip this useless")
    def test_done_todo(self):
        todo = BillRecord(money=1.65,content="add a todo to test",shop="amazon")
        todo.save()
        url = '/done/' + str(todo.id)
        rv = self.app.get(url)
        assert '/undone/' + str(todo.id) in rv.data

    @unittest.skip("skip this useless")
    def test_undone_todo(self):
        todo = BillRecord(money=1.65,content="add a todo to test",shop="amazon")
        todo.save()
        url = '/undone/' + str(todo.id)
        rv = self.app.get(url)
        # print rv.data
        assert  '/done/' + str(todo.id) in rv.data
        # assert 'done' in rv.data  //this is also ok

    def test_delete_todo(self):
        todo = BillRecord(money=1.65,content="add a todo to test",shop="amazon")
        todo.save()
        url = '/delete/' + str(todo.id)
        rv = self.app.get(url)
        assert 'No bills ,please add it' in rv.data

    def test_404(self):
        rv = self.app.get('/404test')
        assert "Not Found" in rv.data