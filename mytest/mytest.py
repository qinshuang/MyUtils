# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/12/16.
"""
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.core.mail import send_mail
import ConfigParser
CONF = ConfigParser.ConfigParser()
CONF.read('jumpserver.conf')
MAIL_FROM = CONF.get('mail', 'email_host_user')
try:
    send_mail('1234', '1231412', MAIL_FROM, ['qinshuang@dnion.com'], fail_silently=False)
except BaseException as e:
    print e[0]
    print e[1]
    import chardet
    print chardet.detect(e[1])
    print e[1].encode('utf-8')