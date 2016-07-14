# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/24/16.
"""

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class BaseConf(object):
    """"""

    def __init__(self, ):
        """Constructor for BaseConf"""
        super(BaseConf, self).__init__()

    def load_parser(self, file_path):
        """  """
        self.parser = configparser.ConfigParser()
        try:
            self.parser.read(file_path)
        except Exception as e:
            print 'read %s faild and Exception is "%s"' % (file_path, e)
            return False
