import getpass

pathaname = r"C:\Users\Rstjean\Documents\Command Scripts\Junk_Files\-Riley.txt"

line = open(pathaname,"r")


skipline =  "\n"

for yes in line: 

    skipline = skipline + "\n"


line.close

line = open(pathaname,"a")
line.write("\n" + "hello")






