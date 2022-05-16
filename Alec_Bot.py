#File Name : Alec_Bot.py
#
#
#
#Purpose This will be a alec bot that will be equvlent to a master menu

from ast import Break, Return
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
import getpass

#this is a arry that will be displayed a random to welcom the user
alecwlcome = ("Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot",)
#will display a input form when user get something wrong
alecwrong = ("Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot","Alec_Bot",)
 
def addadmin():
            
            INPUT = input("are you sure you want to add a user y or n : ")
            
            if(INPUT == "n") or (INPUT == "N"):
                AdminMenu()

            if (INPUT == "y") or (INPUT == "Y"):

                Username = input("Enter in a Username : ")

                pathanmae = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt"
            
                fileesits = os.path.exists(pathanmae)

                if(fileesits == False):
                    filecreate = open(r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt","x")
                    filecreate.close


                test = True

                while(test == True):
                    Pathaname = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files"
                
                    Passwords = input("Plaese enter a password equal or less then 8 : ")
                    passwordlenght = len(Passwords)
                    
                    if (passwordlenght == 8 ):
                        test = False

                        fileusepathname = open(r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt","w")
                        fileusepathname.write(Passwords)
                        fileusepathname.close()
                        clear
                        test = False
                    

                pathaname = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + Username + ".txt"

                filecreate = open(pathaname,"x")
                
                fileequals = open(pathaname,"w")
                fileequals.write("Username : " + Username + "\nPassword : " + Passwords)
                fileequals.close

                print("new admin has be added")
            
            else: print("what you have entered is nmot part of the program")

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
            UINPUT = input("Please enter a the number you wish to be multiplide : ")

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
            sleep(5)

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

def AdminMenu():

    pathanmae = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files"


    dirtest = os.listdir(pathanmae)
    dirtest.remove("adminusers.txt")
    dirtest.remove("Helpmsg.txt")



    iftest = os.path.exists(r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\desktop.ini")

    if(iftest == TRUE):
        dirtest.remove("desktop.ini")

    admin = FALSE
    
    
    while(admin == FALSE):
        
        ifpassword = getpass.getpass('Please enter in Password : ')

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
                if(admin):
                    while(admin)
                        print("-------Admin-Menu-------")
                        print("1 :add a admin")
                        print("2 :cheack to see message")
                        print("3 :message someone")
                        print("")
                        print("------------------------")
                        print("[m]to got to prevoise menu and [q] to quit")

                        inputt = input("Please enter in a number from above : ")
                        
                        if(inputt == "1"):
                            addadmin()

                        elif(inputt == "2"):
                            msgcheck = open(pathaname,"r")
                            msgcheck.read()

                        elif(inputt == "3"):
                            print("correct Upper and lower case needed")
                            othername = input("Please enter users name you wish to meassage : ")

                            anotherpathaname =  r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + othername + ".txt"
                            
                            testingpath = os.path.exists(anotherpathaname)

                            if(testingpath == False):
                                print("the name you have entered is incorect")
                            
                            else:

                                inputtt = input("Plsae enter your the message")

                                msgother = open(anotherpathaname,"w")
                                msgother.write("\n" + "\n" + "\n" + Name +" : " + inputtt)
                            

                        elif(inputt == "m") or (inputt == "M"):
                            menu1

                        elif(inputt == "q") or (inputt == "Q"):
                            quit


            if(count == dirtestL):
                print("Alec_Bot : my dude that is wrong *goble* *goble*")
                admin = FALSE
                if(admin == FALSE):
                    menu1()

    print("-------Admin-Menu-------")
    print("1 :add a admin")
    print("2 :cheack to see message")
    print("3 :message someone")
    print("h :Help")
    print("------------------------")
    print("[m]to got to prevoise menu and [q] to quit")

def helpfulmenu():
    print("Work in progress")

def helpmenu():
    print("Work in progress")

def functioninput1(): 
    print("Work in progress")

    intP = input("Please enter a number or letter from above : ")

    if(intP == "Q"):
        intP = intP.lower

    if(intP == "N"):
        intP = intP.lower

    if(intP == "0"):
        todaysdate = datetime.today
        print("Alec_Bot: todays date :",todaysdate)

    elif(intP == "1"):
        math()
    elif(intP == "2"):
        #Games()
        print("Work in progress")
    elif(intP == "3"):
        AdminMenu()

    elif(intP == "4"):
        os.startfile(r"C:\Users\Rstjean\Documents\Command Scripts\Python\Python_Notes.py")
        exit
    elif(intP == "5"):
       menu1()
    elif(intP == "q"):
        exit
    elif(intP == "6"):
        helpfulmenu()
    elif(intP == "n"):
        menu2()
    elif(intP == "7"):
        os.startfile(r"C:\Users\Rstjean\Documents\Command Scripts\Python\Python_Notes.py")
        exit
    else:print (alecwrong)


def menu2():

    print("----------Menu--------")
    print("5 :Return to Previos menu")
    print("6 :Helpful tips")
    print("")
    print("---------------------")
    print("Enter [5]to return to previous menu")

    functioninput1()

def menu1():
    print("--------------Menu-------------")
    print("0 :Time")
    print("1 :Math")
    print("2 :Game")
    print("3 :admin")
    print("4 :Notes")
    print("Q :Quit")
    print("------------------------------")
    print(" Enter [N] for second page")

    functioninput1()


menu1()



