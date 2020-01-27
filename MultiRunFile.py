##January 15th
##Module for long runs

#imports a bunch of processes needed in the script
import time
import re 
import os
import subprocess
import os.path

#imports functions that are created in other files

from RunAERMOD import RunAERMOD
from ReadFile import MaxConFun
from CreateSubFile import CreateSubFile

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
PFL = [0,0]
SFC = [0,0,0]

#checks if FinalConcs.txt exists and deletes it if it exists
if os.path.isfile('FinalConcs.txt'):
    os.remove("FinalConcs.txt")

    
# creates the FinalConcs.txt file and writes first two lines
f = open("FinalConcs.txt", "x")
f.write("1-hr avg \\ 2-hr avg \n Conc,X-Cord, Y-Cord, Date/Time \n")

#will run for the length of F2 minus 1
for n in range(1,len(f2)-1):
    #provides strings for PFL and SFC
    PFL[0] = f1[n-1]
    PFL[1] = f1[n]
    SFC[0] = f2[n]
    SFC[1] = f2[n+1]
    SFC[2] = f2[0]
    
    #will create a .PFL and .SFC file using SFC and PFL variables
    CreateSubFile(PFL,SFC)
    #runs aermod
    RunAERMOD()
    #extracts the highest concentrations, coordinates and time stamp
    #for 1 hr average and 2 hr average
    x = MaxConFun()
    #converts into a string
    x =str(x).strip('[]') + '\n'
    #writes values into text file
    f= open('FinalConcs.txt',"a")
    f.write(x)
    
    
    
