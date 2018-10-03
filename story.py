import time
from colorama import Fore, Back, Style
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
        
#Functions
def greeting(name): #asks for the user's name
    time.sleep(0.5)
    print("Hi " + bcolors.UNDERLINE + fg.lightcyan + name + bcolors.ENDC + "; the evil bread has taken over your store.")
    return name
    
def askHelp(): # asks for a decison for the user's input
    time.sleep(0.5)
    hlp = str(input("Do you ask your customers for help? "))
    if (hlp == str("Y")) : 
        hlp = True
    elif (hlp == str("K")) :
        hlp = False
    else:
        directions()
        hlp = askHelp()
    return hlp
    
def dSoldier(): # asks for a decision for an army from the user
    time.sleep(0.5)
    hlp = str(input("Do we call for "+Fore.BLUE+"soldiers"+Fore.RESET+" to help you? "))
    if (hlp == str("Y")) :
        hlp = True
    elif (hlp == str("K")): 
        hlp = False
    else:
        directions()
        hlp = dSoldier()
    return hlp

def dFarmer(): # asks the user for a decision about a farmer's offer
    time.sleep(0.5)
    pigs = str(input("Do you accept the farmer's offer for a "+Fore.BLUE+"livestock army"+Fore.RESET+"? "))
    if (pigs == str("Y")):
        pigs = True
    elif (pigs == str("K")):
        pigs = False
    else:
        directions()
        pigs = dFarmer()
    return pigs

def moveAway(): # asks the user for the decision to move away
    time.sleep(0.5)
    dec = str(input("Do you "+Fore.YELLOW+"move"+Fore.RESET+" away? "))
    if (dec == str("Y")):
        dec = True
    elif (dec == str("K")):
        dec = False
    else:
        directions()
        dec = moveAway()
    return dec
    
def revenge(): # asks the user about a decision for revenge
    time.sleep(0.5)
    rev = str(input("Do you try and "+Fore.YELLOW+"take your revenge"+Fore.RESET+"? "))
    if (rev == str("Y")):
        rev = True
    if (rev == str("K")):    
        rev = False
    else:
        directions()
        rev =revenge()
    return rev

def dAttackBread(): # asks the user about a decision to attack the bread
    time.sleep(0.5)
    plan = str(input("Will we "+Fore.YELLOW+"charge"+Fore.RESET+" the bread? "))
    if (plan == str("Y")) :
        plan = True
    elif (plan == str("K")):
        plan = False
    else:
        directions()
        plan = dAttackBread()
    return plan

def dDestroy(): # asks the user about a decision to destroy the store
    time.sleep(0.5)
    plan = str(input("Do we "+Fore.YELLOW+"burn"+Fore.RESET+" your store down? "))
    if (plan == str("Y")):
        plan = False
    elif (plan == str("K")):
        plan = True
    else:
        directions()
        plan= dDestroy()
    return plan

def gameWin(): #tells the user if they won in the story
    time.sleep(0.5)
    print (Back.GREEN+"You win!"+Back.RESET)
    
def gameLose(): #tells the user if they lost in the story
    time.sleep(0.5)
    print (Back.RED+"You lose..."+Back.RESET)
    
def directions(): #if the user does not enter the intended letters for input, this will appear
    time.sleep(0.5)
    print('Only enter '+Fore.GREEN+'"Y"'+Fore.RESET+' for "Yes" or '+Fore.RED+'"K"'+Fore.RESET+' for "No" for the answers.')

#Story
start = input("Press"+Fore.CYAN+' "enter" '+Fore.RESET+"to start. ")
time.sleep(0.5)
directions()
time.sleep(0.5)
print("You are a baker. To help your business survive, you made evil bread.")
time.sleep(0.5)
name = str(input("What is your name? "))
time.sleep(0.5)
greeting(name)
time.sleep(0.5)
hlp = askHelp() #Decision 1
if (hlp == True) :
    print ("The customers die fighting the bread.")
    swrd = dSoldier() #Decision2a
    if swrd == True :
        print ("The army arrives to help you.")
        plan = dAttackBread() #Decision3a
        if plan == True :
            print("The army is decimated by wheat, and everyone dies.")
            gameLose()
        elif plan == False :
            print("The army sneaks around the store and eats the bread.")
            gameWin()
    elif swrd == False :
        print ("Your family decides to claim back your store.")
        plan = dDestroy() #Decision3b
        if plan == True :
            print("Your family fights the bread long after your death.")
            gameLose()
        elif plan == False :
            print("The store is burned;")
            print("however, you are the town hero.")
            gameWin()
elif (hlp == False) :
    print("Your family gets captured by the bread; ")
    print("Some farmers offer assistance.")
    pigs = dFarmer() #Decision2b
    if pigs == True :
        print("The pigs eat all the bread, but destroy your store in the process.")
        dec = moveAway() #Decision4a
        if dec == True:
            print("You and your family live happily ever after.")
            gameWin()
        elif dec == False:
            print("Your family attacks the bread and dies.")
            gameLose()
    elif pigs == False :
        print("Your family is absorbed and killed by the bread.")
        rev = revenge() #Decision4b
        if rev == True:
            print("You eat all of the the bread.")
            gameWin()
        elif rev == False:
            print("You end up with a case of depression and die alone.")
            gameLose()
exit = input("Press " + Fore.CYAN + '"enter"' + Fore.RESET + " to exit the program. ")