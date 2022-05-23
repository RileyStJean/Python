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
from tkinter import Y
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

    admin1 = FALSE
    
    
    while(admin1 == FALSE):
        
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

            a = a.strip("\n")
            Name = Name.strip("\n" + "Username : ")
            Adminpassword = Adminpassword.strip("\n" + "Password : ")
            

            if (ifpassword == Adminpassword):
                pauseuser = False

                if(a == "pause"):
                        print("Sorry it seems that you account is pasue please message a admin for more help")
                        pauseuser = True
                        quit()
                if(pauseuser == False):
                    admin1 = TRUE
                    admin = TRUE
                    if(admin):
                        while(admin == TRUE):
                            print("-------Admin-Menu-------")
                            print("1 :add a admin")
                            print("2 :cheack to see message")
                            print("3 :message someone")
                            print("4 :Change password")
                            print("------------------------")
                            print("[m]to got to prevoise menu and [q] to quit")

                            inputt = input("Please enter in a number from above : ")
                            
                            if(inputt == "1"):
                                #making a statmemt for my loop
                                adduser = TRUE
                                #starting my loop
                                while(adduser == TRUE):
                                    
                                    #making sure the they want to make a admin with a yes or no
                                    INPUT = input("are you sure you want to add a user y or n : ")

                                    #Testing if they did no/n/N
                                    if(INPUT == "n") or (INPUT == "N"):
                                        #bracking them out of the if statment
                                        AdminMenu
                                        #testing if they said yes or y/Y
                                    if (INPUT == "y") or (INPUT == "Y"):
                                        
                                        #asking them what the name will be for the new user
                                        Username = input("Enter in a Username : ")

                                        #puttung a path name to lisk all the in the adminsitator.txt
                                        pathanmae1 = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt"
                                        #testing to see if it exist
                                        fileesits = os.path.exists(pathanmae1)
                                        
                                        #creating if if statemte if it does not exist
                                        if(fileesits == False):
                                            #creting the file if it does not exist
                                            filecreate = open(r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt","x")
                                            #Closeing the file
                                            filecreate.close
                                        
                                        Passwords = getpass.getpass("Plaese enter a password equal or grather then 8 : ")
                                        passwordlenght = len(Passwords)
                                            #testing the password lenth to make sure it is grather then or equal to 8
                                        if (passwordlenght >= 8 ):

                                            good = TRUE

                                            count = -1
                                            for list in dirtest:
                                        
                                                count = count + 1

                                                dirtestL = dirtestL 

                                                filethings = dirtest[count]

                                                Files2 = filethings.strip("-")


                                                pathaname = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + Files2


                                                readfile = open(pathaname,"r")
                                                Name = readfile.readline()
                                                a = readfile.readline()
                                                Adminpassword = readfile.readline()

                                                Name = Name.strip("\n" + "Username : ")
                                                Adminpassword = Adminpassword.strip("\n" + "Password : ")
                                        
                                                if (Passwords == Adminpassword):
                                                    print("sorry the password you have entered incorect please enter in another one ")
                                                    good = FALSE
                                                if(Name == Username):
                                                    good = FALSE
                                                    print("The username does not meet the requirements or are already in uses")
                                                if(count == dirtestL): 
                                                    break
                                            if(good == TRUE):

                                                adminpathusers = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\adminusers.txt"

                                                line = open(adminpathusers,"r")


                                                skipline =  "\n"
                                                for yes in line: 

                                                    skipline = skipline + "\n"


                                                line.close

                                                line = open(adminpathusers,"a")
                                                line.write(Username)
                                                line.close
                                            
                                                pathanameCreate = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + Username + ".txt"

                                                fileadd = open(pathanameCreate,"a")
                                                fileadd.write("Username : " + Username + "\n\nPassword : " + Passwords)
                                                fileadd.flush()
                                                

                                                print("new admin has be added")
                                                adduser = FALSE
                                        
                                        else:print("What you have entered is incorect")

                                    else:print("What you have entered is incorect")
                    
                            elif(inputt == "2"):
                                msgcheck = open(pathaname,"r")
                                msgcheck.readline()
                                msgcheck.readline()
                                msgcheck.readline()
                                print(msgcheck.read())

                            elif(inputt == "3"):
                                print("correct Upper and lower case needed") 
                                print("")
                                othername = input("Please enter users name you wish to meassage : ")

                                anotherpathaname =  r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + othername + ".txt"
                                
                                testingpath = os.path.exists(anotherpathaname)

                                if(testingpath == False):
                                    print("the name you have entered is incorect")
                                
                                else:

                                    inputtt = input("Plsae enter your the message you want to send : ")


                                    line = open(anotherpathaname,"r")


                                    skipline =  "\n"

                                    for yes in line: 

                                        skipline = skipline + "\n"


                                    line.close

                                    line = open(anotherpathaname,"a")
                                    line.write("\n" +"\n" + Name + " : " +inputtt)
                                    line.flush()

                                    print("Message has been sent")
                                
                            elif(inputt == "m") or (inputt == "M"):
                                admin = FALSE
                                menu1()

                            elif(inputt == "q") or (inputt == "Q"):
                                admin = FALSE
                                clear
                                exit()
                            elif(inputt == "pause"):

                                if(Name == "Riley"):
                                    theseinput = input("greetings Riley who is it you would like to pause or unpause : ")
                                    pauseuserpath =  r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-" + theseinput
                                    
                                    testinguser = os.path.exists(pauseuserpath)
                                    if(testinguser == True):
                                        pasueauser = open(pauseuserpath,"a")
                                        pasueauser.write("\npause")

                                        print("the user has been pasue")

                                    else:
                                        print("Print the user you wish to pasue does not exist")



                                    


                if(count == dirtestL):
                    print("Alec_Bot : my dude that is wrong *goble* *goble*")
                    admin = FALSE
                    if(admin == FALSE):
                        menu1()


def helpfulmenu():
    print("Work in progress")

def helpmenu():
    print("Work in progress")

def functioninput1(): 
    
    yes = TRUE

    while(yes == TRUE):

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
        elif(intP == "q") or (intP == "Q"):
            yes = FALSE
            clear
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
    print("7 :message a admin")
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



