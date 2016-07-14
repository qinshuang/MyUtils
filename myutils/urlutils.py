# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/28/16.
"""
import urllib
import urllib2
import logging
import httplib


def http_post(url, data):
    try:
        _data = urllib.urlencode(data)  # 编码工作
        req = urllib2.Request(url, _data)  # 发送请求同时传data表单
        response = urllib2.urlopen(req)  # 接受反馈的信息
        return response
    except urllib2.HTTPError, e:
        if e.code != 200:
            logging.error("connect url(" + url + ") failed.")
    except Exception, e:
        logging.exception(e)
    return None


def http_get(url, data):
    try:
        _data = urllib.urlencode(data)  # 编码工作
        response = urllib2.urlopen(url + "?" + _data)  # 接受反馈的信息
        return response
    except urllib2.HTTPError, e:
        if e.code != 200:
            logging.error("connect url(" + url + ") failed.")
    except Exception, e:
        logging.exception(e)
    return None


def https_get(url, data, host, port=None, headers={}):
    try:
        conn = httplib.HTTPSConnection(host, port=port)
        _data = urllib.urlencode(data)  # 编码工作
        conn.request("GET", url + "?" + _data, headers=headers)
        response = conn.getresponse()
        return response
    except urllib2.HTTPError, e:
        logging.info('https get status code ' + e.code)
        if e.code != 200:
            logging.error("connect url(" + url + ") failed.")
    except Exception, e:
        logging.exception(e)
    return None


