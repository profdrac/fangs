'''
cardPrinter
-----------
Exports report-cards of the students from My-Excel-Resultsheet to PDFs
Also makes a merged PDF with all cards
Important -- In Excel, REPORTCARD should be active-sheet!

by, Ashutosh Sharma
on, 15 September, 2020
'''

from PyPDF2 import PdfFileMerger
import win32com.client
import os

def doMyWork(fil, nos):
    path = os.getcwd()
    app = win32com.client.Dispatch('Excel.Application')
    app.Visible = False
    wb = app.Workbooks.Open(path+'\\'+fil+'.xlsx')
    merger = PdfFileMerger()
    for i in range(1, int(nos)+1):
        wb.Worksheets('TeacherPanel').Range('A2').Value = i
        wb.Activesheet.Name = 'REPORTCARD'
        path_to_pdf = path+'\\'+str(i)+'.pdf'
        wb.ActiveSheet.ExportAsFixedFormat(0, path_to_pdf)
        merger.append(path_to_pdf)
        print('[~] Printed '+str(i)+'.pdf')
    wb.Close(SaveChanges=False)
    app.Quit()
    app = None
    print('[*] Making a merged PDF also... Please wait...')
    merger.write(fil+'.pdf')
    merger.close()
    print('All done! See you next year!')
    return

doMyWork(input('What is the filename? [without .xlsx]: '), input('How many students are there? '))