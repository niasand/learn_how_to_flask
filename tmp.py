# coding: utf-8
from mako.lookup import TemplateLookup
from mako.template import Template
mylookup = TemplateLookup(directories=['/Users/jerry/Library/Mobile Documents/com~apple~CloudDocs/python_love/learn_how_to_flask/mako'])
template = Template('<%include file="Hello.mako"/>', lookup=mylookup)
template.render(name='xiaoMing')