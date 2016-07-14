# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/24/16.
"""

import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from lib.configutils import *


class DBConf(BaseConf):
    """"""

    def __init__(self, ):
        """Constructor for DBConf"""
        super(DBConf, self).__init__()
        self.host = None
        self.port = None
        self.name = None

    def load(self, file_path):
        """  """
        self.load_parser(file_path)
        self.host = self.parser.get('db', 'host')
        self.port = self.parser.getint('db', 'port')
        self.name = self.parser.get('db', 'name')


db_conf = DBConf()

db_conf.load(os.path.join(BASE_DIR, 'temp/test_confg.ini'))

print db_conf.__dict__
