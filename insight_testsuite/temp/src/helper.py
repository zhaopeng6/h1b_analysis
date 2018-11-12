import os
import csv

def readheader():
    inputpath = '../input'
    files = os.listdir(inputpath)
    header = {}
    for file in files:
        filepath = os.path.join(inputpath,file)
        with open(filepath) as f:
            reader = csv.reader(f,delimiter = ';')
            header[file] = next(reader,None)
    return header
    
if __name__=='__main__':
    D = readheader()
    print(D)