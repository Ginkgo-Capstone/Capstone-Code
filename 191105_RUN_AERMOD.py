## Nov 5th 2019
## Let's Run AERMOD

#while true                                          ##should run infinitely

  import xlwt                                        ##allows python to work with excel

  import datetime
  date_time_now = datetime.datetime.now()            ##current date and time
  min_now = date_time_now.minute                     ##pulls minute from date_time_now - to be used as index for for loop

  for min_now != min_prev_run:                     ## i.e will run every new minute

    import os
    import subprocess
   

    os.chdir("C:/Users/Alex/Documents/Capstone Macaroni/PCLI AERMOD FILES")  ##directory needs to be made into a general link

    command = "AERMOD"
    subprocess.Popen(command)
  
  ##pull from the .out that AERMOD spits out the data that we care about and save to easy to process excel 
  ##want to be able to save results iteratively so create directory inside of for loop that will save to the line after the previous
  ## use date_time_now as identification column in excel

    AERMOD_output = book.add_sheet("AERMOD outputs")  ##saves outputs to Excel for the time stamp. Not done yet
 
    min_prev_run = min_now                          ##step back index
  end

#end

<<<<<<< HEAD
##I am making an edit


=======
>>>>>>> 8b07cc4892fdf71a7f8c9498b62978e2da6300dc
