#January 15th 



def CreateSubFile(PFL,SFC):

    import re 
    import os
    import subprocess

    #os.chdir(r"C:\Users\Alex\Documents\Capstoni Macaroni\PCLI AERMOD FILES\Run loop")
    #if files exist deletes them
    
    if os.path.isfile('PetroCanadaLubricants_Mississauga_16216.sfc'):
        os.remove("PetroCanadaLubricants_Mississauga_16216.sfc")
    if os.path.isfile('PetroCanadaLubricants_Mississauga_16216.pfl'):
        os.remove("PetroCanadaLubricants_Mississauga_16216.pfl")
    #writes lines into files    
    f= open('PetroCanadaLubricants_Mississauga_16216.sfc',"w+")
    f.write(SFC[2])
    f.write(SFC[0])
    f.write(SFC[1])
    f.close
    f= open('PetroCanadaLubricants_Mississauga_16216.pfl',"w+")
    f.write(PFL[0])
    f.write(PFL[1])
    f.close
    
