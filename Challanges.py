#1.Write a function that takes a name and returns the string "Hello <name" ! Thanks for being here. Today is <date>
#2.aboslute value thing
#3.Write a function that takes an integer minutes and converts it to seconds. Example: minsec(25) returns 1500. 
#4.Expand the function in option 3 and create a function which takes a date (like your birthday) and returns the number of seconds, minutes, hours, days and years since that time.
#5.Write a Python function to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
#6.Write a Python function to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#7.
#8.
#9.
#
from ast import Return
from datetime import date
from sys import setswitchinterval

#-----------------------------------------------------------------------------#
def dateF():

    Input = input ("Please put your name here : ")
    today = date.today()#

    print("Hello", Input + " " +"Thanks for being here today is", today)#
#-----------------------------------------------------------------------------#

def absalotvalue(num):
    
    """This Function returns the absolute value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

# print(absolute_Vale(2))
# print(absolute_Vale(-4))

#-----------------------------------------------------------------------------#

def converts():

    looping = True
    #doing a loop 
    while(looping):
        #ask for input
        print("max is ")
        inputt = input("\nplease enter a number for minites to translate to seconod : ")

        #check to see if imput a number
        try:
            min = int(inputt)

        except:
            print("-Sorry what you have enterde is not a integer-")

        if(min == 0):
            print("0 Seconds in",min)
        
        else:looping = False
        min = min * 60
        print(f"there is {min} in {inputt}")

converts()

            

        
        

        






















