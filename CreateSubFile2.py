#January 15th 



def CreateSubFile2(PFL,SFC):

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
    f.write(" 43.5017N  79.6117W          UA_ID:    14733  SF_ID:    61587  OS_ID:              VERSION: 16216  ADJ_U*  CCVR_Sub TEMP_Sub")
    for i in range (len(SFC)):
        f.write(SFC[i])
        
    
    f.close
    f= open('PetroCanadaLubricants_Mississauga_16216.pfl',"w+")
    for i in range (len(PFL)):
        f.write(PFL[i])
    f.close
    
