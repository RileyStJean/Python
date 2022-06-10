<#
File : Nate_Functions
Author : Riley .S
Purpose is to create a "Nate Help Bot"
#>
 
#Create a randomly generated beginning Reply
#Have the user to input and have nate to reply in a switch
##in the switch make is so that if you say what is not in switch make a randomly generated answer that will
##happen if  it input is not in switch
#have reply and or switches in a switch
 
 
#The start of running my functions
function -Help {
 
    Write-host "-----------UseFul-CMDLET------------"
    Write-host "Get-Member"
    Write-host "Get-Help Or Help"
    Write-host "Write-Host"
    Write-host "Read-Host"
    Write-host "Funtion"
    Write-host "For,Do While,Do Until"
    Write-host "$ and something after for Varable"
    Write-host "Need Help with f"
    Write-host "------------------------------------"
    Write-host "Q To Leave the Program"
 
}
function -NateHelp {
 
    Write-host "---------------UseFul-Nate_bot-Stuff------------"
    Write-host "There are [Hidden] Ones"
    Write-host ""
    Write-host ""
    Write-host ""
    Write-host ""
    Write-host "Entering [Time] will display Time and Date"
    Write-host "(The Stuff in [ ] or box are ment to be typed and Entered)"
    Write-Host " "
    Write-host "          Type [Menu] to do more"
    Write-host "-------------------------------------------------"
    Write-host "Q To Leave the Program"
 
}
function -MyFunctions {
    Get-ChildItem -Path Function:\-*|Select-Object name
}
function -notes {
    Write-host " Work In Progress" -BackgroundColor Yellow -ForegroundColor Black
    #Start-Process -FilePath .\"PUT NOTE HERE".ps1
}
Function -NateCode {
 
    $IfTrue = $false
   
    $FileList = [array]
    $FileList = Get-ChildItem -Path .\Powershell -name *.ps1
    $FileLength = $FileList.Length
   
    $Count = -1
   
    foreach ($FileLength in $FileList){
    $Count++
    Write-host $Count : $FileList[$Count]
   
    }
    $FileLength = $FileList.Length
   
    Write-Host "Q : To quit the program"
    do {
    #Asking user For Input
    $Input = Read-host "Please choose a Number From above"
   
    if ($Input -eq "Q") {
        Exit
    }
    if ($Input -eq "q") {
        Exit
    }
   
    try {
   
    $Program = $FileList[$Input]
    $Input = [Int]$Input
    $FileLength = [Int]$FileLength
   
    if ($Input -is [Int]) {
   
        if ($Input -le $FileLength) {
   
                if ($Input -gt -1) {
                Start-Process -FilePath .\Powershell\$Program
                $IfTrue = $true
   
                }
        }
    }
       
    }
    catch {
    $Ifture = $False
    $Random = Get-Random -Maximum 10  
    Write-Host $ArrayNate[$Random]
    }
   
    } until ($IfTrue -eq $True)
 
    Exit
}
function -BOOOOOMMMM {
 
    Start-Process -FilePath 'C:\Users\Rstjean\Pictures\Saved Pictures\Holy Pictures\Wallpapers\Yes.jpg'
        $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('BOOOOOM HAHAHA Did I Get You','Nate-Bot','YesNoCancel','Error')"
       
       
        switch ($msgBoxInput) {
            "Yes" {
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Ah Good Nice to see that  I Spook You User','Nate-Bot','Ok','Error')"
           
        }
            'No' {
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('What Do you mean i did not get you. You are a mean Person User','Nate-Bot','YesNoCancel','Error')"
            }
        }
       
   
       
}
    Function -game {
        Write-Host "Game Menu"
        Write-Host "-------------------"
        Write-Host "1 : Heads Or Tail"
        Write-Host "Work In PROGRESS"
        Write-Host "Work In PROGRESS"
        Write-Host "Work In PROGRESS"
        $Input = Read-Host
   
        switch ($input) {
                "1" {
                        $Coin = @("Head","Tails")
                        $Random = Get-random -Maximum 1 -Minimum 0
                        Write-Host $Coin[$Random]
                 }
                Default {
                        $Random = Get-random -Maximum 10
                        Write-Host $ArrayNate[$Random]
                }
        }
   
}    
function -CIMInfo {
    do {
 
        $Cm
 
        Write-Host "-----------Menu------------"
        Write-Host "1 : Disk Storage"
        Write-Host "2 : Memory Module"
        Write-Host "3 : Network Adapter"
        Write-Host "4 : CPU Processors"
        Write-Host "5 : KeyBoard Info"
        Write-Host "6 : General Information"
        Write-Host "7 : BIOS Information"
        Write-Host "q : Quit the Program"
 
    $Input = Read-Host "Please Choose a Number From The Following"
   
        if ($Input -eq "Q") {
            $Input.Tolower
        }
   
    switch ($Input) {
 
       
        "1" {  
            Clear-Host
            Get-CimInstance -ClassName CIM_DiskDrive|select-object Model,Size|Format-List
            
        }
        "2" {  
            Clear-Host
            Get-CimInstance -ClassName CIM_Memory|Select-object Status,BlockSize|Format-List
            
 
        }
        "3" {  
            Clear-Host
            Get-CimInstance -ClassName Win32_NetworkAdapter|Select-object AdapterType,Name,Speed,MacAdress|Format-List
            
        }
        "4" {  
            Clear-Host
            Get-CimInstance -ClassName CIM_Processor|Format-List
            
        }
        "5" {  
            Clear-Host
            Get-CimInstance -ClassName CIM_KeyBoard|Select-object Description,Caption,Status|Format-List
            
        }
        "6" {  
            Clear-Host
            Get-cimInstance -className Win32_ComputerSystem |Format-List
            
        }
        "7"{
            Clear-Host
            Get-CimInstance -ClassName Win32_BIOS|Format-List
            
        }
        "q" {  
            Clear-Host
            Write-host "Goodbye User"
            
        }
 
        Default {
            $CM = False
            Write-Host "$Input is not of the following above"
        }
    }
} while ($CM)
 
}
#The End of running my functions
 
 
 
 #setting $IfTrue to true
