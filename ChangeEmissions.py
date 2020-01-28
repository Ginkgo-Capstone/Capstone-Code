##January 20th
##change the emission data

def ChangeEmissions ():

    import re
    import os
    import subprocess
    os.chdir("C:/Users/Alex/Documents/Capstoni Macaroni/PCLI AERMOD FILES/Run loop")

    f=open("AERMOD.INP", "r")
    f1=f.readlines()
    f.close()
    f=open("MasterEmissions.txt", "r")
    f2=f.readlines()
    f.close()
    i = 0
    

    for x in f1:
        if 'Source Parameters' in x:
            break
        i = i + 1
        
        
    for x in range(0,len(f2)):
        f1[i+1+x] = f2[x]
    

    os.remove("AERMOD.INP")
    f = open("AERMOD.INP", "w")
    for x in range(0,len(f1)-1):
        
        f.write(f1[x])

        if x == i+1+len(f2):
            f.write('\n')

        
        
    
    
    
