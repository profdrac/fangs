'''
set_classdata
-------------
A tool to set my data of online class for next day, so that I can fill my daily report with one click :p
(Prepares data for Reporter)
'''

import os
from datetime import datetime

where = os.path.dirname(os.path.realpath(__file__))
when = input('Date? ')
with open(where+'\\data\\daily\\'+when+'.txt','w') as f:
    while True:
        data = ['']*6
        data[0] = input('Period? ')
        data[1] = input('Chapter Number? ')
        data[2] = input('Recaptulation? ')
        data[3] = input('Homework? ')
        data[4] = input('Summary? ')
        data[5] = input('Shared video [y/n]? ')
        line = ''
        for d in data: line += d + '\\'
        f.write(line[:-1]+'\n')
        another = input('Another class? ')
        if another=='Y' or another=='y': continue
        else: break
