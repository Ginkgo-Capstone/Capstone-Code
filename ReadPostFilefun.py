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
    f.close()
    conmax = 0
    line = 0
    curdate = 0
    f= open("FinalPostConcs.txt","a")
    
    t1 = re.findall(r'\d+',f1[9])
    dayone = int(t1[13])
    
    for x in f1[8:len(f1)]:
        temp = re.findall(r'\d+', x)
        date = int(temp[13])
        conc = int(temp[5])
        if dayone == date:   
            if conc > conmax:
                conmax = conc
                line = x
    f.write(line)
    conmax = 0
    line = 0
    curdate = 0
    
              
    
    for x in f1[8:len(f1)]:
        temp = re.findall(r'\d+', x)
        date = int(temp[13])
        conc = int(temp[5])
        if (date != curdate & curdate != 0):
            f.write(line)
            conmax = 0
        curdate = date
            
        if conc > conmax:
            conmax = conc
            line = x
          
    f.write(line)
    f.close 
        
        
            
    
