# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/14/16.
"""

import os
import imp
import logging

logger = logging.getLogger(__file__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_module(package_name):
    """  """
    _modules = package_name.split(".")
    if not _modules:
        return None
    _modules[-1] += ".py"
    try:
        return imp.load_source('mytest.mytest', os.path.join(BASE_DIR, *_modules))
    except BaseException as err:
        raise ValueError