$IfTrue = $True
 
#Setting a Array if user types something incorrectly and generating a random Number on the next line
$ArrayNate = @("Nate_Bot :Wrong Type something Useful User","Nate_Bot :UHG If you Want Some assistants then Type Help","Nate_Bot :.....Try Again","Nate_Bot :UUUUUMMMMM that is not in my Program","Nate_Bot :I AM A ROBOT *BEEP**BOOP*","Creator :*Sleeping*ZZZZZZZZZ.............","Creator : Remember to Use Help if you are Stuck","Nate_Bot :MMMMHHH CheeseCake","Creator : I AM THE NUTTY ONE HAHAHHAHA","Nate_Bot :Can you do anything right")
      $Random = Get-random -Maximum 16
 
      #Setting a Array for theNate_bot to Welcome the user
          $Array = @("Nate_Bot :.........UMMMMMMMMMM so you want help I see","Nate_Bot :Greetings I will not be helping you good day","Nate_Bot :*Goble*Goble*Gob* ","Nate_Bot :CheeseCake is a Cake Of Cheese","Nate_Bot :Hell0 ; )","Nate_Bot :AHHHH I SEE HAHAHHAHHAH *Cough**Cough*","Nate_Bot :: ) I do math ","Ummmm Hello","Nate_Bot :I SEE YOU HAVE FALLEN FOR MY TRAP CARD HAHAHHAHAHAHHAHAHHAHA","Nate_Bot :So what you need help this","Nate_Bot :hmmm thai is interesting","Nate_Bot :What can I help you with User","Nate_Bot :You Look Funny want some Candy","Nate_Bot :yes,no,maybe,not,Indeed","Nate_Bot :I HAVE ACHIEVE MY FULL POWER AAAAAAAAAHHHHHHHHHH!!","Nate_Bot :*BEEP**BOOP* Loading...")
 
          #I am then Choosing one of the output of the Array and writing to the User
          Write-Host $Array[$random]
          Write-Host "    "#Makinf a space for the next Line
  Write-Host "Creater : PS Type Help If Stuck"#Giving a little bit of guidence for the user
 
 
 
 #Starting my Do Statement
