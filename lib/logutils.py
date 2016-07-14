# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/8/16.
"""

import logging
from logging import handlers

from tornado.log import LogFormatter

# --------------------------------------------------
# 日志格式
# --------------------------------------------------
# %(asctime)s       年-月-日 时-分-秒,毫秒 2013-04-26 20:10:43,745
# %(filename)s      文件名，不含目录
# %(pathname)s      目录名，完整路径
# %(funcName)s      函数名
# %(levelname)s     级别名
# %(lineno)d        行号
# %(module)s        模块名
# %(message)s       消息体
# %(name)s          日志模块名
# %(process)d       进程id
# %(processName)s   进程名
# %(thread)d        线程id
# %(threadName)s    线程名


# timed_rotating_file_handler = logging.handlers.TimedRotatingFileHandler(
#                 filename=options.log_file_prefix,
#                 when=options.log_rotate_when,
#                 interval=options.log_rotate_interval,
#                 backupCount=options.log_file_num_backups)

steam_handler = logging.StreamHandler()
DEFAULT_FORMAT = '%(color)s[%(name)s][%(levelname)1.8s][%(asctime)s][%(module)s:%(lineno)d]%(end_color)s %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_tain_file_handler(filename, max_bytes=100 * 1000 * 1000, backup_count=10):
    """  """
    channel = logging.handlers.RotatingFileHandler(
        filename=filename,
        maxBytes=max_bytes,
        backupCount=backup_count)
    channel.setFormatter(LogFormatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT))
    return channel


def get_steam_handler():
    """  """
    channel = logging.StreamHandler()
    channel.setFormatter(LogFormatter(fmt=DEFAULT_FORMAT, datefmt=DEFAULT_DATE_FORMAT))
    return channel


def logger_init(**kwargs):
    """
        kwargs={
            'console':{'handler':'console','level':'debug'}
        }

    """
    if not kwargs:
        raise ValueError(u"kwargs参数错误")
    for (log_name, kwarg) in kwargs.items():
        logger = logging.getLogger(log_name)
        logger.setLevel(kwarg.get('level', 'info').upper())
        if 'handler' not in kwarg:
            raise ValueError(u"kwargs 中无 handler 参数")
        handlers = kwarg['handler'].split(',')
        for handler in handlers:
            if handler == 'file':
                logger.addHandler(get_tain_file_handler(kwarg['filename']))
            elif handler == 'console':
                logger.addHandler(get_steam_handler())


if __name__ == "__main__":
    logger_init(**{'': {'handler': 'console', 'level': 'debug', 'filename': 'log.log'},
                   '__main__': {'handler': 'file', 'level': 'debug', 'filename': 'log.log'}})
    logger = logging.getLogger(__name__)
    logger.info('aaadfadfa')
