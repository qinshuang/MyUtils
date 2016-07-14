# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/12/16.
"""

from lib.logutils import logger_init

import json
import urllib2
import json
from pprint import pprint

logger_init(**{'': {'handler': 'console', 'level': 'debug', 'filename': 'log.log'}})

# jsonreq = json.dumps({ 'id': 'qwer',
#                       'method': 'aria2.addUri',
#                       'params': [['https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/logo_white_fe6da1ec.png']]})
# c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
# print c.read()

#
# jsonreq = json.dumps({'id': 'qwer', 'method': 'aria2.tellActive'})
# c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
# pprint(json.loads(c.read()))


# jsonreq = json.dumps({'id': 'qwer', 'method': 'aria2.changeGlobalOption', 'params': [{'dir': '/home'}]})
# c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
# pprint(json.loads(c.read()))

jsonreq = json.dumps({'id': 'qwer', 'method': 'aria2.getGlobalOption'})
c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
pprint(json.loads(c.read()))
