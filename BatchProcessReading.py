#Run Batches and read Post file
#March 4th

#imports a bunch of processes needed in the script
import time
import re 
import os
import subprocess
import os.path


#imports functions that are created in other files

from RunAERMOD import RunAERMOD
from ReadPostFilefun import ReadPostFilefun
from TexttoExcelfun import TexttoExcelFun


#change Directory to Run loop
#super important to have Run loop folder otherwise will not work
os.chdir("Run loop")

RunAERMOD()

#checks if FinalConcs.txt exists and deletes it if it exists
if os.path.isfile('FinalPostConcs.txt'):
    os.remove("FinalPostConcs.txt")

    
# creates the FinalConcs.txt file and writes first two lines
f = open("FinalPostConcs.txt", "x")
f.write("  X             Y      AVERAGE CONC    ZELEV    ZHILL    ZFLAG    AVE     GRP       DATE     NET ID \n")

ReadPostFilefun()

f.close()

TexttoExcelFun("FinalPostConcs.xlsx","FinalPostConcs.txt")
