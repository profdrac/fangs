'''
MintMissers
------------
A tool to automatically extract TeachMint absentees from the csv file
+ get low timers as well

by, Ashutosh Sharma
Dont remember the creation date :p Sometime in April 2021?
'''
import csv

def get_absentees(c):
    print('..............................')
    with open(c, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        print("Absentees for ", end='')
        for row in csv_reader:
            if row[0] == 'Name': print(row[-1]+'\n')
            if row[-1]=='A': print(row[0])
    print('..............................'+2*'\n')
    return

def get_lowtimers(c, bound):
    print('..............................')
    with open(c, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        print("Low timers for ", end='')
        for row in csv_reader:
            if row[0] == 'Name':
                print(row[-1]+'\n')
                continue
            if len(row[-1])>1:
                per = int(row[-1][:-4])
                if per<bound: print(row[0] +' = '+ row[-1][:-3])
    print('..............................'+2*'\n')
    return


fil = input('Name of file from TeachMint? [Without .csv][Should be in current folfder]: ')+'.csv'
lows = str.capitalize(input('Get low-timers also? (Y/N): '))
if lows == 'Y': range = input('Minimum % time of the student in lecture? [Do not give % sign]: ')
get_absentees(fil)
if lows == 'Y': get_lowtimers(fil, int(range))