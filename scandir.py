# -*- coding: utf-8 -*-

import os

path = input("Input path: ")
for entry in os.scandir(path):
   if entry.name.startswith('.') and entry.is_dir():
       print(entry.name)