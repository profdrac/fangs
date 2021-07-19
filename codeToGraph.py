'''
Generates a simple line-chart based on the length of code on each line

Usage: python codeToGraph.py <filename>
@author: Ashutosh Shrama
July 19, 2021
'''
import sys
import matplotlib.pyplot as plt

def prepare(infile):
    data = [0]*2
    with open(infile, 'r') as f:
        for line in f:
            data[0] += 1
            if len(line)>data[1]: data[1] = len(line)
    return data

fname = sys.argv[1]
data = prepare(fname)
x, y, i = [0]*data[0], [0]*data[0], 0
with open(fname, 'r') as f:
    for line in f:
        x[i], y[i] = i, len(line)
        i += 1
plt.plot(x, y)
plt.axis([0,data[0],0,data[1]])
plt.show()
