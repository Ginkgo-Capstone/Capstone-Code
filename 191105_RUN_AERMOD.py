## Nov 5th 2019
## Let's Run AERMOD

import xlwt  ##allows python to work with excel
AERMET_FSC = xlwt.AERMET()

while true   ##should run infinitely

  import datetime
  date_time = datetime.datetime.now()   ##current date and time

  import os
  import subprocess

  os.chdir("C:/Users/Alex/Documents/Capstone Macaroni/PCLI AERMOD FILES")

  command = "AERMOD"
  subprocess.Popen(command)

  AERMOD_output = book.add_sheet("AERMOD outputs") ##saves outputs to Excel for the time stamp


