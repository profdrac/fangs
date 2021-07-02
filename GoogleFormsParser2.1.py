'''
GoogleFormsParser 2.1
---------------------
A tool to convert objective question paper from Google Forms to MS-Word file
[ so I don't have to type it again :D ]

by, Ashutosh Sharma
Created on: 20 April 2020
-----------------------------------------------------------------------------
version 1: 20 April 2020
Supports 20-marks tests

version 2: 17 June 2020
Supports 100-marks tests

version 2.1: 5 August, 2021
Added support for questions of any marking scheme
-----------------------------------------------------------------------------
Todo: Make it set my papers? LOL
'''

from urllib import request
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Cm

print('Welcome to Cafe Lockdown')
print('by, Ashutosh Sharma')
print('--- 05-08-2020 ---')
url = input('Paste link to your Google form: ')
html = request.urlopen(url)
soup = BeautifulSoup(html, features="html.parser")
soupName = soup.title.string.strip()
print('[>] ' + soupName)
print('[+] Preparing soup...')
for script in soup(["script", "style"]):
    script.extract()
print('[+] Getting noodles...')
block = soup.findAll("div", {"class": "freebirdFormviewerComponentsQuestionBaseRoot"})
doc = Document()
sections = doc.sections
for section in sections:
    section.top_margin = Cm(1.27)
    section.bottom_margin = Cm(1.27)
    section.left_margin = Cm(1.27)
    section.right_margin = Cm(1.27)
table = doc.add_table(1, 2)
table.style = doc.styles['Table Grid']
c1 = table.cell(0, 0)
c2 = table.cell(0, 1)
c1.merge(c2)
c1.text = bytearray.fromhex('496e73657274204f4c53204865616'
                            '465722048657265202d2d2d20476f6'
                            'f676c65466f726d735061727365722'
                            '0322e3020c2a941736875746f73682'
                            '0536861726d61').decode()
print('[+] Adding veggies...')
for i in block:
    question = i.select('div')[2].text
    if question[-1:] == '*':
        question = question[:-2]
    marks = i.select('div')[4].text
    if marks[-7:] == ' points':
        marks = marks[:-7]
    elif marks[-6:] == ' point':
        marks = marks[:-6]
    if not marks.isnumeric():
        continue
    ans = i.find_all("span", {"class": "docssharedWizToggleLabeledLabelText"})
    answers = 'Options = '
    for j in ans:
        answers += j.text + ', '
    answers = answers[:-2]
    cells = table.add_row().cells
    cells[0].text = question + '\n' + answers
    cells[1].text = marks
    cells[0].width = Cm(18.44)
    cells[1].width = Cm(1.0)
print('[+] Adding spices...')
doc.save(soupName + '.docx')
print('[!] Done! Serving your soup named...' + soupName + '.docx')
print('[>] Bon appétit OLS :)')
input('Press enter to close')