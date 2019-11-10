## Nov 5th 2019
## Let's Run AERMOD

#while true   ##should run infinitely

import xlwt  ##allows python to work with excel

import datetime
date_time_now = datetime.datetime.now()   ##current date and time
hour_now = date_time_now.hour             ##pulls hour from date_time_now - to be used as index for for loop

for hour_now =/= hour_prev_run

  import os
  import subprocess

  os.chdir("C:/Users/Alex/Documents/Capstone Macaroni/PCLI AERMOD FILES")  ##directory needs to be made to a general link

  command = "AERMOD"
  subprocess.Popen(command)

  AERMOD_output = book.add_sheet("AERMOD outputs") ##saves outputs to Excel for the time stamp. Not done yet


