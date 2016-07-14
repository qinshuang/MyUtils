# /usr/bin/python
# -*- coding:utf-8 -*-


import smtplib
from smtplib import SMTPAuthenticationError
import logging

server = smtplib.SMTP('smtp.qq.com', 25)
server.ehlo()
server.starttls()
server.ehlo()
server.login("599304011@qq.com", "QSasd123")
text = 'sdfsfs'
try:
    server.sendmail('qinshuang@163.com', 'qinshuang@dnion.com', text)
except SMTPAuthenticationError as erro:
    logging.exception(erro)