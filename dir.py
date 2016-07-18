# -*- coding: utf-8 -*-

import os
import sys

rootpath = input("请输入目录：")
catedir = os.listdir(rootpath)

for avs in catedir:
    print(avs)
