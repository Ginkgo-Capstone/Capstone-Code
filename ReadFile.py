###Nov 18
###Try to read an Aermod.out file
def MaxConFun():

    ## imports reading function and operating system
    import re 
    import os
    import subprocess

    #Opens Directory
    #os.chdir("C:/Users/Alex/Documents/Capstoni Macaroni/PCLI AERMOD FILES/Run loop")

    #Opens Output file
    f=open("aermod.out", "r")



    ##f1 is a vector of strings each containing a line of the aermod.out
    f1=f.readlines()
    j = 0
    i = 0

    ##will find for 1 and 2 hour average:
    ##concentration maximum, coordinates and time stamp
    conmax = [0,0]
    xcordmax = [0,0]
    ycordmax = [0,0]
    timemax = [0,0]


    ##runs for loop were x is each line of aermod.out
    for x in f1:

        # if find this line of code knows to find concentrations
        if 'VALUES FOR SOURCE GROUP:  ALL' in x:
            k = 1

            #looks at if 2 hour or 1 hour average
            if '2' in x:
                m = 1
            else:
                m = 0
            while k == 1:
                
                #creates each word of the line 11+ down of Values for source
                #into a vector of strings
                temp = re.findall(r'\d+', f1[i+j +11])
                #converts the strings into intergers 
                res = list(map(int, temp))
                xcord1 = res[0] + res[1]/100
                ycord1 = res[2] + res[3]/100
                con1 = res[4] + res[5]/100000
                time1 = res[6]
                xcord2 = res[7] + res[8]/100
                ycord2 = res[9] + res[10]/100
                con2 = res[11] + res[12]/100000
                time2 = res[13]

                #looks if current concentration is bigger than current max
                if con1 > conmax[m]:
                    conmax[m] = con1
                    ycordmax[m] = ycord1
                    xcordmax[m] = xcord1
                    timemax[m] = time1
                    

                #looks if current concentration is bigger than current max              
                    

                if con2 > conmax[m]:
                    conmax[m] = con2
                    ycordmax[m] = ycord2
                    xcordmax[m] = xcord2
                    timemax[m] = time2
                    
                    


                j = j + 1
                # if at end of section will find version ending while loop
                if 'VERSION' in f1[i+j+11]:
                    k = 0
                    j = 0
        i = i + 1

    Return = [0,0,0,0,0,0,0,0]
    Return[0] = conmax[0]
    Return[1] = xcordmax[0]
    Return[2] = ycordmax[0]
    Return[3] = timemax[0]
    Return[4] = conmax[1]
    Return[5] = xcordmax[1]
    Return[6] = ycordmax[1]
    Return[7] = timemax[1]
    return Return 

                


        

        
        

        


        

