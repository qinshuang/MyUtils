#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 指定目录，用于将所有程序编译成pyc，然后删除py文件

import compileall
import sys
import os

# VERSION.
VERSION_INFO = "1.0.0.0"

RET_OK = 0
RET_ERR = -1


def Usage():
    print('Please input parameter ')
    print('-h:\t Help')
    print('usage: python mycompile.py path')
    print('-v:\t Version of the program')


# 执行bash命令
def excute_cmd(cmd):
    import commands

    status, output = commands.getstatusoutput(cmd)
    message = "run [%s],status=[%d],output=[%s]" % (cmd, status, output)
    print "run:", message
    if status != RET_OK:  # 返回值只要不是0都是失败
        print message
    return status, output


if len(sys.argv) == 1:
    Usage()
    sys.exit()
if len(sys.argv) == 2:
    filePath = (sys.argv[1] + '/').replace("//", "/")
    print "path=[%s]" % filePath
    if not os.path.exists(filePath):
        print "path=[%s] is not exists, exit!!!" % filePath
        sys.exit()
    cmd = "find  %s -name '*.pyc' | xargs rm -rf" % (filePath)
    tmpRet, info = excute_cmd(cmd)
    if tmpRet != RET_OK:  # 返回值只要不是0都是失败
        print info
        sys.exit()
    ret = compileall.compile_dir(filePath)
    print "compileall result:[%s] 1=success 0=failed" % ret
    if ret != 1:  # 返回值只要不是0都是失败
        print "compileall failed,exit!"
        sys.exit()

    cmd = "find  %s -name '*.py' | xargs rm -rf" % (filePath)

    tmpRet, info = excute_cmd(cmd)
    if tmpRet != RET_OK:  # 返回值只要不是0都是失败
        print info
        sys.exit()
    print "\n\ncompileall ok!!!"
