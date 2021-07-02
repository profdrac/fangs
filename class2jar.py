# converts compiled java-binary to executable jar
# Ashutosh Sharma
# 06-07-2020

import os

fi = 'manifest-addition'
li = ['Author: ashu@moon\n', 'Main-Class: ']
where = input('Where are you? ') + '/'
os.chdir(where)
which = input('Which file is your main(without extension)? ')
if os.path.exists(which + '.class'):
    li[1] = li[1] + which + '\n'
    fo = open(fi, 'w')
    fo.writelines(li)
    fo.close()
    print('[+] manifest added...')
    os.system('jar cmf manifest-addition ' + which + '.jar ' + which + '.class')
    os.remove(fi)
    print('[+] jar created...')
    para = input('enter any parameters to be passed: ')
    print('[+] launching jar...')
    os.system('java -jar ' + which + '.jar ' + para)
    print('\n[!] Thank you...')
else:
    print('[-] class-file not found!')
