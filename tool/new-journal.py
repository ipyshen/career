import os
from shutil import copy
import datetime


today = datetime.date.today()
date_str = f'{today.year}{str(today.month).zfill(2)}{str(today.day).zfill(2)}'

index = 1
rootpath = f'{os.path.abspath(__file__)}/../..'

while True:
    dirname = f'{date_str}-{index}'
    if dirname in os.listdir(rootpath):
        index += 1
    else:
        newPath = f'{rootpath}/{dirname}'
        oldPath = f'{rootpath}/asset/template.html'

        os.mkdir(f'{rootpath}/{dirname}')
        copy(oldPath, newPath+'/index.html')
        break
