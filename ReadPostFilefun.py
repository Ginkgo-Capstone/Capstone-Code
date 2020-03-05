##Read Post File
## Feb 20th

#import time 
import re 
#import os
#import subprocess

#os.chdir(r"C:\Users\Alex\Documents\Capstoni Macaroni\PCLI AERMOD FILES")


def ReadPostFilefun():
    f = open('POSTPLOT.PLT')

    f1 = f.readlines()
    print(str(len(f1)))
    f.close()
    conmax = 0
    line = 0
    curdate = 0
    f= open("FinalPostConcs.txt","a")

    for x in f1[8:len(f1)]:
        temp = re.findall(r'\d+', x)
        date = int(temp[13])
        conc = int(temp[5])
        if (date != curdate and curdate != 0):
            f.write(line)
            conmax = 0
            curdate = date
            
        if conc > conmax:
            conmax = conc
            curdate = date
            line = x
    f.close 
        
        
            
    
