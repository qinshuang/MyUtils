# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 7/5/16.
"""
import celery
from celery import Task
from celery import Celery
import time
app = Celery('tasks', broker='redis://localhost')

@app.task
def add(x, y):
    time.sleep(10)
    open('a','wr')
    return x + y

print time.time()
add.delay(4, 4)
print time.time()
