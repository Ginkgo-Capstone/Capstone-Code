## Nov 5th 2019
## Let's Run AERMOD

import xlwt  ##allows python to work with excel

while true   ##should run infinitely

from datetime import datetime
date_time = datetime.fromtimestamp(timestamp)

import os
import subprocess

os.chdir("C:/Users/Alex/Documents/Capstone Macaroni/PCLI AERMOD FILES")


command = "AERMOD"

subprocess.Popen(command)


AERMOD_output = book.add_sheet("AERMOD outputs") ##saves outputs to Excel for the time stamp