do {    
 
          # Asking the user For Input
          $input = Read-Host "Write :"
          #Make Sure that the Input is a string
          $Lower = $Input.Tolower()
 
          #I am creating a switch for the Input
          switch ($Lower) {
              "help" {
 
                #in the switch I am write something to the ternal and that activating my function called -NateHelp
                  Write-Host "Nate_Bot :I Guess I can help you gosh you can enter in Menu to see Some Options that I can do your You"
                  -NateHelp
 
              }
              "menu" {
               
                #in the switch I am crearing a menu to and than another switch in it
                      Write-Host "----------Menu----------"
                      Write-Host "1: Code Menu"
                      Write-Host "2: UseFul Tips\Helps"
                      Write-Host "3: Generate a Random Number"
                      Write-Host "4: BOOOOOOOOOMMMMMMMM"
                      Write-Host "5: System Info"
                      Write-Host "6: More Nate"
                      Write-Host "------------------------"
                      Write-Host "q: Quit The Program"
                    Write-Host ""
                    Write-Host "Nate_Bot :Ugh here is the menu"
 
                    #I am making $thenTrue equal False for my do statement
                      $ThenTrue = $False
 
                      #Starting a do Until Statement
                      do {  
 
                        #Going to ask the user for input for my switch statement
                          $Input = Read-Host "Write :"
 
                          #I am then makinf it so you can exit the program with a Lowercase q
                          If($Input -eq "Q"){
                              #Converting it to q lower case
                              $Input.ToLower()
                          }
                          #Starting my swtich in menu
                          switch ($input) {
 
                              "1" {
                                  #this will fun my function -NateCode and setting $ThenTrue to true
                                -NateCode
                                $ThenTrue = $True
                                Clear-Host
                              }
                              "2" {
                                  #Starting my function -Help and setting $ThenTrue to true
                                -Help
                                $ThenTrue = $True
                                Clear-Host
                              }
                              "3" {
                                #I am going to generate a random number and ask to use what they want the max to be
                                  #do a Try staement to make sure that then enter in a Number
                                try {
                                      #asking the user for input and converting it in to a Intiger\Number
                                      $Count = Read-Host "Nate_Bot :Enter the max number you want to generate"
                                      $Int = [Int]$Count
                                      #Then starting a if statement to make sure it is a intiger\Number
                                      If($Int -eq [Int]){
                                        $Random = Get-Random -Maximum $Int
                                        Write-Host $Random
                                      }
 
                                  }
                                  catch {#if something went wrong with the try then will Write a output saying that it is wrong
                                      Write-Host "Bad"
                                     
                                  }
                                  #setting $ThenTrue to true
                              $ThenTrue = $True
                              
                              }
                              "4" {
                                  #Running my -BOOOOOMMMM Funtcion and setting $ThenTrue to true
                                  -BOOOOOMMMM
                                  $ThenTrue = $True
                              }
                              "5" {#Running my -CIMInfo function and setting $ThenTrue to true
                                -CIMInfo
                                  $ThenTrue = $True
                              }
                              "6" {#I am creating a menu if said user wish to do more with the NateBot
                                Write-Host " [What's 9+10]"
                                Write-Host "    [Time]"
                                Write-Host "    [Game]"
                                Write-Host "     [69]"
                                Write-Host "   [Hidden]"
                                Write-Host "Stuff in [] Are what to Enter"
                                #Setting $ThenTrue to = True
                                  $ThenTrue = $True
                              }
                              "q" {
                                  Exit
                              }
                     
                          }
                      } Until ($ThenTrue -eq $True)
 
 
              }
              "what's 9+10" {
                  #I am then creating a iteraction for the user and nate_Bot
                  Write-Host "Nate_Bot :Ummm It's 19"#Writting to termanal
                  $Yes = Read-Host "Creator :Type 21"#Writting to termanal
                  Start-Sleep 1#and then adding a one second Delay\Pause
                  Write-Host "Nate_Bot :Are you Dumb it is 19 How do you even get 21"#Writting to termanal
                 
              }
              "Time" {#I am displaying the time by setting a variable and writting it to host
              $Time = Get-Date
                  Write-Host "Today is $Time"
              }
              "" {#I am then creating a Hidden meassage\Switch for the user to fin
 
                #Work In Progress
                Write-Host "Creator : It looks as if you Found a Hidden One"
 
                switch ($input) {
 
                    "yes" {
 
                     }
                     "no" {
                       
                    }
                    Default {
 
                    }
                }
              }
              "hidden" {

             Write-Host "Nate_Bot : Hidden ones are hidden and or secrect features withing the program"
             Start-sleep 3
             Write-Host "NateBot there is a total of 6 Hidden One"
             Write-Host ""
             Start-sleep 3.5
             Write-Host "Creator : PST hey if you want help finding a Hidden one then note everything in [ ] in help can be entered" 
             

              }
              "condition" {
             #Work In Progress
              }
              "condition" {
             #Work In Progress
              }
              "condition" {
             #Work In Progress
              }
              "condition" {
             #Work In Progress
              }
              "condition" {
             #Work In Progress
              }
              "nate_bot" {
             #Work In Progress
              }
              " " {
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('YOU HAVE FOUND A HIDDEN ONE','Creator','ok','Error')"
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('YOU HAVE FOUND A HIDDEN ONE','Creator','ok','Error')"
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Umm I guess you Found My hint I Think','Creator','ok','Error')"
                $msgBoxInput = PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Yep thats it try and find More Hidden Ones','Creator','ok','Error')"
            
            }
              "Game" {
                Write-Host "So you want to play a game I see I guess I will Join You"
                  -Game
                Clear-host
              }
              "69" {
              Write-Host "Creator : haha That sounds funny"
              }
              "the nutty one" {#this Will be a secrect interaction with the Creator\ME The Nutty One

              Write-Host "Creator : You Called What You Need"#Writting stuff to the termanl
              Write-Host "Nate_Bot : WHAT CREATOR WHAT ARE YOU DOING HERE"#Writting stuff to the termanl
              Write-Host "Creator : ah Nate_Bot it is good to see you as well Anyway user you wanted to ask Something"#Writting stuff to the termanl
              $Box = Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Do you wish to ask the Creator','','YesNo','Error')
              #Above i am making a popup box by by adding a type of object that is the system-Windows-Messagebox
              
              #I am then making a do\looping statmente
              do {
                 #Setting the ThenTrue statement to equal false
                $ThenTrue = $False
 
                #adding the interaction with the pop up box
              switch ($Box) {
                    "Yes" {
                        Write-Host "Creator : hhhmmm What is it "#Writting to the termanal
                        Clear-Host "" #Writting to the termanal
                        Start-Sleep 1#Having a seconed delay
                        Write-Host "Creator : ahhh you ask why I Created Nate_Bot"#Writting to the termanal
                        Clear-Host ""#Writting to the termanal
                        Start-Sleep 1#Having a seconed delay
                        Write-Host "Creator : Well I created he as a idea i got from a friend he was also Called nate"#Writting to the termanal
                       #Setting the ThenTrue statement to equal True
                        $ThenTrue = $True
                     }
                     "No" {
                        Write-Host "Creator : No then why did you call me"#Writting to the termanal
                        Clear-Host ""#Writting to the termanal for a skip line
                        Start-Sleep 1#Having a seconed delay
                        Write-Host "You wish to talk to me umm sorry but i can not do that forgive me"#Writting to the termanal
                        Clear-Host ""#Writting to the termanal for a skip line
                        $ThenTrue = $True
                     }
                }
            } while ($ThenTrue)  
         }
            #End of the Loop
 
              "q" {
                 #I am then Clearing the screen and exiting the Program\Code
                  Clear-Host
                  Exit
             
              }
 
              Default {#I am then Making it so if the user types something not in the switch then it will run this
                  #Chooseing a random number and then writing the randomly selected array
                $Random = Get-Random -Maximum 10  
                  Write-Host $ArrayNate[$Random]
              }
  }
  #the while statement that will keep running untill $IfTrue = True
}while ($IfTrue -eq $True)
 
 
#Below is for me to remember  
#PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('The great message')"##
##Will #Display A Popup Image\Box
 
 
 
 
 
 
 
 

