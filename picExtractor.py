'''
Extract images from all pdf files in a folder

Ashutosh Sharma
Created on: 10 April 2021
'''

import os
import fitz

path = input("where are pfd files? ")
os.chdir(path)
farr = os.listdir()
c = 0
for f in farr:
    if f[-4:] == '.pdf':
        doc = fitz.open(f)
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:
                    pix.writePNG(str(f[0:-4]) + ".png")
                    print("[+] Extracted " + f[0:-4] + ".png")
                    c += 1
                else:
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.writePNG(str(f[0:-4]) + ".png")
                    print("[+] Extracted " + f[0:-4] + ".png")
                    c += 1
                    pix1 = None
                pix = None
print("[.] " + str(c) + " images extracted...")
