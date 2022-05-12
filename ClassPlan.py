from calendar import weekday
import datetime
import datetime as dt
import os
import os.path
from os.path import exists

today = dt.date.today().isoweekday()

if dt.date.today().isoweekday() == 4 or 2:
    

    CodingPlan = "Today is codeing plan is Challanges"

    testing = os.path.exists(r"C:\Users\Rstjean\Documents\Command Scripts\Class\Todays_Plan")
   
    if testing == False:
       open(r"C:\Users\Rstjean\Documents\Command Scripts\Class\Todays_Plan","x")


    WriteFile = open(r"C:\Users\Rstjean\Documents\Command Scripts\Class\Todays_Plan","a")
    WriteFile.write(CodingPlan)


if dt.date.today().isoweekday() == 1 or 3 or 5:
        
