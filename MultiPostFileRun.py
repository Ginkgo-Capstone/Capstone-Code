##February 22
##Post Module for long runs

#imports a bunch of processes needed in the script
import time
import re 
import os
import subprocess
import os.path
import math 

#imports functions that are created in other files

from RunAERMOD import RunAERMOD
from ReadPostFilefun import ReadPostFilefun
from CreateSubFile2 import CreateSubFile2
from TexttoExcelfun import TexttoExcelFun

#dir_path = os.path.dirname(os.path.realpath(__file__))
#dir_path = dir_path + '\Run loop'
#print(dir_path)

#print(os.getcwd())

#change Directory to Run loop
#super important to have Run loop folder otherwise will not work
os.chdir("Run loop")



#reads contents of files    
f = open('MasterPFL.txt')
f1 = f.readlines()
f.close()

f = open('MasterSFC.txt')
f2 = f.readlines()
f.close


#creates variables for function
PFL = [0]*(30*24+1)
SFC = [0]*(30*24+1)

#checks if FinalConcs.txt exists and deletes it if it exists
if os.path.isfile('FinalPostConcs.txt'):
    os.remove("FinalPostConcs.txt")

f = open("MasterSFC.txt")
ftemp =  f.readlines()
lenSFC = math.floor(len(ftemp))
f.close()

f = open("MasterPFL.txt")
ftemp =  f.readlines()
lenPFL = math.floor(len(ftemp))
f.close()

if lenSFC  < lenPFL:
    mlen = lenSFC
else:
    mlen = lenPFL


# creates the FinalConcs.txt file and writes first two lines
f = open("FinalPostConcs.txt", "x")
f.write("  X             Y      AVERAGE CONC    ZELEV    ZHILL    ZFLAG    AVE     GRP       DATE     NET ID \n")

m = math.floor(mlen/(30*24))

#will run for the length of F2 minus 1
for n in range(0,m):
    #provides strings for PFL and SFC
    for i in range (30*24+1):
        PFL[i] = f1[30*24*n + i]
        SFC[i] = f2[30*24*n + i]
    
    #will create a .PFL and .SFC file using SFC and PFL variables
    CreateSubFile2(PFL,SFC)
    #runs aermod
    RunAERMOD()

    ReadPostFilefun()

PFL2 = [0]*(mlen-m*30*24)
SFC2 = [0]*(mlen-m*30*24)

for i in range (len(PFL2)):
    PFL2[i] = f1[30*24*m + i]
    SFC2[i] = f2[30*24*m + i]

CreateSubFile2(PFL2,SFC2)
#runs aermod
RunAERMOD()

ReadPostFilefun()

f.close()

TexttoExcelFun("FinalPostConcs.xlsx","FinalPostConcs.txt")
