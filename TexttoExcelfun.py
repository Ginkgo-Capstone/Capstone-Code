#February 24th
#convert into excel file

#imports functions
import time
import re 
import os
import subprocess
import os.path
import xlsxwriter



#creates a function
def TexttoExcelFun(book,textfile):
    #os.chdir("Run loop")



    #reads contents of files    
    f = open('FinalPostConcs.txt')
    f1 = f.readlines()
    f.close()

    #opens up excel file and creates a worksheet
    workbook = xlsxwriter.Workbook(book)
    worksheet = workbook.add_worksheet("FinalPostConcs")
    row = 0
    col = 0

    #reads line by line of text file
    for x in f1:
        #splits up current line in the file
        temp = x.split()
        #writes each values into different column 
        for i in range(len(temp)):
            worksheet.write(row, col+ i, temp[i])
        row += 1

    

    workbook.close()
