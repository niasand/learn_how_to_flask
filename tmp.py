# coding: utf-8
from mako.lookup import TemplateLookup
from mako.template import Template
from sqlalchemy import create_engine
mylookup = TemplateLookup(directories=['./mako'])
template = Template('<%include file="Hello.mako"/>', lookup=mylookup)
template.render(name='xiaoMing')

def orm():
    engine = create_engine('sqlite://',echo=False)
    with engine.connect() as con:
        rs = con.execute('SELECT 1')
        print rs.fetchone()
if __name__ == '__main__':
    orm()