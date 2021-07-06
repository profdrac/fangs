'''
Reporter v2
--------
Automatically fills the daily class reports of online classes for me :)

by, Ashutosh Sharma
6 July 2021

Version 2:
---------------------------
updated for new schedule
'''

import os
import webbrowser
import pyautogui as p
from datetime import datetime

def getTime(period):
    if period=='1': return '9:00-9:25'
    elif period=='2': return '9:35-10:00'
    elif period=='3': return '10:10-10:35'
    elif period=='4': return '11:00-11:25'
    elif period=='5': return '11:35-12:00'
    else: return '12:10-12:35'

def getTodaysClasses(cfile):
    x = ''
    aajx = str(datetime.today().weekday())
    with open(cfile, 'r') as f1:
        for line1 in f1:
            sl1=line1.split(',')
            for i in range(4,len(sl1)):
                timetable1 = sl1[i].split('=')
                if timetable1[0]==aajx: x+=sl1[0]+','
    return x[:-1]

where = os.path.dirname(os.path.realpath(__file__))
form = ['']*15
print('Welcome to Reporter...')
clsses = getTodaysClasses(where+'\\data\\classes2.txt').split(',')
print('Please do not click mouse until I finish my work!')
for cls in clsses:
    with open(where+'\\data\\classes2.txt', 'r') as f:
        for line in f:
            sl=line.split(',')
            if sl[0]==cls.upper():
                form[0] = sl[1]
                form[1] = datetime.today().strftime('%m%d%Y')
                form[2] = sl[3]
                form[3] = sl[2]
                form[6] = '30'
                aaj = str(datetime.today().weekday())
                for i in range(4,len(sl)+1):
                    timetable = sl[i].split('=')
                    if timetable[0]==aaj:
                        if len(timetable[1])>1: timetable[1]=timetable[1][0]
                        form[5] = getTime(timetable[1])
                        form[7] = timetable[1]
                        break
                break
    form[8] = 'Ashutosh Sharma'
    form[9] = 'None'
    form[4] = ''
    with open(where+'\\data\\daily\\'+form[1]+'.txt','r') as mat:
        for line in mat:
            matline = line.split('\\')
            if form[7] == matline[0]:
                with open(where+'\\data\\'+cls[:-1]+'.txt','r') as chap:
                    for c in chap:
                        chapter_name = c.split(',')
                        tc = matline[1].split(',')
                        for ech in tc:
                            if ech==chapter_name[0]:
                                form[4] += chapter_name[0]+'. '+chapter_name[1] + ', '
                                break
                form[4] = form[4][:-2]
                form[11] = matline[2]
                form[12] = matline[3]
                form[13] = matline[4]
                if matline[5][0]=='y' or matline[5][0]=='Y':
                    msg = 'Recorded lecture shared on Google Classroom'
                    if form[0][0] == 'I' or form[0][0] == 'X': form[10] = msg+'/Code shared on Github'
                    else: form[10] = msg
                else: form[10] = 'N/A'
    form[14] = 'N/A'
    webbrowser.open('google-form-url',autoraise=True)
    p.sleep(5)
    for i in range(0, 15):
        p.press('tab')
        p.write(form[i])
print('Done! Have a nice day!')