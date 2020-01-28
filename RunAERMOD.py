## Nov 5th 2019
## Let's Run AERMOD

def RunAERMOD():

    import os
    import subprocess

    #os.chdir("C:/Users/Alex/Documents/Capstoni Macaroni/PCLI AERMOD FILES/Run loop")


    command = "AERMOD"
    
    #runs aermod
    proc = subprocess.Popen(command)
    #waits intil aermod is finished running
    proc.wait()
    
