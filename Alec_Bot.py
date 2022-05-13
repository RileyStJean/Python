#File Name : Alec_Bot.py
#
#
#
#Purpose This will be a alec bot that will be equvlent to a master menu

from ast import Return
from datetime import date, datetime
import os
from pickle import FALSE, TRUE
from re import A
from time import sleep
from turtle import clear
from venv import create
import os
import os.path
from os.path import exists
from pathlib import Path
from os import listdir
from importlib.resources import path


alecwlcome = ("Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot",)
#will display a input form when user get something wrong
alecwrong = ("Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot",)


def math():
    print("--------Math-Menu--------")
    print("0 : Times a number 50 times")
    print("1 : -,+,*,/ two Numbers")
    print("m : to go back to menu")
    print("------------------------")
    print("q to quite the program")

    I = input("Please choose a number or letter from above : ")
    if(I == "Q") or (I == "M"):
        I = I.lower

    if(I == "0"):

        run = TRUE
        while run == TRUE:
            UINPUT = input("Please enter a the number you wish to be multiplide")

            try:

                UINPUT = int(UINPUT)

            except:
                print("Alec_Bot : a error has accured please remember to enter in a number")
            
            count = -1

            for UIMPUT in 50: 
                count = count + 1
                
                multiple = count * UINPUT

                print(multiple)
            
            run =   FALSE
            sleep(10)

        math()


    elif(I == "1"):
        print("Work In progress")
        # sigh = input("Please enter operation you would like either - + * / : ")

        # if(sigh == "-"):

        # if(sigh == "+"):

        # if(sigh == "/"):

        # if(sigh == "*"):
        #     first = input 


    elif(I == "q"):
        quit
    elif(I == "m"):
        menu1()


def Password():
    pathanmae = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files"


    dirtest = os.listdir(pathanmae)
    dirtest.remove("adminusers.txt")



    iftest = os.path.exists(r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\desktop.ini")

    if(iftest == TRUE):
        dirtest.remove("desktop.ini")

    admin = FALSE
    
    
    while(admin == FALSE):
        
        ifpassword = input("Please Enter a password : ")

        count = -1
        for list in dirtest:
    
            count = count + 1

            dirtestL = len(dirtest)
            dirtestL = dirtestL - 1

            filethings = dirtest[count]

            Files = filethings.strip("-")


            pathaname = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + Files


            readfile = open(pathaname,"r")
            Name = readfile.readline()
            a = readfile.readline()
            Adminpassword = readfile.readline()

            Name = Name.strip("\n")
            Adminpassword = Adminpassword.strip("\n")
    
            if (ifpassword == Adminpassword):
                admin = TRUE
                break

            if(count == dirtestL):
                print("Alec_Bot : my dude that is wrong *goble* *goble*")
                admin = TRUE
                break

def menu1():
    print("--------------Menu-------------")
    print("0 :Time")
    print("1 :Math")
    print("2 :Game")
    print("3 :admin")
    print("4 :Code")
    print("Q :Quit")
    print("------------------------------")
    print(" Enter [N] for second page")

    functioninput1()


def functioninput1(): 

    intP = input("Please enter a number or letter from above : ")

    if(intP == "Q"):
        intP = intP.lower

    if(intP == "N"):
        intP = intP.lower

    if(intP == "0"):
        todaysdate = datetime.today
        print("Alec_Bot: todays date :",todaysdate)

    elif(intP == "1"):
        Math()
    elif(intP == "2"):
        Games()
    elif(intP == "3"):
        Password()
    elif(intP == "4"):
        menu2()
    elif(intP == "5"):
       print ("hello")
    elif(intP == "q"):
       exit
    elif(intP == "6"):
        
    elif(intP == "7"):

    elif(intP == "n"):
        clear
        menu2()
    elif(intP == "8"):
        print("This one is not finnished yet")
    elif(intP == "A1"):

    elif(intP == "B2"):

    else:print (alecwrong)



def menu2():

    print("----------Menu--------")
    print("5 :Return to Previos menu")
    print("6 :Notes")
    print("7 :Helpful tips")
    print("8 :Work in Progress")
    print("---------------------")
    print("Enter [MA]")


menu1()



